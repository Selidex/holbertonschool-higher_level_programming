#!/usr/bin/python3
""" Test function find_peak """

def find_peak(list_of_integers):
   loi = list_of_integers
   if loi is None or len(loi) == 0:
      return None
   start = 0
   end = len(loi) - 1
   while start < end:
      mid = start + (end - start) // 2
      if loi[mid] > loi[mid - 1] and loi[mid] > loi[mid + 1]:
         return loi[mid]
      if loi[mid - 1] > loi[mid + 1]:
         end = mid
      else:
         start = mid + 1
   return loi[start]
