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
c = list(b.items())
for giatri, tansuat in b.items():
    print(giatri, tansuat)
"""



#!SECTION

