# Bagel Util

## Installation

 ```shell
 pip install git+https://github.com/YukiSakamoto/bagel_util
 ```

## Usage and Examples

### Example 1: 

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

`Bagel` requires two arguments, molecule and methods. 

* The first argument `molecule` is an object of `Molecule` class. 

* The second argument `methods` is an object of `Method` class or the list of `Method` object.

* `to_json()` function generates the string of json.

#### Molecule

```python
class Molecule(*, geom_file = None, basis = "6-31G", df_basis = "svp-jkfit", **kwargs)
```

`Molecule` object has the information of the geometry, basis-set, density-fitting basis-set.

* The `geom_file` is the filename of the molecular geometry. At present, only `.xyz` format is supported.

Other parameters are all optional. `basis` and `df_basis` are set as `6-31G` and `svp-jkfit` as defaults.

#### Method

```python
class Method(title, **kwargs)
```

`Method` object has the information of the computational method.

* The 1st argument `title` is the name of the computational method, such as `hf`, `casscf`.

* Other parameters are optional. All the parameters are converted into json *as it is*.


### Example 3: 
 ```python
	from bagel_util.bagel_util import *
	mol = Molecule(filename = "test.xyz", basis = "6-31G", df_basis = "svp-jkfit")
	method = [Method("hf", threshold=1.0e-8, maxiter=150)]
	bagel = Bagel(mol,method)
	print(bagel.to_json())
 ```

### Example 1: Single point calculation
 ```python

	from bagel_util.bagel_util import *
    geometry_file = "test.xyz"	#Please prepare some XYZ file!
    mol = Molecule(filename = geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    bagel = Bagel(mol, HF(threshold=1.0e-10) )
    print( bagel.to_json() )

 ```

### Example 2 : Geometry Optimization 
 ```python

	from bagel_util.bagel_util import *
    geometry_file = "test.xyz"	#Please prepare some XYZ file!
    mol = Molecule(filename = geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    opt = Optimize( method = CASSCF()  )
    bagel = Bagel(mol, opt)
    print( bagel.to_json() )

 ```
