# from lib.diary import *
import sys, os
import entry

# class Contact:
#     def __init__(self,name,number):
#         if type(name) == str and len(name) >= 3:
#             self.name = name
#         else:
#             raise Exception('Invalid input, name must be string and minimum 3 letters long')
    
#         if type(number) == str and len(number) == 11:
#             self.number = number
#         else:
#             raise Exception('Invalid input, number must be string and 11 letters long')
        
#     def set_number(self,num):
#         if type(num) == str and len(num) == 11:
#             self.number = num
#         else:
#             raise('Invalid input, number must be string and 11 letters long')
    
#     def format(self):
#         string =  f'{self.name} : {self.number}'
#         return string

entry1 = entry.Entry('Walk the dog')

print(entry1.text)
for i in sys.path:
    print(i)