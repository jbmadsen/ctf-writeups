# HEEEEEEERE'S Johnny!

**Category:** Cryptography

**Points:** 100

## Task

> Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell.picoctf.com 35225. Files can be found here: [passwd](Files/passwd) [shadow](Files/shadow). 

## Hints

> If at first you don't succeed, try, try again. And again. And again.

> If you're not careful these kind of problems can really "rockyou".


## What do we need to know?

TODO:

- Explain password and shadow files

- Explain John the ripper tool

- Explain RockYou password list / dictionary attack


## Solution

Using John the Ripper to crack the password:

```bash
user@ubuntu:/pico/crypto/heeeeeeeres-johnny# john shadow
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:04 57% 1/3 0g/s 290.9p/s 290.9c/s 290.9C/s root03..Root9999902
password1        (root)
1g 0:00:00:10 100% 2/3 0.09661g/s 290.3p/s 290.3c/s 290.3C/s 123456..pepper
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

And there we have it. Username: root, password: password1.

Lets pass that to the server via netcat:

```bash
user@ubuntu:/pico/crypto/heeeeeeeres-johnny# (echo "root"; echo "password1") | nc 2018shell.picoctf.com 35225
Username: Password: picoCTF{J0hn_1$_R1pp3d_99c35524}
```

And there's the flag from the server!

## Flag

> picoCTF{J0hn_1$_R1pp3d_99c35524}

 