; ModuleID = "merock"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"

define i32 @"test"(i32 %".1")
{
entry:
  %"hello" = alloca i32
  store i32 %".1", i32* %"hello"
  %"hello.1" = load i32, i32* %"hello"
  %".4" = add i32 %"hello.1", 10
  ret i32 %".4"
}

define i32 @"main"(i32 %".1")
{
entry:
  %"dw" = alloca i32
  store i32 %".1", i32* %"dw"
  %"i" = alloca i32
  store i32 10, i32* %"i"
  %"i.1" = load i32, i32* %"i"
  %"test" = call i32 @"test"(i32 %"i.1")
  ret i32 %"test"
}
