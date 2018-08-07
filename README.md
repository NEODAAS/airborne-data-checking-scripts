# Data Checking scripts for Operations Team #

Scripts are written as Windows .bat scripts and are designed to be run by copying to the same directory as data and double clicking on them.
The scripts are designed to give a quick indication if common problems are present in the data.

## Fenix ##

**fenixcheck.bat**

General script for checking Fenix data.

Runs the following checks:

1) Navigation Sync. Prints the number of times `$SPTSMP` occurs in the .nav files. It should be > 0 if the navigation sync is working correctly.

2) Framerate Check. Prints the values for `fps`, `fps_set` and `fps_qpf` in the .hdr files. These values should all be similar if everything is working correctly. If they aren't indicates framerate hasn't been recorded correctly.

## Owl ##

**owlcheck_navsync**

Prints the number of times `$SPTSMP` occurs in the .nav files. It should be > 0 if the navigation sync is working correctly.

**owlcheck_framerate**

Prints the values for `fps`, `fps_set` and `fps_qpf` in the .hdr files. These values should all be similar if everything is working correctly. If they aren't indicates framerate hasn't been recorded correctly. As Owl records the capture data and calibration data as seperate files this prints a lot more output than the Fenix version.


