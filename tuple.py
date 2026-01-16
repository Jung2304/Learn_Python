#REVIEW - TUPLE (BUỔI 9)

#SECTION - LÝ THUYẾT TUPLE
"""
- Tuple là một collection có thứ tự trong Python
- Để tạo tuple, ta để các ptu trong tuple phân cách nhau bởi dấu phẩy và đặt trong đóng mở ngoặc tròn ()
! Các tính chất của Tuple
> Tuples are ordered: Các ptu lưu trong tuple đều có thứ tự
> Accessed by index: Truy cập các ptu trong tuple thông qua chỉ số
> Tuple can contain any sort of object: Tuple có thể chứa các ptu ở mọi loại object như int, float, string, tuple, list,...
> Tuples are immutable: Tuple KHÔNG thể bị thay đổi, tức là không thể thêm, sửa, xóa
"""

#ANCHOR - Tạo tuple
"""
a = (1, 2, 3)
b = ("28tech", "python", "java", "c++")
c = (2304, )
print(type(a), type(b), type(c), sep = " ")

#< Tạo tuple thông qua constructor tuple()
s = "28tech"
b = tuple(s)
c = tuple([1, 2, 3])
print(b)
print(c)
"""

#ANCHOR - Nested tuple
"""
a = ("28tech", (1, 2, 3), 3.4)
print(type(a))
print(a)
"""

#ANCHOR - Tuple unpacking
"""
a = ("28tech", (1, 2, 3), 3.4)
x, y, z= a
print(x, y, z)

#< Sử dụng toán tử *
a = ("28tech", (1, 2, 3), 3.4)
x, *y = a
print(x, y, sep = '\n')
"""

#ANCHOR - Thay đổi tuple
"""
- Tuple không thể thay đổi giá trị, nhưng nếu item trong tuple là mutable object (list, string,...) thì bạn vẫn có thể thay đổi gtri của item đó
! Dù tuple không thể thay đổi nhưng vẫn có thể xóa luôn cả tuple

a = ("28tech", [1, 2, 3], "python", 8.4)
a[1][0] = 100           # a[1] = [1, 2, 3] ; a[1][0] = 1
print(a)    
"""

#ANCHOR - Tuple concatenation và repetition
"""
#< Tuple concatenation: sử dụng toán tử +
a = ("28tech", "java", "python")
b = ("c++", "c#")
c = a + b
print(c)

#< Tuple repetition: sử dụng toán tử *
a = ("28tech", "python", "java")
b = a * 3
print(b) 
"""

#ANCHOR - Sắp xếp tuple
"""
! Bản thân hàm sorted() sẽ trả về list --> ép sang tuple

a = (5, 2, 1, 3, 4, 6, 9)
a = tuple(sorted(a))
print(a)
"""

#ANCHOR - Count và Index
"""
- Tuple hỗ trợ 2 hàm: 
> count() để đếm số lần xuất hiện của 1 ptu trong tuple
> index() để trả về chỉ số đầu tiên của một ptu trong tuple 

a = (5, 1, 2, 3, 2, 1)
print(a.count(1))   # 2
print(a.index(1))   # 1
"""
#!SECTION