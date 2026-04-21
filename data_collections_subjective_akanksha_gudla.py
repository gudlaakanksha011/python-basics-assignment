# -*- coding: utf-8 -*-
"""Data_Collections_Subjective.ipynb


Original file is located at
    https://colab.research.google.com/drive/1nxcsH65yAC44-Zul11JugmMVo1spl5fX

Task 1 Write a for loop that prints all numbers from 1 to 5 using range().
"""

for i in range(1,6):
  print(i)

"""Task 2 Write a for loop that prints only odd numbers between 1 and 10 using the step parameter in range()."""

for i in range(1,11,2):
  print(i)

"""Task 3 Write a nested for loop that prints the following pattern:

0 0
0 1
1 0
1 1
2 0
2 1
"""

for i in range(3):
  for j in range(2):
    print(i,j)

"""Task 4 Write a for loop that prints numbers from 1 to 7. If the number is 5, stop the loop immediately using break."""

for i in range (1,8):
  if(i==5):
    break
  print(i)
