#REVIEW - MẢNG 2 CHIỀU TRONG PYTHON (BUỔI 13)

#SECTION: INTRODUCTION

#ANCHOR - Tạo và nhập mảng
"""
n, m = 3, 4     #< n hàng và m cột
a = [[0 for _ in range(m)] for _ in range(n)]     #< list comprehension

for i in range(n):
  a[i] = list(map(int, input().split()))
print(a) 
"""

#ANCHOR - Truy cập vào ptu
"""
- Để truy cập vào ptu trong mảng, ta dùng chỉ số hàng và chỉ số cột
- array[hàng][cột] or array[row][column]
"""

#ANCHOR - Số lớn nhất và nhỏ nhất
"""
n, m = map(int, input().split())
a = [[None for _ in range(m)] for _ in range(n)]

for i in range(n):
  a[i] = list(map(int, input().split()))

min = 10**9
max = -10**9
pos_min = (-1, -1)
pos_max = (-1, -1)

for i in range(n):
  for j in range(m):
    if a[i][j] < min:
      min = a[i][j]
      pos_min = (i + 1, j + 1)
    if a[i][j] > max:
      max = a[i][j]
      pos_max = (i + 1, j + 1)
print(min, end = "\n")
print(*pos_min)
print(max, end = "\n")
print(*pos_max)     #< unpack
"""

#ANCHOR - Flatten mảng 2 chiều thành 1 chiều
"""
a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]]
b = [x for small_list in a for x in small_list]     
print(min(b))
print(max(b))
print(b)
"""

#ANCHOR - Tính tổng từng hàng của ma trận
"""
a = [[1, 2, 5], [3, 1, 0], [4, 1, 5]]
sum_row = [sum(row) for row in a]
print(sum_row)
"""

#ANCHOR - Tạo ma trận chuyển vị
"""
#< Cách 1: 2 vòng for
n, m = map(int, input().split())
a = [[None for _ in range(m)] for _ in range(n)]

# Ma trận chuyển vị từ (n_hàng * m_cột) thành (n_cột * m_hàng)
a_t = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
  a[i] = list(map(int, input().split()))

for i in range(n):
  for j in range(m):
    a_t[j][i] = a[i][j]
print(a_t)

#< Cách 2: List comprehension
n, m = map(int, input().split())
a = [[None for _ in range(m)] for _ in range(n)]

a_t = [[row[i] for row in a] for i in range(len(a))]
print(a_t)

- len(a) = số hàng (ở đây là 3) -> tương ứng với cột của ma trận gốc
- len(a[0]) khi ma trận không vuông
- [row[i] for row in a]
  - Duyệt từng row trong ma trận a
  - Lấy ptu thứ i của mỗi hàng
"""

#ANCHOR - Các phép toán trên ma trận
"""
- Để 2 ma trận có thể cộng hoặc trừ cho nhau thì phải có cùng số hàng và số cột 
"""

#ANCHOR - Kỹ thuật duyệt các ô liền kề
"""
#< Duyệt 4 ô chung cạnh với ô (i,j)
a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

path = [[-1, 0], [0, -1], [0, 1], [1, 0]]       # các path này đã bao quát gần như toàn bộ matrix
i, j = 1, 1     # 5

for x in path: 
  i1, j1 = i + x[0], j + x[1]
  print(a[i1][j1], end = ' ')

#< Duyệt 8 ô xung quanh nước đi của quân mã
a = [
  [1, 2, 3, 4, 1],
  [5, 6, 7, 8, 0],
  [9, 3, 2, 6, 0],
  [1, 2, 1, 4, 4],
  [1, 2, 3, 5, 3]
]

path = [[-2, -1], [2, 1], [-1, -2], [1, 2], [1, -2], [-1, 2], [-2, 1], [2, -1]]
i, j = 2, 2

for x in path:
  i1, j1 = i + x[0], j + x[1]
  print(a[i1][j1], end = ' ')
"""
#!SECTION

#SECTION: EXERCISE

#ANCHOR - Count Island 1
"""
- Mỗi ô 1 là đất
- Các ô 1 liền kề (trên, dưới, trái, phải) -> cùng 1 đảo
- Mục tiêu: đếm số nhóm 1 liên thông
- Ý tưởng:
  + Duyệt từng ô trong ma trận
  + Nếu gặp 1 thì count += 1 và DFS lan ra biến toàn bộ vùng liên thông đó thành 0
  + Tiếp tục duyệt để tìm đảo tiếp theo
"""

"""
n, m = map(int, input().split())
a = [[None for _ in range(m)] for _ in range(n)]

def dfs(i, j):
  if i < 0 or i >= n or j < 0 or j >= m or a[i][j] == 0:
    return

  a[i][j] = 0     # đánh dấu đã thăm

  # Lan ra xung quanh ô mục tiêu
  dfs(i+1, j)
  dfs(i-1, j)
  dfs(i, j+1)
  dfs(i, j-1)

count = 0

for i in range(n):
  for j in range(m):
    if a[i][j] == 1:      # tìm ô 1 đầu tiên và từ đó DFS lan ra
      count += 1
      dfs(i, j)
print(count)
"""

#ANCHOR - Tổng hàng, tổng cột trên ma trận
"""
n, m = map(int, input().split())
a = [[None for _ in range(m)] for _ in range(n)]

for i in range(n):
  a[i] = list(map(int, input().split()))

for row in a:                   # khi duyệt bth trong ma trận 2 chiều thì luôn duyệt hàng
  print(sum(row), end = " ")

print()

for j in range(m):          # duyệt từng cột
  tong = 0
  for i in range(n):        # ở từng cột, duyệt hàng
    tong += a[i][j]
  print(tong, end = " ")
""" 

#ANCHOR - Số thuận nghịch trong tam giác dưới
""" 
def thuan_nghich(n):
  rev, tmp = 0, n
  while(n != 0):
    rev = rev * 10 + n % 10
    n //= 10
  return rev == tmp

n = int(input())
a = []

for i in range(n):
  row = list(map(int, input().split()))
  a.append(row)

ans = 0

#< Duyệt ma trận dưới
for i in range(n):
  for j in range(n):
    if j <= i and thuan_nghich(a[i][j]):
      ans += 1
print(ans)
""" 

#ANCHOR - In ra ma trận theo mẫu
""" 
n = int(input())
a = []
for i in range(n):
  row = list(map(int, input().split()))
  a.append(row)

print("Pattern 1: ")
for i in range(n):
  for j in range(n):
    print(a[j][i], end = " ")       # in trên cùng dòng, cách nhau dấu cách
  print()                           # cuối mỗi hàng -> xuống dòng

print("Pattern 2: ")
for i in range(n - 1, -1, -1):      # duyệt hàng
  for j in range(n - 1, -1, -1):    # duyệt cột
    print(a[i][j], end = " ")
  print()

print("Pattern 3: ")
for i in range(n - 1, -1, -1):      # duyệt cột
  for j in range(n):                # duyệt hàng
    print(a[j][i], end = " ")
  print()

print("Pattern 4: ")
for i in range(n):
  for j in range(n - 1, -1, -1):
    print(a[i][j], end = " ")
  print()
""" 

#ANCHOR - Hoán vị trên đường chéo
"""
n = int(input())
a = []
for i in range(n):
  b = list(map(int, input().split()))
  a.append(b)

for i in range(n):
  a[i][i], a[i][n - i - 1] = a[i][n - i - 1], a[i][i]

for row in a:
  for x in row:
    print(x, end = " ")
  print()
"""

#ANCHOR - Hoán vị 2 hàng của ma trận
"""
n = int(input())
a = []
for i in range(n):
  b = list(map(int, input().split()))
  a.append(b)

u, v = map(int, input().split())        # 2 hàng cần swap
u, v = u - 1, v - 1

for i in range(n):      # duyệt từng cột
  a[u][i], a[v][i] = a[v][i], a[u][i]

for row in a:
  for x in row:
    print(x, end = " ")
  print()
"""

#ANCHOR - Hoán vị 2 cột của ma trận
"""
n = int(input())
a = []
for i in range(n):
  b = list(map(int, input().split()))
  a.append(b)

u, v = map(int, input().split())
u, v = u - 1, v - 1

for i in range(n):        # duyệt từng hàng
  a[i][u], a[i][v] = a[i][v], a[i][u]

for row in a:
  for x in row:
    print(x, end = " ")
  print()
"""

#ANCHOR - Đếm các ptu là snt trên đường chéo chính và phụ
"""
import math

def check_snt(n):
  if n < 2:
    return False
  for i in range(2, math.isqrt(n) + 1):
    if (n % i == 0):
      return False
  return True

if __name__ == "__main__":
  n = int(input())
  a = []
  for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
  
  cnt = 0
  for i in range(n):
    if check_snt(a[i][i]):
      cnt += 1
    if check_snt(a[i][n - i - 1]):
      cnt += 1
  if n % 2 == 1 and check_snt(a[n // 2][n // 2]):       # giữa ma trận
    cnt -= 1
print(cnt)
"""

#ANCHOR - Đếm các ptu là snt trên đường chéo chính và phụ 2
"""
import math 

def check_snt(n):
  if n < 2: 
    return False
  for i in range(2, math.isqrt(n) + 1):
    if (n % i == 0): return False
  return n > 1

if __name__ == "__main__":
  n = int(input())
  a = []
  for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
  
  se = set()
  for i in range(n):
    if check_snt(a[i][i]):
      se.add(a[i][i])
    if check_snt(a[i][n - i - 1]):        # đường chéo phụ
      se.add(a[i][n - i - 1])
print(len(se))
"""

#ANCHOR - Sắp xếp các hàng của ma trận
"""
n = int(input())
a = []
for i in range(n):
  b = list(map(int, input().split()))
  b.sort()
  a.append(b)

for row in a:
  for x in row:
    print(x, end = " ")
  print()
"""

#ANCHOR - Nhân 2 ma trận
"""
def multiply_matrix(A, B):
  # Số cột A phải = số hàng B
  result = [[sum(A[i][k] * B[k][j] for k in range(len(B)))         
            for j in range(len(B[0]))]
            for i in range(len(A))]
  return result

#< matrix A có k cột, matrix B có k hàng 
#< len(B) là số hàng. B[0] = hàng đầu tiên -> len(B[0]) = số cột

A = [
  [1, 2],
  [3, 4]
]

B = [
  [5, 6],
  [7, 8]
]
print(multiply_matrix(A, B))
"""

#ANCHOR - Count Island 2
"""
#< Các ô số 1 được coi là cùng miền nếu chúng có chung đỉnh

path = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]     # path chung đỉnh

def dq(a, n, m, i, j):
  a[i][j] = 0
  for x in path:
    i1, j1 = i + x[0], j + x[1]
    if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and a[i1][j1] == 1:
      dq(a, n, m, i1, j1) 

n, m = map(int, input().split())
a = []
for i in range(n):
  b = list(map(int, input().split()))
  a.append(b)
ans = 0
for i in range(n):
  for j in range(m):
    if(a[i][j] == 1):
      ans += 1
      dq(a, n, m, i, j)
print(ans)
"""

#ANCHOR - Số điểm cực đại
"""
path = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]     # path chung đỉnh

n, m = map(int, input().split())
a = []
for i in range(n):
  b = list(map(int, input().split()))
  a.append(b)
ans = 0
for i in range(n):
  for j in range(m):
    check = True
    for x in path:
      i1, j1 = i + x[0], j + x[1]
      if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m:
        if a[i1][j1] >= a[i][j]:
          check = False
          break
      if check:
        ans += 1
print(ans)
"""



#!SECTION



