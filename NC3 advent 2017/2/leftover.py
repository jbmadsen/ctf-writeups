import csv

fname = '/Users/Jacob/Desktop/NC3 Advent/Part2/usb_in_leftover.txt'

table = ['', '', '', '', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2','3','4','5','6','7','8','9','0', '','','','', ' ','-','=','[', ']', '', '#', ';', '', '', ',', '.', '/']

data = []

with open(fname) as f:
    data = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in data]
content = list(filter(None, content))

data = []
raw = []

for item in content:
    s = item.split(':')[2]
    raw.append(s)
    #s = "0x" + s
    #s = s.decode('hex')
    s = int(s, 16)
    if s is 0:
        continue
    if s <= len(table):
        if s is 42:
            print("Deleted", data[-1])
            data.pop(-1)
        else:
            s = table[s]
            st = table[int(item.split(':')[3], 16)] # extra data to tell when to clean current
            if st is not '':
                data.pop(-1)
            data.append(s)

#print(raw)
#print(data)
text = ''.join(data)
print("Text:")
print(text)
print("SHA 256 check, der skal være 64 char lang:")
print(len(text.split(' ')[-1]))

# jeg har lige testet min toastermalware og ingen antivirus detecterede den1 fedt man.
# den har sha/256 42c3d3ba5c099106fc21ab53908495d5ef2ff9fcaa890b1c7ef4386bc0893f2f

