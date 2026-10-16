import Compile
import Compile.compile
from llvmlite import ir
import llvmlite.binding as llvm
import save
import Compile.GC
B = Compile.compile.build_ast()
B.loadFile('test.nk')
B.build()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

target = llvm.Target.from_default_triple()
tm = target.create_target_machine()

Moudle = ir.Module("merock")
Moudle.triple = llvm.get_default_triple()      # before saving and parsing
Moudle.data_layout = str(tm.target_data)
B.walk_gc(Moudle)
B.walk_compile(Moudle)
file = save.Save(Moudle)
file.save_file("main.ll")
# print(B)


mod = llvm.parse_assembly(str(Moudle))
mod.verify()

engine = llvm.create_mcjit_compiler(mod, tm)
engine.finalize_object()

Moudle.triple = llvm.get_default_triple()
Moudle.data_layout = str(tm.target_data)
