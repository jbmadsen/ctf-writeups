# Ext Super Magic

**Category:** Forensics

**Points:** 250

## Task

> We salvaged a ruined Ext SuperMagic II-class mech recently and pulled the [filesystem](Files/ext-super-magic.img) out of the black box. It looks a bit corrupted, but maybe there's something interesting in there. You can also find it in /problems/ext-super-magic_3_debae27da9f20eec855067f3e83b45f3 on the shell server. 

## Hints

> Are there any [tools](https://en.wikipedia.org/wiki/Fsck) for diagnosing corrupted filesystems? What do they say if you run them on this one?

> How does a linux machine know what [type](https://www.garykessler.net/library/file_sigs.html) of file a [file](https://linux.die.net/man/1/file) is?

> You might find this [doc](http://www.nongnu.org/ext2-doc/ext2.html) helpful.

> Be careful with [endianness](https://en.wikipedia.org/wiki/Endianness) when making edits.

> Once you've fixed the corruption, you can use /sbin/[debugfs](https://linux.die.net/man/8/debugfs) to pull the flag file out.


## What do we need to know?

TODO

## Solution

TODO

## Flag

> picoCTF{???}

 