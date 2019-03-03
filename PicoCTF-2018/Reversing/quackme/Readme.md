# quackme

**Category:** Reversing

**Points:** 200

## Task

> Can you deal with the Duck Web? Get us the flag from this [program](Files/main). You can also find the program in /problems/quackme_3_9a15a74731538ce2076cd6590cf9e6ca. 


## Hints

> Objdump or something similar is probably a good place to start.


## What do we need to know?

TODO

## Solution

Lets have a look at what we've got in the binary:

```bash
file main
```

> main: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=09dbd61b7f2aa72b7c04e2ab78a4cc9c437c4ac9, not stripped

An executable.
Trying to execute the program, 

```bash
./main
```

gives us a user input and a no response, which probably indicates that is needs a password input to output the flag.

> You have now entered the Duck Web, and you're in for a honkin' good time.<br/>
> Can you figure out my trick?<br/>
> [User input:] AAA<br/>
> That's all folks.<br/>

Running [strings](https://linux.die.net/man/1/strings) and [grepping](https://linux.die.net/man/1/grep) for "pico{" returned nothing as well. Without grepping we get:

> ...<br/>
t$,U<br/>
[^_]<br/>
You have now entered the Duck Web, and you're in for a honkin' good time.<br/>
Can you figure out my trick?<br/>
O+50<br/>
No line read...<br/>
malloc() returned NULL. Out of Memory<br/>
You are winner!<br/>
That's all folks.<br/>
;*2$"<br/>
...<br/>
sekrutBuffer<br/>
...<br/>
main<br/>
_Jv_RegisterClasses<br/>
do_magic<br/>
...<br/>


A lot strings, but no flag, and nothing that looks like an encoded flag right of the bat. However, sekrutBuffer and do_magic does look funny.

Lets stop ignoring the hint, and actually run [objdump](https://linux.die.net/man/1/objdump) on the file:

```bash
objdump -s -d -M intel -S --no-show-raw-insn main > main.dump.txt
```

where -s displays the full contents of any sections, -d disassemles the file, -M intel for intel flavored assembly, and -S display source code intermixed with disassembly, if possible, and --no-show-raw-insn ignores the byte instructions so they won't be displayed.

You can have a look at the [full dump file](./Solution/main.dump.txt). Here I will only go through the steps needed to recover the flag.

Having looked through the file, as well as the strings output, there are three interesting places to dig into: main, do_magic and sekrutBuffer.

The main function, as a place to start:

```assembly
08048715 <main>:
 8048715:	lea    ecx,[esp+0x4]
 8048719:	and    esp,0xfffffff0
 804871c:	push   DWORD PTR [ecx-0x4]
 804871f:	push   ebp
 8048720:	mov    ebp,esp
 8048722:	push   ecx
 8048723:	sub    esp,0x4
 8048726:	mov    eax,ds:0x804a044
 804872b:	push   0x0
 804872d:	push   0x2
 804872f:	push   0x0
 8048731:	push   eax
 8048732:	call   80484b0 <setvbuf@plt>
 8048737:	add    esp,0x10
 804873a:	sub    esp,0xc
 804873d:	push   0x80487f0
 8048742:	call   8048470 <puts@plt>
 8048747:	add    esp,0x10
 804874a:	call   8048642 <do_magic>
 804874f:	sub    esp,0xc
 8048752:	push   0x80488bb
 8048757:	call   8048470 <puts@plt>
 804875c:	add    esp,0x10
 804875f:	mov    eax,0x0
 8048764:	mov    ecx,DWORD PTR [ebp-0x4]
 8048767:	leave  
 8048768:	lea    esp,[ecx-0x4]
 804876b:	ret    
 804876c:	xchg   ax,ax
 804876e:	xchg   ax,ax
```

Without going too much into details about what is going on there, we can see 3 function calls in the main function:

* \<puts@plt>
* <do_magic>
* \<puts@plt>

Puts displays something to the screen, then the do_magic function runs, and something is output to the screen again in the last puts. So, do_magic is the second place of interest, and probably where the "magic" happens:

```assembly
08048642 <do_magic>:
 8048642:	push   ebp
 8048643:	mov    ebp,esp
 8048645:	sub    esp,0x28
 8048648:	call   80485db <read_input>
 804864d:	mov    DWORD PTR [ebp-0x14],eax
 8048650:	sub    esp,0xc
 8048653:	push   DWORD PTR [ebp-0x14]
 8048656:	call   8048490 <strlen@plt>
 804865b:	add    esp,0x10
 804865e:	mov    DWORD PTR [ebp-0x10],eax
 8048661:	mov    eax,DWORD PTR [ebp-0x10]
 8048664:	add    eax,0x1
 8048667:	sub    esp,0xc
 804866a:	push   eax
 804866b:	call   8048460 <malloc@plt>
 8048670:	add    esp,0x10
 8048673:	mov    DWORD PTR [ebp-0xc],eax
 8048676:	cmp    DWORD PTR [ebp-0xc],0x0
 804867a:	jne    8048696 <do_magic+0x54>
 804867c:	sub    esp,0xc
 804867f:	push   0x8048884
 8048684:	call   8048470 <puts@plt>
 8048689:	add    esp,0x10
 804868c:	sub    esp,0xc
 804868f:	push   0xffffffff
 8048691:	call   8048480 <exit@plt>
 8048696:	mov    eax,DWORD PTR [ebp-0x10]
 8048699:	add    eax,0x1
 804869c:	sub    esp,0x4
 804869f:	push   eax
 80486a0:	push   0x0
 80486a2:	push   DWORD PTR [ebp-0xc]
 80486a5:	call   80484c0 <memset@plt>
 80486aa:	add    esp,0x10
 80486ad:	mov    DWORD PTR [ebp-0x1c],0x0
 80486b4:	mov    DWORD PTR [ebp-0x18],0x0
 80486bb:	jmp    804870b <do_magic+0xc9>
 80486bd:	mov    eax,DWORD PTR [ebp-0x18]
 80486c0:	add    eax,0x8048858
 80486c5:	movzx  ecx,BYTE PTR [eax]
 80486c8:	mov    edx,DWORD PTR [ebp-0x18]
 80486cb:	mov    eax,DWORD PTR [ebp-0x14]
 80486ce:	add    eax,edx
 80486d0:	movzx  eax,BYTE PTR [eax]
 80486d3:	xor    eax,ecx
 80486d5:	mov    BYTE PTR [ebp-0x1d],al
 80486d8:	mov    edx,DWORD PTR ds:0x804a038
 80486de:	mov    eax,DWORD PTR [ebp-0x18]
 80486e1:	add    eax,edx
 80486e3:	movzx  eax,BYTE PTR [eax]
 80486e6:	cmp    al,BYTE PTR [ebp-0x1d]
 80486e9:	jne    80486ef <do_magic+0xad>
 80486eb:	add    DWORD PTR [ebp-0x1c],0x1
 80486ef:	cmp    DWORD PTR [ebp-0x1c],0x19
 80486f3:	jne    8048707 <do_magic+0xc5>
 80486f5:	sub    esp,0xc
 80486f8:	push   0x80488ab
 80486fd:	call   8048470 <puts@plt>
 8048702:	add    esp,0x10
 8048705:	jmp    8048713 <do_magic+0xd1>
 8048707:	add    DWORD PTR [ebp-0x18],0x1
 804870b:	mov    eax,DWORD PTR [ebp-0x18]
 804870e:	cmp    eax,DWORD PTR [ebp-0x10]
 8048711:	jl     80486bd <do_magic+0x7b>
 8048713:	leave  
 8048714:	ret    
```

This is quite the long function to look at. Instead of going through it start to finish, lets jump through it, and have a look at the larger pieces that could be interesting at first glance.

```assembly
 8048648:	call   80485db <read_input>
 ...
 804866b:	call   8048460 <malloc@plt>
 ...
 8048676:	cmp    DWORD PTR [ebp-0xc],0x0
 804867a:	jne    8048696 <do_magic+0x54>
 ...
 804867f:	push   0x8048884
 8048684:	call   8048470 <puts@plt>
```

In the first batch of noticable stuff, we read user input, allocate some bytes using malloc, do a comparison against 0, and jump if not equal, else we push something to the stack and prints it (if comparison to zero is true).
Lets use [gdb](https://www.gnu.org/software/gdb/) to have a look at whats at these memory adresses.

So we fire up gdb:

```bash
gdb main
```

and print the first 30 characters from 0x8048884:

```gdb
(gdb) x/1s 0x8048884
0x8048884:      "malloc() returned NULL. Out of Memory\n"
```

And following that in our do_magic objdump, we can see it calls

```assembly
 8048691:	call   8048480 <exit@plt>
```

after that last puts, which exits. That makes sense. So we assume the comarison at 804867a went and continues from the jump to 8048696.
So we continue looking through the do_magic function:

```assembly
 8048696:	mov    eax,DWORD PTR [ebp-0x10]
 ...
 80486bb:	jmp    804870b <do_magic+0xc9>
 ...
 804870b:	mov    eax,DWORD PTR [ebp-0x18]
 804870e:	cmp    eax,DWORD PTR [ebp-0x10]
 8048711:	jl     80486bd <do_magic+0x7b>
 8048713:	leave  
 8048714:	ret    
```

So at 8048696 we push some content into eax, and more or less after we jump to 804870b. There we compares two variables and jump if less than. Lets assume we don't leave the function and follow the jump back.

```assembly
 80486bd:	mov    eax,DWORD PTR [ebp-0x18]
 80486c0:	add    eax,0x8048858
 ...
 80486d3:	xor    eax,ecx
```

Here we move data into eax and then adds data from some memory address into eax before we xor some things. Lets have a look through gdb again:

```gdb
(gdb) x/1s 0x8048858
0x8048858 <sekrutBuffer>:       ")\006\026O+50\036Q\033[\024K\b]+R\027\001W\026\021\\\a]"
```

So it loads in the secretbuffer, which is interesting. And it doesn't look like a normal string, which is probably why [strings](https://linux.die.net/man/1/strings) couldn't pick up on it.  
This is probably whats getting xor'd to get the flag. 
Lets have a go at xor'ing the sekrutBuffer string with "pico{}" to see if that reveals anything useful.

Since we can't really work with the string data from sekrutBuffer, we need it in hexadecimal instead:

```gdb
(gdb) x/32x 0x8048858
0x8048858 <sekrutBuffer>:       0x29    0x06    0x16    0x4f    0x2b    0x35    0x30    0x1e
0x8048860 <sekrutBuffer+8>:     0x51    0x1b    0x5b    0x14    0x4b    0x08    0x5d    0x2b
0x8048868 <sekrutBuffer+16>:    0x52    0x17    0x01    0x57    0x16    0x11    0x5c    0x07
0x8048870 <sekrutBuffer+24>:    0x5d    0x00    0x4e    0x6f    0x20    0x6c    0x69    0x6e
```

We can then write a small [python program](./Solution/xor.py) to xor the masked data to see if it is anything useful.

```python
msg = "picoCTF{"
data = '2906164f2b35301e511b5b144b085d2b5217015716115c075d004e6f206c696e'
xor = bytes.fromhex(data).decode('utf-8')

flag = ''
for i in range(len(msg)):
    data = ord(xor[i]) ^ ord(msg[i])
    flag += chr(data)

print(flag)
```

> You have

So that looks suspiciously like real text! Running strings and grepping for "You have":

```
strings main | grep "You have"
```

returns only:

> You have now entered the Duck Web, and you're in for a honkin' good time.

So lets run the python code again with `msg = "You have now entered the Duck Web, and you're in for a honkin' good time."`, and remembering `len(xor)` this time, as it is shorter.

It gives:

> picoCTF{qu4ckm3_7ed36e4b}D;KL>

This, or the first part at least, looks a lot like a flag!
Lets run the program and test the input:

```bash
./main
```

> You have now entered the Duck Web, and you're in for a honkin' good time.<br/>
> Can you figure out my trick?<br/>
> [User input:] picoCTF{qu4ckm3_7ed36e4b}<br/>
> You are winner!<br/>
> That's all folks.<br/>

So that's all folks. And quite fun how the flag is the solution to figuring out the flag in the first place :) 

## Flag

> picoCTF{qu4ckm3_7ed36e4b}
