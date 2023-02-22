n=int(input)
if n==0:
    print("Time Estimated:0 minutes")
elif n in range(1,2001):
    print("Time Estimated:25 minutes")
elif n in range(2001,4001):
    print("Time Estimated:35 miunutes")
elif n in range(4001,7001):
    print("Time Estimated:45 minutes")
else:
