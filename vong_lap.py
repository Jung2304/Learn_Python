#NOTE - Trong Python không có do...while. Chỉ có for và while.

#ANCHOR - FOR LOOP & RANGE()
"""
Syntax:
    for var in iterable:
        statement
        statement
    else:           (khi vòng for kết thúc, muốn thực hiện câu lệnh gì đó thì ghi vào else)
        statement 
"""

#REVIEW - RANGE
"""
Hàm range() sẽ sinh ra một dãy số và bạn sẽ sử dụng vòng for để duyệt qua từng số trong dãy đã sinh ra.
Syntax:
    range (start, stop, step)
Các tham số:
    start: Giá trị bắt đầu của dãy số (ko có thì mặc định là 0).
    stop: Giá trị cuối cùng của dãy số (cận này không được lấy). 
    step: Bước nhảy của dãy số (ko có thì mặc định là 1). (ko bao giờ = 0 hoặc số âm, luôn phải có bước nhảy)
    Không thể thay đổi biến i, vì cách hoạt động như for each (gán rồi làm việc)
VD:
    for i in range(1, 11, 1):
        print(i)
"""

#ANCHOR - Nested loop
"""
Cách hoạt động: Mỗi vòng lặp của vòng for bên ngoài thì toàn bộ vòng for con bên trong sẽ được thực hiện

for i in range(3):      # start = 0, step = 1
    print('Vong for ngoai khi i =', i)
    for j in range(2):
        print(i, j)
"""

#ANCHOR - Break and Continue
"""
- Break được sử dụng để kết thúc vòng lặp ngay lập tức, FOR LOOP sẽ KẾT THÚC ngay tại thời điểm gặp câu lệnh BREAK và tiếp tục các câu lệnh BÊN DƯỚI vòng for

for i in range(5):
    print(i)
    print('Hello')
    if i == 3: 
        break
    print('Xin chao')
print('End')
"""

"""
- Continue được dùng để bỏ qua lần lặp hiện tại và quay trở lại luôn vòng lặp tiếp theo. Các câu lệnh BÊN DƯỚI continue ở TRONG vòng lặp sẽ được bỏ qua 

for i in range(5):
    print(i)
    print('28tech')
    continue
    print('Dong nay se bi bo qua')      # màu khác
"""

#ANCHOR - WHILE LOOP
"""
Syntax:
    while condition:
        code when condition is TRUE
    else:
        code when condition is FALSE

n = 1
while n < 5:
    print(n, end = ' ')
    n += 1
else:
    print('End')
print('Hello')

while(True):                # vòng lặp vĩnh viễn, điều kiện dừng nằm bên trong
    print('Infinity') 
"""

#ANCHOR - Break & Continue (While)
"""
i = 1
while i <= 5:
    print(i)
    print('Hello')
    if i == 3:
        continue    #< vòng lặp vô hạn vì tới i == 3 thì continue BỎ QUA các câu lệnh BÊN DƯỚI ở TRONG vòng lặp ==> không i += 1 được nữa --> vô hạn
    i += 1
"""

#ANCHOR - Bài 6: Tổng ước
"""
# Tính tổng ước của số nguyên dương n
import math
n = int(input())
total = 0
for i in range(1, math.isqrt(n) + 1):      # chỉ cần xét những ước số nhỏ hơn isqrt(n) là đủ suy ra các ước số còn lại
    if n % i == 0:
        total += i
        if i != n // i:         # số chính phương, vd 16 có cặp (4,4)
            total += n // i
print(total)
"""

#ANCHOR - Bài 7: Liệt kê ước
"""
import math
n = int(input())
count = 0
for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
        count += 1
        if i != n // i:
            count += 1
print(count)
for i in range(1, n + 1):
    if (n % i == 0):
        print(i, end = ' ')
"""

#ANCHOR - Bài 8: Liệt kê số chính phương
"""

import math
n = int(input())
for i in range(1, math.isqrt(n) + 1):
    print(i*i, end = ' ')
"""

#ANCHOR - Bài 9: Tích các ước
"""
# Tính tích các ước của số tự nhiên N
N = int(input())
res = 1
for i in range(1, N + 1):
    if N % i == 0:
        res *= i
print(res)
"""

#ANCHOR - Bài 11: Tổng tự nhiên liên tiếp
"""
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)
#< print (n*(n + 1) // 2)
"""

#ANCHOR - Bài 11.1: Tổng chẵn lẻ
"""
n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total -= i
    elif i % 2 == 0:
        total += i
print(total)
"""

#ANCHOR - Bài 12: Tổng bình phương
"""
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i**2
print(total)
#< print (n * (n+1) * (2n+1) // 6)
"""

#ANCHOR - Bài 12.1: Tổng bội 2
"""
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 2*i
print(total)
"""

#ANCHOR - Bài 13: Tổng bội 3
"""
n = int(input())
total = 0
for i in range(3, n + 1, 3):
    total += i
print(total)
"""

#ANCHOR - Bài 14: Tổng nghịch đảo
"""
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
print('%.3f' % total)
"""

#ANCHOR - Bài 15: Tổng nghịch đảo 2
"""
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / (2*i)
print('%.5f' % total)
"""

#ANCHOR - Bài 17: Tính tổng chữ số của N
"""
n = int(input())
total = 0
while n != 0:
    tmp = n % 10
    total += tmp
    n //= 10
print(total)
"""

#ANCHOR - Đếm chữ snt 
"""
n = int(input())
count = 0
while n != 0:
    tmp = n % 10
    if (tmp == 2 or tmp == 3 or tmp == 5 or tmp == 7):
        count += 1
    n //= 10
print(count)
"""

#ANCHOR - Bài 19: Mua bia
"""
# Cho N xu, tính số chai bia mua được tính cả việc đổi thưởng: 1 chai bia = 28 xu, 3 vỏ đổi được 1 chai bia
n = int(input())
total = 0
num = n // 28
total += num
while num >= 3:
    total += 1
    num -= 3
print(total)

#< Cách 2?
n = int(input())
bia = n // 28
vobia = bia
while vobia >= 3:
    tmp = vobia // 3
    bia += tmp 
    vobia = vobia % 3 + tmp    # số lượng vỏ bia còn lại sau khi đổi + tmp (số lượng chai vừa đổi được)
print(bia)
"""

#ANCHOR - Bài 20: Biểu diễn số nguyên
"""
# Biểu diễn n dưới dạng tổng của các snt sao cho số lượng số hạng trong tổng là lớn nhất có thể
n = int(input())
count = 0
if n == 1:
    print('-1')
else:
    if n % 2 == 0:
        print (n // 2)
        for i in range(n // 2):
            print(2, end = ' ')
    else:
        print (n // 2)
        for i in range(n // 2 - 1):
            print(2, end = ' ')
        print(3)
"""

#ANCHOR - Bài 21: Vẽ hình 1
"""
#< Hình 1
n = int(input())
for i in range(1, n + 1):       # lặp n lần <=> n dòng
    #> Xây dựng dòng
    for j in range(1, n + 1):
        print('*', end = '')
    print('')                 # in xong hàng thì xuống dòng
print('')

#< Hình 2: Chỉ in ra ở các cạnh
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or i == n or j == n:        # duyệt cạnh xung quanh
            print('*', end = '')
        else:
            print(' ', end = '')        # print khoảng trống và xuống dòng
    print('')
print('')    

#< Hình 3: Chỉ in * ở các cạnh, giữa là #
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or i == n or j == n:
            print('*', end = '')
        else:
            print('#', end = '')
    print('')
print('')

#< Hình 4: In số theo thứ tự dòng
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or i == n or j == n:        # in ra giá trị dòng
            print(i, end = ' ')
        else:
            print('  ', end = '')
    print('')
"""

#ANCHOR - Bài 22: Vẽ hình 2
"""
#< Hình 1: In tương ứng với stt dòng
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):           # range(start, stop, step)
        print('*', end = '')
    print('')
print('')

#< Hình 2: In giống hình 1 nhưng đảo ngược
for i in range(1, n + 1):
    for j in range(i, n + 1):           # số lượng * giảm dần khi i tăng
        print('*', end = '')
    print('')
print('')

#< Hình 3: Giống hình 1 nhưng bắt đầu từ bên trái
for i in range(1, n + 1):
    for j in range(1, n + 1): 
        if j > n - i:               # với j = 5 > n = 5 - i = 1 == 4 --> in ở 5
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')
print('')

#< Hình 4: Giống hình 3 nhưng ngược lại 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j < i:
            print(' ', end = '')
        else:
            print('*', end = '')
    print('')
print('')

#< Hình 5: Giống hình 1 nhưng trống giữa
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1 or i == n or j == 1 or j == n or j == i:      # j == i là đường chéo chính 
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')
print('')
"""

#ANCHOR - Bài 24: UCLN của giai thừa 
"""
#< UCLN của 2 giai thừa là giai thừa của số nhỏ hơn
import math
a,b = map(int, input().split())
print(math.factorial(min(a,b)))
"""

#ANCHOR - Bài 26: Giải phương trình
"""
# Cho 3 số a,b,n. Xem pt ax+by=n có tồn tại cặp nghiệm (x,y) nguyên không âm hay không
#< Duyệt x trong khoảng [0, n/a]. Vì khi by = 0 thì x lớn nhất cũng chỉ đến n/a
a,b,n = map(int, input().split())
check = False
for i in range(0, n//a + 1):
    remain = n - i * a
    if remain % b == 0:
        check = True
        break
if check == True:
    print('YES')
else:
    print('NO')
"""

#ANCHOR - Bài 27: (!)Digital root
"""
n = int(input())
while n >= 10:
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    n = total       # gán lại để làm việc tiếp
print(total)
"""

#ANCHOR - Bài 30: Multi-testcases
"""
n = int(input())
for i in range(n):
    j = int(input())
    if j % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
"""