# [PicoCTF 2018](https://2018game.picoctf.com/) Writeup

These write-ups explains the things I learned solving the tasks. Since this was the first CTF I did, some of the methods used getting the right answers might not be conventional, and some might be downright stupid in hindsight and with more knowledge :)

But you know what you know, I guess. 

**Note:** All writeup will be using Linux to solve the challenges.  


## Current CTF status

Score: 8560


## Content
- [Binary Exploitation](./Binary%20Exploitation)
- [Cryptography](./Cryptography)
- [Forensics](./Forensics)
- [General Skills](./General%20Skills)
- [Reversing](./Reversing)
- [Web Exploitation](./Web%20Exploitation)


## Challenges

|Name|Category|Points|Status|Write up
|-|-|-|-|-|
|[Forensics Warmup 1](Forensics/Forensics%20Warmup%201)|Forensics|50|Solved|Yes|
|[Forensics Warmup 2](Forensics/Forensics%20Warmup%202)|Forensics|50|Solved|Yes|
|[General Skills 1](General%20Skills/General%20Warmup%201)|General Skills|50|Solved|Yes|
|[General Skills 2](General%20Skills/General%20Warmup%202)|General Skills|50|Solved|Yes|
|[General Skills 3](General%20Skills/General%20Warmup%203)|General Skills|50|Solved|Yes|
|[Resources](General%20Skills/Resources)|General Skills|50|Solved|Yes|
|[Reversing Warmup 1](Reversing/Reversing%20Warmup%201)|Reversing|50|Solved|Yes|
|[Reversing Warmup 2](Reversing/Reversing%20Warmup%202)|Reversing|50|Solved|Yes|
|[Crypto Warmup 1](Cryptography/Crypto%20Warmup%201)|Cryptography|75|Solved|Next up|
|[Crypto Warmup 2](Cryptography/Crypto%20Warmup%202)|Cryptography|75|Solved|Next up|
|[grep 1](General%20Skills/grep%201)|General Skills|75|Solved|No|
|[net cat](General%20Skills/net%20cat)|General Skills|75|Solved|No|
|[HEEEEEEERE'S Johnny!](Cryptography/HEEEEEEERE%27S%20Johnny!)|Cryptography|100|Solved|No|
|[strings](General%20Skills/strings)|General Skills|100|Solved|No|
|[pipe](General%20Skills/pipe)|General Skills|110|Solved|No|
|[Inspect Me](Web%20Exploitation/Inspect%20Me)|Web Exploitation|125|Solved|No|
|[grep 2](General%20Skills/grep%202)|General Skills|125|Solved|No|
|[Aca-Shell-A](General%20Skills/Aca-Shell-A)|General Skills|150|Solved|No|
|[Client Side is Still Bad](Web%20Exploitation/Client%20Side%20is%20Still%20Bad)|Web Exploitation|150|Solved|No|
|[Desrouleaux](Forensics/Desrouleaux)|Forensics|150|Solved|No|
|[Logon](Web%20Exploitation/Logon)|Web Exploitation|150|Solved|No|
|[Reading Between the Eyes](Forensics/Reading%20Between%20the%20Eyes)|Forensics|150|Solved|No|
|[Recovering From the Snap](Forensics/Recovering%20From%20the%20Snap)|Forensics|150|Solved|No|
|[admin panel](Forensics/admin%20panel)|Forensics|150|Solved|No|
|[assembly-0](Reversing/assembly-0)|Reversing|150|Solved|Partly|
|[buffer overflow 0](Binary%20Exploitation/buffer%20overflow%200)|Binary Exploitation|150|Solved|No|
|[caesar cipher 1](Cryptography/caesar%20cipher%201)|Cryptography|150|Solved|No|
|[environ](General%20Skills/environ)|General Skills|150|Solved|No|
|[hertz](Cryptography/hertz)|Cryptography|150|Solved|No|
|[hex editor](Forensics/hex%20editor)|Forensics|150|Solved|No|
|[ssh-keyz](General%20Skills/ssh-keyz)|General Skills|150|Solved|No|
|[Irish Name Repo](Web%20Exploitation/Irish%20Name%20Repo)|Web Exploitation|200|Solved|No|
|[Mr. Robots](Web%20Exploitation/Mr.%20Robots)|Web Exploitation|200|Solved|No|
|[No Login](Web%20Exploitation/No%20Login)|Web Exploitation|200|Solved|No|
|[Secret Agent](Web%20Exploitation/Secret%20Agent)|Web Exploitation|200|Solved|No|
|[Truly an Artist](Forensics/Truly%20an%20Artist)|Forensics|200|Solved|No|
|[assembly-1](Reversing/assembly-1)|Reversing|200|Solved|Partly|
|[be-quick-or-be-dead-1](Reversing/be-quick-or-be-dead-1)|Reversing|200|Solved|Partly|
|[blaise's cipher](Cryptography/blaise%27s%20cipher)|Cryptography|200|Solved|No|
|[buffer overflow 1](Binary%20Exploitation/buffer%20overflow%201)|Binary Exploitation|200|Solved|No|
|[hertz 2](Cryptography/hertz%202)|Cryptography|200|Solved|No|
|[leak-me](Binary%20Exploitation/leak-me)|Binary Exploitation|200|Solved|No|
|[now you don't](Forensics/now%20you%20don%27t)|Forensics|200|Solved|No|
|[quackme](Reversing/quackme)|Reversing|200|Solved|No|
|[shellcode](Binary%20Exploitation/shellcode)|Binary Exploitation|200|Solved|No|
|[what base is this?](General%20Skills/what%20base%20is%20this)|General Skills|200|Solved|No|
|[you can't see me](General%20Skills/you%20can%27t%20see%20me)|General Skills|200|Solved|No|
|[Buttons](Web%20Exploitation/Buttons)|Web Exploitation|250|Solved|No|
|[Ext Super Magic](Forensics/Ext%20Super%20Magic)|Forensics|250|Solved|No|
|[Lying Out](Forensics/Lying%20Out)|Forensics|250|Solved|No|
|[The Vault](Web%20Exploitation/The%20Vault)|Web Exploitation|250|Solved|No|
|[What's My Name?](Forensics/What%27s%20My%20Name)|Forensics|250|Solved|No|
|[absolutely relative](General%20Skills/absolutely%20relative)|General Skills|200|Solved|No|
|[assembly-2](Reversing/assembly-2)|Reversing|250|Solved|Partly|
|[buffer overflow 2](Binary%20Exploitation/buffer%20overflow%202)|Binary Exploitation|250|Next up|No|
|[caesar cipher 2](Cryptography/caesar%20cipher%202)|Cryptography|250|Solved|No|
|got-2-learn-libc|Binary Exploitation|250|Unsolved|No|
|rsa-madlibs|Cryptography|250|Unsolved|No|
|be-quick-or-be-dead-2|Reversing|275|Unsolved|No|
|in out error|General Skills|275|Unsolved|No|
|Artisinal Handcrafted HTTP 3|Web Exploitation|300|Unsolved|No|
|SpyFi|Cryptography|300|Unsolved|No|
|echooo|Binary Exploitation|300|Unsolved|No|
|learn gdb|General Skills|300|Unsolved|No|
|Flaskcards|Web Exploitation|350|Unsolved|No|
|got-shell?|Binary Exploitation|350|Unsolved|No|
|quackme up|Reversing|350|Unsolved|No|
|Malware Shops|Forensics|400|Unsolved|No|
|Radix's Terminal|Reversing|400|Unsolved|No|
|assembly-3|Reversing|400|Unsolved|No| 
|fancy-alive-monitoring|Web Exploitation|400|Unsolved|No|
|keygen-me-1|Reversing|400|Unsolved|No|
|store|General Skills|400|Unsolved|No|
|Magic Padding Oracle|Cryptography|450|Unsolved|No|
|Secure Logon|Web Exploitation|500|Unsolved|No| 
|script me|General Skills|500|Unsolved|No|
|LoadSomeBits|Forensics|550|Unsolved|No|
|Help Me Reset 2|Web Exploitation|600|Unsolved|No|
|A Simple Question|Web Exploitation|650|Unsolved|No|
|LambDash 3|Web Exploitation|800|Unsolved|No|
|Dog or Frog|General Skills|900|Unsolved|No|
