#write a python program using a while loop to find the sum of first n natural numbers
num=int(input("enter the number"))
if num<0:
  print("enter the number")
else:
  sum_numbers=0
  counter=1
  while counter<=num:
    sum_numbers+=counter
    counter+=1
print("sum of first",num,"natural numbers is",sum_numbers)
