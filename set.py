#REVIEW - SET (BUỔI 9)

#SECTION - LÝ THUYẾT SET
"""
- Set trong Python là một tập hợp các phần tử duy nhất không có thứ tự. Chúng thường được sử dụng để tính toán các phép toán liên quan tới tập hợp
#! Các tính chất của Set
> Sets are unordered: Các ptu trong set không có thứ tự nhất định nào cả
> Set items are UNIQUE: Các ptu trong set là độc nhất, không có 2 ptu nào trong set trùng nhau
> Sets are unindexed: Set không thể truy cập được thông qua chỉ số
> Sets are changeable (mutable): set CÓ thể thay đổi 
"""

#ANCHOR - Tạo set
"""
- Để tạo set, ta để các ptu trong set phân cách nhau bởi dấu phẩy và đặt trong đóng mở ngoặc nhọn {}
- Set KHÔNG lưu những gtri TRÙNG nhau, vì thế nếu trong set tồn tại các ptu giống nhau, nó sẽ tự bị loại bỏ
- Khi in một set, thứ tự xuất hiện là NGẪU NHIÊN (random) (trừ list?)

#< Demo
st = {"28tech", "python", "28tech", "java", "set", "set"}
print(st)
t = {1, 2, 1, 2, 3, "abcd"}
print(t
"""

#ANCHOR - Set Constructor
"""
- Có thể tạo set bằng set constructor từ các object khác như list, string, range,...
#< Demo
s = "28techtech"        # string
t = set(s)
a = [1, 2, 3, 4, 5, 6, 7, "abcd"]           # list
b = set(a)
print(t, b, sep = '\n')
"""

#ANCHOR - Thêm MỘT ptu vào set
"""
- Để thêm ptu vào set, ta sử dụng hàm add()
#< Demo
st = {"28tech", "python", "28tech", "java", "set", "set"}
st.add("abc")
st.add("python")        # already had
print(st)
"""

#ANCHOR - Thêm NHIỀU ptu vào set
"""
- Để thêm nhiều ptu vào set, ta sử dụng hàm update()
#< Demo
st = {"28tech", "python", "28tech", "java", "set", "set"}
st.update([100, "abc", "python", "def"])
print(st)
"""

#ANCHOR - Xóa ptu khỏi set
"""
- Để xóa ptu khỏi set ta sử dụng hàm:
> remove()
> discard()
> clear()
! Sử dụng hàm discard() an toàn hơn vì:
> Khi dùng hàm remove() để xóa một ptu không tồn tại thì sẽ gây lỗi Keyerror
> Ngược lại, dùng hàm discard() thì không

#< Demo
s = {"python", "28tech", "java", "set", "abc"}
s.remove("28tech")
print(s)
s.discard("abc")
print(s)
"""

#ANCHOR - Duyệt set bằng for each và toán tử "in"
"""
- Khi cần tìm kiếm nhiều và các ptu có tính đặc trưng (unique), ta nên dùng set, vì set được Python cài đặt bằng HashTable
--> Tốc độ tìm kiếm là O(1)
> VD: Tìm kiếm ID của một nvien trong công ty

#< Demo
s = {"python", "28tech", "java", "set", "abc"}
for x in s:
    print(x, end = " ")
if "28tech" in s:
    print('\n',"FOUND")
else:
    print("NOT FOUND")
"""

#ANCHOR - Phép UNION
"""
- Phép Union: Phép hợp (kết hợp) lấy ra các ptu thuộc 1 TRONG 2 tập hợp
! Sử dụng hàm union() hoặc phép toán | để tìm hợp của 2 tập 

s = {"28tech", "abc", "python"}
t = {"28tech", "amazon", "java"}
u = s.union(t)
v = s | t
print("u:", u)
print("v:", v)
"""

#ANCHOR - Phép INTERSECTION
"""
- Phép Intersection: Phép giao lấy ra các ptu THUỘC CẢ 2 tập hợp
! Sử dụng hàm intersection() hoặc toán tử &

s = {"28tech", "abc", "python", "same"}
t = {"28tech", "amazon", "java", "same"}
i = s.intersection(t)
print("i:", i)
inter = s & t
print("intersection:", inter)
"""

#ANCHOR - Phép DIFFERENCE
"""
- Phép Difference: Phép khác của A, B lấy ra các ptu thuộc tập A nhưng không thuộc tập B
! Sử dụng hàm difference() hoặc toán tử -  

s = {"28tech", "abc", "python", "same"}
t = {"28tech", "amazon", "java", "same"}
diff = s.difference(t)
print(diff)
differ = s - t
print(differ)
""" 

#ANCHOR - Phép SYMMETRIC_DIFFERENCE
"""
- Symmetric Difference: Phép Symmetric Difference của 2 tập A và B chỉ lấy ra các ptu thuộc 1 trong 2 tập nhưng không thuộc cả 2
! Sử dụng hàm symmetric_difference hoặc toán tử ^

s = {"28tech", "abc", "python", "same"}
t = {"28tech", "amazon", "java", "same"}
sym = s.symmetric_difference(t)
print(sym)
symm = s ^ t
print(symm)
"""

#ANCHOR - CÁC HÀM PHỔ BIẾN CỦA SET
"""
#! isdisjoint(): Xác định xem 2 tập có độc lập không?
s = {"28tech", "abc", "python", "same"}
t = {"28tech", "amazon", "java", "same"}
u = {"UIT", "US", "UET"}
print(s.isdisjoint(t))      # False
print(t.isdisjoint(u))      # True

#! issubset(): Kiểm tra xem tập này có phải là tập con của tập khác không?
s = {"28tech", "abc", "python", "same"}
t = {"28tech", "same"}
u = {"UIT", "US", "UET"}
print(t.issubset(s))            # True
print(u.issubset(s))            # False

#! issuperset(): Kiểm tra xem tập này có phải là tập cha của tập khác không?
s = {"28tech", "abc", "python", "same"}
t = {"28tech", "same"}
u = {"UIT", "US", "UET"}
print(s.issuperset(t))      # True
print(s.issuperset(u))      # False
"""
#!SECTION

#SECTION - SET's EXERCISE

#ANCHOR - Tìm hợp và giao của 2 mảng (1)
"""
#< Cho 2 mảng số nguyên a và b gồm n và m ptu. Gọi mảng c và d lần lượt là mảng chỉ bao gồm các ptu khác nhau của a và b
#< Hãy tìm mảng giao và hợp của mảng c và d và liệt kê theo thứ tự tăng dần

n, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
uni = sorted(a.union(b))
inter = sorted(a.intersection(b))
for x in inter:
    print(x, end = ' ')
print()
for x in uni:
    print(x, end = ' ')
"""

#ANCHOR - Tìm hợp và giao của 2 mảng (2)
"""
< Sample Input 0
4 5
1 2 3 4
2 3 5 6 7
< Sample Output 0
1 2 3 4 5 6 7
2 3

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
giao, hop = [], []
i, j = 0, 0
while i < n and j < m:
    if a[i] == b[j]:
        hop.append(a[i])
        giao.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        hop.append(a[i])
        i += 1
    else:
        hop.append(b[j])
while i < n:
    hop.append(a[i])
    i += 1
while j < m:
    hop.append(b[j])
    j += 1
for x in hop:
    print(x, end = ' ')
print()
for x in giao:
    print(x, end = ' ')
"""

#ANCHOR - Suffix and Query
"""
< Precomputes how many distinct elements are in the suffix starting at each index.
<Answers multiple queries efficiently in O(1) per query.
n = int(input())
a = list(map(int, input().split()))
F = [0] * n
se = set({})
for i in range(n - 1, -1, -1):
    se.add(a[i])
    F[i] = len(se)      
q = int(input())
for i in range(q):
    left = int(input())
    print(F[left])
"""

#!SECTION