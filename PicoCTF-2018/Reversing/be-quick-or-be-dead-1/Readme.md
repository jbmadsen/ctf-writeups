# be-quick-or-be-dead-1

**Category:** Reversing

**Points:** 200

## Task

> You find [this](https://www.youtube.com/watch?v=CTt1vk9nM9c) when searching for some music, which leads you to [be-quick-or-be-dead-1](Files/be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_3_aeb48854203a88fb1da963f41ae06a1c. 


## Hints

> What will the key finally be?


## What do we need to know?

Stuff about gdb

TODO

## Solution

With only a binary file supplied, lets have a look at what we've got:

```bash
file be-quick-or-be-dead-1
```

> be-quick-or-be-dead-1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=909cc4117c2c766583b0633d70b84771e50160d6, not stripped

So, an executable.
Trying to execute the program, 

```bash
./be-quick-or-be-dead-1
```

gives us the following:

> Be Quick Or Be Dead 1<br/>
> == == == == == == == <br/>
> <br/>
> Calculating key...<br/>
> You need a faster machine. Bye bye.<br/>

Running [strings](https://linux.die.net/man/1/strings) and [grepping](https://linux.die.net/man/1/grep) for "pico{" returned nothing as well.

Lets run the file trough [gdb](https://www.gnu.org/software/gdb/) instead,

```bash
gdb be-quick-or-be-dead-1
```

and have a look at the disassembly of the main function, and take it from there:

```gdb
(gdb) set disassembly-flavor intel

(gdb) disassemble main
```

Returns the main function:

```assembly
Dump of assembler code for function main:
   0x0000000000400827 <+0>:     push   rbp
   0x0000000000400828 <+1>:     mov    rbp,rsp
   0x000000000040082b <+4>:     sub    rsp,0x10
   0x000000000040082f <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000400832 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000400836 <+15>:    mov    eax,0x0
   0x000000000040083b <+20>:    call   0x4007e9 <header>
   0x0000000000400840 <+25>:    mov    eax,0x0
   0x0000000000400845 <+30>:    call   0x400742 <set_timer>
   0x000000000040084a <+35>:    mov    eax,0x0
   0x000000000040084f <+40>:    call   0x400796 <get_key>
   0x0000000000400854 <+45>:    mov    eax,0x0
   0x0000000000400859 <+50>:    call   0x4007c1 <print_flag>
   0x000000000040085e <+55>:    mov    eax,0x0
   0x0000000000400863 <+60>:    leave
   0x0000000000400864 <+61>:    ret
End of assembler dump.
```

We have some code, with four interesting functions. Lets set a breakpoint before the function <set_timer>, as it sounds like the suspicsious function that wont let us do our thing, when executing the program normally, and then run the program in gdb:

```gdb
(gdb) break *0x0000000000400845

(gdb) run
```

And we get:

> Be Quick Or Be Dead 1<br/>
> == == == == == == == <br/>
> <br/>
> Breakpoint 1, 0x0000000000400845 in main ()<br/>

We get hit the breakpoint, and executions stops. 

First time around I tried this, I got excited and jumped straigt to the <print_flag> function, but it appears to be scrambled, so it probably needs the <get_key> function as well. So we jump just below the set timer:

```gdb
(gdb) jump *0x000000000040084a
```

and we get the following continuation of the program:

> Continuing at 0x40084a.<br/>
> Calculating key...<br/>
> Done calculating key<br/>
> Printing flag:<br/>
> picoCTF{why_bother_doing_unnecessary_computation_27f28e71}<br/>
> [Inferior 1 (process 25) exited normally]

And there is our flag!

## Flag

> picoCTF{why_bother_doing_unnecessary_computation_27f28e71}
