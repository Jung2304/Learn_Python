#NOTE - ĐỆ QUY (RECURSION)

#ANCHOR - Ngăn xếp (Stack)
"""
- Ngăn xếp là một CTDL có q.hệ mật thiết với cơ chế hoạt động của đệ quy
- Ngăn xếp hỗ trợ 2 thao tác, đều đc thực hiện ở đỉnh ngăn xếp:
    + push: giúp thêm 1 ptu vào đỉnh ngăn xếp
    + pop: giúp xóa 1 ptu khỏi đỉnh ngăn xếp
- Stack hoạt động theo nguyên tắc LIFO (Last In First Out)
"""

#ANCHOR - Đệ quy (syntax)
"""
def recurse():
    ...
    recurse
    ...

if __name__ == '__main__':
    recurse()
"""

#ANCHOR - Tính tổng các số từ 1 đến n 
"""
def sum(n):
    if n == 1:      # bài toán con nhỏ nhất (điểm dừng)
        return n
    else:
        return n + sum(n - 1)       # ct truy hồi 

if __name__ == '__main__':
    print(sum(3))
"""

#ANCHOR - Tính tổng 2
"""
# Tính tổng hàm: S(n) = 1^2 + 2^2 + 3^2 + 4^2 + .. + n^2
def sum_2(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_2(n - 1)

if __name__ == '__main__':
    n = int(input())
    print(sum_2(n))
"""

#ANCHOR - (!)Tổ hợp chập k của n
"""
def nCk(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return nCk(n - 1, k - 1) + nCk(n - 1, k)        # ct Pascal
"""

#ANCHOR - Tính giai thừa
"""
def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n - 1)

if __name__ == '__main__':
    n = int(input())
    print(giai_thua(n))
"""

#ANCHOR -  Fibo thứ n
"""
# VD số fibo thứ 5 là 3 vì: 0 1 1 2 3
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
if __name__ == '__main__':
    n = int(input())
    print(fibo(n))
"""

#ANCHOR - (!) Lũy thừa nhị phân
"""
a^b = a^(b/2) * a^(b/2)     if b is even
    = a^(b/2) * a^(b/2) * a     if b is odd

def binary_expo(a,b,c):             # c là 1e9 + 7
    if b == 0:
        return 1
    tmp = binary_expo(a, b // 2, c)         # lưu số mũ ở dạng b // 2
    if (b & 1) == False:                # số mũ chẵn 
        return tmp * tmp % c                # modular arithmetic
    else:
        return tmp * tmp * a % c
    
if __name__ == '__main__':
    a,b = map(int, input().split())
    print(binary_expo(a,b,1000000007))
"""

#ANCHOR - (!)decimal sang binary
"""
def convert(n):
    if n == 0:
        return
    else:
        convert(n // 2)     # chạy xong mới in
        print(n % 2, end ='')

n = int(input())
if n == 0:
    print(0)
else:
    convert(n)
"""

#ANCHOR - decimal sang hexa
"""
def convert(n):
    if n == 0:
        return
    else:
        convert(n // 16)
        r = n % 16
        if r < 10:         # số dư từ 0 -> 9
            print(r, end = '')
        else:                   # từ số 11 in chữ
            if r == 10:
                print('A', end = '')
            elif r == 11:
                print('B', end = '')
            elif r == 12:
                print('C', end = '')
            elif r == 13:
                print('D', end = '')
            elif r == 14:
                print('E', end = '')
            elif r == 15:
                print('F', end = '')

n = int(input())
if n == 0:
    print('0')
else:
    convert(n)
"""

#ANCHOR - Tính tổng chữ số
"""
def total(n):
    if n < 10:
        return n
    else:
        return n % 10 + total(n // 10)
n = int(input()) 
print(total(n))
"""

#ANCHOR - (!)Đếm SL chữ số
"""
def count(n):
    if n < 10:
        return 1
    else:
        return count(n // 10) + 1
n = int(input())
print(count(n))
"""

#ANCHOR - Tìm chữ số đầu tiên
"""
def find(n):
    if n < 10:
        return n
    else:
        return find(n // 10)

if __name__ == '__main__':
    n = int(input())
    print(find(n))
"""

#ANCHOR - Max và Min
"""
def find_min(n):
    if n < 10:
        return n
    else:
        return min(n % 10, find_min(n // 10))   # so sánh chữ số ở hàng đơn vị với lần lượt các chữ số từ hàng trăm trở đi (n // 10)

def find_max(n):
    if n < 10:
        return n
    else:
        return max(n % 10, find_max(n // 10))

n = int(input())
print(find_max(n), find_min(n)) 
"""

#ANCHOR - In ra n theo thứ tự
"""
def l_to_r(n):
    if n < 10:
        print(n)
    else:
        print(n % 10, end = ' ')
        l_to_r(n // 10)

def r_to_l(n):
    if n < 10:
        print(n, end = ' ')
    else:
        r_to_l(n // 10)
        print(n % 10, end = ' ')

n = int(input())
l_to_r(n)
r_to_l(n)
"""

#ANCHOR - (!) Tổng chẵn, lẻ
"""
def total_even(n):
    if n < 10:          # chỉ có 1 chữ số
        if n % 2 == 0:
            return n
        else:
            return 0
    else:
        if (n % 10) % 2 == 0:           # nếu chữ số ở hàng đơn vị chẵn
            return (n % 10) + total_even(n // 10)       # thì lấy chữ số đó cộng với các chữ số khác 
        else:
            return total_even(n // 10)              # nếu chữ số ở hàng đơn vị lẻ thì tìm tiếp

def total_odd(n):
    if n < 10:
        if (n & 1) == True:
            return n
        else:
            return 0
    else:
        if (n % 10) & 1 == True:
            return (n % 10) + total_odd(n // 10)
        else:
            return total_odd(n // 10)

n = int(input())
print(total_even(n), total_odd(n))
"""

#ANCHOR - Ktra chữ số chẵn
"""
def check(n):
    if n < 10:
        if n % 2 != 0:
            return False
        else:
            return n
    else:
        if (n % 10) % 2 != 0:
            return False
        else:
            return check(n // 10)

n = int(input())
print('YES' if check(n) else 'NO')
"""

#ANCHOR - (!) Đếm số thao tác
"""
def count_step(n):
    if n == 1:      # thao tác nhỏ nhất
        return 0 
    res1, res2, res3 = 10**9, 10**9, 10**9      # Initialize results with a large number to ensure they don't affect min() selection.
    #< Đếm số thao tác ở mỗi nhánh và trả về min
    if n % 2 == 0:
        res1 = 1 + count_step(n // 2)      
    if n % 3 == 0:
        res2 = 1 + count_step(n // 3)
    if n > 1:
        res3 = 1 + count_step(n - 1)
    return min(res1, res2, res3)

n = int(input())
print(count_step(n))
"""
