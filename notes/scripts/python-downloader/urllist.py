#!/usr/bin/python3
import sre_yield
df=open('urls.txt','w')
for each in sre_yield.AllStrings(r'https://0x[a-z0-9][a-z0-9]\.a\.hackycorp\.com'):
  df.write(str(each))
  df.write('\n')
df.close()