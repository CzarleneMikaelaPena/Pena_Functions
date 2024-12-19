food_items = ['Fried Chicken' , 'Fries' , 'Burger' , 'Mac and Cheese' , 'Lasagna' , 'Sundae']
food_prices = [82 , 50 , 69, 250, 300, 65]
order_list=[]
order_price=[]
def welcome():
    print("Welcome to Jam's Cafe")
    print("Choose 1 to see the menu")
    print("Choose 2 to exit")
      
def menu():
    print (food_items[0] , " . . . . . . . . . . . . . . . . ." , food_prices[0])
    print (food_items[1] , " . . . . . . . . . . . . . . . . . . . . ." , food_prices[1])
    print (food_items[2] , " . . . . . . . . . . . . . . . . . . . . " , food_prices[2])
    print (food_items[3] , " . . . . . . . . . . . . . . . . " , food_prices[3])
    print (food_items[4] , " . . . . . . . . . . . . . . . . . . . ." , food_prices[4])
    print (food_items[5] , " . . . . . . . . . . . . . . . . . . . . " , food_prices[5])

def food_choice():
    print("1) Fried Chicken \n 2) Fries \n 3) Burger \n 4) Mac and Cheese \n 5) Lasagna \n 6) Sundae \n 7) Exit")
    while True:
        choice = int(input("Enter your order:"))
        if choice == 1:
            order_list.append(food_items[0])
            order_price.append(food_prices[0])
        elif choice == 2:
            order_list.append(food_items[1])
            order_price.append(food_prices[1])
        elif choice == 3:
            order_list.append(food_items[2])
            order_price.append(food_prices[2])
        elif choice == 4:
            order_list.append(food_items[3])
            order_price.append(food_prices[3])
        elif choice == 5:
            order_list.append(food_items[4])
            order_price.append(food_prices[4])
        elif choice == 6:
            order_list.append(food_items[5])
            order_price.append(food_prices[5])
        elif choice== 7:
            print("Order system exited")
            print("Your order is:\n" , order_list)
            break
        else:
            print("Invalid Input")
            break

def computation():
    total = sum(order_price)
    print("Your total price is:" , total)
    payments = int(input("Would you like to pay?\n1)Proceed\n2)Exit"))
    if payments == 1:
        while True:
            payment = int(input("Enter the payment amount:\n"))
            if payment>total:
                change= payment-total
                print("Your change is:", change)
                break
            else:
                print("Insufficient Amount")
                pay = int(input("Continue payment? \n 1) Yes \n 2) Exit \n"))
                if pay == 1:
                    continue
                if pay == 2:
                    print ("Payment exited")
                    break
                else:
                    print("invalid input")
                    break

    elif payments==2:
        print("Payment exited")
    else:
        print("invalid input")

welcome()
choice = int(input("Your Choice:"))
if choice==1:
    menu()
    food_choice()
    computation()
elif choice==2:
    print("Goodbye!")
else:
    print("Invalid Choice")