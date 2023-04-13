import Crypto.Cipher.AES
import Crypto.Util.Padding
import binascii

def b(t):
    e = "BE45D593014E4A4EB4449737660876CE".encode('utf-8')
    n = "A8909931867B0425".encode('utf-8')
    cipher = Crypto.Cipher.AES.new(e, Crypto.Cipher.AES.MODE_CBC, iv=n)
    decrypted = cipher.decrypt(binascii.a2b_hex(t))
    return Crypto.Util.Padding.unpad(decrypted, Crypto.Cipher.AES.block_size).decode('utf-8')


if __name__ == '__main__':
    text ="N1jfMuHUNZzAwf7B5RzFD9WLxZVvOWITQvJcOo2cP6XQgm4gRAFIln/wh9chBqc9ggcnghp6I+5pwNcSiCzInF1w4HwCgCEcZCk/+twDrQ/4CCOCiCeoRZZVEKBYPwaHUtgJVEWshGV03hyPuMoQYlWKIkDlNWEMYk/uSuBSrS+D4y9iu/rwbKZke3MOvVIBBaISmPJmOp1cRiS2WHOQ7F70covHJtRsgJoURC8yt10euefxKc676CmNGxb3SoC1RKHWUrVoY07LZtkiFj7oTnxrFZcMtSwXRRbAglwdVoIzEGLCtHalEeMGbrn9CxMIAZ7LvjyjKb2Fq2LTQSXvKSVLmyqklXcppfkS4s9OAaS8N3D027MpdX9ZQaZiJyMFmFhZ18JYodatTshSYqTM4JaSdtxH4nqfN0ufXW/BA0hty+c6EktPcAC7wl51g2PDG0dStYmNMYBBIf9S4YnPZzCFbO1dv2w3RhuyMsWyoNGDYJ9BD6mVKEeiwNj51Nr3f3vRp3mhXtb4H8USXmd+NqYBDzonVap4uezoxd9aptz8lauFtFmLiYNOCIWlF+SHNWfu3pZ5j0tMp3ZMo4glWv4LJQzr61dtdR4A18WBlvv5pBgE0KXW3U8lZXLdelg4adMaWh02q9UBYNHkPU7QSg/W7Y2ckkig9Cpk6V40vRgSokt8vkiyc8QpEt+wiT1Y07Eh61Itr9aC6xV2yOlCfw/YVmcY3ZS71+kgc3pIe6ZZIrS3/AuSxE0hFhR49MAUrFhQ14N97lQ3kfYdpMcCBNUyYnukZOKkvOvwU0UjaOjK/xdovmiNDWliJsaqicEt9LANJ9cmUg/WuyXuSh/QgtaNWB6FgIvNch+iO4Ru1n5mmx3lqxRBd1/69iehZ2+fjgAUxAZueS9wnLREs+kzOoKcDqorJuLJmhl2gYEHfHdU+LO44EUCFKr49IWgwLm4".encode().hex()
    print(b(text))
