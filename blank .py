import threading
import time

def saluta():
    for i in range(5):
        print("Ciao!")
        time.sleep(1)

def conta():
    for i in range(5):
        print(i)
        time.sleep(1)

# Avvio i thread
t1 = threading.Thread(target=saluta)
t2 = threading.Thread(target=conta)

t1.start()
t2.start()

# Aspetto che finiscano
t1.join()
t2.join()

print("Fatto!")
