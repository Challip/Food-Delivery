#Program 3: Fantasy adventure game 
#The purpose of this program is to create a game inspired from the movie despicable me
#Author:Prang Kongthongluck
#Date:27/11/2019
#version:2.1

import random
from tkinter import*
import tkinter as tk



item=[]
hplevel=100
vectorhp=100


#when player choosed Gru as his/her character
def Gruitem():
    global itemlist
    global item
    itemlist=Listbox(root)
    
    item.append("Turbo Car")
    Label(root,text="Your HP= 100").grid(row=5,columnspan=3)
    Label(root,text="Start item: Turbo car - use it to escape from anything ").grid(row=6,columnspan=3)
    Button(root,text="Start Game",command=HouseGru).grid(row=7,column=1)

#window for living room scence
def HouseGru():
    global house

    house=Toplevel(root)
    house.title("Living room")
     
    Label(house,text="You are now in living room in Gru's house").grid(row=0,columnspan=3)
    Label(house,text="You meet Gru's pet,'Kyle'").grid(row=1,columnspan=3)
    Label(house,text="What will you do?").grid(row=2,columnspan=3)
    Button(house,text="Turn back",command=quit).grid(row=3,column=0)
    Button(house,text="fight",command=(fight)).grid(row=3,column=1)
    Button(house,text="Use item",command=houseitemGru).grid(row=3,column=2)
       
#player use item to eascape from living room his/her start item will be removed from the item list
def houseitemGru():
    Label(house,text="Gru uses his car to escape from living room").grid(row=4,columnspan=3)
    item.remove("Turbo Car")
    Button(house,text="continue",command=bedroom).grid(row=8,columnspan=3) 
 #----------------------------------------------------------------------------------------------------------------------------------------   
#when player choosed Agnes as his/her character

def Agnesitem():
    global item
    itemlist=Listbox(root)
    
    item.append("Unicorn")
    Label(root,text="Start item: unicorn - use unicorn to trade for anything ").grid(row=4,columnspan=3)
    Label(root,text="Your HP= 100").grid(row=5,columnspan=3)
    Label(root,text="You have 3 lifes").grid(row=6,columnspan=3)
    Button(root,text="Start Game",command=HouseAgnes).grid(row=7,column=1)
#window for living room scence
def HouseAgnes():
    global house
    house=Toplevel(root)
    house.title("Living room")

     
    Label(house,text="You are now in living room in Gru's house").grid(row=0,columnspan=3)
    Label(house,text="You meet Gru's pet,'Kyle'").grid(row=1,columnspan=3)
    Label(house,text="What will you do?").grid(row=2,columnspan=3)
    Button(house,text="Turn back",command=quit).grid(row=3,column=0)
    Button(house,text="fight",command=(fight)).grid(row=3,column=1)
    Button(house,text="Use item",command=houseitemAgnes).grid(row=3,column=2)

#player use item to eascape from living room his/her start item will be removed from the item list
def houseitemAgnes():
    Label(house,text="Agnes gives Kyle her unicorn and walk pass the living room").grid(row=4,columnspan=3)
    item.remove("Unicorn")
    Button(house,text="continue",command=bedroom).grid(row=8,columnspan=3)
    
#----------------------------------------------------------------------------------------------------------------------------------------          
#when player choosed Jerry as his/her character

def Jerryitem():
    global item
    itemlist=Listbox(root)
    
    item.append("Fart Gun")
    Label(root,text="Start item: Fart Gun - distract attention").grid(row=4,columnspan=3)
    Label(root,text="Your HP= 100").grid(row=5,columnspan=3)
    Label(root,text="You have 3 lifes").grid(row=6,columnspan=3)
    Button(root,text="Start Game",command=HouseJerry).grid(row=7,column=1)

#window for living room scence
def HouseJerry():
    global house
    house=Toplevel(root)
    house.title("Living room")

     
    Label(house,text="You are now in living room in Gru's house").grid(row=0,columnspan=3)
    Label(house,text="You meet Gru's pet,'Kyle'").grid(row=1,columnspan=3)
    Label(house,text="What will you do?").grid(row=2,columnspan=3)
    Button(house,text="Turn back",command=quit).grid(row=3,column=0)
    Button(house,text="fight",command=(fight)).grid(row=3,column=1)
    Button(house,text="Use item",command=houseitemJerry).grid(row=3,column=2)

#player use item to eascape from living room his/her start item will be removed from the item list
def houseitemJerry():
    Label(house,text="Jerry use Fart gun to distract Kyle and walk past the living room").grid(row=4,columnspan=3)
    item.remove("Fart Gun")
    Button(house,text="continue",command=bedroom).grid(row=8,columnspan=3)


#----------------------------------------------------------------------------------------------------------------------------------------   
#fight with Kyle
def fight():
    Button(house,text="roll the dice",command=(rollDice)).grid(row=4,columnspan=3)
#roll dice program
def rollDice():
    global life
    global hplevel
    hplevel =100
    tv_rollKyle=StringVar()
    tv_rollplayer=StringVar()
    tv_winner=StringVar()
    tv_hp=StringVar()
   
    #use randome for rolling dice
    rollKyle = random.randint(1,6)
    tv_rollKyle.set(rollKyle)
    
    rollplayer=random.randint(1,6)
    tv_rollplayer.set(rollplayer)

    if (rollKyle>rollplayer):
        winner="You lose, hp-10"
        hplevel=90
        heplevel=("Your HP =",hplevel)
        tv_hp.set(heplevel)
    elif (rollKyle<rollplayer):
        winner="You win!!, you get new item: Zapper"
        item.append("Zapper")

    tv_winner.set(winner)
    
   
        

    Label(house,text="Kyle get:").grid(row=5,column=1)
    Label(house,textvariable=tv_rollKyle).grid(row=5,column=2)
    Label(house,text="You get:").grid(row=6,column=1)
    Label(house,textvariable=tv_rollplayer).grid(row=6,column=2)
    Label(house,textvariable=tv_winner,fg="red").grid(row=7,columnspan=3)
    Label(house,textvariable=tv_hp,fg="red").grid(row=8,columnspan=3)
    Button(house,text="continun",command=bedroom).grid(row=9,columnspan=3)
#------------------------------------------------------------------------------------------------------------------------------------------   
#bedroom scence
def bedroom():
    global bed
    bed=Toplevel(root)
    bed.title("Bedroom")
    Label(bed,text="You are now in the bedroom where you meet Margo").grid(row=0,columnspan=3)
    Label(bed,text="Margo is sleeping and her phone is next to her").grid(row=1,columnspan=3)
    Button(bed,text="Leave the room",anchor="e",command=Kitchen).grid(row=2,column=1)
    Button(bed,text="collect Margo phone",anchor="w",command=MargoPhone).grid(row=2,column=2)

#player choose to collect Phone 
def MargoPhone():
    #Phone is added to the item list
    item.append("Phone")
    Label(bed,text="Phone is added to your item bag").grid(row=3,columnspan=3)
    Button(bed,text="continue",anchor="e",command=Kitchen).grid(row=4,column=1)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#kitchen sence
def Kitchen():
    global kit
 
    kit=Toplevel(root)
    kit.title("Kitchen")
   
    
    Label(kit,text="You are now in the kitchen").grid(row=0,columnspan=3)
    Label(kit,text="Edith try to make herself a pancake").grid(row=1,columnspan=3)
    Label(kit,text="Help Edith by use Margo's phone tocall Nanna").grid(row=2,columnspan=3)
    Button(kit,text="help Edith",command=HelpEdith).grid(row=3,column=1)
    Button(kit,text="dont't have phone",command=GruRoom).grid(row=3,column=2)



#display item the player have in form of listbox
def HelpEdith():
    global itemlist
    itemlist=Listbox(kit)
    itemlist.grid(rowspan=4,column=1)
    for i in item:
        itemlist.insert("end",i)
    Button(kit,text="Select",command=selectedItemHelpEdith).grid(rowspan =7,columnspan=3)


def selectedItemHelpEdith():
    global item
    #delete selected item out of th listbox
    itemlist.delete(tk.ANCHOR)
    #delete the selected item out from the list
    try:
        selection=itemlist.curselection()   
        value=eval(itemlist.get(selection))
        ind=item.index(value)
        del(item[ind])
    except:
        #Phone is removed out of the list
        item.remove("Phone")
        print("Phone is removed from the item list")
    
    Label(kit,text="Pancake is made").grid(row=5,column=2)
    Label(kit,text="Item Pancake is now added to you item bag").grid(row=5,column=2)
    #Pancake is added to the item list
    item.append("Pancake")
    Button(kit,text="Continue",command=GruRoom).grid(row=8,columnspan=3)

   

#-------------------------------------------------------------------------------------------------------------------------------------------
#Gru's working room scence
def GruRoom():
    global gru
    gru=Toplevel(root)
    gru.title("Gru's office")
    Label(gru,text="You are now in Gru office").grid(row=0,columnspan=3)
    Label(gru,text="You meet Carl, he wants to exchange a pancake with his siren hat").grid(row=1,columnspan=3)
    Button(gru,text="Exchange",command=ExchangeCarl).grid(row=2,column=2)
    Button(gru,text="Don't have pancake", command=Backyard).grid(row=2,column=1)

def ExchangeCarl():
     
    itemlist=Listbox(gru)
    itemlist.grid(rowspan=3,column=1)
    for i in item:
        itemlist.insert("end",i)
    Button(gru,text="Select",command=selectedItemExchangeCarl).grid(rowspan =6,columnspan=3)

def selectedItemExchangeCarl():
    #delete item of the list when its selected by player
    itemlist.delete(tk.ANCHOR)
     #delete the selected item out from the list
    try:
        selection=itemlist.curselection()
   
        value=eval(itemlist.get(selection))
        ind=item.index(value)
        del(item[ind])
    except:
        #pancake ir removed out of the list
        item.remove("Pancake")
        print("Pancake is removed from the item list")
   
    Label(gru,text="Siren hat is added to your item bag").grid(row=4,column=2)
    #Siren hat is added to the item list
    item.append("Siren Hat")
    Button(gru,text="Continue",command=Backyard).grid(row=20,columnspan=3)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#backyard scence
def Backyard():
    global back
    back=Toplevel(root)
    back.title("Backyard")
    Label(back,text="You are now in the Backyard").grid(row=0,columnspan=3)   
    Label(back,text="Mr. McDade who lieves next door accidentally drop his spatula to your backyard ").grid(row=1,columnspan=3)   
    Button(back,text="return the spatular",command=returnSpatula).grid(row=2,column=1)   
    Button(back,text="Keep the spactular",command=keepSpatulat).grid(row=2,column=2) 

def returnSpatula():
    Label(back,text="Mr.McDade says Thank you").grid(row=3,columnspan=3)   
    Button(back,text="continue",command=Lab).grid(row=4,columnspan=3)   

def keepSpatulat():
    Label(back,text="Spatular is added to your bag").grid(row=3,columnspan=3)   
    item.append("Spatular")
    Button(back,text="continue",command=Lab).grid(row=4,columnspan=3)   

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#window for lab scence
def Lab():
    global lab
    lab=Toplevel(root)
    lab.title("Minion Lab")
    lab.geometry=("200*250")
    Label(lab,text="You are now in the Minion Laboratory").grid(row=0,columnspan=4)
    Label(lab,text="Dr.Nefario accidently freeze himself by shooting freeze ray to himself").grid(row=1,columnspan=4)
    Button(lab,text="Help him",anchor='w',command=HelpNefario).grid(row=2,column=2)
    Button(lab,text="Ignor him",anchor='e',command=Roof).grid(row=2,column=1)

def HelpNefario():
    global itemlist
    Label(lab,text="Item in your pocket").grid(row=3,column=0)
    itemlist=Listbox(lab)
    itemlist.grid(row=4,column=0)
    for i in item:
        itemlist.insert("end",i)
    Button(lab, text = "select",command=print_HelpNafario).grid(row=6,columnspan=4)



def print_HelpNafario():
    #call a dictionary to print out the text when each item is selected
    gg=Label(lab,text=aaa[itemlist.get(itemlist.curselection())]).grid(row=3,column=1)
    Label(lab,text="You free Dr.Nafario",anchor='w').grid(row=4,column=1)
    Label(lab,text="You receive new item: Freeze Ray").grid(row=5,column=1)
    item.append("Freeze Ray")
    Button(lab,text="Continue",command=RoofHelp).grid(row=7,columnspan=4)

#dictionary to display different text when each item is selected
aaa={
    "Turbo Car":"Turbo Car can't melt Dr.Nafario",
    "Unicorn":"Unicorn can't melt Dr.Nafario",
    "Fart Gun":"Dave is anoyyed by your Fast Gun so he hits you with the Fast Gun",
    "Zapper":"Zapper malt down the ice and free Dr. Nafario",
    "Phone":"Turbo Car can't melt Dr.Nafario",
    "Pancake":"Dave steal your pancake",
    "Spatular":"Use Spatular hit the ice and free Dr.Nafario",
    "Siren Hat":"Siren Hat bring all minion to help free Dr.Nafario"
    }


#-------------------------------------------------------------------------------------------------------------------------------------------


#this window will show up when player choose not to help Dr.Nafario
def Roof():
    global roof
    roof=Toplevel(root)
    roof.title("Roof")


    Label(roof,text="Vector try to steal your masterpiece weapon").grid(row=0,columnspan=3)
    Label(roof,text="You follow Vector up to the roof of the lab").grid(row=1,columnspan=3)
    Label(roof,text="You need to get you masterpiece back!!!",anchor='w').grid(row=2,columnspan=3)
    Label(roof,text="Fight with Vector",anchor='w',fg="gold").grid(row=3,columnspan=3)
    Button(roof,text="roll dice",command=rollDiceVector).grid(row=4,columnspan=3)
    

#this window will show up when the player don't have Freez ray
    
def rollDiceVector():
    global life
    global hplevel
    global vectorhp
    tv_rollVector=StringVar()
    tv_rollplayer1=StringVar()
    winner1=()
    winner2=()
    tv_winner1=StringVar()
    tv_winner2=StringVar()
    tv_hp=StringVar()
    tv_Vhplevel=StringVar()
    
    rollVector = random.randint(1,6)
    tv_rollVector.set(rollVector)
    
    rollplayer1=(random.randint(1,6))
    tv_rollplayer1.set(rollplayer1)

    if (rollVector>rollplayer1):
        winner1="You lose, hp -30"
        hplevel -=30
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))
    if (rollVector<rollplayer1):
        winner1="Vector lost 50 hp"
        vectorhp -=50
        Vhplevel=("Vertor hp level:" ,(vectorhp))
        HP=("Your HP:",hplevel)


    if (rollVector == rollplayer1):
        winner1=("   You are tie  ")
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))
       

    if (vectorhp==0) or (vectorhp <=0):
        winner2="YOU WIN!! you bring masterpiece back"
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))

    if (hplevel == 0) or (hplevel <= 0):
        winner2="You lose"
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))


    


    
    tv_Vhplevel.set(Vhplevel)
    tv_hp.set(HP)
    tv_winner2.set(winner2)
    tv_winner1.set(winner1)    

    Label(roofH,text="Vector get:").grid(row=9,column=1)
    Label(roofH,textvariable=tv_rollVector).grid(row=9,column=2)
    Label(roofH,text="You get:").grid(row=10,column=1)
    Label(roofH,textvariable=tv_rollplayer1).grid(row=10,column=2)
    Label(roofH,textvariable=tv_winner1,fg="red").grid(row=12,columnspan=3)
    Label(roofH,textvariable=tv_winner2,fg="red").grid(row=13,columnspan=3)
    Label(roofH,textvariable=tv_hp,fg="green").grid(row=11,column=1)
    Label(roofH,textvariable=tv_Vhplevel,fg="purple",anchor="e").grid(row=11,column=2)
    Button(roofH,text="Exite Game",command=quit).grid(row=14,columnspan=3)
    

 
    


#this window will show up when the player receive Freez ray by helping DR.Nafario
def RoofHelp():
    global roofH
    roofH=Toplevel(root)
    roofH.title("Roof")

    Label(roofH,text="Vector try to steal your masterpiece weapon").grid(row=0,columnspan=3)
    Label(roofH,text="You follow Vector up to the roof of the lab").grid(row=1,columnspan=3)
    Label(roofH,text="You need to get you masterpiece back!!!",anchor='w').grid(row=2,columnspan=3)
    Label(roofH,text="Fight with Vector",anchor='w',fg="gold").grid(row=3,columnspan=3)
    Button(roofH,text="Use Freez Ray",command=FreezRay).grid(row=4,columnspan=3)

def FreezRay():
    Label(roofH,text="Use Freeze ray to help catch Vector",anchor='w').grid(row=5,column=1)
    Label(roofH,text="+2 score when you roll dice",anchor='w').grid(row=6,column=1)
    Label(roofH,text="Keep roll the dice untill you get you masterpiece back or you die ",anchor='w').grid(row=7,column=1)
    Button(roofH,text="roll dice",command=rollDiceVectorH).grid(row=8,columnspan=3)




def rollDiceVectorH():
    
    global life
    global hplevel
    global vectorhp
    tv_rollVector=StringVar()
    tv_rollplayer1=StringVar()
    winner1=()
    winner2=()
    tv_winner1=StringVar()
    tv_winner2=StringVar()
    tv_hp=StringVar()
    tv_Vhplevel=StringVar()
    
    rollVector = random.randint(1,6)
    tv_rollVector.set(rollVector)
    #+2 score for player when he use item freeze ray
    rollplayer1=(random.randint(1,6))+2
    tv_rollplayer1.set(rollplayer1)

    if (rollVector>rollplayer1):
        winner1="You lose, hp -30"
        hplevel -=30
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))
    if (rollVector<rollplayer1):
        winner1="Vector lost 50 hp"
        vectorhp -=50
        Vhplevel=("Vertor hp level:" ,(vectorhp))
        HP=("Your HP:",hplevel)


    if (rollVector == rollplayer1):
        winner1=("   You are tie  ")
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))
       

    if (vectorhp==0) or (vectorhp <=0):
        winner2="YOU WIN!! you bring masterpiece back"
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))

    if (hplevel == 0) or (hplevel <= 0):
        winner2="You lose"
        HP=("Your HP:",hplevel)
        Vhplevel=("Vertor hp level:" ,(vectorhp))


    


    
    tv_Vhplevel.set(Vhplevel)
    tv_hp.set(HP)
    tv_winner2.set(winner2)
    tv_winner1.set(winner1)    

    Label(roofH,text="Vector get:").grid(row=9,column=1)
    Label(roofH,textvariable=tv_rollVector).grid(row=9,column=2)
    Label(roofH,text="You get:").grid(row=10,column=1)
    Label(roofH,textvariable=tv_rollplayer1).grid(row=10,column=2)
    Label(roofH,textvariable=tv_winner1,fg="red").grid(row=12,columnspan=3)
    Label(roofH,textvariable=tv_winner2,fg="red").grid(row=13,columnspan=3)
    Label(roofH,textvariable=tv_hp,fg="green").grid(row=11,column=1)
    Label(roofH,textvariable=tv_Vhplevel,fg="purple",anchor="e").grid(row=11,column=2)
    Button(roofH,text="Exite Game",command=quit).grid(row=14,columnspan=3)
    





#Start window
root = Tk()
root.title("Select character")
Label(root,text="Welcome to Albuquerque").grid(row=0,columnspan=3)

Label(root,text="Choose youe character",anchor='w').grid(row=1,columnspan=3)
Gru=Button(root,text="Gru",fg="red",command=Gruitem).grid(row=3,column=0)
agnes=Button(root,text="Agnes",fg="pink",command=Agnesitem).grid(row=3,column=1)
jerry=Button(root,text="Jerry",fg="yellow",command=Jerryitem).grid(row=3,column=2)

root.mainloop()


