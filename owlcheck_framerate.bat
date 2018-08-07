@echo off

echo ** Checking framerate ** 
echo All three values should be similar for each line
FOR /R %%G IN (*.hdr) do (FIND "fps" "%%G")

echo "Check Complete"

set /P exit=press enter to exit
