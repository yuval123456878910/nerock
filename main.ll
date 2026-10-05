; ModuleID = "merock"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"

define i1 @"main"()
{
entry:
  %".2" = icmp sgt i32 10, 1
  ret i1 %".2"
}
