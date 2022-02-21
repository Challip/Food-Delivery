
name=()
age=()
weight=()

mets=()
activities=[]
energy=()
energylist=[]

def user():
  global weight
  global name
  global age
  #The porpuse of this loop is to allow user to confirm their datails
  while True:
    
      name=input("Please enter your name: ")
      #make user naem start with alphabet
      name=name.capitalize()
      age=input("Please enter your age: ")
      weight=int(input("Please wnter your weight: "))

      #purpose of this loop is to make sure user input collect input ti weightUnit
      while True:
          weightUnit=input("Please choose unite of your weight you entered (P=pound/KG): ")
          weightUnit= weightUnit.upper()
    
          #convert weight from pounds in kh when user input weight in pounds)
          if (weightUnit=="P"):
              weight=weight*0.45
              print("your weight in kg: ",weight)
              break
          elif (weightUnit=="KG"):

              break
          else:
              print("Invalid input.PLease try again")
  
      print ("Costumer name: ",name)
      print("Costumer age: ",age,"years")
      print ("Costumer weight: ",weight,"kg")

      confirmDetails=input("Confirm your information (Y/N)")
      confirmDetails=confirmDetails.upper()
  
      if confirmDetails=="Y":
          print("your informations are confirmed")
          break
      elif confirmDetails=="N":
          print("Please re-enter your details") 

user()


def MET():
    #import cvs file
    import csv
    try:
        with open ('mettable.csv') as f:
            readF= csv.reader(f, delimiter=',')
            for row in readF:
                print (row)
    except:
        print("file not found")
 
      
MET()

def activity():
    anothergo="Y"
    #the purpose of this loop is to allow user to add more avtivity
    while (anothergo=="Y"):
        #check whether costumer enter right MET
        while True:
            mets=float(input("Please enter your activity MAT: "))
            if (1<= mets<= 18) :
              #Energy expenditure calculation
                energy=float(0.0175*mets* weight)
                #add energy to activities 
                activities.append(energy)
          
                #add energy in to energy list to help calculate total energ at the end 
                energylist.append(energy)

                break
            else:
                print("Invalis input. Please try agian")

        activityName=input("Please enter activity: ")
        activities.append(activityName)
        print("Your energy expenditure is ",energy,"cal/min")
    
    
        anothergo=input("Do you want to add more activities(Y/N):  ")
        anothergo=anothergo.upper()
        if (anothergo=="Y"):
            print("Add activities")
        elif (anothergo=="N"):
            break
        else:
            print("Invalid input. Please try again")
  
   
          


activity()

def summary():
    print("")
    print("")
    print("Your record")
   

    print ("Costumer name: ",name)
    print("Costumer age: ",age,"years")
    print ("Costumer weight: ",weight,"kg")

    index=1
    print ("Activity: ",activities[index])
    enindex=0
    print ("Caleries burn per minute: ",energylist[enindex])
    #print activities that store in the list 
    index=index+2
    print ("Activity: ",activities[index])
    #print engery in the engerylist 
    enindex=enindex+1
    print ("Caleries burn per minute: ",energylist[enindex])
    
    totalcal=sum(energylist)
    prinr("")
    print("Your total cal burn: ",totalcal,"cal/min")
     
    #max() print out the maximum value in the list
    print("Your maximum engergy expenditure: ",max(energylist),"cal/min")


summary()


