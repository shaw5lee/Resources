

|  0x400887  | return to main after pwnme
|  0x4006f0  | callme_three
|    ret     |    
|    rdx     |
|    rsi     |
|    rdi     |
|  0x40093c  | Gadget
|  0x400740  | callme_two
|    ret     |    
|    rdx     |
|    rsi     |
|    rdi     |
|  0x40093c  | Gadget 
|  0x400720  | callme_one 
|    ret     |                %16
|    rdx     |                !%16
|    rsi     | 
|    rdi     | 
|  0x40093c  | Gadget         %16
|------------|
|            |
|            | Filler 0x28 
|            |
|------------|

