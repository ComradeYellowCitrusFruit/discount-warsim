import base64
import os
import math

### Free form encoding, encodes anything you put in, no additional formating, no password applied, no nothin
def Encode(file: str, codec = 'unicode-escape') -> bytes:
    File = base64.b16encode(file.encode(codec))
    File = base64.b32encode(File)
    File = base64.b64encode(File)
    File = base64.b85encode(File)
    return File
### Password encoding, no formating is applied to the data, some password protection is done, and the final product is encoded two additonal passes
def passwordEncode(file : str, password : str, codec = 'unicode-escape', passes = (85,16)) -> bytes:
    Password = list(password)
    for i in range(len(Password)):
        Password[i] = ord(Password[i])
    pwdVal = Password[0] - Password[0]
    for i in range(len(Password)):
        if i%2 == 0:
            pwdVal += Password[i]
        else:
            pwdVal -= Password[i]
    File = list(file)
    for i in range(len(File)):
        File[i] = ord(File[i])
        File[i] = File[i] + pwdVal
        File[i] = int(File[i] * math.ceil(pwdVal/5))
        File[i] = chr(File[i]) 
    for i in File:
        FILE += i
    fst, snd = passes
    if fst == 85:
        FILE = base64.b85encode(FILE.encode(codec))
    elif fst == 64:
        FILE = base64.b64encode(FILE.encode(codec))
    elif fst == 32:
        FILE = base64.b32encode(FILE.encode(codec))
    elif fst == 16:
        FILE = base64.b16encode(FILE.encode(codec))
    File = base64.b16encode(FILE)
    File = base64.b32encode(File)
    File = base64.b64encode(File)
    File = base64.b85encode(File)
    if snd == 85:
        File = base64.b85encode(File)
    elif snd == 64:
        File = base64.b64encode(File)
    elif snd == 32:
        File = base64.b32encode(File)
    elif snd == 16:
        File = base64.b16encode(File)
    return File
def Decode(file: bytes, codec = 'unicode-escape') -> str:
    File = base64.b85decode(file)
    File = base64.b64decode(File)
    File = base64.b32decode(File)
    File = base64.b16decode(File)
    File = File.decode(codec)
    return File
