# -*- coding: utf-8 -*-
"""Family Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kCLgN2b5sFctNaCScxk6plimloiaLs2V
"""

from collections import defaultdict
class Solution:

   def __init__(self, head_name):
      self.family = defaultdict(list)
      self.head = head_name
      self.dead = set()

   def birth(self, p_name, c_name):
      self.family[p_name].append(c_name)

   def death(self, name):
      self.dead.add(name)

   def inheritance(self):
      self.ans = []
      self.depth_search(self.head)
      return self.ans

   def depth_search(self, current):
      if current not in self.dead:
         self.ans.append(current)
      for child in self.family[current]:
         self.depth_search(child)

ob = Solution('Ramesh')
ob.birth('Ramesh', 'suresh')
ob.birth('Ramesh', 'veeresh')
ob.birth('veeresh', 'naresh')
ob.birth('veeresh', 'sireesh')
ob.birth('veeresh', 'maneesh')
ob.death('Ramesh')
print(ob.inheritance())
ob.death('maneesh')
print(ob.inheritance())