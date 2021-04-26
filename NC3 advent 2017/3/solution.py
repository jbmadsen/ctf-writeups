# NC3 solution
import mmap
import re
import os

folder = '/Users/Jacob/Dropbox/Projects/Politiets NC3 adventskalender 2017/3/'
fname = 'three.dd'
fh = open(folder + fname, 'rb')
ba = bytes(fh.read())
fh.close()

print("Parsing", fname.split('/')[-1])

# De første 512 bytes angiver hvilken version af filsystemet der anvendes
print("Version beskrivelse:", ba[0:512].decode("utf-8").rstrip('\x00'))

# FilID og Filsti/Filnavn tabel Starter ved byteoffset 512 ved start fra offset 0.
# indtil headers end
files_end = ba.find(b'\x00\xff\xff\x00\xff\x00')
print("Files structure end at", files_end)

fs = ba[512:files_end]
fs = fs.split(b'\x00\xff\xff')

rest = ba[files_end:]
headers_end = ba.find(b'\xff\x00\x00\x00\x00')
print("Headers end at", headers_end)
headers = ba[files_end+6:headers_end]
rest = ba[headers_end:]

files_info = []

sequence = headers.split(b'\x00\xff')
seq = []
for item in sequence:
    c = item.split(b'\x00')
    seq.append(c[-1])

# Split alle filerne til lists
for item in fs:
    content = item.split(b'\x00')
    md5 = content[-0]
    path = content[-1].decode("utf-8")
    byteoffset = headers.find(content[0]) + headers_end
    ints = seq[fs.index(item)]
    file = [md5, path, byteoffset, ints]
    files_info.append(file)


def find_start_end(sector_start):
    byteoffset = 0#81920
    sector_size = 4096
    block = byteoffset+(sector_start*sector_size)
    return [block, block+sector_size]


def bytes_to_int(bytes):
    if len(bytes) > 0:
        return int(bytes.decode("utf-8"))
    return 0


for item in files_info:
    path = os.path.dirname(item[1])
    print(path)
    if not os.path.exists(folder+path):
        os.makedirs(folder+path)
    name = item[1].split('/')[-1]
    sectors = item[-1].split(b'\x20')
    sectors = [bytes_to_int(i) for i in sectors]
    #print(name, sectors)
    heap = None
    for i in sectors:
        idx = find_start_end(i)
        data = ba[idx[0]:idx[1]]
        if heap is None:
            heap = data
        else:
            heap = heap + data
    if heap is not None:
        newfile=open(folder+item[1],'wb')
        newfile.write(heap)
        newfile.close()
    pass


