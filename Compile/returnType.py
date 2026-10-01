from llvmlite import ir

def typeMatch(Vtype: str):
    match Vtype:
        case 'i32':
            return ir.IntType(32)
        case 'f32':
            return ir.FloatType(32)
        case 'v':
            return ir.VoidType()
        case _:
            raise "Unkowen type"
