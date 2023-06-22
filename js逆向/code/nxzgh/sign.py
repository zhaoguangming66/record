from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 获得 RSA 公钥
pubkey_str = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCIU9rkjyAIx4RAXCj9Zg4ItbIEjaRrYFzJ6qUH3WtQPFdUhfMKZ3CcbqHdD80iBH95iJWqMVNJXsKOJaF7JUYS231V/PKq8xhgwe3y5zx99wEmkT3FXvVf1tICehsIf5kqvbx4V6zEU8aOUnmhGlQde9Dfo41NrJiPgNRahouEuwIDAQAB'
pubkey = RSA.importKey(base64.b64decode(pubkey_str))

# 需要加密的数据
data = "IJNSCUAGEHOZYHVC"

# 使用 RSA 公钥对数据进行加密
cipher = PKCS1_v1_5.new(pubkey)
ciphertext = cipher.encrypt(data.encode('utf-8'))

# 对密文进行 Base64 编码
encoded = base64.b64encode(ciphertext)

print('原始信息：', data)
print('加密后信息：', encoded.decode('utf-8'))


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 获得 RSA 私钥
private_key_str = 'MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIhT2uSPIAjHhEBcKP1mDgi1sgSNpGtgXMnqpQfda1A8V1SF8wpncJxuod0PzSIEf3mIlaoxU0lewo4loXslRhLbfVX88qrzGGDB7fLnPH33ASaRPcVe9V/W0gJ6Gwh/mSq9vHhXrMRTxo5SeaEaVB170N+jjU2smI+A1FqGi4S7AgMBAAECgYBMK95gWoAhp6kDdPsKKt2ojCz9Uk8OF/eAcnTnYhY17KE2/uj/ZTCMl1wlclDBsxWuyFwnjgvlMOcwGWKStg7iYxnnkiPNY/BodGDCrLIdpGqBuL9kdeU/78Qfqk/K8sNhB/USxY+Pltx7vN4Qb9UsbVVfVqux1wBHq/BV3jDOkQJBANqqYDL6a15FFuIQBUFvoHbpm+TdpZOoB7gFjn661QYAzjpuDuhBXtnETWwukWBwmV+O2vajPQfjTN9gWalctZcCQQCfmpRG3PHFscxoIP5YoILn78oS5i1R5ZHNweaFYkL6M3s1XmqXYNiE5oI3BxziU/WEM/KN4W82zqIdEdXy7zZ9AkBEAh9/W3FPVY+jabYovu4abdfFm8YmoWkdK+VAtx0QC+oYNCjAxawZcLtfvTAL3ZlmJgkmEmkl7eT3yIC6cxIrAkAwlRAfhe++WsG6zJg/iBRw32fmWtRewn+gXy55WZDDsloFw8i0bZFa2wO2Fl8vcZkhdeKWV5HP4BQuvxgeC7zNAkBxO/UWJtTL/UTUcxR6tAvxPLDIh2w1Dm2S6G66zblrgh/2ahyNakaq8u3PZyhVvQfq5CIV4bNEjz5ox8KpnnUI'
private_key = RSA.importKey(base64.b64decode(private_key_str))

# 需要解密的数据
encoded = 'MNeauhto5D9kK7GpEexlpD4bfKyBlIIf0hvV+nlVPEMNsbQSJzPs3Jm0jgGZu+zAVWchA2B5KC/81omxaBhIGIW14wBIjiXlUkXDmhfs3elxdO8qZXa8MI39jlgxx/v7/9Hce8012C1QCcSJxd+xJsL9KIBQ4rDYRaFzI9geDYo='

# 使用 RSA 私钥进行解密
decoded = base64.b64decode(encoded)
cipher = PKCS1_v1_5.new(private_key)
origin_text = cipher.decrypt(decoded, None).decode('utf-8')

print('加密后信息：', encoded)
print('解密后信息：', origin_text)


