#REVIEW - LIST & SÀNG SNT (SIEVE) (BUỔI 7)

#SECTION - LIST

#ANCHOR - List definition
"""
- List tương tự như ctdl mảng ở các ngôn ngữ khác nhưng có phần linh hoạt và mạnh mẽ hơn
- Các tính chất của list:
    ! Lists are ordered: Các ptu trong list là có thứ tự
    > Accessed by index: Truy cập các ptu tong list thông qua chỉ số
    < Lists can contain any sort of object: List có thể chứa các kdl khác nhau như int, str, float, thậm chí là một list khác (mảng 2 chiều)
    ! Lists are changeable (mutable): Các ptu trong list có thể thay đổi gtri, các thao tác thêm, xóa các ptu cũng đc hỗ trợ

! Never modifies your lists when you are iterating through them (không nên chỉnh sửa (add(), remove()) khi đang duyệt list)
**Can cause unexpected behaviour in your loops** 
"""

#ANCHOR - Tạo list
"""
# List các số nguyên
integer = [1,2,3,4,5]

# List các xâu kí tự
string = ["28tech", "python", "machine learning"]

# List các số nguyên, xâu kí tự, số phức,...
mix = [1,2,3,4, "java", 3 + 5j]

# List rỗng
empty = []
"""

#ANCHOR - List constructor
"""
# Có thể sử dụng hàm khởi tạo list() để biến đổi các object khác thành list
s = "python"
a = list(s)
print(a)
"""

#ANCHOR - Hàm len()
"""
# Dùng hàm len() để biết số lượng ptu trong list
a = [1,2,3,4,5, "python"]
print(len(a))
"""

#ANCHOR - Truy cập qua chỉ số
"""
#! Được đánh số từ 0, ngoài ra Python list hỗ trợ cả chỉ số âm (negative index)
#> Negative index sẽ tính từ ptu cuối chạy ngược lại (start -1)
a = [1,2,3,4,5, "python"]
print(a[len(a) - 1])        # cách bth để in ptu cuối
print(a[-1])            # cách mới
"""

#ANCHOR - 2 cách duyệt
"""
a = [1,2,5,1,4, "end"]

#< Duyệt bằng range
for i in range(len(a)):
    print(a[i], end = " ")

print("\n")

#< For each
for item in a:
    print(item, end = " ")
"""

#ANCHOR - Thay đổi gtri phần tử
"""
#! Ta thay đổi gtri phần tử bằng cách truy cập index và gán (mutable)

list = [1, 2, 3, 3.5, 4, "python", "java"]
print(list)

list[-1] = "c++"        # ptu cuối
list[0] = "hello"       # ptu đầu
print(list)
"""

#ANCHOR - Thêm 1 ptu vào list
"""
#< Hàm append() thêm mới ptu vào CUỐI list
a = [1, "python", "28tech"]
print(a)
a.append("C++")
a.append(100)
print(a, "\n")

#< Hàm insert thêm 1 ptu vào vị trí bất kì
b = [1,2,3,4, "python", "java"]
print(b)
b.insert(1, "28tech")
print(b, "\n")

#! Chú ý: khi ta insert vào một index nằm ngoài kích thước mảng, nó sẽ insert vào cuối chứ không bị lỗi
c = [1, 2, 3, 3.5, 4, "python", "java"]        #> list c có 7 ptu, khi ta insert 15 thì nó vẫn sẽ nằm cuối chứ không lỗi   
print(c) 
c.insert(15, "hehe")
print(c)
"""

#ANCHOR - Xóa 1 ptu khỏi list
"""
#< Hàm pop() xóa ptu thông qua index. Nếu không có index sẽ xóa ptu cuối cùng trong list
a = [1,20,10,30,50]
a.pop(2)        # xóa ptu 10
print(a, "\n")
a.pop()         # xóa ptu 50 (cuối) 
print(a, "\n")  

#< Hàm del() cũng tương tự nhưng bắt buộc phải có index
b = [1,20,5,7,10]
del b[1]
print(b, "\n")

#< Hàm remove() xóa thông qua gtri, nếu trong list tồn tại nhiều ptu giống ptu bạn cần xóa thì hàm này chỉ xóa đi ptu đầu tiên
c = ['A', 'B', 'C', 'D', 'C', 'E']
c.remove('C')
print(c, "\n")

#< Hàm clear() xóa mọi ptu trong list
a = [1,5,10,20,30,5]
a.clear()
print(a)
"""

#ANCHOR - Sao chép list (list repetition)
"""
# Sao chép list có thể giúp bạn NHÂN BẢN nội dung của 1 list ban đầu
a = [1,2,3,4]
b = a * 2
print(b, "\n")

# Tạo 1 list có 1000 ptu là số 0
c = [0] * 1000
print(c)
"""

#ANCHOR - COPY LIST
"""
#! Copy và gán list HOÀN TOÀN KHÁC NHAU

#< Khi dùng dấu = để gán list thì cả hai đều sẽ trỏ đến chung một địa chỉ ô nhớ (cùng object)
a = [1,2,3]
b = a               
print(id(a), id(b))     # chung id --> cùng object
b[-1] = "python"        # vì cùng địa chỉ ô nhớ nên thay đổi gtri cũng là chung
print(a, "\n")

#< Dùng hàm Copy (tối ưu hơn)
a = [1,4,5]
b = a.copy()        # shallow copy (copy nông)
print(id(a), id(b))     # khi này sẽ không dùng chung địa chỉ ô nhớ
b[-1] = "python"
print(a)
print(b, "\n")

#< If your list contains mutable objects (like other lists), a shallow copy will still share those nested mutable objects. 
a = [1,2,3,4,5, [6,7,8]]
b = a.copy()             # khi này, dù đã shallow copy ra 2 object khác nhau nhưng vì list là nested mutable object nên vẫn share chung địa chỉ ô nhớ
print(b)
b[-1][-1] = "python"
#> Cả 2 list đều bị thay đổi chung
print(a)            
print(b, "\n")

#< For a completely independent copy, including nested mutable objects, you would need a deep copy (using the copy.deepcopy() function from the copy module).
import copy as cp       # import copy module
c = [1,2,3,4,5, [6,7,8]]
d = cp.deepcopy(c)
print(d)
d[-1][-1] = "ilovepython"
print("List c:", c)
print("List d:", d)
"""

#ANCHOR - Toán tử IS 
"""
#! Khi dùng toán tử == thì sẽ so sánh giá trị
#> Khi dùng toán tử is thì sẽ so sánh địa chỉ ô nhớ (xem có phải cùng object không?)
a = [1,2,3,4]
b = a
print(a is b)
"""

#ANCHOR - Toán tử IN
"""
#! Gọi là membership operator, dùng để check xem một ptu có nằm trong list hay không (tìm kiếm tuyến tính)
list = [1,2,3,4]
print(1 in list)        # True
print(5 in list)        # False
"""

#ANCHOR - Combine List
"""
#! Sử dụng hàm extend() để thêm các ptu của 1 list khác vào list hiện tại
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#! Hoặc sử dụng toán tử +
c = [7,8,9]
d = [10,11,12]
c += d
print(c)
"""

#ANCHOR - Các phương thức list
"""
#! Hàm Count(): Trả về số lần xuất hiện của 1 ptu bất kì trong list
a = [1, 2, 3, 1, 1, 4, 5]
print(a.count(1))       # return 3

#! Hàm Index(): Trả về chỉ số đầu tiên của 1 ptu trong list
a = [4, 3, 1, 2, 1, 1]
print(a.index(1))       # return 2

#! Hàm Reverse(): Lật ngược một list
a = [1, 2, 3, 4]
print(a)
a.reverse()
print(a)

#! Hàm Sort(): Sắp xếp các ptu trong list
a = [1, 3, 2, 7, 4, 9, 10, 6]
a.sort()
print(a)
"""

#ANCHOR - Các hàm built-in trong list
"""
Hàm              Chức năng
all()            Trả về True nếu mọi ptu trong list đều là True
any()            Trả về True nếu có ít nhất 1 ptu trong list là True
>max()           Trả về ptu lớn nhất trong list
>min()           Trả về ptu nhỏ nhất trong list
sorted()         Trả về list đã sắp xếp của list ban đầu
>sum()           Trả về tổng các ptu trong list
"""

#ANCHOR - Hàm Sorted
"""
#! Sử dụng hàm sort thông thường sẽ sắp xếp list gốc
a = [1, 3, 2, 7, 4, 9, 10, 6]
a.sort()
print(a)

#! Sử dụng sorted sẽ lưu list được sắp xếp lên biến khác
b = [1, 3, 2, 7, 4, 9, 8, 10, 6] 
c = sorted(b)
print(c)
"""

#ANCHOR - Input list
"""
n = int(input())    # nhập số ptu trong mảng
a = list(map(int, input().split()))
print(a)
#< a = list(map(int, input().split()))
# input(): waits for the user to type something and press Enter
# .split(): splits the input string by spaces (default). From "5 10 15" → becomes ["5", "10", "15"] (a list of strings).
# map(int, ...): Applies the int() function to each element of the list. (you know, 'mapping')
#> list(...): Converts the map object into a list.
"""
#!SECTION

#SECTION - LIST's EXERCISE

#ANCHOR - Đếm số cặp
"""
# Cho mảng số nguyên A[] gồm N ptu, hãy đếm cặp 2 ptu trong mảng có tổng bằng K cho trước
n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

#! Dùng 2 vòng for lồng nhau
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j] == k):
            cnt += 1
print(cnt)
"""

#ANCHOR - Mảng đối xứng (1)
"""
# Cho mảng số nguyên A[] gồm N ptu, kiểm tra xem mảng có đối xứng hay không? (Dùng 2 con trỏ)

def palindrome(list, n):
    left = 0
    right = n - 1
    while(left < right):
        if list[left] != list[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    n = int(input())
    list = list(map(int, input().split()))
    if (palindrome(list, n)):
        print('YES. List is palindrome!')
    else:
        print('NO. List is not palindrome!')
"""

#ANCHOR - Liệt kê và đếm số fibonacci
"""
# Cho mảng số nguyên A[] gồm N ptu, hãy liệt kê các số trong mảng số Fibonacci
fibo = [0] * 100
fibo[0] = 0
fibo[1] = 1

if __name__ == '__main__':
    for i in range(2, 100):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    n = int(input())
    list = list(map(int, input().split()))

    ok = False
    for x in list:
        if x in fibo:
            ok = True
            print(x, end = ' ')
    if not ok:                      # equals to: if ok == False
        print('NONE')
"""

#ANCHOR - Vị trí số lớn nhất và nhỏ nhất
"""
# Tìm vị trí cuối cùng của gtri nhỏ nhất trong mảng và vị trí đầu tiên của gtri lớn nhất trong mảng.
n = int(input())
list = list(map(int, input().split()))
min_val, max_val = min(list), max(list)

#> Vị trí cuối cùng của gtri nhỏ nhất trong mảng -> duyệt từ cuối về
for i in range(n - 1, -1, -1):
    if min_val == list[i]:
        print(i, end = ' ')
        break

#> Vị trí đầu tiên của gtri lớn nhất trong mảng -> duyệt từ đầu lên
for i in range(n - 1):
    if max_val == list[i]:
        print(i)
        break

! Explanation of the range(start, stop, step):
start = n - 1: the last index of the list
stop = -1: not inclusive, so the loop stops BEFORE reaching -1
step = -1: move backward by 1 each time
< If you had used range(n - 1, 0, -1), it would skip index 0.
"""

#ANCHOR - Tính tổng và tích các ptu trong mảng
"""
n = int(input())
list = list(map(int, input().split()))
tong = sum(list) % (10**9 + 7)
tich = 1
for x in list:
    tich *= x
    tich %= (10**9 + 7)
print(tong, tich, sep = '\n')
"""

#ANCHOR - Tìm gcd của mọi ptu trong mảng
"""
import math
n = int(input())
list = list(map(int, input().split()))
res = 0
for x in list:
    res = math.gcd(res, x)
print(res)
"""

#ANCHOR - Số lớn nhất và lớn thứ 2 (2 gtri có thể giống nhau)
"""
#< Cách 1: Dùng biến và vòng for
n = int(input())
list = list(map(int, input().split()))
min_val, max_val = min(list), max(list)
sec_max = 0
print('Số lớn nhất:', max_val)
for i in list:
    if (i > min_val) and (i <= max_val):
        sec_max = i
print('Số lớn thứ 2:', sec_max)

#< Cách 2: Dùng sort
n = int(input())
list = list(map(int, input().split()))
list.sort()         # sort theo thứ tự tăng dần
print('Số lớn nhất:', list[-1])
print('Số lớn thứ hai:', list[-2])
"""

#ANCHOR - Liệt kê
"""
from math import *

#! Cách 1: Đếm thông thường
#< Số lượng snt trong list
def checkSnt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):            # range cần int
        if n % i == 0:
            return False
    return n > 1

#< Số lượng số thuận nghịch trong dãy
def checkThuanNghich(n):
    if n < 10:
        return True
    tmp = n
    rev = 0
    while n != 0:
        rev += n % 10
        n //= 10
    if tmp == rev:
        return True
    else:
        return False

#< Số lượng số chính phương trong dãy
def checkChinhPhuong(n):
    return (isqrt(n)) ** 2 == n 

#< Số lượng số có tổng chữ số của nó là số nguyên tố
def checkWTF(n):
    sumDigit = 0
    while n != 0:
        sumDigit += n % 10
        n //= 10
    return checkSnt(sumDigit)

if __name__ == '__main__':
    countSNT, countThNg, countChPh, countWTF = 0, 0, 0, 0
    n = int(input())
    list = list(map(int, input().split()))
    for x in list:
        if checkSnt(x):
            countSNT += 1
        if checkThuanNghich(x):
            countThNg += 1
        if checkChinhPhuong(x):
            countChPh += 1
        if checkWTF(x):
            countWTF += 1
    print(countSNT, countThNg, countChPh, countWTF, sep = '\n')

#! Cách 2: Dùng list comp lấy ra từng list riêng, sau đó dùng len(list) để đếm số ptu
def checkSnt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):            # range cần int
        if n % i == 0:
            return False
    return n > 1

#< Số lượng số thuận nghịch trong dãy
def checkThuanNghich(n):
    if n < 10:
        return True
    tmp = n
    rev = 0
    while n != 0:
        rev += n % 10
        n //= 10
    if tmp == rev:
        return True
    else:
        return False

#< Số lượng số chính phương trong dãy
def checkChinhPhuong(n):
    return (isqrt(n)) ** 2 == n 

#< Số lượng số có tổng chữ số của nó là số nguyên tố
def checkWTF(n):
    sumDigit = 0
    while n != 0:
        sumDigit += n % 10
        n //= 10
    return checkSnt(sumDigit)

if __name__ == '__main__':
    countSNT, countThNg, countChPh, countWTF = 0, 0, 0, 0
    n = int(input())
    list = list(map(int, input().split()))
    listSnt = [x for x in list if checkSnt(x)]
    listThNg = [x for x in list if checkThuanNghich(x)]
    listChPh = [x for x in list if checkChinhPhuong(x)]
    listWTF = [x for x in list if checkWTF(x)]
    print(len(listSnt), len(listThNg), len(listChPh), len(listWTF), sep = '\n')
"""

#ANCHOR - Mảng đối xứng (2)
"""
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(reversed(a))       # trả về list lật ngược của a
    if a == b:
        print('YES')
    else:
        print('NO')
"""

#ANCHOR - Liền kề trái dấu
"""
# Hãy liệt kê theo thứ tự xuất hiện các số thỏa mãn có ít nhất 1 số trái dấu với nó đứng cạnh nó
n = int(input())
a = list(map(int, input().split()))
if a[0] * a[1] < 0:
    print(a[0], end = ' ')      # special case: a[0] là thg đầu, không có thg đứng trước
for i in range(1, n - 1):
    if a[i] * a[i - 1] < 0 or a[i] * a[i + 1] < 0:
        print(a[i], end = ' ')
if a[-2] * a[-1] < 0:
    print(a[-1])            # special case: a[-1] là thg cuối, không có thg đứng sau
"""

#ANCHOR - Khác biệt nhỏ nhất
"""
# Tìm khoảng cách nhỏ nhất giữa 2 ptu a[i], a[j] khác nhau trong mảng (i != j)
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    min_val = 10**18            # min chọn lớn nhất
    for i in range(0, n - 1):
        for j in range(i + 1, n - 1):  
            #< Cách 1:
            if abs(a[i] - a[j]) < min_val:
                min_val = a[i] - a[j]

            #< Cách 2:
            min_val = min(min_val, abs(a[i] - a[j]))
    print(min_val)
"""  

#ANCHOR - Find BRT
"""
#< Tìm ra 2 số nguyên C và D, lần lượt là khoảng cách ngắn nhất giữa 2 thị trấn, và số lượng cặp thị trấn có cùng khoảng cách này 
n = int(input())
a = list(map(int, input().split()))
min_val, count = 10**18, 0
a.sort()
for i in range(1, n):
    if a[i] - a[i - 1] < min_val:
        min_val = a[i] - a[i - 1]
        count = 1
    elif a[i] - a[i - 1] == min_val:
        cnt += 1
print(min_val, count)
"""

#ANCHOR - Đếm tần suất
"""
#< Phần 1: In ra tần suất xuất hiện của các ptu từ bé đến lớn, sau đó bỏ trống 1 dòng
#< Phần 2: In ra tần suất xuất hiện của các ptu theo thứ tự xuất hiện trong mảng (mỗi gtri chỉ liệt kê 1 lần)
if __name__ == '__main__':
    n = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (10**7 + 1)
    c = [0] * (10**7 + 1)
    for x in a:
        b[x] += 1
        c[x] += 1
    
    for x in sorted(a):
        if (b[x] > 0):
            print(x, b[x], end = ' ')
            print()
            b[x] = 0
    print()

    for x in a:
        if (c[x] > 0):
            print(x, c[x], end = ' ')
            print()
            c[x] = 0
"""     

#ANCHOR - Đếm phân phối sử dụng mảng
"""
n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 1001
for x in a:
    cnt[x] += 1
se = set({})            # create an empty set

#< Liệt kê các gtri xuất hiện trong mảng và tần suất tương ứng theo thứ tự xuất hiện
for x in a:
    if x not in se:
        print(x, cnt[x])        
        se.add(x)               # elements in set are UNIQUE
print()

#< Liệt kê các gtri xuất hiện trong mảng và tần suất tương ứng theo thứ tự từ nhỏ tới lớn
for x in range(1001):
    if cnt[x] != 0:
        print(x, cnt[x])
print()

#< Tìm số có số lần xuất hiện nhiều nhất, nếu có nhiều số có cùng số lần xuất hiện thì chọn số lớn hơn
res, dem = 0, -10**9
for x in range(1001):
    if cnt[x] != 0 and cnt[x] >= dem:               # dấu = là chọn số lớn hơn 
        dem = cnt[x]
        res = x
print(res)
#< Tìm số có số lần xuất hiện ít nhất, nếu có nhiều số có cùng số lần xuất hiện thì chọn số nhỏ hơn
res1, dem1 = 0, 10**9
for x in range(1001):
    if cnt[x] != 0 and cnt[x] < dem1:
        res1 = x
        dem1 = cnt[x]
print(res1) 
"""

#ANCHOR - Kiểm tra mảng tăng dần
"""
- Ktra xem mảng đã cho có tăng chặt hay không, tức là các ptu đứng sau luôn lớn hơn ptu đứng trước

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    if a[i] <= a[i - 1]:            # nếu thg đứng sau <= thg đứng trước là false
        print('NO')
        exit()
print('YES')
"""

#ANCHOR - Số lớn hơn các số đứng trước
"""
- Hãy liệt kê các ptu trong dãy lớn hơn tất cả các số đứng trước nó (Ptu đầu tiên đc coi là 1 ptu thỏa mãn)

n = int(input())
a = list(map(int, input().split()))
max = -10**9
for x in a:             # a[x] only with index
    if x > max:
        print(x, end = ' ')
        max = x
"""

#ANCHOR - Trộn 2 dãy đã sắp xếp 
"""
import math
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
i, j = 0, 0 
while i < n and j < m:
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
while i < n:
    res.append(a[i])
    i += 1
while j < m:
    res.append(b[j])
    j += 1
for x in res:
    print(x, end = ' ')
"""

#ANCHOR - Đếm tần suất snt
"""
from math import *
def checkSNT(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    a = list(map(int, input().split()))
    d = {}
    b = [x for x in a if checkSNT(x)]
    for x in b:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for value, frequency in d.items():
        print(value, frequency)
"""

#ANCHOR - Định lý Pytago
"""
#< Bình phương và sort theo thứ tự tăng dần, sau đó tìm a + b = c
#< Dùng kĩ thuật gặp nhau ở giữa

def checkPytago(a, n):
    for i in range(n - 1, 1, -1):       # i is treated as the largest (potential hypotenuse)
        left, right = 0, i - 1          # Two pointers starting from both ends
        while left < right:
            if a[left] + a[right] == a[i]:
                return True
            elif a[left] + a[right] < a[i]:
                left += 1
            else:
                right -= 1
    return False

n = int(input())
a = list(map(int, input().split()))
a.sort()
a = [x**2 for x in a]
if checkPytago(a, n):
    print('YES')
else:
    print('NO')
"""

#ANCHOR - Truy vấn tổng trên đoạn (List Slicing)
"""
#< Dùng list slicing chậm hơn bình thường --> Complexity: O(n)
n = int(input())
a = list(map(int, input().split()))
q = int(input())            # q là số lượng truy vấn
for i in range(q):
    l, r = map(int, input().split())
    l -= 1                          	# Chuyển chỉ số từ 1-based → 0-based ()
    r -= 1
    ans = sum(a[l : r + 1])         # list slicing với start = l, stop = r, step = 1
    print(ans)
"""

#ANCHOR - Truy vấn tổng trên đoạn (Mảng cộng dồn)
"""
n = int(input())
a = list(map(int, input().split()))

< CT: Sum from l to r = F(r) - F(l - 1)
> F(r): Từ chỉ số 0 -> r
> F(l - 1): Từ chỉ số 0 -> l - 1

< EX: Build prefix sum array F 
a = [3, 1, 4, 2]
F = [3, 4, 8, 10]

F = [None] * n
for i in range(n):
    if i == 0:
        F[0] = a[0]
    else:
        F[i] = F[i - 1] + a[i]
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l == 0:
        print(F[r])
    else:
        print(F[r] - F[l - 1])
"""

#ANCHOR - Đếm số lượng cặp số bằng nhau
"""
#< Dùng ct tổ hợp để tìm số cặp: n*(n-1) / 2
> Đếm tần suất của từng ptu
> Dùng ct tổ hợp
n = int(input())
a = list(map(int, input().split()))
d = {}
for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
ans = 0
for x in d:
    ans += d[x] * (d[x] - 1) // 2       # cộng dồn số cặp bằng nhau
print(ans)
"""

#ANCHOR - Sliding Window (1)
"""
#! Hãy tìm dãy con liên tiếp có k ptu sao cho dãy con đó có tổng các ptu lớn nhất
> Biến ans để lưu kết quả, pos để lưu vị trí bắt đầu của dãy
> Duyệt từ i = 0 đến chỉ số n - k
< Sử dụng list slicing để tính sum
< Sử dụng list slicing để print

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans, pos = 0, 0         
for i in range(n - k + 1):           #> stop = n - k + 1 vì index stop thực sự luôn là stop - 1
    tmp = sum(a[i : i + k])
    if tmp > ans:
        ans = tmp
        pos = i
print(ans)
for x in a[pos : pos + k]:
    print(x, end = ' ')
"""

#ANCHOR - Sliding Window (2) 
"""
#! Dù (1) ngắn gọn nhưng tốn rất nhiều thời gian, đặc biệt ở thao tác dùng list slicing để tính sum
> Đổi thành thao tác xóa ptu đầu tiên của cửa sổ trước và cộng thêm ptu cuối của cửa sổ sau
< Lúc này sẽ chỉ tốn 1 câu lệnh để tính cửa số mới

n, k = map(int, input().split())
a = list(map(int, input().split()))
s, pos = sum(a[0 : k]), 0             #> biến ans bây giờ lưu cửa sổ đầu tiên
ans = s
for i in range(1, n - k + 1):
    s = s - a[i - 1] + a[i + k - 1]         
    if s > ans:
        ans = s
        pos = i
print(ans)
for x in a[pos : pos + k]:
    print(x, end = ' ')
"""

#ANCHOR - Số bị lặp đầu tiên
"""
#! Cho mảng các số nguyên. Tìm ptu lặp đầu tiên trong mảng
n = int(input())
a = list(map(int, input().split()))
se = set()
ok = False
for x in a:
    if x in se:             #> sau khi add mà duyệt sang các ptu sau vẫn tìm thấy trong set thì lặp -> in  
        ok = True
        print(x)
        break
    else:
        se.add(x)
if not ok:
    print(-1)
"""

#ANCHOR - Trộn 2 dãy và sắp xếp
"""
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)
for i in range(n):              #> index chẵn cho mảng a, lẻ cho mảng b
    print(a[i], b[i], end = ' ')
"""

#ANCHOR - Vị trí đầu tiên và cuối cùng
"""
#! In ra vị trí xuất hiện đầu tiên và cuối cùng của X trong mảng
n, x = map(int, input().split())
a = list(map(int, input().split()))
first, last = -2, -2
for i in range(n):
    if a[i] == x:
        last = i
        if first == -2:             #> nếu như chưa có first thì cập nhật           
            first = i
print(first + 1, last + 1)          #> index bắt đầu từ 1
"""

#ANCHOR - Mảng 012
"""
#< Dùng counting sort
n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 3           #> sử dụng mảng đếm cho 3 ptu 0 1 2
for x in a:
    cnt[x] += 1         #> mảng sẽ đếm mỗi ptu xuất hiện bao nhiêu lần
for i in range(3):      #> start = 0, end = 2
    for j in range(cnt[i]):
        print(i, end = ' ')
"""

#ANCHOR - Số thao tác giúp mảng tăng dần 
"""
#! In ra số thao tác tối thiểu cần thực hiện để biến mảng thành dãy tăng chặt 
> Nhập n ptu của mảng và d là lượng tăng
> In ra số thao tác cần để biến mảng thành dãy tăng chặt
Input:
3 3
15 17 9
Output: 
3
< Explanation: 9 + 3 = 12 + 3 = 15 + 3 = 18 -> 15 17 18 là dãy tăng chặt -> cần tối thiểu 3 thao tác

import math
n, d = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(1, len(a)):
    if a[i] <= a[i - 1]:            #> nếu ptu sau nhỏ hơn hoặc bằng ptu trước thì chưa là dãy tăng chặt
        tmp = math.floor((a[i - 1] - a[i]) / d + 1) 
        res += tmp
        a[i] += d * tmp
print(res)
"""

#ANCHOR - Chia tập [Tham Lam]
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
k = max(k, n - k)       #> k luôn là tập có số lượng ptu lớn hơn
a.sort(reverse = True)
sum1, sum2 = 0, 0
for i in range(n):
    if i < k:           #> k ptu đầu tiên luôn là lớn I
        sum1 += a[i]
    else:
        sum2 += a[i]
print(sum1 - sum2)
"""


#!SECTION

#SECTION - LIST's SPECIALS

#SECTION - LIST SLICING
"""
#! Python list slicing là một kỹ thuật giúp truy cập vào 1 khoảng các ptu trong list thông qua toán tử
+) Với toán tử: Có thể xác định chỉ số bắt đầu, chỉ số kết thúc, bước nhảy của các ptu trong list mà mình muốn cắt ra
+) Cú pháp: List[start : stop : step]
+) Giá trị trả về: Một list trong đoạn từ start đến (stop - 1) với bước nhảy là step. Nếu không chỉ rõ thì mặc định step = 1
#< Demo:
a = [1, 2, 3, 4, 5, 6, 7]
#id: 0  1  2  3  4  5  6
print(a[2 : 6 : 1])         # start = 2, end = 6 - 1 = 5, step = 1
"""

#NOTE - Slicing với chỉ số KHÔNG âm
"""
- Nếu không có stop thì gtri mặc định của stop sẽ là len() của list, nếu không có start thì gtri mặc định của start sẽ là 0
! Nếu start quá nhỏ (nhỏ hon 0) hoặc stop quá lớn thì start sẽ bắt đầu từ 0 và stop sẽ kết thức tại len() của list
"""

#NOTE - Slicing với chỉ số âm
"""
#< Demo
a = [2, 3, 1, 5, 7, 4, 3]
b = a[-4 : -1]      # end = -2
print(b)

#< Kết hợp chỉ số âm và chỉ số dương
c = a[2 : -2]      # end = -3
print(c)
"""

#ANCHOR - Lật ngược list (cách mới)
"""
# Bỏ chỉ số đầu và chỉ số cuối, bước nhảy = -1 
a = [1, 2, 3, 4, 5]
reverse = a[::-1]
print(reverse)
"""

#ANCHOR - Thay đổi gtri của nhiều ptu trong 1 đoạn
"""
# Có thể thay đổi hoặc xóa 1 loạt các ptu trong 1 đoạn xác định bằng list slicing
#! Chú ý: Chỉ có thể gán 1 iterable cho slice mà mình đã cắt 
-> iterable là bất kỳ đối tượng nào có thể duyệt từng phần tử một, ví dụ: list, tuple, str, range, set, dict (chỉ keys). Không phải: int, float, bool, None

a = [2, 3, 5, 2, 0, 3, 3]
a[2 : 6] = ['Python'] 
print(a)
a[:0] = ['hehe']        # thêm vào đầu list
print(a)
a[len(a):] = ['helo']   # thêm vào cuối list
print(a)
"""

#ANCHOR - Xóa một đoạn
"""
# Muốn xóa đi một đoạn trong list thì gán sliced list = []
a = [2, 3, 5, 2, 0, 3, 3]
a[0 : 3] = []
print(a)
"""
#!SECTION

#SECTION - LIST COMPREHENSION (LIST COMP)
"""
#! Comprehension là một cách nhanh chóng để có thể tạo một CTDL từ iterable (list, tuple...). Nó có thể kết hợp với điều kiện và vòng lặp để rút gọn cú pháp. 
-> List comp sẽ giúp code của bạn Pythonic hơn
+) Cú pháp: [Expression for var_name in iterable]
> Expression: biểu thức được thực hiện mỗi khi vòng lặp được thực thi 
> Var: một biến là một item trong iterable
> Iterable: Colletions chứa các object (list, tuple, string,...)

#< Demo: List comp dùng để bình phương tất cả ptu trong list
a = [1, 2, 3, 4]
b = [x**2 for x in a]
print(b)
"""

#ANCHOR - Lấy mã ASCII của từng kí tự sử dụng hàm ord
"""
str = '28tech'
c = [ord(x) for x in str]
print(c)
"""

#ANCHOR - Kết hợp hàm với list comp
"""
def digitSum(n):
    sum = 0
    while (n != 0):
        sum += n % 10
        n //= 10        # '/' - Floating-point division         '//' - Integer (floor) division
    return sum

a = [123, 31, 20, 503, 114]
b = [digitSum(x) for x in a]
print(b)
"""

#ANCHOR - List Comp + IF
"""
#! Khi sử dụng list comprehension, có thể sử dụng mệnh đề if để lọc dữ liệu phù hợp
#< Demo: Lọc ra các số không âm
a = [1, 2, 3, -5, 3, -4, 0]
b = [x for x in a if x >= 0]
print(b)

#< Demo: Lọc ra các số chẵn từ 0 -> n
n = 10
a = [x for x in range(n) if x % 2 == 0]
print(a)

#< Demo: Chỉ bình phương các số lẻ
n = 10
a = [x**2 for x in range(n) if x % 2 == 1]
print(a)
"""

#ANCHOR - Nested list comprehension
"""
#! Biểu thức bên trong list comp có thể là một list comp khác
#< Demo: Đưa mọi ptu trong nested list thành một list (flatten in numpy: biến mảng 2 chiều thành 1 chiều)
list = [[1, 2, 3], [4, 5], [6, 7, 8]]
b = [x for small_list in list for x in small_list]
print(b)
""" 
#!SECTION

#SECTION - UNPACKING
"""
- Là kĩ thuật gán từng biến cho từng ptu trong list theo thứ tự xuất hiện
#< Demo
a = [1, 2, 3, 4]
x,y,z,t = a
print(x,y,z,t)
"""

#ANCHOR - Unpack thông tin 
"""
information = ["Nguyen Minh Dung", "minhdung38109141@gmail.com", 'DS', '23-04-2005']
name, email, position, birth = information
print('Name:', name)
print('Email:', email)
print('Job:', position)
print('Birth:', birth)
"""

#ANCHOR - Toán tử *
"""
- Sử dụng toán tử *, Python sẽ gán toàn bộ ptu cho biến đó
#> Cú pháp: *var
#< Demo: gán tất cả ptu còn lại cho biến z
n = 10
a = [x for x in range(n)]
x, y, *z = a 
print(x)    # x = 0
print(y)    # y = 1
print(z)    # z lúc này sẽ như một list của các ptu còn lại = [2, 3, 4, 5, 6, 7, 8, 9]

#< Nếu gán như vậy, Python sẽ tự chừa ptu cuối cho biến z
n = 10
a = [x for x in range(n)]
x, *y, z = a 
print(x)    
print(y)     
print(z)    

#< Nếu chỉ muốn 2 ptu đầu và cuối -> Dùng dấu '_' (underscore) (cho đỡ nhầm lẫn)
n = 10
a = [x for x in range(n)]
x, *_, z = a
print(x)
print(z)
"""
#!SECTION

#!SECTION

#SECTION - SÀNG SNT (SIEVE)

#ANCHOR - Sàng snt
"""
import math
p = [True] * (10**6 + 1)        # Tạo mảng có (10^6 + 1) ptu đều là True

def sieve(n):
    p[0] = p[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        
        #! Ktra nếu i là snt thì duyệt các bội của i <= n 
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = False

if __name__ == '__main__':
    sieve(10**6)
    for i in range(10**6 + 1):
        if p[i]:
            print(i, end = ' ')
"""
#!SECTION

