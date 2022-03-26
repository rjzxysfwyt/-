from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64


class Rsa:
    def __init__(self):
        # 伪随机数生成器
        self.random_generator = Random.new().read
        # rsa算法生成实例
        self.rsa = RSA.generate(1024, self.random_generator)
        # 私钥的生成
        self.private_pem = self.rsa.exportKey()
        # 公钥的生成
        self.public_pem = self.rsa.publickey().exportKey()

    def encrypt(self, message):  # 参数为需要加密的信息
        """
        1024位的证书，加密时最大支持117个字节，解密时为128；
    　　2048位的证书，加密时最大支持245个字节，解密时为256。
        :return:
        """
        rsakey = RSA.importKey(self.public_pem)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 创建用于执行pkcs1_v1_5加密或解密的密码
        cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
        return cipher_text.decode('utf-8')

    def decrypt(self, cipher_text):  # 传入加密后的数据
        encrypt_text = cipher_text.encode('utf-8')
        rsakey = RSA.importKey(self.private_pem)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 创建用于执行pkcs1_v1_5加密或解密的密码
        text = cipher.decrypt(base64.b64decode(encrypt_text), '解密失败')
        # print(text.decode('utf-8'))
        return text.decode('utf-8')


if __name__ == '__main__':
    r = Rsa()
    jiami = r.encrypt('test')
    print(jiami)
    jiemi = r.decrypt(jiami)
    print(jiemi)
