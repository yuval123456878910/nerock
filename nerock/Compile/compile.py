from .dependesise import *
from llvmlite import ir
from .GC.GC import GC_walk
from functions import LoadGCtoListener
class build_ast:
    def __init__(self):
        self.context = ""
        self.parser: any = None
        self.tree: any = None
        self.GC = None
    def loadFile(self, path: str):
        with open(path, 'r') as file:
            self.context = file.read()

    def build(self):
        input_stream = InputStream(self.context)
        lexer = nerockLexer(input_stream)
        stream = CommonTokenStream(lexer)
        self.parser = nerockParser(stream)
        self.tree = self.parser.prog()

    def walk_compile(self, moudle):
        walker = ParseTreeWalker()
        Lis = Listener(moudle)
        LoadGCtoListener(self.GC, Lis)
        walker.walk(Lis, self.tree)

    def walk_gc(self,moudle):
        walker = ParseTreeWalker()
        GC = GC_walk(moudle)
        walker.walk(GC, self.tree)
        self.GC = GC

    
    def __repr__(self):
        return self.tree.toStringTree(recog=self.parser)

