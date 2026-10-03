; ModuleID = "merock"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"

define i32 @"test"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %"n.1" = load i32, i32* %"n"
  %".4" = sub i32 %"n.1", 2
  ret i32 %".4"
}

define i32 @"main"()
{
entry:
  %"num" = alloca i32
  store i32 18, i32* %"num"
  %"num.1" = load i32, i32* %"num"
  %"test" = call i32 @"test"(i32 %"num.1")
  ret i32 %"test"
}
