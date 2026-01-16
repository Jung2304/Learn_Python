#ANCHOR - Câu lệnh IF
"""
Các câu lệnh bên trong if được thụt lề (1 tab) so với if
Syntax: 
    if condition:
        #code

#! VD1: Kiểm tra xem n có phải là số nằm trong đoạn [50, 100]
n = int(input())
if (n >= 50 & n <= 100): 
    print('Hello Python')
"""

#ANCHOR - Luyện tập viết câu điều kiện
"""
import math
N = int(input())
#1
if (N % 2 == 0):
    print('YES')
else: 
    print('NO')
#2
if (N % 3 == 0) and (N % 5 == 0): 
    print('YES')
else: 
    print('NO')
#3
if (N % 3 == 0) and (N % 7 != 0): 
    print('YES')
else:
    print('NO')
#4 
if (N % 3 == 0) or (N % 7 == 0):
    print('YES')
else:
    print('NO')
#5
if (N > 30) and (N < 50):
    print('YES')
else:
    print('NO')
#6
if (N >= 30) and ((N % 2 == 0) or (N % 3 == 0) or (N % 5 == 0)):
    print('YES')
else:    
    print('NO')
#7. Số có 2 chữ số --> >= 10 and <= 99
r = N % 10  #tìm chữ số cuối cùng
if (N >= 10) and (N <= 99) and ((r == 2) or (r == 3) or (r == 5) or (r == 7)):
    print('YES')
else:
    print('NO')
#8 
if (N <= 100) and (N % 23 == 0):
    print('YES')
else: 
    print('NO')
#9 
if (N < 10) or (N > 20):
    print('YES')
else:
    print('NO')
#10
if (r % 3 == 0):
    print('YES')
else:
    print('NO')
"""

#ANCHOR - Shorthand if 
"""
#< Shorthand if: Bạn có thể sử dụng câu lệnh if trên 1 dòng
a, b = 100, 200
if a < b : print(a, 'less than', b)

#< Nếu trong if có nhiều câu lệnh, bạn có thể đặt dấu chấm phẩy giữa các câu lệnh
a, b = 100, 200
if a < b : print(a, 'less than', b); print('28tech'); print('abcd')
"""

#ANCHOR - Toán tử ba ngôi (Ternary operator) (Condition operator)
"""
variable = statement (true branch)  if condition else   statement (false branch)

a, b = 100, 200
res = '28tech' if a < b else 'python'
print(res)

n = 200
print("Even number" if n % 2 == 0 else "Odd number")
"""

#ANCHOR - Bài 8: Tổng, hiệu, tích, thương
"""
a, b = map(int, input().split())
print(a + b, a - b, a * b, sep = '\n')
if b == 0:
    print('INVALID')
else:
    q = a / b
    print('%.4f' % q)
"""

#ANCHOR - Bài 9: Kiểm tra năm nhuận
"""
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('YES')
else:
    print('NO')
"""

#ANCHOR - Bài 10: Tam giác hợp lệ
"""
# Cho 3 cạnh a, b, c là độ dài 3 cạnh của tam giác, kiểm tra xem a, b, c có thể tạo thành một tam giác hợp lệ hay không?
a, b, c = map(int, input().split())
if a > 0 and b > 0 and c > 0 and (a + b > c and a + c > b and b + c > a):
    print('YES')
else:
    print('NO')
"""

#ANCHOR - Bài 11: Kiểm tra tam giác
"""
# Tam giác đều in ra 1, tam giác cân in ra 2, tam giác vuông in ra 3, tam giác thường in ra 4, không hợp lệ in ra "INVALID"
a,b,c = map(int, input().split())
if (a > 0 and b > 0 and c > 0):
    if (a == b == c):
        print("1")
    elif (a == b or b == c or a == c):
        print("2")
    elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        print("3")
    elif (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
        print("4")
else:
    print("INVALID")
"""

#ANCHOR - Bài 12: Số ngày của tháng
"""
# Cho biết tháng và năm, hãy in ra số ngày tương ứng có trong tháng đó. Chú ý tháng 2 của năm nhuận có 29 ngày
t,n = map(int, input().split())
if t >= 1 and t <= 12 and n >= 0:
    if (t == 4 or t == 6 or t == 9 or t == 11):
        print("30")
    elif (t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12):
        print("31")
    elif (t == 2):
        if (n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)):
            print("29")
        else:
            print("28")
else:
    print("INVALID")
"""

#ANCHOR - Bài 15: Mua nước
"""
n,a,b = map(int, input().split())
res = 0
if a * 2 <= b:      # VD: nếu chai 1 lít rẻ hơn thì mua n loại chai 1 lít đó
    print(n * a)
else:
    if (n % 2 == 0):
        print(n // 2 * b)
    else:
        print(n // 2 * b + a)
"""

#ANCHOR - Bài 19: Domino
"""
M,N = map(int, input().split())
if (N % 2 == 0):
    print(N // 2 * M)   # tính vùng cơ bản
else:
    print(N // 2 * M + M // 2)
"""

#ANCHOR - Bài 20: Lát đá quảng trường
"""
n,m,a = map(int, input().split())
x, y = 0, 0
if (n % a == 0):
    x = n // a
else:
    x = n // a + 1
if (m % a == 0):
    y = m // a
else:
    y = m // a + 1
print(x * y)
"""

#ANCHOR - Bài 21: Frog
"""
a,b,k = map(int, input().split())
if (k % 2 == 0):
    print((k // 2 * a) - (k // 2 * b))
else:
    print((k // 2 + 1) * a - (k // 2 * b))
"""

#ANCHOR - Bài 22: Đồng xu
"""
n,S = map(int, input().split())
if (S % n == 0):
    print(S // n)
else:
    print(S // n + 1)
"""

#ANCHOR -  Bài 24: Đường đi ngắn nhất
"""
import math
a,b,c = map(int, input().split())
d1 = a + b + c
d2 = 2*(a+c)
d3 = 2*(a+b)
d4 = 2*(b+c)
print(min(d1,d2,d3,d4))
"""

#ANCHOR - Bài 25: Đổi tiền
"""
n = int(input())
res = 0
res += n // 100
n %= 100        # VD: 3455, đổi được 34 tờ 100 --> 3455 - 34 * 100 = 55 <=> 3455 % 100 == 55
res += n // 20
n %= 20
res += n // 10
n %= 10
res += n // 5
n %= 5
res += n 
print(res)
"""

#ANCHOR - Bài 28: Cấp số cộng
"""
#> CT: S(n) = (n * (u1 + un)) / 2
#>     un = u1 + (n - 1)*d
n,u1,d = map(int, input().split())
un = u1 + (n - 1)*d         #> u(n+1) = un + d <=> u2 = u1 + d => u3 = u1 + 2d --> un = u1 + (n-1)*d
S = (n * (u1 + un)) // 2
print(int(S))
"""

#ANCHOR - Bài 29: Cấp số nhân
"""
a,b,c,d = map(int, input().split())
q = b / a       #< không chia nguyên được vì nếu có dãy: 2 4 9 18 thì sẽ nhầm lẫn công bội = 2
if (b % a == 0):
    if (q * b == c and q * c == d):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
"""

#ANCHOR - Bài 30: Bizon the Champion

a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())
cup, medal = a1+a2+a3, b1+b2+b3
shelf1, shelf2 = 0, 0
if (cup % 5 == 0):
    shelf1 = cup // 5
else: 
    shelf1 = cup // 5 + 1
if (medal % 10 == 0):
    shelf2 = cup // 10
else:
    shelf2 = cup // 10 + 1
if (shelf1 + shelf2 <= n):
    print("YES")
else:
    print("NO")