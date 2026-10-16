; ModuleID = "merock"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"

declare void @"free"(i8* %".1")

define i32 @"main"()
{
entry:
  %".2" = sdiv i32 9, 2
  ret i32 %".2"
}
