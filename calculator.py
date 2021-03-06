from tkinter import *

class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("269x360")
        self.master.config(bg="#2A3037")
        self.master.title("Calculator")
        self.expression = ""
        self.generate()
    
    def buttonPress(self, key):
        self.expression_field["fg"] = "black"
        if key == "Ans":
            key = self.result
        self.expression = self.expression + str(key)
        self.equation.set(self.expression)
    
    def error(self, message):
        self.expression_field["fg"] = "red"
        self.equation.set(message)
        self.expression = ""
        if self.bans["state"] == "normal":
                self.bans["state"] = "disabled"
                self.bans["text"] = "Ans"

    def enter(self):
        try:
            self.expression_field["fg"] = "black"
            self.result = str(eval(self.equation.get()))
            self.equation.set(self.result)
            self.expression = ""
            if self.bans["state"] == "disabled":
                self.bans["state"] = "normal"
            self.bans["text"] = f"Ans\n({self.result})"
        except ZeroDivisionError:
            self.error("Divide by Zero Error!")
        except SyntaxError:
            self.error("Incorrect Syntax!")
        except NameError:
            self.error("No letters allowed!")

    def clear(self):
        self.expression = ""
        self.equation.set(self.expression)

    def makeButtons(self):
        self.button_color = "red"
        self.button_width = 7
        self.button_height = 3
        self.b0 = Button(self.master, text="0", command=lambda: self.buttonPress(0), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b1 = Button(self.master, text="1", command=lambda: self.buttonPress(1), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b2 = Button(self.master, text="2", command=lambda: self.buttonPress(2), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b3 = Button(self.master, text="3", command=lambda: self.buttonPress(3), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b4 = Button(self.master, text="4", command=lambda: self.buttonPress(4), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b5 = Button(self.master, text="5", command=lambda: self.buttonPress(5), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b6 = Button(self.master, text="6", command=lambda: self.buttonPress(6), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b7 = Button(self.master, text="7", command=lambda: self.buttonPress(7), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b8 = Button(self.master, text="8", command=lambda: self.buttonPress(8), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.b9 = Button(self.master, text="9", command=lambda: self.buttonPress(9), bg=self.button_color, height=self.button_height, width=self.button_width)

        self.button_list = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]

        for i in range(0,len(self.button_list)):
            x = self.button_list[i]
            if i == 0:
                x.grid(row=5,column=1)
            elif i <= 3:
                x.grid(row=4, column=i)
            elif i > 3 and i <= 6:
                x.grid(row=3, column=(i-3))
            elif i > 6 and i <= 9:
                x.grid(row=2, column=(i-6))

        self.bequ = Button(self.master, text="=", command=self.enter, bg=self.button_color, height=4, width=29)
        self.bans = Button(self.master, text="Ans", command=lambda: self.buttonPress("Ans"),bg=self.button_color, height=3, width=29, state=DISABLED)
        self.bper = Button(self.master, text=".", command=lambda: self.buttonPress("."), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.bcle = Button(self.master, text="c", command=self.clear, bg=self.button_color, height=self.button_height, width=self.button_width)
        self.badd = Button(self.master, text="+", command=lambda: self.buttonPress("+"), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.bsub = Button(self.master, text="-", command=lambda: self.buttonPress("-"), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.bmul = Button(self.master, text="×", command=lambda: self.buttonPress("*"), bg=self.button_color, height=self.button_height, width=self.button_width)
        self.bdiv = Button(self.master, text="÷", command=lambda: self.buttonPress("/"), bg=self.button_color, height=self.button_height, width=self.button_width)

        self.bequ.grid(row=7, column=1, columnspan=10)
        self.bans.grid(row=6, column=1, columnspan=10)
        self.bper.grid(row=5, column=2)
        self.bcle.grid(row=5, column=3)

        self.badd.grid(row=2, column=4)
        self.bsub.grid(row=3, column=4)
        self.bmul.grid(row=4, column=4)
        self.bdiv.grid(row=5, column=4)
                
    def makeInput(self):
        self.equation = StringVar()
        self.expression_field = Entry(self.master, textvariable=self.equation, fg="blue")
        self.expression_field.grid(columnspan=5, row=1, ipadx=38)
        self.equation.set('Enter Expression')

    def generate(self):
        self.makeButtons()
        self.makeInput()
            
master = Tk()
a = Calculator(master=master)
a.mainloop()