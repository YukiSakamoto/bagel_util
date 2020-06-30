# Bagel Util

## Installation

 ```shell
 pip install git+https://github.com/YukiSakamoto/bagel_util
 ```

## Example

### Example 1: Single point calculation
 ```python

	from bagel_util.bagel_util import *
    geometry_file = "test.xyz"	#Please prepare some XYZ file!
    mol = Molecule(filename = geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    opt = Optimize( method = CASSCF()  )
    bagel = Bagel(mol, opt)
    print( bagel.to_json() )

 ```

### Example 2 : Geometry Optimization 
 ```python

	from bagel_util.bagel_util import *
    geometry_file = "test.xyz"	#Please prepare some XYZ file!
    mol = Molecule(filename = geometry_file, basis = "6-31G", df_basis = "svp-jkfit")
    bagel = Bagel(mol, HF(threshold=1.0e-10) )
    print( bagel.to_json() )

 ```
