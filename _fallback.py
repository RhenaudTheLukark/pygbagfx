import pathlib
import sys as _sys
import cppyy as _cppy

_cppy.include('png.h')
_cppy.load_library('libpng')
_cppy.include(pathlib.Path(__file__).parent.resolve() / 'src' / '_gbagfx.c')
_sys.modules['pygbagfx.src._gbagfx'] = _cppy.gbl.PyInit__gbagfx()
from .src import *

print('Running gbagfx from c source')

# clean up globals
del(globals()['pathlib'])