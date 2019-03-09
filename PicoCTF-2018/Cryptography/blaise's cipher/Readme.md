# blaise's cipher 

**Category:** Cryptography

**Points:** 200

## Task

> My buddy Blaise told me he learned about this cool cipher invented by a guy also named Blaise! Can you figure out what it says? Connect with nc 2018shell.picoctf.com 59396.

## Hints

> There are tools that make this easy.

> This cipher was NOT invented by Pascal


## What do we need to know?

The first (and most important) clue is in the name of the challange. There is a cipher called [Vigenére cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) that was invented by [Blaise de Vigenére](https://en.wikipedia.org/wiki/Blaise_de_Vigen%C3%A8re).

TODO: What is a Vigenére cipher, and how does it work? and how do we break it?

There's even a chapter on breaking this cipher in the book [Invent with Python](https://inventwithpython.com/hacking/chapter21.html).

## Solution

Connecting to the server with netcat, it prints [a bunch of ciphered text](./Files/ciphered_text.txt) for us to look at. We can save it to a text file to work with:

```bash
nc 2018shell.picoctf.com 59396 > ciphered_text.txt
```

Looking at the text, we see a suspicious text string in the end of the third paragrah: pohzCZK{g1gt3w3_n1pn3wd_ax3s7_maj_1h7m92d3}. 
I would assume that is the cipher-text of the flag.

Going by the name of the challange, lets see if this isn't a Vigenére cipher.
Luckily for us, we don't really have to do any work, as there's a cool [website](https://www.dcode.fr/vigenere-cipher) that has implemented a method for deciphering Vigenére ciphers. 

Using [dcode.fr](https://www.dcode.fr/vigenere-cipher)
and setting "Try to decrypt automatically (statistical analysis)"
gives the most likely key: FLAG

With the key, we can [decipher the text](./Files/deciphered_text.txt). There, in the end of the third paragraph is the correct flag: picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_1c7b92d3}


## Flag

> picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_1c7b92d3}

 