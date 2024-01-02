# Programming Notes

Table of contents
- [Programming Notes](#programming-notes)
  - [Python](#python)
    - [Know for Board](#know-for-board)
    - [Concepts](#concepts)
  - [C](#c)
    - [Know for Board](#know-for-board-1)
    - [Useful links](#useful-links)
    - [Concepts](#concepts-1)
  - [Assembly](#assembly)
    - [Know for Board](#know-for-board-2)
    - [Useful links](#useful-links-1)
    - [Concepts](#concepts-2)
      - [Registers](#registers)
        - [Registers as parameters (in order):](#registers-as-parameters-in-order)
        - [Important registers:](#important-registers)
        - [Other registers](#other-registers)
      - [Fundamental Data Types](#fundamental-data-types)
      - [Accessing Memory](#accessing-memory)
      - [System calls](#system-calls)
      - [Frequently used instructions](#frequently-used-instructions)
  - [Networking](#networking)
    - [Know for Board](#know-for-board-3)
    - [Useful links](#useful-links-2)
    - [Concepts](#concepts-3)


## Python
### Know for Board
- 'with' statement
- socket module
  - send() vs. sendall()
  - clients and servers
- struct module
  - struct pack
  - struct unpack
- official python documentation

### Concepts

## C

### Know for Board
- dynamic memory allocation
  - malloc vs. calloc
  - stack vs. heap
- functions
- loops
  - continue
  - break
- structs
  - nested structs
- memory deferencing
  - "*"
  - "[ ]"
- man pages

### Useful links
https://users.ece.utexas.edu/~adnan/gdb-refcard.pdf

https://dev.to/zirkelc/how-to-iterate-over-c-string-lcj

https://stackoverflow.com/questions/23279119/creating-and-understanding-linked-lists-of-structs-in-c

https://stackoverflow.com/questions/27679969/how-to-create-a-linked-list-of-structs-in-c

https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/tutorial/

https://www.learn-c.org/en/Linked_lists


### Concepts


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

### Useful links
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

### Concepts

We have been using x86_64 intel assmebly.
- On x86, a word is 16 bits (as opposed to ARM where a word is 32 bits).
- It is a 64-bit version, so registers can go up to RAX (quadword / 64 bits) and there are the additional registers r8-r16.

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

Memory can also be accessed by an offset.\
Offsetsa are particularly useful when taking parameters from the stack (rsp + offset) and when accessing elements of an array or string.

#### System calls

#### Frequently used instructions
- mov
- cmp
- test
- jmp
- call
- push/pop
- syscall
- inc
- dec
- add
- sub
- div
- mul
- idiv
- imul
- xor
- ror
- rol
- shr
- shl
- xchg
  - Swaps the contents of the given two registers

## Networking

### Know for Board

### Useful links

https://tacooper.github.io/packet-decoder.html

https://www.geeksforgeeks.org/socket-programming-cc/#

https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/#

https://realpython.com/python-sockets/

https://stackoverflow.com/questions/2408560/non-blocking-console-input

https://stackoverflow.com/questions/11436502/closing-all-threads-with-a-keyboard-interrupt

https://docs.python.org/3/library/socket.html#timeouts-and-the-connect-method


### Concepts