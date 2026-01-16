#ANCHOR - Xây dựng hàm
"""
- Để xây dựng hàm, ta sử dụng từ khóa def
- Xác định các tham số trước khi xây dựng hàm 
- Return nếu mong muốn hàm trả về một giá trị nào đó
- Hàm chỉ chạy khi nó được gọi (function call). 
#< Sytax:
    def function_name(parameter):
        #code

def xin_chao(name):
    print('Hello', name)
xin_chao('Dung')
"""

"""
def tong(a, b):
    sum = a + b
    return sum
print(tong(100, 200))

#! Function call is made by assignment
a,b: Tham số: Parameter
100,200: Đối số: Arguement
--> Lời gọi hàm sẽ được thực hiện bằng việc gán đối số cho tham số
"""

#ANCHOR - Số nguyên tố
"""
import math
def nguyento(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
print(nguyento(n))
"""


#ANCHOR - Số fibonacci (in ra n số fibo đầu tiên)
"""
def fibo(n):
    f0 = 0
    f1 = 1
    print(f0, f1, end = ' ')
    for i in range(2, n):
        fn = f0 + f1 
        print(fn, end = ' ')
        f0 = f1
        f1 = fn
"""

#ANCHOR - Fibonacci 1
"""
# In ra số Fibonancci thứ n và chia dư với 1e8+7
def fibo1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f0 = 0
        f1 = 1
        for i in range(2, n):
            fn = f0 + f1
            fn %= 1e9 + 7       # hạn chế TLE
            f0 = f1
            f1 = fn
    return int(fn % (1e9 + 7)) 
n = int(input())
print(fibo1(n))
"""

#ANCHOR - UCLN & BCNN
"""
#< UCLN (Giải thuật Euclid)
import math
def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
print(gcd(18,24))

#< BCNN 
def lcm(a,b):
    return a*b // gcd(a,b)
print(lcm(100,30))

#! Cách 2: dùng hàm có sẵn
def gcd_1(a,b):
    return math.gcd(a,b)

def lcm_1(a,b):
    return a * b // math.gcd(a,b)
"""

#ANCHOR - Phân tích thừa snt (dưới dạng tích các thừa snt)
"""
def analyze_prime_num(n):
    import math
    for i in range(2, math.isqrt(n) + 1):
        #< Nếu n chia hết cho i: i sẽ là thừa snt
        while n % i == 0:
            print(i, end = ' ')
            n //= i
    if n > 1:         # sau vòng for mà n chưa ptich hết mà vẫn != 1 thi n chính là thừa snt cuối cùng --> in ra riêng
        print(n)
analyze_prime_num(60)
"""

#ANCHOR - Bậc của thừa snt trong N!
"""
#< Cách 1:
def analyze_prime_factorial(n, p):
    for i in range(p, n + 1, p):
        while i % p == 0:
            res += 1
            i //= p
    return res
print(analyze_prime_factorial(10,2))

#ANCHOR - Legandre
#< Cách 2: Legendre
#> CT: N // p + N // p^2 + N // p^3 + ... + N // p^k (p^k <= N)
# VD: p = 3. Lượt thứ nhất chỉ xét những bội chia hết cho 3, lượt thứ hai cho 3^2, lượt thứ ba cho 3^3,...
def legandre(n, p):
    res = 0
    tmp = p
    while tmp <= n:
        res += n // tmp
        tmp *= p
    return res
print(legandre(10,2)) 
"""

#ANCHOR - BINARY EXPONENTIATION (lũy thừa nhị phân)
# Thay vì tính lũy thừa bằng vòng for thì độ phức tạp sẽ rất lớn --> dùng lũy thừa nhị phân --> Độ phức tạp log2(b)
"""
Công thức:
    Với b chẵn: a^(b//2) * a^(b//2)
    Với b lẻ: a^(b//2) * a^(b//2) * a   

def bin_pow(a, b):
    res = 1
    while b != 0:
        # Check if the last bit of b is either 1 or 0
        if b % 2 == 1:
            res *= a
        b //= 2     # Dịch bit sang trái --> dùng phép chia
        a *= a      # Lũy thừa nhân dần 
    return res 
print(bin_pow(2,5))
"""

#ANCHOR - MODULAR ARITHMETIC (lý thuyết đồng dư)
"""
- 4 công thức:
    (a + b) % c = ((a % c) + (b % c)) % c
    (a - b) % c = ((a % c) - (b % c)) % c
    (a * b) % c = ((a % c) * (b % c)) % c
    (a / b) % c = ((a % c) * (b^(-1) % c)) % c      #> Vì b ở dưới mẫu nên muốn đưa lên tử thì phải mũ -1 (nghịch đảo module)
    (a^b) % c = (a % c)^b % c       #> Module cơ số
    #< Bài toán chia dư, tính đến đâu chia dư đến đấy

def pow_mod(a,b,c):
    res = 1
    while b != 0:
        if b % 2 == 1:
            res *= a 
            res %= c
        b //= 2
        a *= a
        a %= c      # sau khi lũy thừa lên thì % c lập tức
    return res
a,b = map(int, input().split())
print(pow_mod(a, b, 10000000007))
"""

#ANCHOR - (!)TỔ HỢP 
"""
- Tính tổ hợp chập k của n: 
    CT: n! / k! * (n - k)!
    CT rút gọn: n * (n - 1) * (n - 2)...(n - k + 1)! / k!  

def to_hop(n, k):
    res = 1
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res
print(to_hop(12,10))
"""

#ANCHOR - Luyện tập viết hàm 
"""
import math
#1. ktra n là snt
def prime_check(n):
    if n < 2:
        return 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

#2. In tổng chữ số của n
def total_digit(n):
    if n < 10:
        return False
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res

#3. In tổng chữ số CHẴN của n
def total_even_digit(n):
    res = 0
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            res += digit
        n //= 10
    return res

#4. In tổng chữ số của n là SNT
def total_prime_digit(n):
    res = 0
    while n != 0:
        digit = n % 10
        if digit in [2,3,5,7]:
            res += digit
        n //= 10
    return res

#5. In số lật ngược của n
def reverse(n):
    res = 0
    while n != 0:
        res = res * 10 + n % 10
        n //= 10
    return res

#6. In SỐ LƯỢNG ước của n là snt
def analyze_prime_num(n):
    cnt = 0
    for i in range(2, math.isqrt(n) + 1):
        #< Nếu n chia hết cho i: i sẽ là thừa snt
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n //= i
    if n > 1:         # sau vòng for mà n chưa ptich hết mà vẫn != 1 thi n chính là thừa snt cuối cùng --> in ra riêng
        cnt += 1
    return cnt

#7. In ước nguyên tố LỚN NHẤT của n (thừa snt cuối cùng)
def largest_prime_num(n):
    res = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            res = i
            while n % i == 0:
                n //= i
    if n > 1:
        res = n
    return res

#8. ktra nếu n tồn tại ít nhất 1 số 6
def check_6(n):
    while n != 0:
        digit = n % 10
        if digit == 6:
            return 1
        n //= 10
    return 0  

#9. ktra nếu tổng chữ số của n chia hết cho 8
def divide_by_8(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    if res % 8 == 0:
        return 1
    return 0

#10. Tính tổng giai thừa của các chữ số n
def total_factorial(n):
    res = 0
    while n != 0:
        res += math.factorial(n % 10)
        n //= 10
    return res

#11. Ktra n có phải chỉ được tạo bởi 1 số hay không (VD: 222, 3333, ....)
def check_one_digit(n):
    res = 0
    tmp = n
    while tmp != 0:
        res = res * 10 + tmp % 10
        tmp //= 10
    if n == res:
        return 1
    else: 
        return 0

#< 11.1 (cách 2)
def check_one_digit_1(n):
    last = n % 10
    while n != 0:
        if n % 10 == last:
            return 0
        n //= 10
    return 1 
    
#12. Ktra chữ số ở hàng đơn vị của n lớn nhất hay không
def check_max(n):
    max = n % 10
    n //= 10
    while n != 0:
        tmp = n % 10
        if tmp > max:
            return 0
        n //= 10
    return 1

#13. In tổng lũy thừa chữ số của n với số mũ là số chữ số
def total_power(n):
    count = 0
    tmp = n
    while tmp != 0:
        count += 1
        tmp //= 10
    res = 0
    while n != 0:
        res += math.pow((n % 10), count)
        n //= 10
    return int(res)

n = int(input())

print(1, prime_check(n))
print(2, total_digit(n))
print(3, total_even_digit(n))
print(4, total_prime_digit(n))
print(5, reverse(n))
print(6, analyze_prime_num(n))
print(7, largest_prime_num(n))
print(8, check_6(n))
print(9, divide_by_8(n))
print(10, total_factorial(n))
print(11, check_one_digit(n))
print(11.1, check_one_digit_1(n))
print(12, check_max(n))
print(13, total_power(n))
"""

#ANCHOR - Số thuần nguyên tố
"""
# Cho trong đoạn a,b. Hãy đếm xem có bao nhiêu số thuần nguyên tố (là snt, chữ số là snt, tổng cũng là snt)
import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check_every_digit_and_sum(n):
    sum = 0
    while n != 0:
        r = n % 10
        if r not in [2,3,5,7]:
            return False
        sum += r
        n //= 10
    return snt(sum)         #check luôn

a,b = map(int, input().split())
cnt = 0
for i in range(a,b + 1):
    if check_every_digit_and_sum(i) and snt(i):         # nếu trong if có nhiều điều kiện kết nối bằng and, thì nếu a sai sẽ không check b và c
        cnt += 1
print(cnt) 
"""

#ANCHOR - Số chính phương trong đoạn 
"""
# chú ý cận dưới
import math
a,b = map(int, input().split())
can1, can2 = math.isqrt(a), math.isqrt(b)
if can1 * can1 != a:            # lấy vd a = 10, b = 100 sẽ hiểu
    can1 += 1
for i in range(can1, can2 + 1):
    print(i*i, end = ' ')
"""

#ANCHOR - Số chính phương 3
"""
import math
a,b = map(int, input().split())
can1, can2 = math.isqrt(a), int(math.sqrt(b))
if can1 * can1 != a:
    can1 += 1
print(can2 - can1 + 1)
"""

#ANCHOR - Số lộc phát
"""
# Một số lộc phát nếu chỉ có các chữ số 0,6,8
n = int(input())
while n != 0:
    if n % 10 not in [0,6,8]:
        print(0)
    n //= 10
print(1)
"""

#ANCHOR - Goldbach conjecture
"""
# Một số nguyên dương chẵn >= 4 đều có thể biểu diễn dưới dạng tổng của 2 snt
import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

test = int(input('Hay nhap so testcase: '))
for i in range(test):
    n = int(input())
    for i in range(2, n//2 + 1):      # n//2 vì 1 cặp chỉ in 1 lần, chỉ cần 1 số là suy ra cả cặp
        if snt(i) and snt(n - i):       # i + (n - i) = n là snt
            print(i, n - i)
"""

#ANCHOR - Cặp snt cùng nhau
"""
# Các cặp snt cùng nhau trong khoảng a,b đều có ucln = 1
import math
a,b = map(int, input().split())
for i in range(a, b):
    for j in range(i + 1, b + 1):
        if math.gcd(i, j) == 1:
            print('(' + str(i), str(j) + ')', sep = ',')
"""

#ANCHOR - Ước SNT nhỏ nhất
"""
# In ra ước snt nhỏ nhất của các số từ 1 đến N. Ước snt nhỏ nhất của 1 là 1, số chẫn là 2, của các snt là chính nó
#< Cách 1
import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print(1)
    if i % 2 == 0:
        print(2)
    elif snt(i):
        print(i)

#< Cách 2
import math
def solve(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    for i in range(3, math.isqrt(n) + 1, 2):        # bắt đầu từ 3 và step = 2 để luôn là số lẻ
        if n % i == 0:
            return i
    return n

n = int(input())
for i in range(1, n + 1):
    print(solve(i))
"""

#ANCHOR - (!)Phân tích thừa snt
"""
import math
def analyze(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:      # chỉ khi là ước số thì mới làm việc
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(i, cnt, sep = '^', end = '')
            #! chú ý
            if n > 1:
                print(' * ', end = '')
    if n > 1:               # n > 1 là chưa ptich xong thì còn in ra dấu * ở giữa, n về 1 thì không in nữa
        print(n, end = '^1')

n = int(input())
analyze(n)
"""

#ANCHOR - (!) Số Sphenic
"""
# Số Sphenic là số đc ptich dưới dạng tích của ba thừa snt KHÁC NHAU. VD: 30 = 2*3*5
import math
def solve(n):
    cnt = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:      # là một thừa snt
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i
            if mu >= 2:
                return False
            else:               # khi mũ = 1 thì mới tính là một thừa snt
                cnt += 1        
    if n > 1:                   # thừa snt cuối cùng
        cnt += 1
    return cnt == 3     # giống return n > 1, tức nếu cnt == 3 thì True, không thì False

if __name__ == '__main__':
    n = int(input())
    if solve(n):
        print(1)
    else:
        print(0)
"""

#ANCHOR - (!) Số Smith
"""
# Số Smith nếu N không là snt và có tổng các chữ số của N bằng tổng các chữ số của các thừa snt trong ptich N
#> VD: N = 666 có các tích thừa snt là 2,3,3,37 có tổng các chữ số là 18 (2 + 3 + 3 + 3 + 7)
import math
def cal_sum(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res

def nguyento(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    if nguyento(n):
        return False
    sum1 = cal_sum(n)
    sum2 = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                sum2 += cal_sum(i)
                n //= i
    if n > 1:
        sum2 += cal_sum(n)
    return sum1 == sum2

if __name__ == '__main__':
    n = int(input())
    if solve(n):
        print('YES')
    else:
        print('NO')
"""

#ANCHOR - Ước SNT lớn nhất
"""
import math
def solve(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            res = 0
            while n % i == 0:
                res = i
                n //= i
    if n > 1:
        res = n
    return res
    
if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        n = int(input())
        print(solve(n))
        
"""

#ANCHOR - (!)Bình phương snt 1
"""
# Số đẹp là khi: chia hết cho một snt và chia hết cho bình phương snt đó 
#> Ptich một thừa snt có ít nhất một snt có số mũ là 2
import math
def solve(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i
            if mu >= 2:
                return True
    return False

if __name__ == '__main__':
    a,b = map(int, input().split())
    for i in range(a, b + 1):
        if solve(i):
            print(i, end = ' ')
            
"""

#ANCHOR - Bình phương snt 2
"""
# Số đẹp là khi: chia hết cho một snt THÌ CŨNG PHẢI chia hết cho bình phương snt đó (đk và, bắt buộc đi chung)
#> Mọi thừa snt bắt buộc phải có số mũ là 2 hết
import math
def solve(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i
            if mu == 1:
                return False
    if n > 1:       # chắc chắn có số mũ là 1
        return False
    return True

if __name__ == '__main__':
    a,b = map(int, input().split())
    for i in range(a, b + 1):
        if solve(i):
            print(i, end = ' ')
"""
            
#ANCHOR - Số hoàn hảo
"""
# Số hoàn hảo có tổng các ước bằng chính số đó  
import math
def snt(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
for i in range(1, 32):      # vì 2^(2p) = 2^64 --> p = 32
    if snt(i) == True:
        tmp = int((2 ** i) - 1)
        if snt(tmp) == True:
            hh = int(tmp * 2**(i - 1))
            print(hh)
            if hh == n:
                print('YES')
                exit(0)
else:
    print('NO')
"""

#ANCHOR - Số thuận nghịch có 3 ước nt
"""
# Một số đc coi là đẹp nếu nó là số thuận nghịch và có ít nhất 3 ước nt khác nhau
import math
def check_rev(n):
    if n < 10:
        return False
    rev = 0
    tmp = n
    while tmp != 0:
        rev = rev * 10 + tmp % 10
        tmp //= 10
    return rev == n

def solve(n):
    cnt = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n //= i
    if n > 1:
        cnt += 1
    return cnt >= 3

if __name__ == '__main__':
    a,b = map(int, input().split())
    ok = False
    for i in range(a, b + 1):
        if check_rev(i) and solve(i):
            print(i, end = ' ')
            ok = True
    if not ok:
        print('-1')
"""

#ANCHOR - Số thuận nghịch, lộc phát
"""
# Số đẹp: thuận nghịch, có chứa ít nhất một số 6, tổng các chữ số của nó có chữ số cuối cùng là 8
import math
def check_rev(n):
    rev = 0
    tmp = n
    while tmp != 0:
        rev = rev * 10 + tmp % 10
        tmp //= 10
    return rev == n

def cal_sum(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total

def loc_phat(n):
    sum = cal_sum(n)    
    ok = False
    if check_rev(n):
        while n != 0:
            if n % 10 == 6 and sum % 10 == 8:
                ok = True
            n //= 10
    return ok

if __name__ == '__main__':
    a,b = map(int, input().split())
    for i in range(a, b + 1):
        if loc_phat(i):
            print(i, end = ' ')
"""

#ANCHOR - Chữ số cuối cùng lớn nhất
"""
# Nhập n, liệt kê các snt: <= n và có chữ số cuối cùng lớn nhất
import math
def snt(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def last_digit(n):
    max = n % 10
    n //= 10
    while n != 0:
        if max < (n % 10):
            return False
        n //= 10
    return True

if __name__ == '__main__':
    n = int(input())
    cnt = 0
    for i in range(n):
        if snt(i) and last_digit(i):
            cnt += 1
            print(i, end = ' ')
    print()
    print(cnt)      
"""

#ANCHOR - (!)Thừa snt thứ K
"""
# VD: n = 28, k = 3 sẽ có output = 7 vì n = 28 = 2 * 2 * 7
import math
def solve(n, k):
    cnt = 0
    for i in range(2, math.isqrt(n) + 1):
        while n % i == 0:
            cnt += 1
            if cnt == k:
                return i
            n //= i
    if n > 1:
        cnt += 1
    if cnt == k:
        return n
    return -1        

if __name__ == '__main__':
    n,k = map(int, input().split())
    print(solve(n,k))
"""

#ANCHOR - Tính gtri của hàm F
"""
# Tính: f(n) = -1 + 2 - 3 + .. + (-1)^n * n
def cal_f(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += (-1) * i
        else:
            total += i
    return total

if __name__ == '__main__':
    n = int(input())
    print(cal_f(n)) 
"""

#ANCHOR - T-prime
"""
# N là t-prime nếu nó là bình phương của 1 số nguyên tố --> tìm các ước snt và in ra bình phương nó
import math
def snt(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve(n):
    for i in range(1, math.isqrt(n) + 1):
        if snt(i):
            print(i**2, end = ' ')

if __name__ == '__main__':
    n = int(input())
    solve(n)
"""

#ANCHOR - (!)Count ƯỚC SỐ của số nguyên dương N
"""
import math
if __name__ == '__main__':
    T = int(input())
    ans = 1
    for i in range(T):
        p,e = map(int, input().split())
        ans *= (e + 1)
        ans %= 1000000007       # modular arithmetic
    print(int(ans % 1e9 + 7))
"""

#ANCHOR - Đếm chữ số 0 liên tiếp tính từ cuối của N!
"""
# SL số 0 là do tích của số 2 và 5 (số 0 ở cuối bắt buộc phải = 10, là do tích của 2 & 5) --> tìm bậc của 2 và 5, lấy bậc nhỏ hơn (chắc chắn là 5)
def legen(n,p):
    # n là tử số, p là mẫu số, mẫu số lũy thừa sau mỗi lần
    total = 0
    tmp = p
    while tmp <= n:
        total += n // tmp
        tmp *= p
        total %= 1000000007
    return total

if __name__ == '__main__':
    n = int(input())
    print(legen(n, 5) % 1000000007)
"""

