# Forensics Warmup 2

**Category:** Forensics

**Points:** 50

## Task
> Hmm for some reason I can't open this [PNG](Files/flag.png)? Any ideas? 

## Hints

> How do operating systems know what kind of file it is? (It's not just the ending!)

> Make sure to submit the flag as picoCTF{XXXXX}

## What do we need to know?



https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header

https://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

To see the first bytes of the file, we can use [od](https://linux.die.net/man/1/od), which reads the first 8 bytes (--read-bytes=8) of a file and outputs it to standard output in hex format (--format=x1).

```
od --format=x1 --read-bytes=8 flag.png
```
> 0000000 89 50 4e 47 0d 0a 1a 0a

This gives us 

## Solution

TODO

## Flag

> picoCTF{???}