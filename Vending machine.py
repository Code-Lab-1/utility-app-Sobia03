# Creating a categorized menu of drinks and snacks for efficient user experience. 
# Assigning Item Number to each product so the user can easily input a number to buy a specific product.
print("Welcome! What woukd you like to have today?")
print("\n      -----     Hot Foods     -----     ")
print("\nProduct        Price     Stock     Item No")
print("\nFrench fries    5Dhs      20         1")
print("\nDumplings       7Dhs      17         2")
print("\nPizza slice     6Dhs      15         3")
print("\nCheese Burger   9Dhs      10         4")

print("\n      -----     Beverages     -----     ")
print("\nProduct        Price     Stock     Item No")
print("\nOrange Juice    4Dhs       9        5 5")
print("\n7Up             2Dhs       7         6")
print("\nPepsi           2Dhs      10         7")
print("\nApple Juice     3Dhs       5         8")

print("\n      -----     Coffee     -----     ")
print("\nProduct        Price     Stock     Item No")
print("\nAmericano       2Dhs      12          9")
print("\nIced Latte      3Dhs      11         10")
print("\nMilk Tea        2Dhs       6         11")

print("\n     -----     Bakery Goods     -----    ")
print("\nProduct             Price     Stock     Item No")
print("\nButter Croissant     3Dhs      13         12")
print("\nPlain Bagel          2Dhs       8         13")
print("\nGlazed Donut         4Dhs       4         14")
print("\nCheesecake           6Dhs       7         15")

# Making 2 methods of payment of available. The user can easily pay through cash or card.
# Making the change function available so that the user can enter any amount of money and have the correct change returned.
# Displaying a message that informs the user their product has been dispensed. 
def vending(Name,Price,User_Payment):

 print("\nYou selected " + Name+ ". "+ "How would you like to pay for your purchase?")
 reply= int(input("By 1. Cash  2. Card "))
 if reply== 1:
   print("Please enter "+ str(Price)+ "Dhs.")
   User_Payment=float(input())
   if User_Payment==Price:
     print("Perfect! Here is your "+ Name+ ".")
   elif User_Payment<Price:
     Expected_amount=Price-User_Payment
     Reply= float(input("The amount you have entered is not enough. You have to enter "+ str(Expected_amount)+ "Dhs more." ))
     print(Reply)
     if Reply==Expected_amount:
      print("Perfect! Here is your "+ Name+ ".")
     elif Reply>Expected_amount:
       Money=Reply-Expected_amount
       print("Perfect! Here is your "+ Name+ "."+ "Your change will be "+ str(Money)+"Dhs.")
     elif Reply<Expected_amount:
       Number=Expected_amount-Reply
       Repeat= float(input("The amount you have entered is not enough. Please enter "+ str(Number)+ "Dhs more."))
       if Repeat==Number:
        print("Perfect! Here is your "+ Name+ ".")
   else:
        Remaining_Money= User_Payment - Price
        print("There you go! Here is your " + Name + ". Your change will be "+ str(Remaining_Money)+"Dhs.")    
 elif reply== 2:
   int(input("Insert your card and enter your card pin code: "))
   print("\nAuthorization may take a few seconds...Please wait...")
   print("..................")
   print("\nYour transaction was completed. Please remove your card. Here is your "+ Name+ ". "+ "Enjoy!")
 else:
     Change= User_Payment-Price
     print("Perfect! Here is your "+ Name+ "."+ "Your change will be "+ str(Change)+ ".")


# Entering the code of the item that the user wants to buy.
# Using functions to improve program structure.
def Main_function():
  Item_Code= float(input("\nPlease enter the code of the item you want to purchase."))
  if Item_Code== 1:
    vending('French Fries',5,'User_Payment')
    Other_purchase('French Fries','7Up',2)
  elif Item_Code== 2:
    vending('Dumplings',7,'User_Payment')
    Other_purchase('Dumplings','Apple Juice',3)
  elif Item_Code== 3:
    vending('Pizza slice',6,'User_Payment')
    Other_purchase('Pizza slice','Pepsi',2)
  elif Item_Code== 4:
    vending('Cheese Burger',9,'User_Payment')
    Other_purchase('Cheese Burger','Pepsi',2)
  elif Item_Code== 9:
    vending('Americano',2,'User_Payment')
    Other_purchase('Americano','Glazed Donut',4)
  elif Item_Code== 10:
    vending('Iced Latte',3,'User_Payment')
    Other_purchase('Iced Latte','Butter Croissant',3)
  elif Item_Code== 11:
    vending('Milk Tea',2,'User_Payment')
    Other_purchase('Milk Tea','Plain Bagel',2)
  elif Item_Code== 5:
    vending('Orange Juice',4,'User_Payment')
    Other_purchase('Orange Juice','Dumplings',7)
  elif Item_Code== 6: 
    vending('7Up',2,'User_Payment')
    Other_purchase('7Up','French Fries',5)
  elif Item_Code== 7:
    vending('Pepsi',2,'User_Payment')
    Other_purchase('Pepsi','Cheese Burger',9)
  elif Item_Code== 8:
    vending('Apple Juice',3,'User_Payment')
    Other_purchase('Apple Juice','Dumplings',7)
  elif Item_Code== 12:
    vending('Butter Croissant',3,'User_Payment')
    Other_purchase('Butter Croissant','Iced Latte',3)
  elif Item_Code== 13:
    vending('Plain Bagel',2,'User_Payment')
    Other_purchase('Plain Bagel','Milk Tea',2)
  elif Item_Code== 14:
    vending('Glazed Donut',4,'User_Payment')
    Other_purchase('Glazed Donut','Americano',2)
  elif Item_Code== 15:
    vending('Cheesecake',6,'User_Payment')
    Other_purchase('Cheesecake','Americano',2)
  else:
    print("Invalid code.")
    Main_function()
  Ask_again()

# Using intelligence system to suggest other items the user can buy.
# Creating the Yes or No option so that the user can agree or disagree.
def Other_purchase(Name,Recommendation,Price):
  print("\n"+ Recommendation+ " goes well with "+ Name+ "."+ " Would you like to purchase that as well? Enter Yes or No.")
  Response=input()
  if Response== 'Yes' or Response=='yes':
   print("Great choice!")
   vending(Recommendation,Price,'User_Payment')
  elif Response== 'No' or Response=='no':
    print("Alright")
  else:
    print("Invalid Response")
    input("Please enter Yes or No only:")
    if Response== 'Yes' or Response=='yes':
      print("Perfect! You bought "+ Recommendation+ ".")
      vending(Recommendation,Price,'User_Payment') 
    elif Response== 'No' or Response=='no':
      print("Alright")  

# Function that asks users if they want to purchase anything else. If user enters Yes, the Main_function function runs again. 
# If the user enters No, the function won't run again and stops.
def Ask_again():
  print("Would you like to purchase something else?")
  User_choice= input("Type Yes or No:")
  if User_choice== 'Yes' or User_choice=='yes':
   Main_function()
  elif User_choice== 'No' or User_choice=='no':
   print("\nThank you for purchasing from us! Enjoy your food!")

# Calling the main funtion 
Main_function()