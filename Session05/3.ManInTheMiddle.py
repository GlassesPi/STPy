def enc(msg):
    enc_msg = ''
    for i in range(len(msg)):
        t = (ord(msg[i]) - 65 + 1) % 26
        enc_msg += chr(t + 65)
    return enc_msg

def dec(enc_msg):
    msg = ''
    for i in range(len(enc_msg)):
        t = (ord(enc_msg[i]) - 65 - 1) % 26
        msg += chr(t + 65)
    return msg

print(enc('HI'))
print(dec('IJ'))