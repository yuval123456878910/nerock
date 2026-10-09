; ModuleID = "merock"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"

define i1 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  %"a.1" = load i32, i32* %"a"
  %".3" = icmp sgt i32 10, %"a.1"
  ret i1 %".3"
}
