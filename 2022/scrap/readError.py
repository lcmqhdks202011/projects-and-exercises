# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1un2qiFXQBeB_e6bHjslLCvct5LpHBkb8
"""

fichier = open("errors.txt", 'r')

lines = fichier.readlines()
dic = {}

for line in lines:
  a = line.split(" | ")
  error = a[0]
  name = a[1][:-1]
  
  if dic.get(a[0]) is None:
    se = set()
    se.add(name)
    dic[error] = se

  else:
    se = dic.get(error)
    se.add(name)
  


for error in dic:
  print(error)
  files = " Files : "
  for htmls in dic.get(error):
    files += htmls + " "

  print(files)