
"""计算vlaue在1-max_value之间的逆元"""
def get_inverse_element(value,max_value):
    for i in range(1,max_value):
        if(i*value) % max_value ==1:
            return i
    return -1

"""计算最大公约数，gcd是找最大公约数的函数"""
def gcd_x_y(x,y):
    if y == 0:
        return x
    else:
        return gcd_x_y(y,x % y)
    
"""计算p+q"""
def calculate_p_q(x1,y1,x2,y2,a,p):
    flag  = 1   #定义符号位
    if x1 == x2 and y1 == y2:
        member = 3 * (x1 ** 2) + a  #计算分子，斜率的计算公式
        denominator = 2 * y1        #计算分母
    else:
        member = y2 -y1
        denominator = x2 - x1
        if member * denominator < 0:
            flag  = 0
            member = abs(member)#abs是取绝对值函数
            denominator = abs(denominator)
    
    """将分子分母化为最简"""
    gcd_value = gcd_x_y(member,denominator)#因为gcd是取最大公约数，也就类似约分所以可以化简
    member = int(member / gcd_value)
    denominator = int(denominator / gcd_value)

    """求分母的逆元"""
    inverse_value = get_inverse_element(denominator,p)
    k = (member * inverse_value)
    if flag ==0:
        k = -k
    k =  k %p
    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k *(x1 - x3) -y1)  % p
    return [x3,y3]

"""计算椭圆曲线的阶"""
def get_order(x0,y0,a,b,p):
    x1 = x0
    y1 =  (-1 * y0)  % p
    temp_x = x0
    temp_y = y0
    n = 1
    while True:
        n += 1
        p_value = calculate_p_q(temp_x,temp_y,x0,y0,a,p)
        if p_value[0] == x1 and p_value[1] == y1:
            print("============该椭圆曲线的阶为%d===================="% (n+1))
            return n+1
        temp_x = p_value[0]
        temp_y = p_value[1]

        """计算p和-p"""
def get_x0_y0_x1_y1(x0,a,b,p):
            y0 = -1
            for i in range(0,p):
                if i ** 2 % p == (x0 **3 +a*x0 + b) %p:
                    y0 = i
                    break
                
            if y0 == -1:
                return False
            x1 = x0
            y1 = -1 * y0 %p
            return [x0,y0,x1,y1]
        
"""输出散列图"""
def draw_graph(a,b,p):
    x_y=[]
    for i in range(p):
        x_y.append(["-"for i in range(p)])

    for i in range(p):
        value = get_x0_y0_x1_y1(i,a,b,p)
        if value  != False:
            x0 = value[0]   
            y0 = value[1]
            x1 = value[2]
            y1 = value[3]
            x_y[x0][y0] = 1
            x_y[x1][y1] = 1
    print("椭圆曲线的散列图为：")
    for j in range(p):
        if p-1-j >= 10:
            print (p-1-j,end=" ")
        else:
            print(p-1-j,end=" ")
        for i in range(p):
            print(x_y[i][p-j-1],end=" ")    
            print()
        print(" ",end=" ")        
        for i in range(p):
            if i >= 10:
                print(i,end=" ")
            else:
                print(i,end =" ")
        print()

"""计算NG"""
def calculate_np(G_x,G_y,private_key,a,p):
    temp_x = G_x
    temp_y = G_y
    while private_key != 1:
        p_value = calculate_p_q(temp_x,temp_y,G_x,G_y,a,p)
        temp_x = p_value[0]
        temp_y = p_value[1]
        private_key -= 1
    return p_value

def ecc_encrypt_and_decrypt():
    while True:
        a = int(input("请输入椭圆曲线的参数a:"))
        b = int(input("请输入椭圆曲线的参数b:"))
        p = int(input("请输入椭圆曲线的参数p(p为质数):"))

        if (4*(a**3) + 27*(b ** 2)) % p ==0:
            print("选取的椭圆参数不能用于加密，请重新选择\n")
        else:
            break

    draw_graph(a,b,p)
    print("在图上选出一个点作为生成元G")
    G_x = int(input("你选择的横坐标G_x:"))
    G_y = int(input("你选择的纵坐标G_y:"))
    
    n = get_order(G_x,G_y,a,b,p)
    private_key = int(input("请输入私钥key(<%d):" % n))
    Q = calculate_np(G_x,G_y,private_key,a,p)
    print("===========生成公钥{a=%d,b=%d,p=%d,阶%d,G(%d,%d),Q(%d,%d)}=======")

    #开始加密
    k =  int(input("请给出整数（<%d）:" % n))
    k_G = calculate_np(G_x,G_y,k,a,p)
    k_Q = calculate_np(Q[0],Q[1],k,a,p)
    plain_text = int(input("请输入要加密的明文："))
    cipher_text = plain_text * k_Q[0]

    C = [k_G[0],k_G[1],cipher_text]
    print("密文为：{(%d,%d,),%d,}" % (C[0],C[1],C[2]))

    #解密
    decrypto_text = calculate_np(C[0],C[1],private_key,a,p)

    inverse_value = get_inverse_element(decrypto_text[0],p)
    m = C[2] * inverse_value % p
    print("解密后的明文为%d" % m)

if __name__ == '__main__':
    ecc_encrypt_and_decrypt()



"""key：明文需要小于p"""
