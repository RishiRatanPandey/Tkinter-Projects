from tkinter import*
import random
import pygame
thing='Rock','Paper','Scissors'
root=Tk()
computer_point=0
player_point=0
comp_point_data=StringVar()
player_point_data=StringVar()
player_point_data.set(f'Your Points: {player_point}')
comp_point_data.set(f'Comp Points: {computer_point}')
pygame.mixer.init()
root.geometry('689x600')
thing='Rock','Paper','Scissors'
root.title('Rock, Paper & Scissors Game!')
USER_choice=StringVar()
USER_choice.set('None')
label=Label(root,text='')
ChoiceS_Label=Label(root,text='')
rOcK_Image=PhotoImage(file='rock1.png')
PaPeR_Image=PhotoImage(file='paper1.png')
scissorS_Image=PhotoImage(file='scissors1.png')
rOcK_lab=Label(root,image=rOcK_Image)
paper_lab=Label(root,image=PaPeR_Image)
siccors_lab=Label(root,image=scissorS_Image)
rOcK_Image1=PhotoImage(file='rock1.png')
PaPeR_Image1=PhotoImage(file='paper1.png')
scissorS_Image1=PhotoImage(file='scissors1.png')
rOcK_lab_1=Label(root,image=rOcK_Image1)
paper_lab_1=Label(root,image=PaPeR_Image1)
siccors_lab_1=Label(root,image=scissorS_Image1)
def set_Scissors():
   global player_point,computer_point
   USER_choice.set('Scissors')
   random_thing=(random.choice(thing))
   print(random_thing)
   vs_label=Label(root,text='Vs',font=('Arial Rounded MT Bold',40,'bold'),fg='black').place(x=300,y=400)
   rOcK_lab.place(y=350,x=75)
   if USER_choice.get()=='Rock':
      rOcK_lab.place(y=350,x=75)
      paper_lab.place(x=34343)
      siccors_lab.place(x=54544)
   if USER_choice.get()=='Paper':
      rOcK_lab.place(y=3550,x=75)
      paper_lab.place(x=75,y=350)
      siccors_lab.place(x=54544)
   if USER_choice.get()=='Scissors':
      rOcK_lab.place(y=3550,x=75)
      paper_lab.place(x=4344,y=3540)
      siccors_lab.place(x=75,y=350)
   your_move_and_stats=Label(root,text='Your Move & Stats',font=('Arial Rounded MT bold',20,'bold'),fg='grey').place(x=40,y=300)
   comp_move_and_stats=Label(root,text='Comp Move & Stats',font=('Arial Rounded MT bold',20,'bold'),fg='grey').place(x=400,y=300)
   point=Label(root,text=f'Your Points: {player_point}',textvariable=player_point_data,fg='Indian Red4',font=('Arial Rounded MT bold',20,'bold')).place(y=500,x=55)
   comp_point=Label(root,text='Comp Points: 0',fg='Indian Red4',textvariable=comp_point_data,font=('Arial Rounded MT bold',20,'bold')).place(y=500,x=425)
   if USER_choice.get()=='Scissors' and random_thing=='Paper':
            pygame.mixer.music.load('nioce (1).mp3')
            pygame.mixer.music.play()
            player_point+=1
            player_point_data.set(f'Your Points: {player_point}')
            computer_point+=0
            comp_point_data.set(f'Comp Points: {computer_point}')
   if USER_choice.get()=='Scissors' and random_thing=='Rock':
            pygame.mixer.music.load('bruh.mp3')
            pygame.mixer.music.play()
            player_point+=0
            player_point_data.set(f'Your Points: {player_point}')
            computer_point+=1
            comp_point_data.set(f'Comp Points: {computer_point}')
   if USER_choice.get()=='Scissors' and random_thing=='Scissors':
            pass
   if random_thing=='Paper':
      paper_lab_1.place(y=350,x=450)
      rOcK_lab_1.place(x=5444)# set a called mode called 2 player or 3 player....
      siccors_lab_1.place(x=4444)
   if random_thing=='Scissors':
      siccors_lab_1.place(y=350,x=450)
      rOcK_lab_1.place(y=3560,x=450)
      paper_lab_1.place(y=3550,x=450)
   if random_thing=='Rock':
      rOcK_lab_1.place(y=350,x=450)
      paper_lab_1.place(y=3550,x=450)
      siccors_lab_1.place(x=4444)
def set_paper():
   global player_point
   global computer_point
   USER_choice.set('Paper')
   random_thing=(random.choice(thing))
   print(random_thing)
   vs_label=Label(root,text='Vs',font=('Arial Rounded MT Bold',40,'bold'),fg='black').place(x=300,y=400)
   rOcK_lab.place(y=350,x=75)
   if USER_choice.get()=='Rock':
      rOcK_lab.place(y=350,x=75)
      paper_lab.place(x=34343)
      siccors_lab.place(x=54544)
   if USER_choice.get()=='Paper':
      rOcK_lab.place(y=3550,x=75)
      paper_lab.place(x=75,y=350)
      siccors_lab.place(x=54544)
   if USER_choice.get()=='Scissors':
      rOcK_lab.place(y=3550,x=75)
      paper_lab.place(x=4344,y=3540)
      siccors_lab.place(x=75,y=350)
   your_move_and_stats=Label(root,text='Your Move & Stats',font=('Arial Rounded MT bold',20,'bold'),fg='grey').place(x=40,y=300)
   comp_move_and_stats=Label(root,text='Comp Move & Stats',font=('Arial Rounded MT bold',20,'bold'),fg='grey').place(x=400,y=300)
   point=Label(root,text='Your Points: 0',textvariable=player_point_data,fg='Indian Red4',font=('Arial Rounded MT bold',20,'bold')).place(y=500,x=55)
   comp_point=Label(root,text='Comp Points: 0',textvariable=comp_point_data,fg='Indian Red4',font=('Arial Rounded MT bold',20,'bold')).place(y=500,x=425)
   if USER_choice.get()=='Paper' and random_thing=='Scissors':
            pygame.mixer.music.load('bruh.mp3')
            pygame.mixer.music.play()
            player_point+=0
            player_point_data.set(f'Your Points: {player_point}')
            computer_point+=1
            comp_point_data.set(f'Comp Points: {computer_point}')
   if USER_choice.get()=='Paper' and random_thing=='Rock':
            pygame.mixer.music.load('nioce (1).mp3')
            pygame.mixer.music.play()
            player_point+=1
            player_point_data.set(f'Your Points: {player_point}')
            computer_point+=0
            comp_point_data.set(f'Comp Points: {computer_point}')
   if USER_choice.get()=='Paper' and random_thing=='Paper':
            pass
   if random_thing=='Paper':
      paper_lab_1.place(y=350,x=450)
      rOcK_lab_1.place(x=5444)
      siccors_lab_1.place(x=4444)
   if random_thing=='Scissors':
      siccors_lab_1.place(y=350,x=450)
      rOcK_lab_1.place(y=3560,x=450)
      paper_lab_1.place(y=3550,x=450)
   if random_thing=='Rock':
      rOcK_lab_1.place(y=350,x=450)
      paper_lab_1.place(y=3550,x=450)
      siccors_lab_1.place(x=4444)
def set_rocks():
   global player_point
   global computer_point
   USER_choice.set('Rock')
   random_thing=(random.choice(thing))
   vs_label=Label(root,text='Vs',font=('Arial Rounded MT Bold',40,'bold'),fg='black').place(x=300,y=400)
   rOcK_lab.place(y=350,x=75)
   if USER_choice.get()=='Rock':
      rOcK_lab.place(y=350,x=75)
      paper_lab.place(x=34343)
      siccors_lab.place(x=54544)
   if USER_choice.get()=='Paper':
      rOcK_lab.place(y=3550,x=75)
      paper_lab.place(x=75,y=350)
      siccors_lab.place(x=54544)
   if USER_choice.get()=='Scissors':
      rOcK_lab.place(y=3550,x=75)
      paper_lab.place(x=4344,y=3540)
      siccors_lab.place(x=75,y=350)
   your_move_and_stats=Label(root,text='Your Move & Stats',font=('Arial Rounded MT bold',20,'bold'),fg='grey').place(x=40,y=300)
   comp_move_and_stats=Label(root,text='Comp Move & Stats',font=('Arial Rounded MT bold',20,'bold'),fg='grey').place(x=400,y=300)
   point=Label(root,text='Your Points: 0',textvariable=player_point_data,fg='Indian Red4',font=('Arial Rounded MT bold',20,'bold')).place(y=500,x=55)
   comp_point=Label(root,text='Comp Points: 0',textvariable=comp_point_data,fg='Indian Red4',font=('Arial Rounded MT bold',20,'bold')).place(y=500,x=425)
   if USER_choice.get()=='Rock' and random_thing=='Scissors':
            pygame.mixer.music.load('nioce (1).mp3')
            pygame.mixer.music.play()
            player_point+=1
            player_point_data.set(f'Your Points: {player_point}')
            computer_point+=0
            comp_point_data.set(f'Comp Points: {computer_point}')
            rOcK_lab.place(y=350,x=75)
   if USER_choice.get()=='Rock' and random_thing=='Paper':
            pygame.mixer.music.load('bruh.mp3')
            pygame.mixer.music.play()
            player_point+=0
            player_point_data.set(f'Your Points: {player_point}')
            computer_point+=1
            comp_point_data.set(f'Comp Points: {computer_point}')
            rOcK_lab.place(y=350,x=75)
            rOcK_lab.place(y=350,x=75)
   if USER_choice.get()=='Rock' and random_thing=='Rock':
            label.config(text='Tie')   
            rOcK_lab.place(y=350,x=75)       
   if random_thing=='Paper':
      paper_lab_1.place(y=350,x=450)
      rOcK_lab_1.place(x=5444)
      siccors_lab_1.place(x=4444)
#create a reason why computer wins and add shaking hand sound.
   if random_thing=='Scissors':
      siccors_lab_1.place(y=350,x=450)
      rOcK_lab_1.place(y=3560,x=450)
      paper_lab_1.place(y=3550,x=450)
   if random_thing=='Rock':
      rOcK_lab_1.place(y=350,x=450)
      paper_lab_1.place(y=3550,x=450)
      siccors_lab_1.place(x=4444)
head=Label(root,text='Select Rock Or Paper Or Scissors',font=('Arial Rounded Mt Bold',20,'bold'),fg='Red').pack()
button=Button(root,text='Rock',fg='White',bg='black',activebackground='Black',activeforeground='white',font=('Arial Rounded Mt Bold',20,'bold'),command=set_rocks,borderwidth=6)
button.place(x=280,y=54)
button_0=Button(root,text='Paper',fg='White',bg='black',activebackground='Black',activeforeground='white',font=('Arial Rounded Mt Bold',20,'bold'),command=set_paper,borderwidth=6)
button_0.place(x=275,y=140)
button_1=Button(root,text='Scissors',fg='White',bg='black',activebackground='Black',activeforeground='white',font=('Arial Rounded Mt Bold',20,'bold'),command=set_Scissors,borderwidth=6)
button_1.place(x=265,y=230)
mainloop()
