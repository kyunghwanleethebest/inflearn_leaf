# Meta Class -> Class Customizing / 동적함수 생성, 커스텀 생성

class Parent1:
    pass


test = type('myclass', (Parent1,),
dict(attr_1 = 12, attr_2 = 'abc', subtract=lambda x,y: x-y))

print(test)
print(test.__base__)
print(test.__dict__)
print(test.attr_1)
print(test.attr_2)
print(test.subtract(12, 2))



# Custom Class

def acc_add(self):
    for i in range(1, len(self)):
        self[i] = self[i] + self[i-1]




class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print('__init__ -> ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print('__call__ -> ', self, args, kwargs)
        
        return super().__call__(*args, **kwargs)

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(metacls, name, bases, namespace):
        print('__new__ -> ', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 클래스'
        namespace['acc_add'] = acc_add
        # namespace['cus_replace'] = cus_replace
        return type.__new__(metacls, name, bases, namespace)


test2 = CustomListMeta(
'test2',
(list, ),
{}
)
t2 =test2([1, 2, 3, 4, 5])
t2.acc_add()

print(t2)
print(t2.desc)


