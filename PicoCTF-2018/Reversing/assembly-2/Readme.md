# assembly-2

**Category:** Reversing

**Points:** 250

## Task

> What does asm2(0x6,0x28) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](Files/loop_asm_rev.S) located in the directory at /problems/assembly-2_0_24775b87ffbbe8e643da10e71018f275.


## Hints

> assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)


## What do we need to know?

TODO

## Solution

Just as we did in the the previous assembly challenges, we need to figure out the return value of a function, this time `asm2(0x6,0x28)`.

Lets have a look at the supplied source code for the challenge:

```assembly
.intel_syntax noprefix
.bits 32
	
.global asm2

asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD PTR [ebp+0xc]
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8]
	mov     DWORD PTR [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1
	add     DWORD PTR [ebp+0x8],0x8f
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0x8f90
	jle    	part_a
	mov    	eax,DWORD PTR [ebp-0x4]
	mov     esp,ebp
	pop     ebp
	ret
```

And just like the previous times, lets jump in and go through the code as needed, starting with the [function prologue](https://en.wikipedia.org/wiki/Function_prologue), as previously explained:

```assembly
	push	ebp
	mov     ebp,esp
```

We then reserve 16 bytes on the stack (hexadecimal 0x10 is 16 in decimal):

```assembly
	sub    	esp,0x10
```

Following that, we do shuffle some numbers around before we jump:

```assembly
	mov    	eax,DWORD PTR [ebp+0xc]
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8]
	mov     DWORD PTR [ebp-0x8],eax
	jmp    	part_b
```

We send the 4 bytes at [ebp+0xc] to the eax registry, and then copy the contents of eax into [ebp-0x4] which we previously reserved on the stack.
And then we to the same again for [ebp+0x8] into eax, and then copy that eax content into [ebp-0x8].

with that in place we should have the following:

* [ebp+0xc] and [ebp-0x4] holds 0x28
* [ebp+0x8] and [ebp-0x8] holds 0x6

And then we jump to part_b:

```assembly
	cmp    	DWORD PTR [ebp+0x8],0x8f90
	jle    	part_a
```

First, a comparison between out content in [epb+0x8] and 0x8f90 (36752 in decimal), and if [ebp+0x8] is less than or equal to 0x8f90 we jump to part_a. As 0x6 is indeed less than 0x8f90, we jump:

```assembly
	add    	DWORD PTR [ebp-0x4],0x1
	add     DWORD PTR [ebp+0x8],0x8f
```

We add 1 to [ebp-0x4], and we add 143 to [ebp-0x8], before continuing back to part_b again.

So, we are stuck in a loop until [ebp+0x8] becomes greater than 0x8f90. 
So lets calculate when that will happen:

[ebp+0x8] started at 0x6, and grows 143 each loop until it is greater than 36752. The equation to solve is:

> 6 + (143 * x) > 36752

Solve for x gives x = 257. The loop breaks after 257 loops, with these values in memory: 

* [ebp-0x4] = 0x129 (297)
* [ebp-0x8] = 0x8f95 (36757)

We continue:

```assembly
	mov    	eax,DWORD PTR [ebp-0x4]
	mov     esp,ebp
	pop     ebp
	ret
```

We move [ebp-0x4] into the eax register, cleanup and [function epilogue](https://en.wikipedia.org/wiki/Function_prologue#Epilogue), and the function returns 0x129, which is our flag, as again, in this challenge we do not use the normal flag format.

## Flag

> 0x129
