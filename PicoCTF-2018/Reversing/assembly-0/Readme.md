# assembly-0

**Category:** Reversing

**Points:** 150

## Task

> What does asm0(0xb6,0xc6) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](Files/intro_asm_rev.S) located in the directory at /problems/assembly-0_0_5a220faedfaf4fbf26e6771960d4a359. 

## Hints

> basical assembly [tutorial](https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm)

> assembly [registers](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)


## What do we need to know?

> TODO


## Solution

Som what does the program return, when executing the function asm0(0xb6,0xc6) (function asm0 with input parameters 0xb6,0xc6)?

Quick conversion from hexadecimal to decimal: 0xb6 = 182, and 0xc6 = 198. Not sure that will be needed, but I tend to do mental calculations with the numbers I am working with :)

Lets have a look at the supplied source code for the challenge:

```assembly
.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp
	mov     ebp,esp
	mov     eax,DWORD PTR [ebp+0x8]
	mov     ebx,DWORD PTR [ebp+0xc]
	mov     eax,ebx
	mov     esp,ebp
	pop     ebp	
	ret
```

What we have here, is source code written in assembly, using Intel syntax. We have the entrypoint for the function `asm0` we are interested in, so lets dig in, and manually go through the code in the `asm0` function, and see if we learn anything.

First:

```assembly
	push	ebp
	mov     ebp,esp
```

This is the [function prologue](https://en.wikipedia.org/wiki/Function_prologue). 
It stores the previous base pointer (ebp) and sets the base pointer as it was the top of the stack. 
This means that all the stack contents is saved down the stack, so the function can push/pop in the stack.

Next: 

```assembly
	mov     eax,DWORD PTR [ebp+0x8]
	mov     ebx,DWORD PTR [ebp+0xc]
```

The 4 bytes at [ebp+0x8] are moved to a register. This is where we are loading our first passed argument (0xb6).
Next, the 4 bytes at [ebp+0xc] are moved to a register, loading our second passed argument (0xc6).

We then copy the value from ebx into eax:

```assembly
	mov     eax,ebx
```

Doing this, we override eax we just loaded. 
Since this is the last use of eax in this piece of code it can be interpreted as a return value of the function.

Finally, the last of the function: 

```assembly
	mov     esp,ebp
	pop     ebp	
	ret
```

This is the inverse of the function prologue, the [function epilogue](https://en.wikipedia.org/wiki/Function_prologue#Epilogue), which reverses the actions of the function prologue and returns control to the calling function.

If we take this behaviour, and translates it into a simple C language function, it would look similar to this:

```c
int func(int a, int b)
{
    return b;
}
```

In our case, with the input being a = 0xb6 & b = 0xc6, the output is: 0xc6.

And if we remember the note from the challenge:

> NOTE: Your submission for this question will NOT be in the normal flag format.

Then we have the flag.

## Flag

> 0xc6
