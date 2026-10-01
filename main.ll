; ModuleID = "merock"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define float @"main"(i32 %".1")
{
entry:
  %"wow" = alloca float
  store float 0x3ff99999a0000000, float* %"wow"
  ret float 0x3ff99999a0000000
}
