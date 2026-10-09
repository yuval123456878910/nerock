; ModuleID = "merock"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  %"a.1" = load i32, i32* %"a"
  %"PLUS" = call i32 @"PLUS"(i32 %"a.1", i32 10)
  ret i32 %"PLUS"
}

define i32 @"PLUS"(i32 %".1", i32 %".2")
{
entry:
  %"num1" = alloca i32
  store i32 %".1", i32* %"num1"
  %"num2" = alloca i32
  store i32 %".2", i32* %"num2"
  %"num1.1" = load i32, i32* %"num1"
  %"num2.1" = load i32, i32* %"num2"
  %".6" = add i32 %"num1.1", %"num2.1"
  ret i32 %".6"
}
