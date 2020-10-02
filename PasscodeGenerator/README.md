# PasscodeGenerator

For WIFI `ATT***` usually come with 10-digits passcode.


This python passcodeGenerator will generate 10 digits passcode.
But from 0000000000 - 9999999999 passcode file size can be up to 100GB.
Therefore, we will split into 10 sub-files. 


Sample:
0000000000 to 1000000000 	- > passcode_0+.txt
1000000000 to 2000000000 	- > passcode_1+.txt
...........
9000000000 to 10000000000 	- > passcode_9+.txt

Each file up to around 11GB.

Modify:
  - output files 'passcode_*+.txt'
  - 'range()'value inside forloop. 

Execute:
 - python3 main.py