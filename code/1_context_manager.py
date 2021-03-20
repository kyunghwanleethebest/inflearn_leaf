# with 구문 - 리소스 관리 차원에서 중요

with open('test.txt', 'w') as f:
    f.write('This is test')


# Context Manager & Time Checker
import time
class file_writer_with_time():
    def __init__(self, file_name, method, msg):
        print('This is __init__')
        self.file_obj = open(file_name, method)
        # self._msg = msg
        
    def __enter__(self):
        self._start = time.monotonic()
        print('This is  __enter__')
        return self.file_obj, self._start

    def __exit__(self, exc_type, value, trace_back):
        print('This is  __exit__')
        if exc_type:
            print("Type of exception {}".format((exc_type, value, trace_back)))
        else:
            print('{}: {} s'.format(self._msg, time.monotonic() - self._start))
        
        self.file_obj.close()
        return True
        

with file_writer_with_time('test2.txt', 'w', 'Check Time') as v:
    print('start monotonic : {}'.format(v))
    # Excute job.
    for i in range(1000):
        pass
    v.write('Use Context Manager So good')


