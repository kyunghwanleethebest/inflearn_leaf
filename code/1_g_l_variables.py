# Scope, Global, Nonlocal, Locals, Globals

# Global / Local
a = 10
def test():
    # global a를 선언하면 달라 위에 a가 20으로 변함!
    a= 20
    print('local a {}'.format(a))

print('global a {}'.format(a))

test()

# Nonlocal
def nl_test(): # Closure 형태
    k = 7
    def nl_test_in():
        nonlocal k
        k +=11
        print(k) # 18이 나오겠죠
    return nl_test_in

nl_test() # nl_test()안에 있는 함수가 실행이 안됨! 신기
temp = nl_test()
temp()

# Locals

def lo_test():
    x = 1
    y = 2
    def lo_test_in():
        z=3
        n = 4
    print('local variable {}'.format(locals())) 

lo_test()


# Globals
a =1 
b = 2
c = 3
d = 4
for j in range(10):
    globals()['test_{}'.format(j)]=j

print('global variable {}'.format(globals()))