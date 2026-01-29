#REVIEW - DICTIONARY (BUỔI 10)

#SECTION - LÝ THUYẾT DICTIONARY
"""
- Dictionaries là một CTDL thuộc dạng associative array hay hashmap
- Dict (viết tắt) là một CTDL mà mỗi ptu của nó sẽ là một ánh xạ từ một khóa (key) sang một gtri tương ứng (value)
! Example:
>Keys                    >Values
'name'                   '28tech'
'job'                    'dev'
'city'                   'HCM'
'salary'                 '500'
'web'                    '28tech.com.vn'
"""

#ANCHOR - Tạo dict
"""
- Để tạo dict, bạn liệt kê các cặp key:value phân cách nhau bởi dấu phẩy và đặt giữa đóng mở ngoặc nhọn. 
! Mỗi cặp key:value được ngăn cách nhau bởi dấu :
- Tương tự như set, các key trong dict KHÔNG được trùng nhau 

#< Demo: Tạo dict lưu thông tin cá nhân
infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
print(type(infor))

#< Tạo dict bằng hàm zip()
key = ['name', 'job', 'web']          # lưu key trong một list
value = ['28tech', 'dev', '28tech.com.vn']          # lưu values trong một list 
c = dict(zip(key, value))
print(c)

#< Tạo dict bằng hàm fromkeys: Khi muốn các key đều chung một value
a = ['a', 'b', 'c']
defaultValue = 0
b = dict.fromkeys(a, defaultValue)
print(b)                    # {'a': 0, 'b': 0, 'c': 0}
"""

#NOTE - Các tính chất quan trọng của dict
"""
- Key trong dict là duy nhất: Dict không thể chứa 2 key giống nhau, trong trường hợp bạn gán nhiều value cho cùng 1 key thì dict sẽ giữ lại value sau cùng
- Key phải là object không thể thay đổi (IMMUTABLE): Có thể lựa chọn tuple, string, int, double,... làm key, còn value có thể là bất kì object nào
--> KHÔNG thể lấy list làm key vì list là MUTABLE -> "TypeError: unhashable type: 'list'" 
"""

#ANCHOR - Truy cập phần tử
"""
! Để truy cập value thông qua key, ta dùng cú pháp: dict['key']
infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
print(infor['name'], infor['job'], end = ' ')
"""

#ANCHOR - Lấy tập key, value, item
"""
- Lấy key, value, item trong dict: Sử dụng METHOD keys(), values(), items() trong dict để lấy về ADDRESS của bộ key, value, hoặc items trong dict.
! Cả 3 phương thức đều trả về iterable object, có thể convert sang list

infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
a = list(infor.items())
b = list(infor.keys())
c = list(infor.values())
print(a, b, c, sep = '\n')
"""

#ANCHOR - Duyệt dict
"""
infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
for x in infor:              
    #< print(x)              # duyệt bằng for each default chỉ in ra key
    print(x, infor[x])       # in ra key và value tương ứng
"""

#ANCHOR - Duyệt các cặp key, value trong dict
"""
infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
for (key, value) in infor.items():       # method items() trả về iterable chứa các cặp (key, value)
    print(key, value, sep = '->')     
"""

#ANCHOR - Thêm và sửa dict
"""
#< Thêm item: Thêm key và value chưa có sẵn
infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
infor['brand'] = 'asus'
print(list(infor.items()))

#< Sửa dict: Sửa key và value đã có sẵn
infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
infor['city'] = 'HN'
print(list(infor.items()))
"""

#ANCHOR - Xóa ptu trong dict
"""
#< Hàm pop(): Xóa cả key lẫn value
infor = {
    'name' : '28tech',
    'job' : 'dev',
    'salary' : 500,
    'web' : '28tech.com.vn',
    'city' : 'HCM'
}
infor.pop('job')
print(infor)
"""

#ANCHOR - Một số ví dụ với dict
"""
! Với dict, có thể sử dụng vào những bài toán liên quan tới tần suất, đếm, đánh dấu,...

#< Đếm tần suất xuất hiện của ptu trong mảng
a = [1, 3, 2, 1, 2, 3, 1, 0, 1, 4, 5, 6, 2, 0, 4]
d = {}      # create an empty dict
for x in a:
    if x in d:
        d[x] += 1           # nếu đã xuất hiện thì tần suất += 1
    else:
        d[x] = 1            # nếu chưa thêm vào dict d thì tần suất = 1
for value, frequency in d.items():
    print(value, frequency)

! d is a dictionary where:
> key = a number in the list a
> value = how many times that number appears
"""

#ANCHOR - Dict comprehension
"""
- Tương tự như list comp, dict comp là một cách gọn nhẹ giúp tạo ra một dict giúp code chuẩn Pythonic hơn
#> Cú pháp: {key : value for var in iterable}

a = [1, 2, 3, 4]
d1 = {}
for x in a:
    d1[x] = x**2

#< Dict comp
d2 = {x : x**2 for x in a}
print(d1)
print(d2)

#< Dict comp với string: Nhân 3 các chữ
s = 'abc'
d = {x : x * 3 for x in s}
print(d)
"""

#ANCHOR - Key, Value trong Dict comp
"""
s = ["28tech", "PyThON", "jaVA", "c++"]
d = {x.lower() : x.upper() for x in s}          # khi này x.lower() là key, x.upper() là value
for key, val in d.items():
    print(key, val) 
"""

#ANCHOR - Sort trong dictionary
"""
a = [1, 3, 2, 1, 2, 3, 1, 0, 1, 4, 5, 6, 2, 0, 4]
d = {}
for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
#< Sắp xếp các ptu trong mảng theo thứ tự tần suất giảm dần, nếu 2 ptu có cùng tần suất thì ptu nào nhỏ hơn đc in ra trước
d1 = sorted(d.items(), key = lambda x : (-x[1], x[0]))
for value, frequency in d1:
    print(value, frequency, sep = '->')
"""
#!SECTION

#SECTION - DICTIONARY's EXERCISES

#ANCHOR - Đếm tần suất (1)
"""
n = int(input())
a = list(map(int, input().split()))
d = {}
for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

d1 = sorted(d.items())
for value, frequency in d1:
    print(value, frequency)
print()

for value, frequency in d.items():
    print(value, frequency)
"""

#ANCHOR - Đếm tần suất (2)
"""
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = dict(Counter(a))
for giatri, tansuat in b.items():
    print(giatri, tansuat)
"""

#ANCHOR - Đếm phân phối sử dụng mảng
"""
n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 1001
for x in a:
  cnt[x] += 1
se = set({})

# Theo thứ tự xuất hiện
for x in a: 
  if x not in se:
    print(x, cnt[x])
    se.add(x)       
print()

# Theo thứ tự từ nhỏ tới lớn
for x in range(1001):     # Theo thứ tự
  if cnt[x] != 0:
    print(x, cnt[x])
print()

# Số có số lần xuất hiện nhiều nhất, nếu cùng số lần xuất hiện thì chọn số lớn hơn
res, dem = 0, 0
for x in range(1001):
  if cnt[x] >= dem:
    res = x
    dem = cnt[x]
print(res, dem)
print()

# Số có số lần xuất hiện ít nhất, nếu cùng số lần xuất hiện thì chọn số nhỏ hơn
res1, dem1 = 0, 10**9
for x in range(1001):
  if cnt[x] != 0 and cnt[x] < dem1:
    res1 = x
    dem1 = cnt[x]
print(res1, dem1)
"""

#ANCHOR - Kiểm tra mảng tăng dần (tăng chặt)
"""
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
  if a[i] <= a[i - 1]:
    print("NO")
    exit()          # gặp đk dừng là dừng luôn
print("YES")
"""

#ANCHOR - Số lớn hơn các số đứng trước
"""
# Liệt kê các ptu trong dãy lớn hơn TẤT CẢ các số đứng trước nó (Ptu đầu tiên đc coi là thỏa mãn)
n = int(input())
a = list(map(int, input().split()))
Max = -10**9
for x in a:
  if x > Max:
    print(x, end = ' ')
    Max = x
"""

#ANCHOR - Die hard
"""
def check(a, n):
  price = 25
  total = 0
  for x in range(n):
    if (a[x] == price):
      total += a[x]
    else:
      payback = a[x] - price
      total -= payback
      if (total < 0):
        return False
  return True

n = int(input())
a = list(map(int, input().split()))
if check(a, n):
  print("YES")
else:
  print("NO")
"""

#ANCHOR - Gửi thư
"""
# Gần nhất: thành phố đứng trước và sau
# Xa nhất: thành phố đầu và cuối
import math
n = int(input())
a = list(map(int, input().split()))
mini, maxi = {}, {}
for x in range(n):
  previous = abs(a[x] - a[x - 1])
  after = abs(a[x] - a[x + 1]) if x != (n - 1) else previous        # khi không phải ptu cuối
  mini = previous if previous < after else after 
  
  first = abs(a[x] - a[0])
  last = abs(a[n - 1] - a[x])
  maxi  = first if first > last else last
  print(mini, maxi, end = "\n")
"""

#ANCHOR - Đếm cặp snt cùng nhau
"""
# Hai snt cùng nhau có UCLN bằng 1
import math
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
  for j in range(i):
    if math.gcd(a[i], a[j]) == 1:
      print(f"({a[i]},{a[j]})", end = ", ")
      ans += 1
print("\n", ans)
"""

#ANCHOR - Đổi tiền tham lam
"""
n = int(input())
cnt = 0
tmp = n
money = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
length = len(money)
for x in range(length - 1, -1, -1):
  cnt += tmp // money[x]      # chia nguyên làm tròn xuống để biết số tờ cần dùng của mệnh giá đó. VD: 580 // 1000 = 0 ; 580 // 500 = 1
  tmp %= money[x]   # chia lấy dư để lấy số tiền còn lại. VD: 580 % 1000 = 580
print(cnt)
"""

#ANCHOR - Dãy con dài nhất các ptu liền kề khác nhau
"""
# Tìm độ dài của dãy con liên tiếp các ptu sao cho các ptu liền kề nhau trong dãy con đều khác nhau
# Nếu có nhiều dãy con thỏa mãn, hãy in ra dãy con có tổng lớn nhất
n = int(input())
a = list(map(int, input().split()))
a.append(a[-1])       # ép dãy cuối cùng được xử lý khi vòng lặp kết thúc
sum, cnt, res, idx, ans = a[0], 1, 1, 0, a[0]        
#< sum: tổng dãy con hiện tại, cnt: số ptu trong dãy con hiện tại, res: độ dài dãy tốt nhất, idx: vị trí bắt đầu dãy tốt nhất, ans: tổng lớn nhất của dãy dài nhất

for i in range(1, n + 1):       # n + 1 vì append thêm 1 ptu
  if (a[i] != a[i - 1]):        # nếu ptu sau != ptu trước
    cnt += 1                    # thì cnt += 1
    sum += a[i]                 # tính tổng dãy
  else:                         # khi dãy con kết thúc (ptu sau != ptu trước)
    if (cnt > res):             # nếu sl ptu trong dãy hiện tại > sl ptu trong dãy tốt nhất
      res = cnt                 # thì cập nhật sl ptu tốt nhất mới
      ans = sum                 # cập nhật tổng lớn nhất = tổng dãy con hiện tại
      idx = i - cnt             # i: ptu đầu tiên KHÔNG thuộc dãy, cnt: độ dài dãy con vừa kết thúc --> index bắt đầu của dãy con lớn nhất  
    elif cnt == res:            # nếu bằng độ dài
      if sum > ans:             # chọn dãy có tổng lớn hơn
        ans = sum               # lưu tổng độ dài lớn nhất  
        idx = i - cnt           
    cnt = 1                     # chuẩn bị cho dãy kế tiếp
    sum = a[i]                  
print(res)
for i in range(res):
  print(a[idx + i], end = ' ')        # in từng ptu trong dãy con lớn nhất
"""

#ANCHOR - Dãy số ưu thế
"""
# Gọi là dãy ưu thế nếu thỏa 1 trong 2 điều kiện sau đây:
#> Ưu thế chẵn: Số ptu của dãy là chẵn và sl chẵn trong dãy nhiều hơn sl lẻ
#> Ưu thế lẻ: Số ptu của dãy là lẻ và sl lẻ trong dãy nhiều hơn sl chẵn
a = list(map(int, input().split()))
length = len(a)
cnt_odd, cnt_even = 0, 0
for x in range(length):
  if (a[x] % 2 == 0):
    cnt_even += 1
  else:
    cnt_odd += 1
if (length % 2 == 0 and cnt_even > cnt_odd):
  print("YES. Ưu thế chẵn")
elif (length % 2 != 0 and cnt_odd > cnt_even):
  print("YES. Ưu thế lẻ")
else:
  print("NO")
"""

#ANCHOR - Số thao tác giúp mảng tăng dần
"""
# Tìm số đơn vị tối thiểu cần thêm vào các ptu trong mảng sao cho mảng trở thành một dãy tăng chặt
n = int(input())
a = list(map(int, input().split()))
res = 0
for x in range(1, n):
  if (a[x] <= a[x - 1]):
    amount = abs(a[x] - a[x - 1])
    res += amount + 1
print(res)  
"""

#ANCHOR - Trộn 2 dãy đã sắp xếp
"""
# Cho 2 mảng đã được sắp xếp tăng dần, thực hiện trộn 2 dãy trên thành một dãy được sắp xếp
#< Merge sort
n, m = list(map(int, input().split()))
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
  print(x, end = " ")
"""

#ANCHOR - Đếm tần suất
"""
n = int(input())
a = list(map(int, input().split()))
d = {}
for x in a:
  if x in d:
    d[x] += 1
  else:
    d[x] = 1

d1 = sorted(d.items())
for value, frequency in d1:
  print(value, frequency)
print()
for value, frequency in d.items():
  print(value, frequency)
"""

#ANCHOR - Tìm hợp và giao của 2 mảng (1)
"""
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = set(a)      # Dùng set để lấy các ptu UNIQUE của list a
d = set(b)      

intersection = sorted(c & d)    # Giao: là tập hợp chứa tất cả các phần tử chung của hai hay nhiều tập hợp A và B
union = sorted(c | d)           # Hợp: là tập hợp chứa tất cả các phần tử thuộc tập A, thuộc tập B, hoặc thuộc cả hai

print(*intersection)
print(*union)     #< "*": unpacking operator 
"""

1:44:06
#!SECTION

