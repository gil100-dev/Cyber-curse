import threading

count = 0
def Thread_Add():
    global count
    for i in range(100000):
        count += 1

def Thread_Subtract():
    global count
    for i in range(100000):
        count -= 1  

t1 = threading.Thread(target=Thread_Add)
t2 = threading.Thread(target=Thread_Subtract)

t1.start()
t2.start()
t1.join()
t2.join()


print("Final count:", count)