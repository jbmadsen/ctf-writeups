def get_flag(msg):
    data = '2906164f2b35301e511b5b144b085d2b5217015716115c075d004e6f206c696e'
    xor = bytes.fromhex(data).decode('utf-8')
    
    flag = ''
    for i in range(min(len(msg),len(xor))):
        data = ord(xor[i]) ^ ord(msg[i])
        flag += chr(data)

    print(flag)


msg = "picoCTF{"
get_flag(msg)

msg = "You have now entered the Duck Web, and you're in for a honkin' good time."
get_flag(msg)
