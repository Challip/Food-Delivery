
#The purpose of this profram is to create fitness app used to record the number of calories burned during different kinds of exercise.
#Author: Prang Kongthongluck
#Version: 2.0
#Date: 06/12/2019
age=()
weight=()

mets=()
activities=[]
energy=()
energylist=[]
durationlist=[]

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
      #make sure user input interger
      while True:
        try:
            weight=int(input("Please enter your weight: "))
            break
        except ValueError:
            print("Please input weight as integer")
       


      #purpose of this loop is to make sure user input collect input to weightUnit
      while True:
          weightUnit=input("Please choose unite of your weight you entered (P=pound/KG): ")
          weightUnit= weightUnit.upper()
    
          #convert weight from pounds in kg when user input weight in pounds)
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
    global selected
    global act
    global energy
    global duration
    
    try:
        file= open ("mettable.txt")
    except:
        print("Something went wrong when writing to the file")
    
    
    #use file to print out list of acttivites
    print(file.read())
    file.close()
    
    anothergo="Y"
    #the purpose of this loop is to allow user to add more avtivity
    while (anothergo=="Y"):  
        check="Y"
       
       #check whether costumer enter right number for activity
        while check=="Y":
            #make sure user input interger
            while True:
                try:
                    userselect=int(input("Please select your activity by input number located in front of met and activity name:  "))
                    break
                except ValueError:
                    print ("Please input with integer")
                
            #split each column in file
            with open("mettable.txt") as file:
                for i in file:
                    column=i.split(",")
                    selected=column[0]
                    met=column[1]
                    act=column[2]
                    if str(userselect)==selected:
                        print("Your activity:",act)
                        activities.append(act)
                        #make sure user input interger
                        while True:
                            try:
                                duration=int(input("How long you do the activity(in minute): "))
                                break
                            except ValueError:
                                print ("Please input with integer")
                        
                        durationlist.append(duration)
                        
                        #Energy expenditure calculation
                        energy=float(0.0175*(float(met))* weight)
                        
                        #add energy in to energy list to help calculate total energ at the end
                        energylist.append(energy)

                        print("Your energy expenditure for",act,"is ",energy,"cal/min")
                        
                        
                            
                if (userselect <0) or (userselect>72):
                    print("Incorrect input, please try again")
                elif (userselect >0) or (userselect<=72):
                    break
                else:
                    print("Incorrect input, please try again")



        anothergo=input("Do you want to add more activities(Y/N):  ")
        anothergo=anothergo.upper()
        if (anothergo=="Y"):
            print("Add activities")
        elif (anothergo=="N"):
            break
        else:
            print("Invalid input. Please try again")
  


 
MET()




#this function will help print out activity summary
def activity(a,b,c):
    x=0
    num=1
    for i in range(len(activities)):
        print("Activity ",num,": ",a[x])
        print("Duration: ",b[x])
        print("Energy expenditure: ",c[x]) 
        x +=1
        num +=1



def summary():
    print("")
    print("")
    print("Your record")
   

    print ("Costumer name: ",name)
    print("Costumer age: ",age,"years")
    print ("Costumer weight: ",weight,"kg")
    #call function activity
    activity(activities,durationlist,energylist) 
  
    
    totalcal=sum(energylist)
    print("")
    print("Your total cal burn: ",totalcal,"cal/min")
     
    #max() print out the maximum value in the list
    print("Your maximum engergy expenditure: ",max(energylist),"cal/min")


summary()
