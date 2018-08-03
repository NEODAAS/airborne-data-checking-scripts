@echo off
echo ** 1) Checking for navigation sync **
echo Should be > 1 for each file
FOR %%G IN (*.nav) do (FIND /C "$SPTSMP" "%%G")

echo ** 2) Checking framerate ** 
echo All three values should be similar for each line
FOR %%G IN (*.hdr) do (FIND "fps" "%%G")

echo "Checks Complete"

set /P exit=press enter to exit
