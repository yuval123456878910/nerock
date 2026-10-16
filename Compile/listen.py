from llvmlite import ir

from .dependesise import *
from . import funcDecl, packager, varDecl, expr, mallocing
from .returnType import typeMatch

class Listener(nerockListener):
	def __init__(self, moudle):

		self.Moudle = moudle
		self.CurrentFunc = ir.Function
		self.builder: any = None
		self.TargetBlock: any = None
		self.last_value = None


		self.variables = {}
		self.FuncTypes: dict[packager.Package, ir.types.FunctionType] = {}
		self.Funcs: dict[str, ir.Function] = {}
		self.GC_LOAD_FUNCTIONS = []
		self.GC_LOAD_VAR_REF = {}
		self.values = {}

		self.mallocated_vars = []

		self.Included_libaries: dict[str, str] = {}

	def enterFunc_decleration(self, ctx):
		funcDecl.funcDecl(self,ctx)
		return super().enterFunc_decleration(ctx)

	def exitFunc_decleration(self, ctx):
		self.variables = {}
		self.values = {}
		self.builder: any = None
		self.TargetBlock: any = None
		self.last_value = None

	def exitDecl_var(self, ctx:nerockParser.Decl_varContext):
		varDecl.varDecl(self, ctx)
		return super().enterDecl_var(ctx)

	def exitExpr(self, ctx:nerockParser.ExprContext):
		expr.Expr(self, ctx)
		return super().exitExpr(ctx)
	
	def exitReturn(self, ctx):
		for ptr in self.mallocated_vars:
			self.builder.call(self.Funcs["free"], [ptr])
		self.builder.ret(self.last_value)
		self.mallocated_vars = []
		return super().enterReturn(ctx)

	def exitDecl_malloc(self, ctx):
		mallocing.mallocCreate(self, ctx)
		return super().exitDecl_malloc(ctx)

	def enterCommand(self, ctx):
		if ctx.return_() is not None or ctx.func_decleration() is not None:
			return
		self._clear()	

	def _clear(self):
		freeFunc = self.Funcs["free"]
		NewGC = self.GC_LOAD_VAR_REF.copy()
		NewGC[self.CurrentFunc.name] = self.GC_LOAD_VAR_REF[self.CurrentFunc.name].copy()

		for ptr in self.GC_LOAD_VAR_REF[self.CurrentFunc.name].items():
		
			if ptr[1].refrences > 0: continue
			if ptr[0] not in self.variables: continue
			slot = self.variables[ptr[0]]
			heap_ptr = self.builder.load(slot, name=f"{ptr[0]}.ptr")
			self.builder.call(freeFunc, [heap_ptr])
			# The return cleanup must not free this allocation again.
			self.mallocated_vars = [
				allocated for allocated in self.mallocated_vars
				if allocated.name != ptr[0]
			]
			NewGC[self.CurrentFunc.name].pop(ptr[0])

		self.GC_LOAD_VAR_REF = NewGC
			
