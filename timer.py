import time
Mytime = int(input("enter the time in seconds"))
for x in range(Mytime,0,-1):
    hour=int(x/3600)
    minutes = int((x%3600)/60)
    seconds= x%60
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("time's up")