# Use Contextlib Decorator
import contextlib
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


@contextlib.contextmanager
def filewriter(file_name, method):
    f = open(file_name, method) 
    yield f # similar as __enter__
    f.close() # similar as __exit

with filewriter('test_2nd_week.txt', 'w') as f:
    f.write('2nd week contextmanager Decorater Test!')

