from multiprocessing import Process
import os,time

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('A',))
    p.start()
    time.sleep(0.1)
    p2 = Process(target=f, args=('B',))
    p2.start()
    time.sleep(1)
    p2.join()
    p.join()