# Programming Notes

Table of contents
- [Programming Notes](#programming-notes)
  - [Python](#python)
    - [Know for Board](#know-for-board)
      - ['with' statement](#with-statement)
      - [socket module](#socket-module)
        - [send() vs. sendall()](#send-vs-sendall)
        - [clients and servers](#clients-and-servers)
      - [struct module](#struct-module)
  - [C](#c)
    - [Know for Board](#know-for-board-1)
      - [dynamic memory allocation](#dynamic-memory-allocation)
      - [functions](#functions)
      - [loops](#loops)
      - [structs](#structs)
      - [memory deferencing](#memory-deferencing)
      - [man pages](#man-pages)
      - [(Additional note) networking](#additional-note-networking)
  - [Assembly](#assembly)
    - [Know for Board](#know-for-board-2)
    - [General Info](#general-info)
      - [Registers](#registers)
        - [Registers as parameters (in order):](#registers-as-parameters-in-order)
        - [Important registers:](#important-registers)
        - [Other registers](#other-registers)
      - [Fundamental Data Types](#fundamental-data-types)
      - [Accessing Memory](#accessing-memory)
      - [System calls](#system-calls)
      - [Flags](#flags)
      - [Frequently used instructions](#frequently-used-instructions)
  - [Networking](#networking)
    - [General Info](#general-info-1)
  - [Useful Links](#useful-links)
    - [Python](#python-1)
    - [C](#c-1)
    - [Assembly](#assembly-1)
    - [Networking](#networking-1)


## Python
### Know for Board
#### 'with' statement
  - Ensures proper acquisition and release of resources
    - aka, handles exceptions and in the case of files, closes it once done
#### socket module
  ##### send() vs. sendall()
    - send(): equivalent to the C/syscall send() method
      - It may send less bytes than requested, but will return how many bytes were actually sent
    - sendall(): high-level Python-only method that sends the entire buffer passed
      - Includes the "keep trying" implementation of send() that we did by hand
      - Returns `None` on success, or raises an exception on error. 
        - There is no way to know how much data was sent when an exception is raised
        - But, an exception is not generally raised when not all the data was sent anyways (errors happen for other reasons)
  ##### clients and servers
    - Server
      - create socket
      - bind to address
      - listen at that address
        - Then accept a connection when it comes in
        - Can recv and send on this connection
      - Once client disconnects, start listening again for new connections
      - close the socket
      - Can use threads for keyboard input during socket listening
    - Client
      - create socket
      - connect to the address
        - Can send a recv on this connection
        - Should send a closing message to the server
        - I decided to determine that the server was closed when no response was received
      - close the socket
    - Python socket module is *not* threadsafe
    - In my implementation, to account for not all bytes being received at once;
      - I had an initial blocking recv
      - Then had a while-loop of non-blocking recv's (with the flag MSG_DONTWAIT) and excepted the Blocking IO error to know that comm was done
#### struct module
  - struct pack
  - struct unpack

## C

### Know for Board
#### dynamic memory allocation
  - malloc vs. calloc
  - stack vs. heap
#### functions
#### loops
  - continue
  - break
#### structs
  - nested structs
#### memory deferencing
  - "*"
  - "[ ]"
#### man pages
#### (Additional note) networking
  - For my recv, I MSG_PEEK flagged the recv, and continued to recv until the amount received was less than the buffer size
  - Once I had my size, I allocated that memory and then received `n` bytes with recv() into the allocated memory

## Assembly

### Know for Board
- register sizing
- memory access
- test vs. cmp
- base + offset
- loops/ jmp
- function arguments
- caller vs. calle-saved registers
- intel manual

### General Info

We have been using x86_64 intel assmebly.
- On x86, a word is 16 bits (as opposed to ARM where a word is 32 bits).
- It is a 64-bit version, so registers can go up to RAX (quadword / 64 bits) and there are the additional registers r8-r16.
  - Must use REX prefix for many of these operations
    - Uses 64 bits instead of the default 32 bits
    - doing so prevents usage within the intruction of the high-byte part: ah, bh, ch, dh

#### Registers

##### Registers as parameters (in order):
|               | rdi | rsi | rdx   | rcx   | r8 | r9 | Stack (rsp)  |
|---------------|-----|-----|-------|-------|----|----|--------------|
| Param #       | 1   | 2   | 3     | 4     | 5  | 6  | 7+           |
|              | Scratch | Scratch | Scratch | Scratch | Scratch | Scratch | Preserved |
| h/l char | -   | -   | dh dl | ch cl | -  | -  | rsp + offset |

##### Important registers:
|        | rax | rbp | rsp | rbx |
|--------|-----|-----|-----|-----|
| Info   | Return value | Frame pointer | Stack pointer | "base" pointer |
|        | Scratch | Preserved | Preserved | Preserved |
| h/l char | ah al | - | - | bh bl |

##### Other registers
64-bit scratch registers: r8, r9, r10, r11\
64-bit preserved registers: r12, r13, r14, r15

Special purpose:
- rip: points to the next instruction to be executed
  - branch/jmp modify this register directly
  - addresses are always 64 bits, so eip and ip are rarely used
- rflags: stores flags as bits
  - Generally don't need to worry about these because condition instructions check them
- the 'mov' instruction cannot be used on these. They instead have specialized instructions for getting and setting their values.

#### Fundamental Data Types
| byte | word | double word | quadword | double quadword |
| --- | --- | --- | --- | --- |
| 8 bits | 16 bits | 32 bits | 64 bits | 128 bits |
| 1 byte | 2 bytes | 4 bytes | 8 bytes | 16 bytes |
| char   | short   | int, float | long, double, pointer, size_t | long double |
| h/l, or ##l | ## | e## | r## | r##:r&& |
| r#b | r#w | r#d | r# | r#:r& |

#### Accessing Memory
Any instruction can only contain a maximum of one memory location.\
i.e.:\
mov rax, QWORD[rdx] -> Okay \
mov BYTE[al], cl -> Okay\
mov WORD[ax], WORD[cx] -> Invalid

Memory does not require a prefix, only square brackets, but without a given size prefix the compiler makes inferences on what the size should be.

The register the data is being moved to must be the same size as the data being accessed. Size prefixing helps.

In x86_64 Intel assembly, pointers are 8 bytes (QWORD).

Memory can also be accessed by an offset.

Offsets are particularly useful when taking parameters from the stack (rsp + offset) and when accessing elements of an array or string.

#### System calls

#### Flags

| Abbreviation | Description | Category | =1 | =0 |
| ------------ | ----------- | -------- | --- | --- |
| CF | Carry flag | Status | CY(Carry) | NC(No Carry) |
| PF | Parity flag | Status | PE(Parity Even) | PO(Parity Odd) |
| AF | Auxillary Carry Flag | Status | AC(Auxillary Carry) | NA(No Auxillary Carry) |
| ZF | Zero Flag | Status | ZR(Zero) | NZ(Not Zero) |
| SF | Sign Flag | Status | NG(Negative) | PL(Positive) |
| OF | Overflow Flag | Status | OV(Overflow) | NV(Not Overflow) |

#### Frequently used instructions
- mov
  - Both the source and destination must be the same size
  - The only instruction which supports QWORD immediate operands.
    - ex: you can do `mov rax, some_huge_constant`, but not `add rax, some_huge_constant`
  - The high dword of the destination for mov of 32-bit registers is implicitly set to zero. 
    - This zero-ing however does not occur for words or bytes
    - This behavior applies to many other instructions as well
- movzx
  - "Move with zero-extended"
  - Moves smaller registers into larger ones, zeroing the higher, unspecifified portion of the destination/larger register.
- movsx
  - Same as movzx, but also extends the sign
- cmp
  - Subtracts the second operand from the first operand, and sets the flags (CF, OF, SF, ZF, AF, PF) accordingly
  - The Jcc, CMOVcc, and SETcc instructions are based off the flags set by this instruction
- test
  - Computes the bitwise logical AND of the two operands, then sets the SF, ZF, and PF flags according to the result
  - Is marginally faster than cmp when checking if a value is zero
  - Checks for parity, sign, and zero-ness
- jmp
  - Within the *jcc* family
  - Transfers program control to a different point in the instruction stream (without recording return information)
    - Changes the instruction pointer (rip) to the location given after jmp
  - j*cc* are jump conditional instructions.
    - Will jump to the given location *if* the designated flag is set accordingly
    - ex:
      - jz: jump if zero flag is true (works the same as je)
      - jc: jump if carry flag is true 
      - jg: jump if greater (ZF=0 and SF=OF) (not equal, but the sign is positive if no overflow, and negative if overflow)
      - jge: jump if greater than or equal to (SF=OF)
      - jle: jump if less than or equal to (SF!=OF)
      - jp: jump if parity (even number)
- call
  - it is important to push callee-saved registers onto the stack (non preserved) that will be used later
    - a called function may modify non preserved/scratch registers
  - the stack should be aligned in 16 byte "chunks"; ie, the stack pointer should be divisible by 16 bytes.
    - Can ensure this by only pushing 16 byte increments onto the stack before calling a function
    - Or by performing `push rbp` `mov rsp, rbp` at the beginning of the code.
    - 8 bytes is a quadword, which is also the size of pointers. Stack alignment will be an issue when calling functions with pointer parameters (and long, double, size_t)
- push/pop
  - pop loads the value at the top of the stack into the destination operand (a register or memory), then increments the stack pointer
  - push decrements the stack pointer, then stores the source operand (register or memory) at the top of the stack
  - the operand size (16, 32, or 64) determines the amount by which the stack pointer is incremented (2, 4, or 8)
  - adding bytes (only 8 bits) is not supported.
- syscall
  - invokes an OS system-call handler at privilege level 0
  - the register RAX stores the value of the system call number
    - Can be found online
      - https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86_64-64_bit
    - Or, can find installation-specific values by using `grep` within `usr/include`.
      - The flags and mode are also defined in `usr/include`
- inc
  - adds 1 to the destination operand (register or memory)
  - unlike add, does not affect the Carry Flag (CF)
  - Useful for counters
- dec
  - subtracts 1 from the destination operand (register or memory)
  - unlike sub, does not affect the Carry Flag (CF)
  - Useful for counters
- add
  - Adds the values of the first and second operands, then stores the result in the first operand
  - when an immediate value is used as an operand, it is sign-extended to the length of the first operand
  - works for signed and unsigned operations
  - Updates the CF, OF, and SF flags
- sub
  - performs integer subtraction on the values of the first and second operands, then stores the result in the first operand
  - when an immediate value is used as an operand, it is sign-extended to the length of the first operand
  - works for signed and unsigned operations
  - Updates the CF, OF, and SF flags
- mul
  - unsigned multiplication of RAX and the operand
  - result is stored in RDX:RAX for 16, 32, and 64 bit registers
  - OF and CF flags are cleared if the high-order bytes bits of the product are zero, or set if otherwise
- div
  - divides the unsigned value in the AX, DX:AX, EDX:EAX, or RDX:RAX registers by the given operand
  - the result is stored in rdx:rax
    - rax is the quotient
    - rdx is the remainder
  - Does not affect flags
- imul
  - signed multiplication
  - with one operand, works like mul but signed
  - with two operands, the first operand is multiplied by the second, then the result is truncated and stored in the first
  - with three operands, the second two operands are multiplied together, then truncated and stored in the first operand register
- idiv
  - Same as div, but is signed
- xor
  - Performs the logical exclusive-or operation on two registers
  - can be used with duplicate registers to zero it out
    - a bit more efficient than `mov r, 0`
- ror
- rol
- shr
- shl
- xchg
  - Swaps the contents of the given two registers
  - Neither argument can be an immediate value. Both must be either registers or a register and memory.
  - 32-bit registers implicitly zeroes the high dword.
- lea
  - "Load effective address"
  - loads the address of the second operand into the first
  - important when you would like to calculate of an address inside brackets, and then place that calculated address into the dest operand
  - never looks at the contents at a memory address
  - ex: `lea ecx, [msg + 4 + eax*4 + edx]`
  - better than mov for address math

## Networking

### General Info

## Useful Links
### Python

https://www.geeksforgeeks.org/with-statement-in-python/#

### C
https://users.ece.utexas.edu/~adnan/gdb-refcard.pdf

https://dev.to/zirkelc/how-to-iterate-over-c-string-lcj

https://stackoverflow.com/questions/23279119/creating-and-understanding-linked-lists-of-structs-in-c

https://stackoverflow.com/questions/27679969/how-to-create-a-linked-list-of-structs-in-c

https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/tutorial/

https://www.learn-c.org/en/Linked_lists

### Assembly
https://github.com/cyrus-and/gdb-dashboard

https://hacs208e.umd.edu/weeks/05/05-IntroductionToX64.html

https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86_64-64_bit

https://www.tortall.net/projects/yasm/manual/html/nasm-pseudop.html

http://6.s081.scripts.mit.edu/sp18/x86-64-architecture-guide.html

https://www.cs.uaf.edu/2017/fall/cs301/lecture/09_11_registers.html#:~:text=rax%20is%20the%2064%2Dbit,processors%20with%20the%2080386%20CPU.

https://www.cs.virginia.edu/~evans/cs216/guides/x86.html

https://www.tortall.net/projects/yasm/manual/html/index.html

https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/

https://www.asciitable.com/

https://www.tutorialspoint.com/assembly_programming/assembly_file_management.htm

https://tldp.org/HOWTO/Assembly-HOWTO/

https://www.tutorialspoint.com/assembly_programming/assembly_system_calls.htm

https://www.reddit.com/r/C_Programming/comments/l8zs5a/calling_printf_from_nasm_cause_seg_fault/

https://stackoverflow.com/questions/45500399/why-can-i-access-lower-dword-word-byte-in-a-register-but-not-higher

https://cs.brown.edu/courses/cs033/docs/guides/x64_cheatsheet.pdf

https://staffwww.fullcoll.edu/aclifton/cs241/lecture-registers-simple-loops.html

https://www.mwftr.com/uC12/416_05_F12_x86_Assembly%202.pdf

https://home.adelphi.edu/~siegfried/cs174/174l4.pdf

### Networking
https://tacooper.github.io/packet-decoder.html

https://www.geeksforgeeks.org/socket-programming-cc/#

https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/#

https://realpython.com/python-sockets/

https://stackoverflow.com/questions/2408560/non-blocking-console-input

https://stackoverflow.com/questions/11436502/closing-all-threads-with-a-keyboard-interrupt

https://docs.python.org/3/library/socket.html#timeouts-and-the-connect-method