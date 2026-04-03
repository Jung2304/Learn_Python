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
  - Duyệt từng ô trong ma trận
  - Nếu gặp 1 thì count += 1 và DFS lan ra biến toàn bộ vùng liên thông đó thành 0
  - Tiếp tục duyệt để tìm đảo tiếp theo
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




#!SECTION



