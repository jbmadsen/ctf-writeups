# caesar cipher 1 

**Category:** Cryptography

**Points:** 150

## Task

> This is one of the older ciphers in the books, can you decrypt the [message](Files/ciphertext)? You can find the ciphertext in /problems/caesar-cipher-1_1_6fbf7a9ce0aac23bab1c37836cc20c3b on the shell server. 

## Hints

> caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)


## What do we need to know?

The [link](https://learncryptography.com/classical-encryption/caesar-cipher) in the hint, along with what we learned in warmup-2 gives us everything we need to know to solve the puzzle. 

A Caesar Cipher is a simple shifted substitution cipher, where each character is shifted N characters in the alphabet, wrapping back to the beginning (a) if you exceed z. Or noted as: `cipher(C) = C + N % 26`, where the cipher character is the original character rotated N places [mod](https://en.wikipedia.org/wiki/Modulo_operation) 26 (or length of the alphabet used).

## Solution

With the ciphered flag: picoCTF{vgefmsaapaxpomqemdoubtqdxoaxypeo}, I assume we only have to decipher the message part of the flag, as the "wrapper" picoCTF{} looks as it should.

We could do this by hand, but given that we don't know how many characters to rotate the ciphered text by, I opted to write a [small python script](./Solution/brute-force.py) to brute force all combinations, since there are only 25 combinations.

```python
cipher = "vgefmsaapaxpomqemdoubtqdxoaxypeo"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for r in range(1,len(alphabet)):
    msg = ""
    for c in cipher:
        msg += alphabet[(alphabet.index(c) + r) % len(alphabet)]
    print("Rot", r, msg)
```

There's not much to it. We start by defining the cipher, the alphabet used, and then looping through all rotations (1-26).
For each number, we again loop trhough all characters, looking up the value in the alphabet, shift it according to the outer loop (the number of rotations to use) mod 26.
We add this new character to the message, and after looping through the cipher, we output it. And repeat 24 times more.

And we get the result:

```python 
Rot 1 whfgntbbqbyqpnrfnepvcureypbyzqfp
Rot 2 xighouccrczrqosgofqwdvsfzqczargq
Rot 3 yjhipvddsdasrpthpgrxewtgardabshr
Rot 4 zkijqweetebtsquiqhsyfxuhbsebctis
Rot 5 aljkrxffufcutrvjritzgyvictfcdujt
Rot 6 bmklsyggvgdvuswksjuahzwjdugdevku
Rot 7 cnlmtzhhwhewvtxltkvbiaxkevhefwlv
Rot 8 domnuaiixifxwuymulwcjbylfwifgxmw
Rot 9 epnovbjjyjgyxvznvmxdkczmgxjghynx
Rot 10 fqopwckkzkhzywaownyeldanhykhizoy
Rot 11 grpqxdllaliazxbpxozfmeboizlijapz
Rot 12 hsqryemmbmjbaycqypagnfcpjamjkbqa
Rot 13 itrszfnncnkcbzdrzqbhogdqkbnklcrb
Rot 14 justagoodoldcaesarcipherlcolmdsc
Rot 15 kvtubhppepmedbftbsdjqifsmdpmnetd
Rot 16 lwuvciqqfqnfecguctekrjgtneqnofue
Rot 17 mxvwdjrrgrogfdhvduflskhuofropgvf
Rot 18 nywxeksshsphgeiwevgmtlivpgspqhwg
Rot 19 ozxyflttitqihfjxfwhnumjwqhtqrixh
Rot 20 payzgmuujurjigkygxiovnkxriursjyi
Rot 21 qbzahnvvkvskjhlzhyjpwolysjvstkzj
Rot 22 rcabiowwlwtlkimaizkqxpmztkwtulak
Rot 23 sdbcjpxxmxumljnbjalryqnaulxuvmbl
Rot 24 tecdkqyynyvnmkockbmszrobvmyvwncm
Rot 25 ufdelrzzozwonlpdlcntaspcwnzwxodn
```

Looking through the list, looking for english words, that could be the original message, only the Rot 14 shift appears to work: justagoodoldcaesarcipherlcolmdsc (just a good old caesar cipher lcolmdsc).

So we submit that, and we have our flag, once we wrap as per the challenge.

## Flag

> picoCTF{justagoodoldcaesarcipherlcolmdsc}

 