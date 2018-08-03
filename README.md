# Data Checking scripts for Operations Team #

## Fenix ##

**fenixcheck.bat**

General script for checking Fenix data. Copy script to Fenix data directory and double click.

Runs the following checks:

1) Navigation Sync. Prints the number of times `$SPTSMP` occurs in the .nav files. It should be > 0 if the navigation sync is working correctly.

2) Framerate Check. Prints the values for `fps`, `fps_set` and `fps_qpf` in the .hdr files. These values should all be similar if everything is working correctly. If they aren't indicates framerate hasn't been recorded correctly.
