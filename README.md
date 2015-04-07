A python scripts that takes encrypted passwords and checks if any are dictionary words.

For this script copy /etc/shadow to /tmp/passwords.txt. Then run 
$python crack.py
to see if any users on your system have passwords that are dictionary words.

This script's dictionary.txt comes from the word list of ubuntu package 'wamerican'. 

Noah Lidell
April 2015
# unix-passwd-cracker
