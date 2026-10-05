from llvmlite import ir

def typeMatch(Vtype: str):
    match Vtype:
        case 'i32':
            return ir.IntType(32)
        case 'i1':
            return ir.IntType(1)
        case 'f32':
            return ir.FloatType()
        case 'v':
            return ir.VoidType()
        case _:
            raise "Unkowen type"


I32 = ir.IntType(32)
I1 = ir.IntType(1)
F32 = ir.FloatType()