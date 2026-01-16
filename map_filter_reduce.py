#REVIEW - MAP, FLITER, REDUCE (BUỔI 8)

#SECTION - MAP
"""
#! Map là một hàm trong Python có chức năng apply một hàm có sẵn cho mọi ptu trong 1 iterable (list, tuple, string,...)
# Cú pháp: map(function, iterable...)
> Function: Hàm sẽ được sử dụng để apply với các ptu trong iterable
> Iterable: Các iterable vd: list, tuple, string,...
> Gtri trả về: map trả về một đối tượng thuộc lớp map. Nên ép sang list để sử dụng

#< Demo: User's input
a = list(map(int, input().split()))
> input().split(): thực ra là một iterable, một xâu được tách ra thì tạo một list chứa các từ đấy
> int: hàm được apply lên từng ptu trong iterable đó
"""

#ANCHOR - Apply một hàm từ định nghĩa
"""
def add100(n):
    return n + 100
if __name__ == '__main__':
    a = range(5)        # range is also iterable
    b = list(map(add100, a))
    print(b)
"""
    
#ANCHOR - Apply một hàm built-in (ord)
"""
#! In Python, ord() is a built-in function that returns the Unicode code point (an integer) of a single character.
if __name__ == '__main__':
    str = '28tech'
    a = list(map(ord, str))
    print(a)
"""

#ANCHOR - Apply một hàm built-in (chr)
"""
#! In Python, chr() is a built-in function that help goes from number → character
if __name__ == '__main__':
    a = [97, 98, 99, 100, 101, 102]
    b = list(map(chr, a))
    print(b)
"""

#ANCHOR - Áp dụng map với nhiều iterable
"""
#< Demo: cộng 2 list lại với nhau 
def adding(a, b):
    return a + b
    
if __name__ == '__main__':
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = list(map(adding, a, b))
    print(c) 
"""
#!SECTION

#SECTION - FILTER
"""
#! Filter được sử dụng để trích xuất các ptu trong một iterable khi apply một hàm nào đó với ptu đó mà hàm trả về gtri là True
# Cú pháp: filter(function, iterable)
> Function: Hàm sẽ được sử dụng để apply với các ptu trong iterable
> Iterable: Các iterable ví dụ như list, tuple, string, range,...
> Gtri trả về: filter trả về một đối tượng của lớp filter, nên ÉP sang list hoặc tuple
-> Không như map là áp dụng và trả về với mọi ptu; filter áp dụng với từng ptu trong iterable, ptu nào đúng mới trả về  

#< Demo: 
def even(n):
    return n % 2 == 0

if __name__ == '__main__':
    n = 10
    #> List comprehension
    a = [x for x in range(n) if x % 2 == 0]
    print(a)
    #> Fiter
    b = list(filter(even, range(n)))
    print(b)
"""

#ANCHOR - Lọc ra các snt trong list

import math
def checkPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = 50
    a = list(filter(checkPrime, range(n)))
    print(a)




#!SECTION