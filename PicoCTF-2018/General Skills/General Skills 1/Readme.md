# General Warmup 1

**Category:** General Skills

**Points:** 50

## Task

> If I told you your grade was 0x41 in hexadecimal, what would it be in ASCII?  

## Hints

> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## What do we need to know?

This challenge introduces [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) numbers as well as [ASCII](https://en.wikipedia.org/wiki/ASCII) characters. 

> In mathematics and computing, **hexadecimal** (also base 16, or hex) is a positional numeral system, which uses 16 distinct symbols. "0–9" to represent values zero to nine, and "A–F" to represent values ten to fifteen.

> **ASCII** codes represent text in computers, telecommunications equipment, and other devices. Most modern character-encoding schemes are based on ASCII, although they support many additional characters.

From the [wiki](https://en.wikipedia.org/wiki/ASCII) we see that all ASCII characters have a number representation in binary,	octal, decimal and hexadecimal. For this challenge, the conversion between hex and ASCII characters are what is interesting. Another great lookup table can be found at [asciitable.com](http://www.asciitable.com/).


## Solution

Since this is an easy challenge, where we only have to lookup a single character, a lookup in [this table](http://www.asciitable.com/) at hex position 41, gives us the answer `A`.

Alternatively we could use a [Python](https://www.python.org/), which will come in handy for later challenges, using the built-in function [chr](https://docs.python.org/3/library/functions.html#chr):

```python
chr(0x41)
```
> 'A'

And remember to submit the answer in the competitions flag format, as the hints reminds us.



## Flag

> picoCTF{A}
