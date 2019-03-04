rot13 = str.maketrans( 
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
cipher = "cvpbPGS{guvf_vf_pelcgb!}"
message = cipher.translate(rot13)
print(message)
