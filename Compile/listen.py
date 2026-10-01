from llvmlite import ir

from .dependesise import *
from . import funcDecl, packager, varDecl, expr
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
		self.values = {}

	def enterFunc_decleration(self, ctx):
		funcDecl.funcDecl(self,ctx)
		return super().enterFunc_decleration(ctx)

	def exitDecl_var(self, ctx:nerockParser.Decl_varContext):
		varDecl.varDecl(self, ctx)
		return super().enterDecl_var(ctx)

	def enterExpr(self, ctx:nerockParser.ExprContext):
		expr.Expr(self, ctx)
		return super().exitExpr(ctx)
