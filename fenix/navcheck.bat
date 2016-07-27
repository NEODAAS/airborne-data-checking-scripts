@echo off
FOR %%G IN (*.nav) do (FIND /C "$SPTSMP" "%%G")
set /P exit=press enter to exit
