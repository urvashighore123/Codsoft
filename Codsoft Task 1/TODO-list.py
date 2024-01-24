from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do List')
        self.root.geometry('800x600')
        
        self.label_1 = Label(self.root, text="To-do List", font="Arial 25 bold", width=10, bg="#b161d4", fg="#40082e")
        self.label_1.pack(side="top", fill=BOTH)

        self.label_2 = Label(self.root, text="Add Task", font="Arial 18 bold", width=10, bg="#b161d4", fg="#40082e")
        self.label_2.place(x=40, y=54)

        self.label_3 = Label(self.root, text="Tasks", font="Arial 18 bold", width=10, bg="#b161d4", fg="#40082e")
        self.label_3.place(x=330, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=25, font="Arial 20 bold")
        self.main_text.place(x=205, y=100)

        self.text = Text(self.root, bd=5, height=2, width=18, font="Arial 12 bold")
        self.text.place(x=20, y=120)

        def add_task():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete_task():
            delete= self.main_text.curselection()
            look= self.main_text.get(delete)
            with open('data.txt', 'r+') as f:
                new_f= f.readlines()
                f.seek(0)
                for line in new_f:
                    item= str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete)

        with open('data.txt', 'r') as file:
            read= file.readline()
            for i in read:
                ready= i.split()
                self.main_text.insert(END, ready)  
            file.close()

        self.button = Button(self.root, text="Add", font="sarif, 15 bold ", width=7, bd=5, bg="#b161d4", fg="#40082e", command=add_task) 
        self.button.place(x=70, y=180)

        self.button2 = Button(self.root, text="Delete", font="sarif, 15 bold ", width=7, bd=5, bg="#b161d4", fg="#40082e", command=delete_task) 
        self.button2.place(x=70, y=260)       

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()        