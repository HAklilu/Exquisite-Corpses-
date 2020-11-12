from tkinter import *

root = Tk()

f1 = Frame(root, bg='papaya whip').pack(fill=BOTH)
f2 = Frame(root, bg='papaya whip').pack(fill=BOTH)


story = []

label1 = Label(f1, text="Instructions").pack()
lastLine = Label(f1, text="Last line goes here").pack()

T = Text(f1)
T.pack(expand= True)
T.insert(END, "")

def commit():
    fragment = T.get(1.0, END)
    if len(fragment) < 40:
        print('you must type at least 60 characters')
    else:
        story.append(fragment)
        T.delete(1.0, END)
        ##TODO:    grab the last few characters and insert into lastLine label. 

def finish():
    ##TODO:    clear the last written text
    ##TODO: show the full story in the text box
    finalstory = ''.join(story)
    
    ##TODO: write to a text file
    with open("story.txt", "w") as f:
        f.write(finalstory)
    
done = Button(f2, text="click me to move on", command= lambda : (commit())).pack(side=RIGHT)
doneDone = Button(f2, text="click me to finish", command= lambda : (finish())).pack(side=RIGHT)




mainloop()




