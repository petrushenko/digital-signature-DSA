from math import sqrt
from random import randint
from hashlib import sha1


def dsa_file_sign(*, p, q, g, h, k, x, filename):
    err = check_values(q = q, p = p, g = g, h = h, x = x, k = k)
    if (not err):
        f = open(filename, "r")
        data = f.read()

        f.close()
        data.encode("utf-8")

        my_hash = get_sha1(data)

        r = (fast_pow(g, k, p) % q)

        s = fast_pow(k, q-2, q) * (my_hash + x * r) % q

        if (r != 0 and s != 0):
            f = open(filename, "w")

            data = f.read()
            f.close()
            data += '|' + str(r) + '|' + str(s)
            f = open(filename, "w")
            f.write(data)
            f.close()
            return (data, r, s)
        else:
            return -1
    return err


    


def fast_pow(num, power, mod):
    '''
    Быстрое возведение в степень
    Результат по mod
    '''
    #result
    res = 1 
    # (b ^ k) * p = num ^ power
    while power > 0:
        while power % 2 == 0:
            power /= 2
            num = (num * num) % mod
        power -= 1
        res = (res * num) % mod
    return res      


def is_prime(num, k = 30):
    '''
    Вероятностная проверка числа на простоту
    Алгоритм Миллера-Рабина
    num - проверяемое число
    k - количество проверок
    True - вероятно простое 
    False - составное 
    '''
    if(num < 2):
        return False

    if(num == 2):
        return True

    # n - 1 = 2^s * t
    s = 0
    t = num - 1
    while (t % 2 != 1):
        t /= 2
        s += 1
    t = int(t)

    flag = True # flag == False - переход на следующие проверку
    for i in range (1, k):
        a = randint(2, num - 1)
        x = fast_pow(a, t, num)
        if (x == 1 or x == num - 1):
            flag = False
            continue
        for j in range(s - 1):
            x = fast_pow(x, 2, num)
            if (x == 1):
                return False # составное
            if (x == (num - 1)):
                flag = False
                break
        if (flag):
            return False # составное
    return True

def check_values(q, p, g, h, x, k):
    if (not is_prime(q)):
        return 1
    if (not ((p - 1) % q == 0)):
        return 2
    if (not (h in range(1, p - 1))):
        return 3
    if (not (g == fast_pow(h, (p-1) / q, p))):
        return 4
    if (not (0 < x < q)):
        return 5
    if (not (0 < k < q)):
        return 6
    return 0

def get_sha1(data):
       bytes = ""

       h0 = 0x67452301
       h1 = 0xEFCDAB89
       h2 = 0x98BADCFE
       h3 = 0x10325476
       h4 = 0xC3D2E1F0

       for n in range(len(data)):
           bytes+='{0:08b}'.format(ord(data[n]))
       bits = bytes+"1"
       pBits = bits
       #pad until length equals 448 mod 512
       while len(pBits)%512 != 448:
           pBits+="0"
       #append the original length
       pBits+='{0:064b}'.format(len(bits)-1)

       def chunks(l, n):
           return [l[i:i+n] for i in range(0, len(l), n)]

       def rol(n, b):
           return ((n << b) | (n >> (32 - b))) & 0xffffffff

       for c in chunks(pBits, 512): 
           words = chunks(c, 32)
           w = [0]*80
           for n in range(0, 16):
               w[n] = int(words[n], 2)
           for i in range(16, 80):
               w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  

           a = h0
           b = h1
           c = h2
           d = h3
           e = h4

           #Main loop
           for i in range(0, 80):
               if 0 <= i <= 19:
                   f = (b & c) | ((~b) & d)
                   k = 0x5A827999
               elif 20 <= i <= 39:
                   f = b ^ c ^ d
                   k = 0x6ED9EBA1
               elif 40 <= i <= 59:
                   f = (b & c) | (b & d) | (c & d) 
                   k = 0x8F1BBCDC
               elif 60 <= i <= 79:
                   f = b ^ c ^ d
                   k = 0xCA62C1D6

               temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
               e = d
               d = c
               c = rol(b, 30)
               b = a
               a = temp

           h0 = h0 + a & 0xffffffff
           h1 = h1 + b & 0xffffffff
           h2 = h2 + c & 0xffffffff
           h3 = h3 + d & 0xffffffff
           h4 = h4 + e & 0xffffffff

       return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
hash_ = sha1("Hello, world".encode("utf-8"))
my_hash = hash_.hexdigest()
print(my_hash)
print(get_sha1("Hello, world"))



    