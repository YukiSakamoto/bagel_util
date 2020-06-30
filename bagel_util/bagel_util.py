import json

class Bagel:
    def __init__(self, molecule, method):
        self.molecule = molecule
        self.methods  = []
        if isinstance(method, list):
            for m in method:
                self.methods.append(m)
        else:
            self.methods.append(method)
    
    def as_dict(self):
        ret = dict()
        ret["bagel"] = []
        ret["bagel"].append( self.molecule.as_dict() )
        for m in self.methods:
            if isinstance(m, dict):
                ret["bagel"].append(m)
            else:
                ret["bagel"].append( m.as_dict() )
        return ret

    def to_json(self, ensure_ascii = True, indent = 2, **kwargs):
        s = json.dumps(self.as_dict(), ensure_ascii = ensure_ascii, indent = indent, **kwargs)
        return s

class Molecule:
    def __init__(self, *, geom_file = None, basis = "6-31G", df_basis = "svp-jkfit", **kwargs):
        self.params = dict()
        self.geometry = []

        self.set_keyword("basis", basis)
        self.set_keyword("df_basis", df_basis)
        for k,v in kwargs.items():
            self.set_keyword(k,v)

        if geom_file != None:
            self.read_file(geom_file)

    def set_keyword(self, key, value):
        self.params[key] = value

    def add_atom(self, atom_type, pos_x, pos_y, pos_z):
        pos = [float(pos_x), float(pos_y), float(pos_z)]
        self.geometry.append( {"atom": atom_type, "xyz" : pos} )


    def read_file(self, filepath):
        import os
        import os.path
        ext = os.path.splitext(filepath)[1]
        self.geometry.clear()
        if ext == ".xyz":
            self.read_xyz(filepath)
        else:
            raise "Unknown file type"

    def read_xyz(self, filename):
        with open(filename) as f:
            self.set_keyword("angstrom", True)
            all_lines = f.readlines()
            # 1st line: num of atoms
            num_of_atoms = int(all_lines[0].strip() )
            comment = all_lines[1]
            if (num_of_atoms + 2) != len(all_lines):
                raise "Invalid Number"
            for i in range(2, len(all_lines)):
                temp = all_lines[i].split()
                atom_type = temp[0]
                pos_x = float( temp[1] )
                pos_y = float( temp[2] )
                pos_z = float( temp[3] )
                self.add_atom(atom_type, pos_x, pos_y, pos_z)

    def as_dict(self):
        ret = dict()
        ret["title"] = "molecule"
        for k,v in self.params.items():
            ret[k] = v

        ret["geometry"] = []
        for atom in self.geometry:
            ret["geometry"].append(atom)

        return ret

class Method(object):
    def __init__(self, title, **kwargs):
        if "title" in kwargs:
            raise
        self.title = title
        self.params = {}
        self.set_params(**kwargs)

    def set_keyword(self, key, value):
        self.params[key] = value

    def set_params(self, **kwargs):
        for k,v in kwargs.items():
            if k in self.params:
                "Warn ({title}): the value = {key} is replaced.  {old_v} => {new_v}".format(
                        title = self.title, key = k , old_v = self.params[k], new_v = v)
            self.params[k] = v

    def as_dict(self):
        ret = dict()
        ret["title"] = self.title
        for k,v in self.params.items():
            ret[k] = v
        return ret

class HF(Method):
    def __init__(self, hf_type = "hf" ,*, thresh = 1.0e-8, **kwargs):
        super().__init__(hf_type, thresh = thresh, **kwargs)

class CASSCF(Method):
    def __init__(self, *, nstates = 1, nact = 0, nclosed = 0, active = [], **kwargs):
        super().__init__("casscf", nstates = nstates, nact = nact, nclosed = nclosed, active = active, **kwargs)

class CASPT2(Method):
    def __init__(self, *, method = "caspt2", ms = True, xms = True, sssr = True, shift = 0.0, **kwargs):
        super().__init__("smith", method=method, ms = ms, xms = xms, sssr = sssr, shift = shift)

class Optimize:
    def __init__(self, *, target = 0, opttype = "energy", method = HF() ):
        self.params = dict()
        self.set_keyword("target", target)
        self.set_keyword("opttype", opttype)

        self.methods = []
        if isinstance(method, list):
            for m in method:
                self.methods.append(m)
        else:
            self.methods.append(method)

    def set_keyword(self, key, value):
        self.params[key] = value

    def as_dict(self):
        ret = dict()
        ret["title"] = "optimize"

        for k,v in self.params.items():
            ret[k] = v

        ret["method"] = []
        for m in self.methods:
            if isinstance(m, dict):
                ret["method"].append(m)
            else:
                ret["method"].append( m.as_dict() )
        return ret


if __name__ == '__main__':
    import sys
    geometry_file = "test.xyz"
    if 1 < len(sys.argv):
        geometry_file = sys.argv[1]

    mol = Molecule(filename = geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    opt = Optimize( method = CASSCF()  )
    bagel = Bagel(mol, HF("uhf") )
    print( bagel.to_json() )
    
