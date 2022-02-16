binary = []
denary = int(input("Denary Number up to 256: "))

for i in range(0,8):
  if denary % 2 == 0:
    binary.append(0)
  else:
    binary.append(1)
  denary = denary // 2

binary.reverse()  
for i in binary:
  print(i, end=" ")
