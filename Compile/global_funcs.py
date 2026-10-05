def FormatType(type) -> str:
    match type:
        case 'f32':
            return 'float'
        case 'f64':
            return 'double'
        case _:
            return type