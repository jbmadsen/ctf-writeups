# General Warmup 3

**Category:** General Skills

**Points:** 50

## Task

> What is 0x3D (base 16) in decimal (base 10). 

## Hints

> Submit your answer in our competition's flag format. For example, if you answer was '22', you would submit 'picoCTF{22}' as the flag.

## What do we need to know?

Following in the steps of warmup 1 & 2, this challenge again asks us to do conversion. We can start to get a sense that this will be expected a great deal in future challenges.

[Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) numbers were introduced in the first general warmup challenge, so there really shouldn't be anything new here to explain.


## Solution

Again, [Python](https://www.python.org/) has us covered with the built-in function [int](https://docs.python.org/3/library/functions.html#int):

> int(x, base=10): Return an integer object constructed from a number or string x. The default base is 10. The allowed values are 0 and 2–36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code.

We input:

```python
int('0x3D', 16)
```
> 61

So the decimal representation of 0x3D is the number 61.

Again, remember to submit the answer in the competitions flag format, as the hints reminds us.

## Flag

> picoCTF{61}
