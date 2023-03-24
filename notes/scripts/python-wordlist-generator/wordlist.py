#!/usr/bin/python3
df=open('numbers.txt','w')
for i in range(0,1000):
  df.write(str(i))
  df.write('\n')
df.close()