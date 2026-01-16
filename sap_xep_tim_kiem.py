#REVIEW - SẮP XẾP, TÌM KIẾM TRONG PYTHON (BUỔI 9)

#SECTION - HÀM SORT
"""
- Hàm sort trong Python là Tim sort, có tính chất stable vì thế những ptu trong list có cùng tổng chữ số sẽ được giữ nguyên thứ tự ban đầu
- Mặc định thì sort sẽ được sắp xếp theo thứ tự tăng dần về số và tăng dần theo thứ tự từ điển với xâu kí tự
# Cú pháp: sort(key = ..., reverse = ...)
> Key: Đây là hàm được sử dụng để làm tiêu chí sắp xếp
> Reverse: Nếu reverse = True thì sẽ sắp xếp theo thứ tự NGƯỢC.
! Hàm sort không trả về gtri nào cả mà thay đổi trực tiếp list (in-place)

#< Demo: Sắp xếp theo thứ tự tăng dần
a = [5, 42, 1, 2, 43, 54, 75, 44]
a.sort()
print(a)

#< Demo: Sắp xếp theo thứ tự giảm dần (tham số reverse = True)
b = a.copy()
b.sort(reverse = True)
print(b)
"""

#ANCHOR - Sử dụng key là hàm built-in
"""
#< Demo: Sắp xếp theo độ dài chữ tăng dần
a = ["28tech", "apple", "C++", "Python"]
a.sort(key = len)       #> sử dụng hàm built-in (len) để đo độ dài chữ
print(a)

#< Demo: Sắp xếp theo trị tuyệt đối tăng dần
b = [1, 2, 3, -20, -10, 11, 43, 42, 654, 64]
b.sort(key = abs)
print(b)
"""

#ANCHOR - Sử dụng key là hàm mình tự define
"""
#< Demo: Sắp xếp theo digitSum tăng dần
def digitSum(n):
    sum = 0
    while (n != 0):
        sum += n % 10
        n //= 10
    return sum

a = [4, 10, 100, 10000, 3, 12, 13, 54, 32, 24, 765, 34, 22, 31, 53]
a.sort(key = digitSum)
print(a)
"""

#ANCHOR - Sử dụng key là lambda
"""
#< Demo: Sắp xếp theo bình phương tăng dần
a = [4, 10, 100, 10000, 3, 12, 13, 54, 32, 24, 765, 34, 22, 31, 53]
a.sort(key = lambda x : x**2)
print(a)
"""

#ANCHOR - Sắp xếp nested lsit
"""
#< Demo: Theo thành phần thứ 2 tăng dần, sau đó tới thành phần thứ 1 tăng dần (define function)
def getItem(a):
    return a[1], a[0]

if __name__  == '__main__':
    a = [[3, 2], [4, 5], [2, 6], [1, 4], [3, 1]]
    a.sort(key = getItem)       # sort theo ptu thứ nhất trong nested list
    print(a)
#> vì khi dùng a.sort thì sẽ thao tác trên các ptu trong list, khi dùng getItem thì sẽ truy cập lần 2 -> nested list 

#< Demo: Theo thành phần thứ 1 tăng dần, sau đó thành phần thứ 2 giảm dần (trái nhau -> trái dấu)
def getItem(a):
    return a[0], -a[1]          # thứ nhất (a[0]) tăng dần, thứ hai (a[1]) giảm dần -> trái dấu

if __name__ == '__main__':
    a = [[3, 2], [4, 5], [2, 6], [1, 4], [3, 1]]
    a.sort(key = getItem)
    print(a)
"""

#ANCHOR - Sắp xếp theo nhiều tiêu chí 
"""
#< Sắp xếp theo lương tăng dần, nếu 2 người cùng lương thì sort theo tên tăng dần theo thứ tự từ điển
dictionary = [
    {'name' : 'Tran Xuan Loc', 'job' : 'Dev', 'salary' : 500}, 
    {'name' : 'Thieu Ngoc Tuan', 'job' : 'Dev', 'salary' : 1500}, 
    {'name' : 'Phung Duc Kien', 'job' : 'BA', 'salary' : 500}, 
    {'name' : 'Huynh Manh Tuong', 'job' : 'Tester', 'salary' : 2000}, 
]
dictionary.sort(key = lambda x : (x.get('salary'), x.get('name')))
for x in dictionary:
    print(x)
"""

#ANCHOR - Kết hợp hàm sort với itemgetter() và attrgetter()
"""
#< Có thể sử dụng itemgetter() và attrgetter() từ module operator, cách hoạt động gần giống hàm getItem() mình tự define phía trên
from operator import itemgetter, attrgetter

#> List of tuples, each item inside the list is a tuple ("name", age) -> itemgetter() dùng cho list, tuple và dict
friends = [("Huynh Manh Tuong", 30), 
        ("Tran Nhat Phi", 28),
        ("Tuan Binh", 21),
        ("Thieu Tuan", 35)]
friends.sort(key = itemgetter(1))       # sort theo độ tuổi
for x in friends:
    print(x)

#> Sort theo nhiều tiêu chí
friends = [("Huynh Manh Tuong", 30, 'B'), 
        ("Tran Nhat Phi", 28, 'A'),
        ("Tuan Binh", 28, 'C'),
        ("Thieu Tuan", 30, 'Z')]
friends.sort(key = itemgetter(1, 2))    # sort theo độ tuổi và id
for x in friends:
    print(x)


#> Hàm attrgetter: dùng cho object (class instance)
from operator import attrgetter

class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

friends = [
    Friend("Tuong", 30),
    Friend("Phi", 28),
    Friend("Binh", 21)
]

# Sắp xếp theo age (thuộc tính của object)
sorted_friends = sorted(friends, key=attrgetter("age"))
for f in sorted_friends:
    print(f.name, f.age)
"""

#ANCHOR - HÀM SORTED
"""
#! Hàm sorted sẽ không thay đổi iterable mà nó sẽ luôn retun một LIST đã được sắp xếp tương ứng với iterable đã tryền vào
a = (5, 4, 1, 2, 3)     #< tuple(), list[]
b = sorted(a)
print(a)
print(b)

#< Demo
s = "abczza28tech"
t = sorted(s)           # list of sorted characters.
print(s)
print(t)
print("".join(t))       # turn t back into a string
"""
#!SECTION

#SECTION - [Sắp Xếp - Tìm Kiếm]'s EXERCISE

#ANCHOR - Các số khác nhau trong mảng
"""
n = int(input())
a = set(list(map(int, input().split())))
print(len(a))
"""

#ANCHOR - Binary search (tìm kiếm nhị phân)
"""
#! Binary Search chỉ hoạt động với mảng được sắp xếp tăng dần
#> Time complexity: O(logN)
def binarySearch(a, x):             # list a và gtri cần tìm x
    left, right = 0, len(a) - 1
    while (left <= right):
        mid = (left + right) // 2
        if (a[mid] == x):
            return True
        elif (a[mid] < x):
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = int(input())
    for i in range(q):
        x = int(input())
        if (binarySearch(a, x)):
            print('YES')
        else:
            print('NO')
"""

#ANCHOR - Tìm kiếm nhị phân biến đổi
"""
#1: Tìm vị trí xuất hiện đầu tiên của ptu X trong mảng
def binarySearchFirstElement(a, x):
    left, right = 0, len(a) - 1
    result = -1
    while(left <= right):
        mid = (left + right) // 2
        if (a[mid] == x):
            result = mid
            right = mid - 1         # keep searching on the left to find the left-most index
        elif (a[mid] < x):
            left = mid + 1
        else:
            right = mid - 1
    return result

#2: Tìm vị trí xuất hiện cuối cùng của ptu X trong mảng         
def binarySearchLastElement(a, x):
    left, right = 0, len(a) - 1
    result = -1
    while(left <= right):
        mid = (left + right) // 2
        if (a[mid] == x):
            result = mid
            left = mid + 1        # keep searching on the right to find the right-most index
        elif (a[mid] < x):
            left = mid + 1
        else:
            right = mid - 1
    return result

#3: Tìm vị trí xuất hiện đầu tiên của ptu >= X trong mảng
def binarySearchFirstBiggerOrEqualThan(a, x):
    left, right = 0, len(a) - 1
    result = -1
    while (left <= right):
        mid = (left + right) // 2
        if (a[mid] >= x):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

#4: Tìm vị trí xuất hiện đầu tiên của ptu >= X trong mảng
def binarySearchFirstBiggerThan(a, x):
    left, right = 0, len(a) - 1
    result = -1
    while (left <= right):
        mid = (left + right) // 2
        if (a[mid] > x):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

#5: Tìm số lần xuất hiện của ptu X trong mảng sử dụng kết quả của hàm 1 và 2
if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    first = binarySearchFirstElement(a, x)
    last = binarySearchLastElement(a, x)
    third = binarySearchFirstBiggerOrEqualThan(a, x)
    fourth = binarySearchFirstBiggerThan(a, x)
    print(first, last, third, fourth, sep = '\n')
    if first == -1:             # không tồn tại ptu đó
        print(0)
    else:           
        print(last - first + 1)     # vì đã được sắp xếp tăng dần 
"""

#ANCHOR - Tăng dần, giảm dần
"""
n = int(input())
a = list(map(int, input().split()))
a.sort()
for x in a:
    print(x, end = ' ')
print()
for x in a[::-1]:
    print(x, end = ' ')
"""

#ANCHOR - Sắp xếp theo trị tuyệt đối
"""
n = int(input())
a = list(map(int, input().split()))
a.sort(key = lambda x : abs(x))
#< a.sort(key = abs)       # khỏi cần lambda
for x in a:
    print(x, end = ' ')
"""

#ANCHOR - Sắp xếp theo tổng chữ số 
"""
def calSum(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x : (calSum(x), x))     # tổng chữ số trước, sau đó là giá trị
    for x in a:
        print(x, end = ' ')
"""

#ANCHOR - Khoảng cách nhỏ nhất
"""
n = int(input())
a = list(map(int, input().split()))
a.sort()
res = 10**18
for i in range(1, n):
    res = min(res, a[i] - a[i - 1])
print(res)
"""

#ANCHOR - Số xuất hiện nhiều nhất
"""
n = int(input())
a = list(map(int, input().split()))
d = {}
for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
b = sorted(d.items())
res, fre = 0, 0
for giatri, tansuat in b:               # giatri = key, tansuat = value
    if tansuat > fre:
        fre = tansuat
        res = giatri
print(res, fre)
"""

#ANCHOR - Trộn 2 dãy
"""
n, m = map(int, input().split())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
i, j = 0, 0
while i < n and j < m:
    if b[i] <= c[j]:
        print('b', i + 1, sep = '', end = ' ' )
        i += 1
    else:
        print('c', j + 1, sep = '', end = ' ')
        j += 1
while i < n:
    print('b', i + 1, sep = '', end = ' ')
    i += 1
while j < m:
    print('c', j + 1, sep = '', end = ' ')
    j += 1
"""

#ANCHOR - Khiêu vũ
"""
n, m = map(int, input().split())
nam = list(map(int, input().split()))
nu = list(map(int, input().split()))
nam.sort()
nu.sort()
ans = 0
i, j = 0, 0
while i < n and j < m:
    if nam[i] <= nu[j]:             # bạn nam thấp nhất thấp hơn cả bạn nữ thấp nhất thì tăng lên bạn nam kế
        i += 1
    else:
        ans += 1
        i += 1
        j += 1
print(ans)
"""

#ANCHOR - Xếp gạch
"""
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
docung, res = a[0], 1               # docung viên gạch dưới cùng luôn lớn nhất
for i in range(1, n):
    if docung <= 0:
        break
    else:
        res += 1
        docung = min((docung - 1), a[i])       # khi đặt 1 viên gạch lên thì docung của viên gạch trước giảm đi 1 và ktra viên gạch vừa đặt lên có docung bao nhiêu
print(res)
"""

#ANCHOR - Vắt sữa bò
"""
n = int(input())
a = list(map(int, input().split()))
res = 0
a.sort(reverse = True)          # lấy số lượng lớn nhất
for i in range(n):
    if a[i] > i:
        res += a[i] - i         # trường hợp bị trừ không còn lít nào -> tránh số âm
    else:
        break
print(res)
"""

#ANCHOR - The 2014 ACM-ICPC Asia Jakarta Regional Contest
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 1         # kể cả khi không có nhóm nào thì tất cả số vẫn là 1 nhóm
a.sort()
for i in range(1, n):
    if (a[i] - a[i - 1]) > k:          # chỉ khi vượt quá k thì mới tách thành 1 nhóm khác
        ans += 1
print(ans)
"""

#ANCHOR - Xếp lịch diễn
"""
#< Input
6
3 8
9 12
6 10
1 4
2 7 
11 14

#< Output
3

#! Explanation
- Các lịch diễn không trùng nhau là: 
1 4
6 10
11 14
--> Sắp xếp theo t/gian kết thúc tăng dần, sau đó so sánh t/gian kết thúc đó với t/gian bắt đầu tiếp theo

n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
a.sort(key = lambda x : x[1])   #< sắp xếp theo t/gian kết thúc tăng dần
ans, end_time = 1, a[0][1]      #> t/gian của công việc đầu tiên là a[0][1]
for i in range(1, n):
    if a[i][0] > end_time:      #> t/gian bắt đầu của công việc thứ i phải lớn hơn end_time của công việc trước
        ans += 1
        end_time = a[i][1]
print(ans)
"""

#ANCHOR - Điền số còn thiếu
"""
n = int(input())
a = set(list(map(int, input().split())))        # Read list, remove duplicates using set 
m, M = min(a), max(a)
print(M - m + 1 - len(a))     #< đầu - cuối + 1: số ptu đáng lẽ phải có trong set, len(a): số ptu thật sự đang có --> trừ sẽ ra số ptu còn thiếu
"""

#ANCHOR - Sắp xếp chữ số
"""
#< Cách 1: Dùng nguyên lý của set
n = int(input())
a = set(input())        # đưa vào set sẽ tách ra từng chữ số
if ' ' in a:
    a.remove(' ')
b = sorted(a)
for x in b:
    print(x, end = ' ')

#< Cách 2: Tách từng số
n = int(input())
se = set({})
a = list(map(int,input().split()))
for x in a:
    tmp = x
    while tmp != 0:
        se.add(tmp % 10)
        tmp //= 10
b = sorted(se)
for x in b:
    print(x, end = ' ')
"""

#ANCHOR - Sắp xếp theo tần suất
"""
n = int(input())
a = list(map(int, input().split()))
d = {}
for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

#< Tần suất giảm dần, nếu cùng tần suấtthì số nào nhỏ hơn in trước
b = list(d.items())
b.sort(key = lambda x : (-x[1], x[0]))
for giatri, tansuat in b:
    for _ in range(tansuat):
        print(giatri, end = ' ')
print()
#< Tần suất giảm dần, nếu cùng tần suất thì in theo thứ tự xuất hiện
c = list(d.items())
c.sort(key = lambda x : -x[1])
for giatri, tansuat in c:
    for _ in range(tansuat):            #> range(tansuat) → loop tansuat times.
        print(giatri, end = ' ')
"""

#ANCHOR - Biểu thức cho ra giá trị lớn nhất
"""
#< k dấu cộng vào k ptu lớn nhất, (n - 1 - k) dấu trừ vào các ptu nhỏ nhất
n, k = map(int, input().split())
a = list(map(int, input().split()))
a[1:] = sorted(a[1:], reverse = True)       #> This sorts the list from index 1 to the end in descending order.
ans = a[0]
for i in range(1, n):
    if i <= k:                  #> For the first k elements after a[0], we add them to ans.
        ans += a[i]
    else:
        ans -= a[i]            #> For the remaining elements, we subtract them from ans.
print(ans)
"""

#ANCHOR - Check in sân bay
"""
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
a.sort(key = lambda x : x[0])           # ai đến trước thì check in trước
end_time = a[0][0] + a[0][1]            # t/gian cần thiết cho khách 1
for i in range(1, n):
    end_time = max(end_time, a[i][0])      # so sánh t/gian end_time và arrival_time của khách thứ i
    end_time += a[i][1]                    # xong rồi cộng thêm check-in_time của khách thứ i đó
print(end_time)
"""

#ANCHOR - Sắp đặt số 0
"""
n = int(input())
a = list(map(int, input().split()))
for x in a:
    if x != 0:
        print(x, end = ' ')
print('0 ' * a.count(0))
"""

#NOTE - SELECTION SORT (sắp xếp chọn)
"""
def selectionSort(a, n):
    cnt = 1
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        print(f'Buoc {cnt}:', end = ' ')        # f-string formatting to insert the current step number cnt into the string 
        printArray(a)
        cnt += 1

def printArray(a):
    for x in a:
        print(x, end = ' ')
    print()

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    selectionSort(a, n)
"""

#NOTE - INSERTION SORT (sắp xếp chèn) 

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    #> Chèn a[i] vào đoạn [0; i - 1]
    pos, val = i - 1, a[i]
    while pos >= 0 and a[pos] > val:
        a[pos + 1] = a[pos]         # dịch sang phải
        pos -= 1
    a[pos + 1] = val
    print("Buoc " + str(i) + " : ", end = ' ')
    for x in a:
        print(x, end = ' ')
    print()


#!SECTION

