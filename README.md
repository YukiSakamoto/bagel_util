# Bagel Util

## Installation

 ```shell
 pip install git+https://github.com/YukiSakamoto/bagel_util
 ```

## Usage and Examples

### Simple Example: 

 ```python
	from bagel_util.bagel_util import *
	mol = Molecule(geom_file = "test.xy", basis = "6-31G", df_basis = "svp-jkfit")
	method = [Method("hf", maxiter=150)]
	bagel = Bagel(mol,method)
	print(bagel.to_json())
```

### Objects

#### Bagel

```python
class bagel_util.Bagel(molecule, method)
```

`Bagel` requires two arguments, molecule and methods. Both must be specified.

* The first argument `molecule` is an object of `Molecule`. 

* The second argument `method` is an object of `Method` or the list of `Method` object.

* `to_json()` function generates the string of json.

#### Molecule

```python
class bagel_util.BMolecule(*, geom_file = None, basis = "6-31G", df_basis = "svp-jkfit", **kwargs)
```

`Molecule` object has the information of the geometry, basis-set, density-fitting basis-set.

* `geom_file` is the filename of the molecular geometry. At present, only `.xyz` format is supported.

* `basis` and `df_basis` are set as `6-31G` and `svp-jkfit` as defaults.

* If other parameters are specified in keyword-argument style(`keyname=value`), they will be converted into json format *as it is*.

#### Method

```python
class bagel_util.Method(title, **kwargs)
```

`Method` object has the information of the computational method.

* `title` is the name of the computational method, such as `hf`, `casscf`. This value is essential.

* Other parameters are optional. All the parameters are converted into json *as it is*.

### Example: Single point calculation
 ```python
	from bagel_util.bagel_util import *
    geometry_file = "test.xyz"	#Please prepare some XYZ file!
    mol = Molecule(geom_file = geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    bagel = Bagel(mol, HF(threshold=1.0e-10) )
    print( bagel.to_json() )
 ```

#### HF and CASSCF
Some computational methods, such as `HF` ,`CASSCF`, are defined as special class.

In these class, the `title` is unnecessary. Furthermore, some parameters and default values are specified.

### Example : Geometry Optimization 
 ```python
	from bagel_util.bagel_util import *
    geometry_file = "test.xyz"	#Please prepare some XYZ file!
    mol = Molecule(geom_file= geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    opt = Optimize( method = CASSCF()  )
    bagel = Bagel(mol, opt)
    print( bagel.to_json() )

 ```

#### Optimize

```python
class bagel_util.Optimize(method = HF(), *, target = 0, opttype = "energy", **kwargs):
```

* `method` is an object of `Method` or a list of `Method` objects.

* As for other parameters, please see [here](https://nubakery.org/opt/optimize.html). They will be converted into json *as it is* .

