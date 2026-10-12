; ModuleID = "merock"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %".2" = getelementptr [4 x i8], [4 x i8]* @".1", i32 0, i32 0
  %"a" = alloca i8*
  store i8* %".2", i8** %"a"
  ret i32 1
}

@".1" = constant [4 x i8] c"wow\00"