import random
from tkinter import *
from tkinter import messagebox as mb

root =Tk()
root.geometry("800x550")
root.title('Dice Game')

canvas_width = 700
canvas_height = 500
can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

i = ''


def roll():
	global bttn_clicks
	d1=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	
	d= {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
	
	d2=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	
	c= {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
	
	die1=random.choice(d1)
	die2=random.choice(d2)
	
	label_Dice.configure(text=f"{die1} {die2}")
	can_widget.create_window(350,250,window=label_Dice)

	p1res=d[die1]
	p2res=c[die2]

	p_label.configure(text="Player1")
	can_widget.create_window(90,250,window=p_label)
	p2_label.configure(text="Player2")
	can_widget.create_window(610,250,window=p2_label)

	l1.configure(text="Player1 got  "+str(p1res))
	l3.configure(text="Player2 got  "+str(p2res))

	bttn_clicks +=1
	while (bttn_clicks == 3 and res !=3):
		if p1res==p2res :
			Rb.configure(state="disabled")
			mb.showerror("Game Over","Game Draws")
		elif p1res>p2res:
			Rb.configure(state="disabled")
			p1res=p1res+1
			l4.configure(text="Player1 wins")
		else :
			Rb.configure(state="disabled")
			p2res=p2res+1
			l4.configure(text="Player2 wins")
	#bttn_clicks=bttn_clicks+1


	#dice working


def start():
	global bttn_clicks
	Rb.configure(state="normal")

def restart():
	global bttn_clicks
	global i
	bttn_clicks= 0
	l1.configure(text="")
	l3.configure(text="")
	l2.configure(text="Not rolled yet")
	if i:
		can_widget.delete(i)
	Rb.configure(state='normal')




label_Dice=Label(root,font=("times",200),text=" ")
p_label=Label(root,font=("times",15,"bold"),text=" ")

p2_label=Label(root,font=("times",15,"bold"),text=" ")

Rb=Button(root,text="Let's Roll",font=("times",16,"bold"),state="disabled",fg="black",bg="red",height=1,width=12,command=roll)
can_widget.create_window(350,100,window=Rb)

b=Button(root,text="Start",font=("times",16,"bold"),fg="white",bg="black",height=1,width=15,command=start)
can_widget.create_window(120,60,window=b)

b1=Button(root,text="Restart",font=("times",16,"bold"),fg="white",bg="black",height=1,width=15,command=restart)
can_widget.create_window(580,60,window=b1)

l1=Label(root,text=" ",font=("times",16,"bold"),fg="green")
can_widget.create_window(180,400,window=l1)

l2=Label(root,text="Keep Rolling",font=("times",16,"bold"),fg="white",bg="red")
can_widget.create_window(490,420,window=l2)

l3=Label(root,text=" ",font=("times",16,"bold"),fg="green")
can_widget.create_window(610,400,window=l3)

l4=Label(root,text="  ",font=("times",16,"bold"),fg="green")
can_widget.create_window(470,380,window=l4)

root.mainloop()
