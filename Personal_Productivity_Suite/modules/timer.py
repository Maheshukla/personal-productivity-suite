import time

def timer():
    seconds = int(input("Enter seconds: "))

    while seconds > 0:
        print("Time left:", seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's up")