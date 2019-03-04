cipher = "vgefmsaapaxpomqemdoubtqdxoaxypeo"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for r in range(1,len(alphabet)):
    msg = ""
    for c in cipher:
        msg += alphabet[(alphabet.index(c) + r) % len(alphabet)]
    print("Rot", r, msg)