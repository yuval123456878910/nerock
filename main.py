import Compile
import Compile.compile
from llvmlite import ir
import save
B = Compile.compile.build_ast()
B.loadFile('test.nk')
B.build()

Moudle = ir.Module("merock")
B.walk_compile(Moudle)
file = save.Save(Moudle)
file.save_file("main.ll")