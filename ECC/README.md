一、ECC原理

椭圆曲线密码学（Elliptic Curve Cryptography，简称ECC）是一种基于椭圆曲线数学结构的公钥加密技术，与传统的RSA密码系统相比，ECC能够在远短的密钥长度下提供同等甚至更高的安全性。例如，一个256位的ECC密钥提供的安全强度，大致相当于一个3072位的RSA密钥。因此ECC特别适合在计算能力、存储空间和带宽受限的环境中（如移动设备、物联网芯片和区块链系统）使用，目前被广泛应用于数字签名（ECDSA）、密钥交换（ECDH）和加密传输等关键领域。

在分析分析量子破解前，有必要简单介绍一下椭圆曲线以及其数据加密的基本原理，首先椭圆曲线是一些列满足以下方程的曲线：y^2=x^3+ax+b

<img width="1000" height="700" alt="image" src="https://github.com/user-attachments/assets/e9badbd6-9fae-4a7b-82f6-5c21b0c82116" />

在这里，我们需要知道椭圆曲线上的点加和点乘运算：

<img width="822" height="651" alt="image" src="https://github.com/user-attachments/assets/fdf5e1ce-94fd-4d0a-8ddd-8e7daaac59ba" />

还需要知道阶的计算：

<img width="799" height="505" alt="image" src="https://github.com/user-attachments/assets/c5526b77-7f14-42f5-bd00-598bc763db74" />


二、ECC加密流程

（1）生成密钥

选择椭圆曲线 E和基点 G ，基点G的阶为质数 n， 生成小于 n 的随机整数 k 作为加密私钥。我们在通过私钥k和基点G来生成公钥 Q 即 Q=k⋅G 

（2）加密明文

 将明文编码为曲线上的点 M。 选择随机数（r<n ）。 然后通过公钥 Q 计算得到密文对 ( cipher1,cipher2),cipher1=M+r·Q,cipher2=rG

(3)解密密文

有了密文对后，我们可以通过私钥解密密文得到明文： M=Cipher1−k⋅Cipher2=M+r⋅Q−k⋅r⋅G=M+r⋅Q−r⋅k⋅G=M+r⋅Q−r⋅Q=M


三、参考资料

1.https://ehds.github.io/uploads/papers/ecc.pdf

2.https://bbs.kanxue.com/thread-289750.htm

3.https://xz.aliyun.com/news/13476  【原理很清晰】

4.https://zhuanlan.zhihu.com/p/42629724

5.https://www.cnblogs.com/l-xx123/p/18227104
