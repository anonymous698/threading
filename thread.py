import threading
import time

def wake_up(name):
    time.sleep(7)
    print(name, "Hey wake up")

def brush_your_teeth(someone):
    time.sleep(4)
    print(someone, "brushed the teeth")

def go_to_school(any):
    time.sleep(6)
    print(any, "Went to school")

def main():
    name=str(input("enter a name: "))
    someone=str(input("enter someone: "))
    any=str(input("enter anything: "))

    work1 = threading.Thread(target=wake_up , args=(name ,) )
    work1.start()

    work2=threading.Thread(target=brush_your_teeth , args=(someone ,))
    work2.start()

    work3=threading.Thread(target=go_to_school ,args=(any,) )
    work3.start()

    work1.join()
    work2.join()
    work3.join()
        
    time.sleep(2)
    print("all work completed")

if __name__=="__main__":
    main()
  

