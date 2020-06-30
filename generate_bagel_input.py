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

class Molecule:
    def __init__(self,  *, filename = None, basis = "6-31G", df_basis = "svp-jkfit"):
        self.params = dict()
        self.geometry = []

        self.set_keyword("basis", basis)
        self.set_keyword("df_basis", df_basis)

        if filename != None:
            self.read_file(filename)

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

class Optimize:
    def __init__(self, *, target = 0, method = {"title" :"hf", "thresh" :  1.0e-12}):
        self.target = 0
        self.methods = []
        if isinstance(method, list):
            for m in method:
                self.methods.append(m)
        else:
            self.methods.append(method)

    def as_dict(self):
        ret = dict()
        ret["title"] = "optimize"
        ret["target"] = self.target
        ret["method"] = []
        for m in self.methods:
            if isinstance(m, dict):
                ret["method"].append(m)
            else:
                ret["method"].append( m.as_dict() )
        return ret

class Method:
    def __init__(self, title, **kwargs):
        self.title = title
        self.params = {}
        self.params.update(kwargs)

    def set_keyword(self, key, value):
        self.params[key] = value
    def as_dict(self):
        ret = dict()
        ret["title"] = self.title
        for k,v in self.params.items():
            ret[k] = v
        return ret

if __name__ == '__main__':
    import sys
    geometry_file = "test.xyz"
    if 1 < len(sys.argv):
        geometry_file = sys.argv[1]

    mol = Molecule(filename = geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    opt = Optimize(target = 0, method = [Method("hf", thresh = 1.0e-8)] )
    bagel = Bagel(mol, opt)
    print( json.dumps( bagel.as_dict(), ensure_ascii = True, indent = 2 ) )
    
