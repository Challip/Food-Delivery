#Program 1: Food Delivery Program    

#The purpose of the program is creat a food delivery app for local chinese resturant   

#Name:Prang Kongthongluck   

#Date:25/10/2019   

#Version:1.0   




#set up variable       


price=()

totalPrice=()


payMethod=()
orderPrice=[]

userOrder=[]


menu=[
{"1-Orange Chicken"},
{"2-Honey Sesame Chicken Breast"},
{"3-String Bean Chicken Breast"},
{"4-Beijing Beef"},
{"5-Shanghai Angus Steak"},
{"6-Honey Walnut Shrimp"},
{"7-Kung Pao Chicken"},
{"8-Eggplant Tofu"}]


#printMenu is menu wittout number. It will be ues to print out the order for customer       

printMenu=["Orange Chicken",
           "Honey Sesame Chicken Breast",
           "String Bean Chicken Breast",
           "Beijing Beef",
           "Shanghai Angus Steak",
           "Honey Walnut Shrimp",
           "Kung Pao Chicken",
           "Eggplant Tofu"]


sideMenu=[
    "1-Chow mein",
    "2-Fried rice",
    "3-White steam rice",
    "4-Brown Stem rice"
    ]

#printsideMenu is sidemenu wittout number. It will be ues to print out the order for customer       


printsideMenu=[
    "Chow mein",
    "Fried rice",
    "White steam rice",
    "Brown Stem rice"
    ]
userOrder=[]
#list locate inside for loop     

printOrder=[]


address=[]


orderStatus=()

costumerName=()

deliveryTime=()


userentreeChoice=()


entree=()

amount=()

entreelist=[]
sidelist=[]

#---------------------------------------------------------------------------------------------------      




print("welcome to Panda express food delivery app")

print("Today promotion: Free delivey  ")



#create a pickupDelivery function    

def pickupDelivery():

    #set some valiables as globle so it can be use outside their function   

    global customerName 

    global orderStatus 

    global deliveryTime 



    #ask customer what they prefer pick up or delivery   

    delivery=input("Please type 'P' for pick and 'D' for delivery: ")


    #change input from delivery to be uppercase      

    delivery=delivery.upper()   
    #ask for customer name   

    customerName=input("Costumer Name: ") 


    #make customerName begin with capital letter   

    customerName=customerName.capitalize()

    #when customer choose delivery option   

    if delivery== "D":
        orderStatus='Delivery'
    #loop to confirm deliver address 
        while True:
            houseNumber=input("Please enter you house number: ")

    # add houseNumber in to addres list   

            address.append(houseNumber)
            street=input("Please enter street: ")

    # add street in to addres list   

            address.append(street)

            postcode=input("Please enter postcode: ")
            # add postcode in to addres list   
            address.append(postcode)
            deliveryTimeAsk=input("Do you want your order to deliver in specific time? (Type Y for yes and N for no): ")#make input in deliveryTimeAsk to be uppercase   
            delivertTimeAsk=deliveryTimeAsk.upper()
            
            #if customer what their order to deliver in specific time    
            if (deliveryTimeAsk=="Y"):
                deliveryTime=input("What time do you want your order to be deliver")#if customer dont what their order to deliver in specific time. Their order will be delivered as soon as possible    

            else:
                deliveryTime="ASAP"
                print("Your order wil be deliver as soon as possible")
                #print out delivery details   

            
            print("Customer name:",costumerName)
            #print address list vertically      

            for a in (address):
                print (a)
            
            print("Delivery time: ",deliveryTime)
                
            #make customer to re checkt their delivery details   
            confirmAddress=input("Confirm Information (Type Y for yes and N for no):")
            #make input of confirmAddress alwasy uppercase      
            confirmAddress=confirmAddress.upper()

            #costumer dont confirm delivery details                    
            if confirmAddress=="N":
               
                #remove the data in the address list when constumer dont confirm the divery adress      
                address.remove(houseNumber)
                address.remove(street)


                address.remove(postcode)
                print("Your delivery address has been cancel")
                print("Please enter your delivery adress")
                    
                #customer confirm delivery details   

            elif confirmAddress=="Y":
                print("your delivery address is confirmed")
                break

            else:
                print("wrong input. Please try again")
            
                    
                    
              #customer choose to pick up order themselves   

            if  delivery=="P":
                orderStatus='Pick Up'
                print("Customer Name: ",customerName)
                print("Customer will pick up the order")
                

 #call pickupDelivery function   
pickupDelivery()



print(

        """        


    ------------------------------------        

    

          !Creat your own plate!        

    

     

    

     any 1 side + 2 entrees         £6     

    

    

     any 1 side + 3 entrees         £7        

    

     

     additional entrees         +   £1.25        

    

   ------------------------------------        

     

    

    """
)
 

#create order function   

def order():
    #set some valiables as globle so it can be use outside their function   
    global entree
    global amount
    #the purpose of this loop is to confirm order details   
    while True:
        amount=int(input("How many plate you want to order : "))
        #make a loop repeat respectively to amount of plate costumer choosed     

        for i in range(amount):
            #the purpose of this loop is to make sure number of entree costumer choose is between 2 and 5   
            while True:
                entree=int(input("How many entress you want(minimum 2 entrees and maximum 5 entress): "))
               
                #make sure number of entree costumer choose is between 2 and 5
                if (entree<=1) or (entree>=5):
                    
                    print("INCORRECT INPUT.Please try again")
                else:
                    break
                
            #this will help to calculate the price    
            if (entree==2):
                price=6
            if (entree==3):
                price=7
            if (entree==4):
                price=8.25
            if (entree==5):
                price=9.5
            
                
            #add price in orderPrice list   
            orderPrice.append(price)
            #display menu vertically     
            for i in (menu):
                print (i)
                
            #Purpose of this list is to display the order for costumer inside the loop so it can print each order seperatly        

            printOrder=[]
            
            #make a loop repeat respectively to number of entree costumer choose       
            for i in range(entree):
                
                #make sure user input right number od entree(1-8)  
                while True:
                  
                    entreeChoice=int(input("Please selet the entree: "))
                    if (entreeChoice<1) or (entreeChoice>8):
                       print("INVALID INOUT.Please choose number 1-8")

                    else:
                        break

               
                        
                #to print out the correct entree choice of costumer
                userentreeChoice=printMenu[entreeChoice-1]
                
                print(userentreeChoice)
                      
                
                #insert user's choice of entrees in userOrder list and entreelist       
                userOrder.append(userentreeChoice)
                entreelist.append(userentreeChoice)
            
            
            #use for loop to print side menu vertically
            for x in sideMenu:
                print (x)
            
            sideChoice=int(input("Please select your side: "))
            
            
            #to print out the correct side dish choice of costumer   
            userSideChoice=printsideMenu[sideChoice-1]
            print(userSideChoice)
            #insert user's choice of side dish to userOrder list and sidelist     
            userOrder.append(userSideChoice)
            sidelist.append(userSideChoice)
            
            #print out customer choice
            
            def OrderRecipe(choiceE,choiceS):
                print("Your order is",choiceE,"with",choiceS)
             
            #call function
            OrderRecipe(entreelist,sidelist)
            
            #customer order morethen 1 plate 
            
            #data in printOrder list will be deleted so that program able to print out each plate choic individually   

            if (amount>=2):
                entreelist.remove(userentreeChoice)
                sidelist.remove(userSideChoice)
        
                
        #display order details for customer to confirm
        print("number of plate: ",amount)
        print("Order(s): ")
                
        #print order details vertically   
        for i in (userOrder):
            print (i)
                
            
        confirmOrder=input("Confirm order (Type Y for yes and N for no): ")
        confirmOrder.upper()
        
        #allow customer to confirm their order
        if (confirmOrder=="N"):
            print("Order has been cancel")
            print("Please order again")
            
        else:
            print("Order is confirmed")
            break


#call order function   
order()





#create payment function    
def payment():
    #set some valiables as globle so it can be use outside their function   
    global totalPrice
    global payMethod

    #total price is sum of number in orderPrice list   

    totalPrice=sum(orderPrice)
    print("Total price: ",totalPrice,"£")
    
    #inform customer discount code   
    print("Today 15% discount code is:  happypanda")
    
    #make a loop TRUE   
    reenter="Y"
    #the purpose of this loop is to make sure customer enter the correct discount code   

    while (reenter=="Y"):
        discount=input("Please insert discount code: ")
        
        #make input from discount always be in lower case   
        discount=discount.lower()
        
        if (discount == "happypanda"):
            #totelprice reduce by 15%   
            totalPrice=totalPrice-(0.15*totalPrice)
            print("Congraturation you get 15% discount")
            print("Total price with discount: ",totalPrice,"£")
            break
        
        else:
            print("Incorret discount code")
            
            
        #ask customer do they want to re-enter the code         
        reenter=input("Do you want to re-enter discount code (Type Y for yes and N for no): ")
        reenter=reenter.upper()
        
        if (reenter == "N"):
            break
        
        else:
            print("Incorrect input") 

    #Ask customer how they would like to pay   

    payMethod=input("How you world like to pay(CASH/CARD): ")
    payMethod=payMethod.upper()
    
    #check whether customer select the collect payMethod   

    while True:
        if (payMethod=="CASH") or (payMethod=="CARD"):
            break
        else:
            print("Incorrect in out. Please select payment method")



#call payment function   
payment()








#create receipt function   

#allow customer to see all details(delivery,order and payment)   

def receipt():

    print ("Customer Name: ",customerName)
    print("Order Status: ",orderStatus)

    if (orderStatus=="Delivery"):
        print("Delivery address: ")
        
        for i in address:
            print (i) 
    
        print("Delivery Time: ",deliveryTime)

    print("Amount of Plate: ",amount)
    print("Order(s): ")
    
    for i in userOrder:
        print(i)

    print("Total price: ",totalPrice,"£")
    print("Pay by: ",payMethod)


#call receipt function   

receipt()

 