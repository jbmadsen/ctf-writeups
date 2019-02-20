# Forensics Warmup 2

**Category:** Forensics

**Points:** 50

## Task
> Hmm for some reason I can't open this [PNG](Files/flag.png)? Any ideas? 

## Hints

> How do operating systems know what kind of file it is? (It's not just the ending!)

> Make sure to submit the flag as picoCTF{XXXXX}

## What do we need to know?

We are still just getting our feet wet. Looking at the first hint, the authors of the challenge wants us to think about [how the operating system determines the file type](https://en.wikipedia.org/wiki/File_format#Identifying_file_type).

Clearly the file must not be a png file, or else there wouldn't be any challenge, and it would be even easier than the first warmup. Using [file](https://linux.die.net/man/1/file) to determine the file information

```bash
file flag.png
```
> flag.png: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 909x190, frames 3

we can see that it is actually a jpeg in disguise. But how could the operating system know that, with the extension being .png?  

The [wiki link above](https://en.wikipedia.org/wiki/File_format#Identifying_file_type) also mentions that the metadata contained in a file header are usually stored at the start of the file.
Using [od](https://linux.die.net/man/1/od) to read the first 8 bytes (--read-bytes=8) of a file and outputs it to standard output in hex format (--format=x1).

```bash
od --format=x1 --read-bytes=8 flag.png
```
> 0000000 ff d8 ff e0 00 10 4a 46

Referencing this against known headers for [png](https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header) and [jpeg](https://en.wikipedia.org/wiki/JPEG#Syntax_and_structure) it sure does look like the start of a jpg file with the first 3 bytes being `ff d8 ff`, where had it been a png file, the header would have been `89 50 4e 47 0d 0a 1a 0a`. 

## Solution

To be honest, I just opened the file, and apparently my imageviewer did not care about the png extension and correctly opened the file. So, I had to workout what the challenge was after getting the flag.
If it hadn't just worked, we could use [file](https://linux.die.net/man/1/file) to determine the file information. 

```bash
file flag.png
```
> flag.png: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 909x190, frames 3

We can then rename the file to flag.jpg

```bash
mv flag.png flag.jpg
```

and open the file, and read the flag.

## Flag

> picoCTF{extensions_are_a_lie}