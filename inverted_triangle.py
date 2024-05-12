# PRINT AN INVERTED TRIANGLE
# N represents the height
# N > 0
'''
XXXX
XXX
XX
X
'''
def triangle(n: int):
    for i in range(n,0,-1):
        print("X"*i)

triangle(4)
print()
triangle(5)



