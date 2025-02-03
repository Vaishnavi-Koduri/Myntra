#def print_items(n):
 #   for i in range(n):
  #      for j in range(n):
   #         print(i,j)
#print_items(10)

##CLASSES
#class Cookie:
 #   def __init__(self, color):
  #      self.color=color
   # def get_color(self):
    #   return self.color
    #def set_color(self, color):
     #   self.color=color
#cookie_1=Cookie("Blue")
#cookie_2=Cookie("Green")
#print("Cookie one is",cookie_1.get_color())
#print("Cookie two is",cookie_2.get_color())

#cookie_1.set_color('Yellow')

#print("Cookie one is now ",cookie_1.get_color())
#print("Cookie two is still",cookie_2.get_color())

##POINTERS
##Q1
#num1=11
#num2=num1
#print("Num2 before update:")
#print("num1=",num1)
#print("num2=",num2)
#print("num1 points to:",id(num1))
#print("num2 points to:",id(num2))
#num2=22
#print("Num2 after update:")
#print("num1=",num1)
#print("num2=",num2)
#print("num1 points to:",id(num1))
#print("num2 points to:",id(num2))

##Q2
dict1={'value':11}
dict2=dict1
print("dict2 before update:")
print("dict1=",dict1)
print("dict2=",dict2)
print("dict1 points to:",id(dict1))
print("dict2 points to:",id(dict2))
dict2={'value':22}
print("dict2 after update:")
print("dict1=",dict1)
print("dict2=",dict2)
print("dict1 points to:",id(dict1))
print("dict2 points to:",id(dict2))
