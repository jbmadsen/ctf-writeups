# Reversing Warmup 2

**Category:** Reversing

**Points:** 50

## Task

> Can you decode the following string `dGg0dF93NHNfczFtcEwz` from base64 format to ASCII? 


## Hints

> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.


## What do we need to know?

So, base64 it is. A great start for learning a new topic is always [Wikipedia](https://en.wikipedia.org/wiki/Base64).
Looking at the information on Wikipedia, we can see that base64 is yet another way of representing data, just as binary, decimal, octal and hexadecimal (with slight differences!), we were presented in earlier challenges. 

From the wiki:

> Each Base64 digit represents exactly 6 bits of data. Three 8-bit bytes (i.e., a total of 24 bits) can therefore be represented by four 6-bit Base64 digits. 

> Encoded in ASCII, the characters M, a, and n are stored as the bytes 77, 97, and 110, which are the 8-bit binary values 01001101, 01100001, and 01101110. These three values are joined together into a 24-bit string, producing 010011010110000101101110. Groups of 6 bits (6 bits have a maximum of 26 = 64 different binary values) are converted into individual numbers from left to right.

> `=` padding characters might be added to make the last encoded block contain four Base64 characters. 

So there are slight differences to the previous challenges, as this encoding is more sophisticated than number conversion.

## Solution

Luckily for us, python and its [base64 library](https://docs.python.org/3.7/library/base64.html) can do the decoding of the string.

```python
import base64
base64.b64decode("dGg0dF93NHNfczFtcEwz")
```

> b'th4t_w4s_s1mpL3'

As it returns a bytestryng, the element within the b' ' are the actual return string we are lookin for. And remember the competition's flag format.

## Flag

> picoCTF{th4t_w4s_s1mpL3}
