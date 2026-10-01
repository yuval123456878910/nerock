import Compile
import Compile.compile
from llvmlite import ir

B = Compile.compile.build_ast()
B.loadFile('test.nk')
B.build()

# print(B)
Moudle = ir.Module("merock")
B.walk_compile(Moudle)
print(Moudle)
