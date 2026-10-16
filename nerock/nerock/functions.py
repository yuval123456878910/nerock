from Compile.listen import Listener
from Compile.GC.GC import GC_walk
def LoadGCtoListener(gc: GC_walk, lis: Listener):
    lis.GC_LOAD_FUNCTIONS = gc.Funcs
    lis.GC_LOAD_VAR_REF = gc.VarsPerFunc
    lis.Funcs = gc.Funcs
