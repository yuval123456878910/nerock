def FormatType(type) -> str:
    match type:
        case 'f32':
            return 'float'
        case _:
            return type