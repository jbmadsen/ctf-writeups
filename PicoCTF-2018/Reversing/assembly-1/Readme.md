# assembly-1

**Category:** Reversing

**Points:** 200

## Task

>  What does asm1(0x15e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](Files/eq_asm_rev.S) located in the directory at /problems/assembly-1_3_cfc4373d0e723e491f368e7bcc26920a.


## Hints

> assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)


## What do we need to know?

TODO

## Solution

Like the previous assembly challenge, we need to figure out the return value of a function, this time `asm1(0x15e)`.

First a quick conversion from hexadecimal to decimal: 0x15e = 350, for my mental state.

Lets have a look at the supplied source code for the challenge:

```assembly
.intel_syntax noprefix
.bits 32
	
.global asm1

asm1:
	push	ebp
	mov     ebp,esp
	cmp     DWORD PTR [ebp+0x8],0xdc
	jg      part_a	
	cmp     DWORD PTR [ebp+0x8],0x8
	jne     part_b
	mov     eax,DWORD PTR [ebp+0x8]
	add     eax,0x3
	jmp     part_d
part_a:
	cmp     DWORD PTR [ebp+0x8],0x68
	jne     part_c
	mov     eax,DWORD PTR [ebp+0x8]
	sub     eax,0x3
	jmp     part_d
part_b:
	mov     eax,DWORD PTR [ebp+0x8]
	sub     eax,0x3
	jmp     part_d
	cmp     DWORD PTR [ebp+0x8],0xfc
	jne     part_c
	mov     eax,DWORD PTR [ebp+0x8]
	sub     eax,0x3
	jmp     part_d
part_c:
	mov     eax,DWORD PTR [ebp+0x8]
	add     eax,0x3
part_d:
	pop     ebp
	ret
```

so, this one is slightly longer than the last function, and with even more fun stuff going on! 
Lets dive in, and manually go through the code, again.

First, we start at the entry point for the asm1 function:

```assembly
	push	ebp
	mov     ebp,esp
```

This is the [function prologue](https://en.wikipedia.org/wiki/Function_prologue), as explained in the first [assembly challenge](../assembly-0).

```assembly
	cmp     DWORD PTR [ebp+0x8],0xdc
	jg      part_a	
```

We then compare 4 bytes at [ebp+0x8] (out input parameter 0x15e) with 0xdc.
If [ebp+0x8] is larger than 0xdc (0x15e > 0xdc), we jump to part_a. 0xdc is 220, and (350 > 220) evaluates as true. So we jump to part_a:

```assembly
	cmp     DWORD PTR [ebp+0x8],0x68
	jne     part_c
```

This compare 4 bytes at [ebp+0x8] (again input) with 0x68, and this time, we jump if the parameters compared are not equal. They are not (0x15e == 0x68 evaluates false). Jumping to part_c:

```assembly
	mov     eax,DWORD PTR [ebp+0x8]
	add     eax,0x3
```

The 4 bytes at [ebp+0x8] are moved to the eax register, and we add 0x3 to the value stored in eax: 0x15e + 0x3 = 0x161. Since there are no more jumps, we flow down the code into part_d,

```assembly
	pop     ebp
	ret
```

which calls the [function epilogue](https://en.wikipedia.org/wiki/Function_prologue#Epilogue), and the function returns 0x161.

Again, in this challenge we do not use the normal flag format, so we have our flag.


## Flag

> 0x161
