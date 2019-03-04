# Crypto Warmup 1

**Category:** Cryptography

**Points:** 75

## Task

> Crpyto can often be done by hand, here's a message you got from a friend, **llkjmlmpadkkc** with the key of **thisisalilkey**. Can you use this [table](Files/table.txt) to solve it?.  

## Hints

> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.

> Please use all caps for the message.


## What do we need to know?

In this first warmup challenge, we are dealing with a simple [cipher](https://en.wikipedia.org/wiki/Cipher).

> In cryptography, a cipher (or cypher) is an algorithm for performing encryption or decryption—a series of well-defined steps that can be followed as a procedure. ([wiki](https://en.wikipedia.org/wiki/Cipher))

There's not really a lot "to know" for this challenge. 
We are given a secret (encrypted) message, a key to use for decrypting the message, and a lookup table where we can see how the key and message fit together. 

So what we need to do, is to go through the message character by character, and using the table and the key, convert the character from the encoded version to a decoded version. Afterwards we assemble the decoded message from the individual characters we have decoded.


## Solution

**TLDR**: I wrote a small [python script](./Solution/decypher.py) to display the lookup if you don't want to do it by hand.

Displaying the [table]():

| |  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|- |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|A|\||A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|B|\||B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|
|C|\||C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|
|D|\||D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|
|E|\||E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|
|F|\||F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|
|G|\||G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|
|H|\||H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|
|I|\||I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|
|J|\||J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|
|K|\||K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|
|L|\||L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|
|M|\||M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|
|N|\||N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|
|O|\||O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|
|P|\||P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|
|Q|\||Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|
|R|\||R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|
|S|\||S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|
|T|\||T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|
|U|\||U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|
|V|\||V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|
|W|\||W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|
|X|\||X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|
|Y|\||Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|
|Z|\||Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|

Lets go through this one by hand to get the hang of it.

* Message: **llkjmlmpadkkc**
* Key: **thisisalilkey**

With the first character of the message 'l', and the first character of the key 't', lets look it up in the table:

| |  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|- |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| |\||...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|
|T|\||T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|**L**|M|N|O|P|Q|R|S|
| |\||...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|

In the T row (the character in the key), we navigate to L (the character in the message), and look at the corresponding column: S

> First letter of the decrypted message is: S

With the second character of the message also 'l', and the second character of the key 'h', lets look it up in the table:

| |  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|- |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| |\||...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|
|H|\||H|I|J|K|**L**|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|
| |\||...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|

In the H row (the character in the key), we navigate to L (the character in the message), and look at the corresponding column: E

> Second letter of the decrypted message is: E

With the third character of the message also 'k', and the second character of the key 'i', lets look it up in the table:

| |  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|- |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| |\||...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|
|I|\||I|J|**K**|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|
| |\||...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|

In the I row (the character in the key), we navigate to K (the character in the message), and look at the corresponding column: C

> Second letter of the decrypted message is: C

If we continue this process for all letters in the encrypted message, the decrypted message becomes: SECRETMESSAGE.

Remember to enclose the response in the flag format of the challenge, and we have the flag. 

## Flag

> picoCTF{SECRETMESSAGE}

 