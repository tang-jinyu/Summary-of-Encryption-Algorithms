import random
from sympy import isprime   #isprime用于判断一个数是不是素数
from math import gcd        #gcd函数用于计算最大公约数

#找两个大素数
def generate_large_prime(keysize = 1024):
    while True:#无限循环直至找到素数
        num = random.randrange(2**(keysize-1),2**(keysize))#计算2的（keysize-1）次方确保生成的位数有size-1位
        if isprime(num):
            return num
    
#计算模反运算
def modinv(a,m):  #用于计算a模m的逆元，即：找到x使得ax=1mod m
    def egcd(a,b):  #egcd为递归函数，
        if a == 0:
            return b,0,1
        g, x, y = egcd(b % a,a) #g=gcd(a,b)
        return g,y - (b // a) * x, x
    
    g, x, y = egcd(a,m)
    if g != 1:#说明a和m不互质
        raise Exception('模反元素不存在')
    return x % m

#生成RSA密钥对
def generate_keypair(keysize=1024):
    p = generate_large_prime(keysize // 2)
    q = generate_large_prime(keysize // 2)
    n = p * q
    phi_n = (p-1) * (q-1)

    e = 65537
    d = modinv(e, phi_n)

    return ((n,e),(n,d))

#加密
def encrypt(public_key,plaintext):
    n,e = public_key
    plaintext_int = int.from_bytes(plaintext.encode('utf-8'),'big')
    return pow(plaintext_int,e,n)

#解密
def decrypt(private_key,ciphertext):
    n,d = private_key
    decrypted_int = pow(ciphertext,d,n)
    return decrypted_int.to_bytes((decrypted_int.bit_length()+7) // 8,'big').decode('utf-8')

#测试RSA算法
public_key,private_key = generate_keypair()
message = "tangjinyu是超级巨无敌宇宙第一冰雪聪明机智迷人的美女唐耶！！！"
print("原始消息:", message)
      
ciphertext = encrypt(public_key,message)
print("加密后的密文:", ciphertext)
      
decrypted_message = decrypt(private_key,ciphertext)
print("解密后的消息:", decrypted_message)