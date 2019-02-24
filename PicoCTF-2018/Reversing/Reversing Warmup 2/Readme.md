# Reversing Warmup 2

**Category:** Reversing

**Points:** 50

## Task

> Can you decode the following string `dGg0dF93NHNfczFtcEwz` from base64 format to ASCII? 


## Hints

> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.


## What do we need to know?

So, base64 it is. A great start for learning a new topic is always [Wikipedia](https://en.wikipedia.org/wiki/Base64).
Looking at the information on Wikipedia, we can see that base64 is yet another way of representing data, just as binary, decimal, octal and hexadecimal, we were presented in earlier challenges. 

TODO: Simple explanation


## Solution

We use python, and its [base64 library](https://docs.python.org/3.7/library/base64.html) to decode the string.

```python
import base64
base64.b64decode("dGg0dF93NHNfczFtcEwz")
```

> b'th4t_w4s_s1mpL3'

As it returns a bytestryng, the element within the b' ' are the actual return string we are lookin for. And remember the competition's flag format.

## Flag

> picoCTF{th4t_w4s_s1mpL3}
