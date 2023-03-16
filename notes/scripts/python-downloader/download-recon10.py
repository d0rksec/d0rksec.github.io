#!/usr/bin/python3
import sre_yield
for each in sre_yield.AllStrings(r'0x[a-f0-9][a-f0-9]\.a\.hackycorp\.com'):
  os.system("wget " + each + "/logo.png")