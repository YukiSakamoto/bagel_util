# Bagel Util

## Installation

 ```shell
 pip install git+https://github.com/YukiSakamoto/bagel_util
 ```

## Example

 ```python
	from bagel_util.bagel_util import *
	mol = Molecule(filename = "test.xyz", basis = "6-31G", df_basis = "svp-jkfit")
	method = [Method("hf", maxiter=150)]
	bagel = Bagel(mol,method)
	print(bagel.to_json())
```

`Bagel` requires two arguments, molecule and methods. 

* The first argument, molecule, is a instance of `Molecule` class. 

* The second argument, methods, is a instance of `Molecule` class or the list of `Molecule` object.

* The instalce method `to_json` generate the string of json.

### Example 1: 
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
