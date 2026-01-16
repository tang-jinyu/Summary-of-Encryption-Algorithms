一、RSA简介

RSA是一种典型的非对称加密算法，也是使用最为广泛的公钥算法之一。



二、RSA推导

1.设计目标

首先我们要设计非对称加密系统，即需要公钥和私钥，且满足①公钥推不出私钥；②私钥可以推出公钥；

2.设计思想

为了满足上述两点要求，主要用到模指数运算【特点：正向计算容易，逆向计算特别困难，满足条件①】和欧拉定理【满足条件②】

欧拉定理：如果整数M和n互质，那么就有M^Φ(n)≡1 mod n 成立

Φ(n)是正整数n的欧拉函数，表示小于n且与n互质的正整数的个数
a. 如果n是质数，和任意一个比它小的正整数都是互质的，因此当n是质数时，Φ(n)=n-1，
b. 如果n是合数，我们令n=p*q，则有Φ(n)=Φ(p*q)，根据欧拉函数的”积性“，上式可以分解为Φ(n)=Φ(p)*Φ(q)

<img width="1100" height="731" alt="image" src="https://github.com/user-attachments/assets/0a582d19-ef1e-4f26-a8f7-f2ff1037bd51" />

<img width="1042" height="789" alt="image" src="https://github.com/user-attachments/assets/6c14ba03-b949-4e26-8895-f729b0b01207" />

[博主不知道如何在这里进行公式编辑，这篇文章的原理讲得很清晰，需要自取：https://www.cnblogs.com/shall2019/p/19433272]

三、RSA流程

基于上述推导，我们可知RSA加密算法的流程：

（1）密钥生成

①选择两个巨大的质数p和q

②计算n=p*q和Φ(n)=(p-1)*(q-1)

③选择整数e使得1<e<Φ(n)，并且e和Φ(n)互质（通常e=65537）

④求出d使得e * d ≡ 1 mod Φ(n)

（2）加密

对于明文M，计算密文C=M^e mod n

（3）解密

对于密文C，计算明文M=C^d mod n

四、结果

可以正常进行加密解密

<img width="1177" height="410" alt="image" src="https://github.com/user-attachments/assets/0377a032-786c-49e0-b500-97963ed74f48" />

<一些碎碎念>

真的很好玩哎！！以后要是姐喜欢的人出现了，我就给他一堆加密后的数字和私钥，让他解密才能知道我在讲啥~


五、参考文献

1.https://www.cnblogs.com/shall2019/p/19433272  【原理很清晰】

2.https://harlanhu.com/posts/explore/algorithm/rsa-algorithm/


六、展望

【因为我应该还是做后量子或者全同态，所以不深究，如果后续有时间的话：】

1.与对称加密联合，RSA加密密钥，对称加密数据；

2.试着实现数字签名、身份认证等实际应用
