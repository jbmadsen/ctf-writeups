# General Warmup 2

**Category:** General Skills

**Points:** 50

## Task

> Can you convert the number 27 (base 10) to binary (base 2)?

## Hints

> Submit your answer in our competition's flag format. For example, if you answer was '11111', you would submit 'picoCTF{11111}' as the flag.

## What do we need to know?

This time we are introduced to [binary numbers](https://en.wikipedia.org/wiki/Binary_number) (you may want to jump to the section on [counting](https://en.wikipedia.org/wiki/Binary_number#Counting_in_binary) if the history isn't interesting).

Basically, we are being taught how to count in binary and convert from decimal to binary:

|Decimal number|Binary number|
|-|-|
|0|0|
|1|1|
|2|10|
|3|11|
|4|100|
|5|101|

and so on...

https://docs.python.org/3/library/functions.html#bin

## Solution

Similar to the last challenge, we could do this by hand, since we only have to count to 27.

Or, we could use a [Python](https://www.python.org/) again, this time using the built-in function [bin](https://docs.python.org/3/library/functions.html#bin), which:

>Converts an integer number to a binary string prefixed with “0b”. 

We input:

```python
bin(27)
```
> '0b11011'

So the binary number is 11011.

Again, remember to submit the answer in the competitions flag format, as the hints reminds us.

## Flag

> picoCTF{11011}
