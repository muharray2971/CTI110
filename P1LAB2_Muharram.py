"""
CTI110
P1LAB2 - sales
Muharram
8/31
Simple point of sales program 

"""
# set up our store 
Store_name = "Joe unlimted shoes "
Product = "Shoes"
Stock = 20
Price = 49.99

# greet customer
print("welcome to",Store_name,".")
print("what's tour name ?")
customer_name = input()
print("Nice to meet you,", customer_name)

# Explain product
print("our special today is:", Product)
print() # blank line 
print("on sale for: $", Price)
print("only", Stock,"left!")

# take order
print("how many",Product, " would you like?")
# input gives us a string 
#order = input()
# convert it to a number
#order = float(order)

# or ....
order = int(input())

# Finish up 
# opitional
if (order > Stock):
  order = Stock
  print("sorry, we cam only sell you", order)


total_price = order * Price
print("so you would like")
print(order,Product,"for a total of $", total_price)
print("<y/n",sep="")
confirm = input ()
if (confirm == "y"):
  print("Shipped!")
else:
  print("order canceled.")
print("Thank for shopping with", Store_name,"!")