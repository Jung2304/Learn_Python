#ANCHOR - printf(object, sep = seperator, end = end) 
"""
print('Xin Chao')
print('Xin Chao', 'Python', sep = "#")      #sep = seperator: Phân cách giữa các đối tượng khi in, không có thì mặc định dấu cách
print('Xin Chao', 'Python', sep = '\n')
print('Xin Chao', 'Python', end = '?')      #end = end: print thông thường sẽ tự xuống dòng không cần end, end = '?' ở đây sẽ kết thúc câu bằng '?' và in tiếp câu dưới
print('Xin Chao')
"""
#Chú thích trên nhiều dòng --> đưa vào 3 dấu nháy kép """
"""
Đây là chú thích trên nhiều dòng, sẽ đưa vào 3 DẤU NHÁY KÉP
"""

#ANCHOR - Biến (variable)
"""
Trong Python, không cần phải khai báo biến cũng như chỉ rõ kdl của biến đó
Biến sẽ được xác định kiểu tự động (dynamic typing) khi bạn gán giá trị cho nó
Để biết kdl của biến đó, bạn dùng hàm: type()
Không đặt tên biến có chứa dấu cách, kí tự đặc biệt, bắt đầu bằng chữ số. Tên biến trong Python phân biệt hoa thường (case sensitive)

a = 100
b = 'Hello'
c = 37.5
print(type(a))
print(type(b))
print(type(c))
"""

#ANCHOR - Kiểu dữ liệu (data type) 
"""
Trong Python có 3 kdl số: Số nguyên (Integer), Số thực dấu phẩy động (Floating-point numbers) và Số phức (Complex numbers) 
a/ Số nguyên (integer) (kdl: int)
Trong Python không có giới hạn về gtri mà số nguyên có thể lưu --> vô cực

b/ Số thực (float) (kdl: float)
Có giới hạn: 
    max = 1.8*10^308, lớn hơn gtri này đc mô tả bởi chuỗi inf (Infinity)
    min = 5.0*10^-324, nhỏ hơn gtri này đc coi là 0

c/ Số phức (Complex numbers)
Có thể trích xuất phần thực và phần ảo của số phức
a = 10 + 51j
print(a.real, a.imag) 

a = 100
b = 34.5
c = 5 + 3j
print(type(a), type(b), type(c), sep = '\n')

e = 15e5    # e là scientific notation, 15e5 = 15^5
f = 100e-2  # 100e-2 = 100^-2 = 1
print(e, f, sep = '\n')

g = 10^5    #int
h = 10e5    #float 
print(type(g), type(h))

i = 34.5349645070653        #in ra với 2 số sau dấu thập phân
print(round(i, 2))

k = 10 + 34j        #in số phức
print(k.real, k.imag)
"""

#ANCHOR - Kiểu đúng sai
"""
Kiểu bool chỉ lưu 2 giá trị True hoặc False (viết hoa chữ cái đầu)
Chú ý: Các gtri được xác định là True trong Python: xâu khác rỗng, các số khác

a = True
print(type(a))
print(bool(100))
print(bool(0))
print(bool('hello'))
print(bool(''))
"""

#ANCHOR - Kiểu xâu kí tự (str)
"""
string = 'hello'
print(type(string))

Muốn in xâu trên nhiều dòng thì bỏ vào trong cặp nháy kép và gán biến
"""

#ANCHOR - Ép kiểu (Type casting)
# Sử dụng constructor khi ép kiểu (int(), float(), str())
"""
b = 12.8
a = int(b)
print(type(a))
print(a)

c = "1232423052"
d = float(c)
print(d)        # 1232423052.0

# Những xâu không hợp lệ (xâu số có chữ) sẽ không thể ép thành int
e = "123434523ad"
f = int(e)
print(e)        #error
"""

#ANCHOR - Toán tử
"""
#< Assignment operator (toán tử gán)
a,b,c = 100,200,300
print(a,b,c)    #Gán nhiều gtri trên cùng một dòng

#< Arithmetic operator (toán tử toán học)
# Ngoài cộng, trừ, nhân (+ - *)
    #> Phép chia thập phân (/) và phép chia nguyên (floor division, làm tròn xuống) (//)
a, b = 300, 7
c = a/b
d = a//b
print(c)
print(d)
    #> Phép chia dư (%) chỉ lấy phần dư. VD: 15 % 2 == 1
e = a%b 
print(e)
    #> Phép lũy thừa (**). VD: 2**10 = 2^10 == 1024
f = 2**8
print(f)

#< Comparison operator (toán tử so sánh) 
# Phép so sánh sẽ trả về True hoặc False

print(10 == 10)
print(10 != 10)
print(10 <= 10)

#< Logic operator (toán tử logic)
# Các phép logic (and, or, not)
"""

#! Bài 1: Tính toán gtri của biểu thức
"""
# Cho biểu thức A(x) = x^3 + 3x^2 + x + 1. Với gtri của x đc nhập từ bàn phím, tính và in ra gtri của biểu thức trên
x = int(input('Nhap gia tri cho bien x: '))     #> nhập gtri x từ bàn phím, những giá trị được nhập thông qua hàm input đều có kdl str
a = int(x**3 + 3*(x**2) + x + 1)
print('Gia tri la:', a)

# Nhập chiều dài, chiều rộng của 2 biến trên 2 dòng. In ra chu vi và diện tích HCN
a = int(input('Chieu dai la: '))
b = int(input('Chieu rong la: '))
C = (a+b)*2
print('Chu vi la:', C)
S = a*b
print('Dien tich la:', S)

# Nhập nhiều giá trị và split ra từng dòng (vì đối với hàm input() bth sẽ in ra tất cả trên một dòng)
x,y,z = map(int, input().split())
    #< input().split() cho phép ta tách chuỗi string ra từng ptu. map() sẽ áp dụng tất cả ptu theo kdl int
print(x)
print(y)
print(z)
"""

#! Bài 2: Tính toán gtri của biểu thức 2
"""
# Cho ba số nguyên a, b, c, hãy tính S = a*(b+c)+b*(a+c)
print("Hay nhap ba gia tri a,b,c:")
a,b,c = map(int, input().split())
S = a*(b+c)+b*(a+c)
print(S)
"""

#! Bài 3: Đổi nhiệt độ 
"""
# Chuyển từ độ C sang độ F. Công thức: F = (C * 9/5) + 32
C = int(input())
F = (C * 9/5) + 32
print('%.2f' % F) 
"""

#! Bài 4: Chu vi và diện tích hình tròn 
"""
# Cho bán kính R của hình tròn. Yêu cầu tính chu vi và diện tích của hình tròn đó. Lấy PI = 3.14
print('Hay nhap ban kinh hinh tron:')
R = int(input())
PI = 3.14
print('%.4f' % (2*R*PI))
print('%.4f' % (R*R*PI))
"""

#! Bài 5: Khoảng cách Euclid
"""
# Tính khoảng cách Euclid giữa 2 điểm trong hệ tọa độ Oxy
import math
x1,y1,x2,y2 = map(int, input().split())
euclid = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)
print('%.2f' % euclid)
"""

#! Bài 7: Số lớn nhất và nhỏ nhất
"""
# Cho 2 số nguyên a và b. Hãy tìm 2 số sau, số thứ 1 là số lớn nhất <= a mà chia hết cho b, số thứ 2 là số nhỏ nhất >= a mà chia hết cho b.
import math
a,b = map(int, input().split())
print((a // b) * b)    # chia nguyên nhân ngược lại 
print(math.ceil(a / b) * b)     # chia nguyên rồi làm tròn lên rồi nhân ngược lại
"""

#! Bài 13: Đổi ngày sang năm, tuần, ngày
"""
# Cho trước N ngày, hãy đổi N thành số năm, số tuần và số ngày. Biết rằng một năm có 365 ngày
import math
N = int(input())
Year = N // 365         
N = N % 365
Week = N // 7
N = N % 7
print(Year, Week, N)
"""

#! Bài 27: Làm tròn số
"""
# Cho một số thực a, hãy tìm số nguyên a gần nhất. Trong trường hợp phần thực của a = 0.5 thì làm tròn lên
import math
a = float(input())
print(round(a))             
print('%.0f' % a)       # better
"""

#! Bài 30: Tổ hợp chập 2
"""
# Trong lớp có n sinh viên, muốn chọn ra 2 bạn sinh viên để tham gia cuộc thi khiêu vũ, hỏi có bao nhiêu cách
#< Cách 1: Dùng công thức (testcase lớn sẽ không dùng được)
import math
N = int(input())
res = (math.factorial(N)) / (math.factorial(2) * math.factorial(N - 2))
print(int(res)) 

#< Cách 2: Rút gọn công thức (better) (k = 2)
# n! / k!*(n-k)! <=> n*(n-1)*(n-2)*(n-k)! / k!*(n-k)! ==> n*(n-1)*(n-2) / k!
import math
N = int(input())
res = N*(N-1) / 2       
print(int(res))
"""

#! Bài 35: HPNY
"""
# Còn bao nhiêu phút nữa là đến Tết
import math
h, m = map(int, input().split())
print(1440 - h * 60 - m)            # một ngày có 1440 phút - (số giờ đã trôi qua) * 60 - số phút còn lại
"""

#ANCHOR - Hàm toán học
"""
import math
print(math.sqrt(36))
# print(help(math))     
print(math.ceil(3.2))       # làm tròn lên = 4
print(math.floor(3.8))      # làm tròn xuống = 3
print(round(3.6))           # làm tròn lên 4 (theo phần thập phân)
print(math.pow(2,10))       # <=> 2**10
print(math.fabs(-100))      # tính trị tuyệt đối = 100.0 (float abs)
print(abs(-100))
print(math.factorial(10))   # tính giai thừa
print(math.isqrt(10))       # chỉ lấy phần nguyên của căn bậc hai (integer sqrt)
"""

