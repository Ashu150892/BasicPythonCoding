list = [1,2,3,4,5]
for i in list:
    if i==3:
        break
        print(i)
print("Break list")
for i in range(5):
    if i==3:
        break
        print(i)
print("Break")
for i in range(5):
    if i==3:
        continue
        print(i)
print("Continue")
for i in range(5):
    if i==3:
        pass
        print(i)
print("Pass")