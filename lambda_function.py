#REVIEW - LAMBDA FUNCTION (LAMBDA OPERATOR) (BUỔI 8)

#SECTION - LAMBDA FUNCTION
"""
- Lambda là một trong những tính năng cực kì mạnh mẽ, quan trọng và thú vị của ngôn ngữ lập trình Python
- Lambda là một cách đơn giản để định nghĩa một hàm trong Python. Lambda thường được gọi dưới cái tên toán tử lambda (lambda operator) hoặc hàm lambda (lambda function)
- Lambda là một cách để định nghĩa hàm vô danh (anonymous), một hàm mà không cần tên hàm. 
! Nó được sử dụng khi bạn cần xây dựng những hàm chỉ bao gồm 1 câu lệnh, khi đó việc sử dụng keyword def để định nghĩa hàm là quá thừa thãi và dài dòng
#> Cú pháp: lambda parameters : expression 

#< Demo: Bình phương tất cả số trong list
cal = lambda x : x**2
n = 10
a = [cal(x) for x in range(n)]
print(a)

#< Demo: Nhân 3 số lại với nhau
print((lambda x, y, z: x * y * z)(100, 200, 300))
"""

#NOTE - Các tính chất của Lambda
"""
- Lambda không thể chứa các câu lệnh: Ví dụ như return, assest, pass,...
- Lambda chỉ chứa 1 biểu thức duy nhất
- IIFE: Immediately Invoked Function Expression: Biểu thức lambda có thể được gọi ngay lập tức
"""

#ANCHOR - Lambda và Map
"""
import math
n = 10
a = map(lambda x : math.sqrt(x), range(n))
print(list(a))
"""

#ANCHOR - Lambda và Filter
"""
n = 10
a = filter(lambda x : x % 2 == 1, range(n))
print(list(a))
"""

#ANCHOR - Lambda và IF-ELSE
"""
findMax = lambda x, y : x if x > y else y (nearly like ternary operator)
print(findMax(200,300))
"""
#!SECTION