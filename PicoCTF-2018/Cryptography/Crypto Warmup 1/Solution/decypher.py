inp = list('llkjmlmpadkkc'.upper())
key = list('thisisalilkey'.upper())

shift = 65
mod = 25

res = []

for i in range(len(inp)):
    key_char = ord(key[i]) - shift
    in_char = ord(inp[i]) - shift

    pos = ((mod + 1) - key_char + in_char) % (mod + 1)
    val = chr(pos + shift)    
    
    prnt = "({:s},{:s},{:s}) -> {:s}"
    print(prnt.format(str(pos),key[i],inp[i],val))

    res.append(val)

print(''.join(res))
