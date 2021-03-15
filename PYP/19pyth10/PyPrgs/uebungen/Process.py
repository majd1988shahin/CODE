def is_prime(x):
    return [div for div in range(2,x) if x%div==0]==[]
def prime_gen():
    yield 2
    p=3
    while True:
        if is_prime(p): yield p
        p+=2

def ithPrime_mp(i,results):
    pg=prime_gen()
    for _ in range(i-1):
        next(pg)
    results.put((i,next(pg)))

from multiprocessing import Process, Queue

results=Queue()
ipJobs=[]
for i in range(1700,1702):
    job=Process(target=ithPrime_mp,args=(i,results))
    ipJobs.append(job)

for job in ipJobs:job.start()
for job in ipJobs:job.join()

for _ in range(len(ipJobs)):
    i,p=results.get()
    print("%dth prime :%d"%(i,p))

###https://docs.python.org/3/library/multiprocessing.html
