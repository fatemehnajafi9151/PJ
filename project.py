#contract tkinter to tik to be more comfortable
import tkinter as tik
from tkinter.messagebox import showinfo

#creat our window

window=tik.Tk()
window.title("my lovely project")



def show():
    show_frame=tik.Frame(window)
    show_frame.grid(row=0)
    lable_player_one=tik.Label(show_frame,text="player 1",font=(10),padx=8)
    lable_player_two=tik.Label(show_frame,text="player 2",font=(10),padx=8)
    lable_player_one.grid(row=0 , column=0)
    lable_player_two.grid(row=0 , column=2)

    socor_frame=tik.Frame(window)
    socor_frame.grid(row=1)
    lable_player_one_socor=tik.Label(socor_frame ,text=score[0],font=(10),padx=25)
    lable_player_two_socor=tik.Label(socor_frame ,text=score[1],font=(10),padx=25)
    lable_player_one_socor.grid(row=1 , column=0)
    lable_player_two_socor.grid(row=1 , column=2)

global turn,finial,score
turn="*"
finial = ["","","","","","","","",""]
score=[0 , 0]

def click(btn):
    global turn 
    btn=int(btn)
    if finial[btn]== "":
        if turn=="*":
            finial[btn]="*"
            buttons[btn]['bg']="black"
            buttons[btn]['fg']="white"
            buttons[btn]["text"]="*"
            #buttons[btn]['state']=tik.DISABLED
            turn="+"
        else :
            finial[btn]="+"
            buttons[btn]['bg']="white"
            buttons[btn]['fg']="black"
            buttons[btn]["text"]="+" 
            #buttons[btn]['state']=tik.DISABLED
            turn="*"   
        legislation()

def legislation():
    if(finial[0]==finial[1]==finial[2] and finial[0]!=""):
        print(f"player{finial[1]} win")
        winner(finial[1])
    else:
        if(finial[3]==finial[4]==finial[5] and finial[5]!=""):
            print(f"player{finial[4]}win")
            winner(finial[5])
        else:
            if(finial[6]==finial[7]==finial[8] and finial[7]!=""): 
                print(f"player{finial[7]}win")
                winner(finial[7])
            else:
                if(finial[0]==finial[3]==finial[6] and finial[3]!=""): 
                    print(f"player{finial[3]}win")
                    winner(finial[6])
                else:
                    if(finial[1]==finial[4]==finial[7] and finial[7]!=""): 
                        print(f"player{finial[7]}win") 
                        winner(finial[4])
                    else:
                       if(finial[0]==finial[4]==finial[8] and finial[8]!=""): 
                            print(f"player{finial[4]}win")
                            winner(finial[8])
                       else:
                           if(finial[2]==finial[5]==finial[8] and finial[8]!=""): 
                                print(f"player{finial[8]}win")
                                winner(finial[8])
                           else:
                               if(finial[2]==finial[4]==finial[6] and finial[6]!=""): 
                                    print(f"player{finial[6]}win")
                                    winner(finial[6])
                               else:
                                    check()

def check():
    if ""not in finial:
        showinfo("the end","play is equal")                                  
        reset()


def winner(winner):
    if winner=="*":
        score[0] += 1
        showinfo("the end","player * win")
        print(score)
        reset()
    
    else:
        score[1] += 1
        showinfo("the end","player + win")
        print(score)
        reset()


def reset():
    global finial,again
    finial=["","","","","","","","",""]
    turn="*"
    main()
    show()
    

                             
#making it buttons
def main():
    #insted of writing them one by one i made a list
    global buttons
    buttons=[]
    counter=0
    main_frame=tik.Frame(window)
    main_frame.grid(row=2)
    for row in range(1 , 4):
        for column in range(1 , 4):
                      #made a frame with 3 length buttons  and 3 wide buttons
             x=counter
                    #add counter in our list
             buttons.append(x)
             buttons[x]=tik.Button(main_frame , text=f"btn {x}",command=lambda c=f"{x}": click(c) )
             
             buttons[x].config(width=10 , height=4 , font=("None",18, "bold"))
             buttons[x].grid(row=row , column=column)
             counter += 1
main()
show()

window.mainloop()