@echo off
echo ** Checking for navigation sync **
echo Should be greater than 1 for each file
FOR /R %%G IN (*.nav) do (FIND /C "$SPTSMP" "%%G")

echo "Check Complete"

set /P exit=press enter to exit
