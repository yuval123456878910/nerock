# Nerock

> THE README WAS CREATED BY AI

Nerock is a small experimental programming language. This repository contains an ANTLR 4 grammar, generated Python lexer/parser files, and a Python compiler that builds LLVM IR with `llvmlite`.

## Requirements

- Python 3
- The Python packages `antlr4-python3-runtime` and `llvmlite`
- Java is only needed if you regenerate the parser from the grammar

Install the Python packages with:

```powershell
py -m pip install antlr4-python3-runtime llvmlite
```

If you use a virtual environment, activate it before installing and running Nerock.

## Quick start

The current driver in `main.py` reads `test.nk` from the project directory and writes generated LLVM IR to `main.ll`:

```powershell
py main.py
```

To try your own program, put it in `test.nk` first. The driver currently uses that fixed filename; it does not accept a source path as a command-line argument. `main.exe` is a checked-in artifact and is not produced by this command.

A minimal example using currently supported integer functionality is:

```nerock
decl main() -> i32 {
    var answer i32 = 42
    return answer
}
```

After compilation, inspect `main.ll` to see the generated LLVM IR. The current driver verifies the LLVM module and creates a JIT engine, but does not call a function or print its return value.

## Language basics

### Functions

Declare a function with `decl`, its name, a parenthesized parameter list, an optional return type, and a block:

```nerock
decl add(i32 left, i32 right) -> i32 {
    return left + right
}
```

Parameter and return types use the same type names as variables. In the current compiler, include a return type: the implementation expects one when it builds function declarations.

### Variables

Use `var`, a name, a type, `=`, and an expression:

```nerock
var count i32 = 3
var ratio f32 = 1.5
```

### Expressions and calls

The grammar includes integer and floating-point literals, variable names, function calls, `+`, `-`, `*`, `/`, comparisons (`>`, `<`), and equality (`==`). For example:

```nerock
var total i32 = add(2, 3)
```

The grammar accepts more expression forms than the compiler currently implements. At present, the compiler has code paths for integer/float addition and subtraction and the greater-than comparison. Multiplication, division, less-than, equality, and unary minus are not yet implemented by the expression compiler.

### Types

The grammar lists these types:

| Type | Meaning in the grammar |
| --- | --- |
| `i32` | 32-bit integer |
| `f32` | 32-bit floating-point number |
| `i1` | 1-bit boolean value |
| `str` | String |
| `v` | Void |

Compiler support is incomplete: the current type-conversion code supports `i32`, `f32`, `i1`, and `v`, but not `str`. Although string literals are parsed and the expression compiler has a string-literal loader, declaring a `str` variable or using `str` as a function type may fail until string types are wired through the compiler.

## Comments and strings

A `#` starts a comment that continues to the end of its line:

```nerock
# This is a comment
decl main() -> i32 {
    return 0
}
```

The grammar recognizes single- or double-quoted strings. Escape handling depends on the current implementation of `LoadString` in `Compile/expr.py`; check that code for the supported escapes. String support is still incomplete as described above.

## Project layout

- `AST/nerock.g4` — ANTLR grammar
- `AST/nerockLexer.py`, `AST/nerockParser.py`, `AST/nerockListener.py` — generated parser support
- `Compile/` — parse-tree listener and LLVM code generation
- `main.py` — current compiler/JIT driver (reads `test.nk`)
- `save.py` — writes LLVM IR text to a file
- `test.nk` — sample input used by `main.py`
- `main.ll` — generated LLVM IR output

## Current limitations

Nerock is a work in progress. The grammar describes some syntax that code generation does not yet support. In addition to the expression and string limitations above, the `main.py` driver is fixed to `test.nk`, and the JIT engine is created without invoking the compiled function. Errors may therefore occur for programs that parse successfully but use unsupported compiler features.
