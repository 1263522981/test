  from random import random
  from math import sqrt
  from time import clock
  DARTS=1200              #抛洒点数
  hits=0                  #落在目标1/4圆域内的点数
  clock()                 #计时函数
  for i in range (1,DARTS):
      x,y = random(),random()
      dist = sqrt(x**2 + y**2)
     if dist <=1.0:      #表示点落在1/4圆域内
         hits=hits+1
 pi = 4 * (hits/DARTS)
 print("Pi的值是%s" %pi)
 print("程序运行时间是%-5.5ss"%clock())
