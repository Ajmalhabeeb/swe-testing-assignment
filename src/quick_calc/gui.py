from tkinter import Tk, Label, Button
from quick_calc.core import evaluate, CalcError

class QuickCalcApp:
    def __init__(self):
        self.t1 = Tk()
        self.t1.geometry("570x600+100+200")
        self.t1.title("Calculator")
        self.t1.resizable(False, False)
        self.t1.configure(bg="#000000")

        self.calcresult = Label(
            self.t1, width=25, height=2, text="0", font=("arial", 30), bg="#ffffff"
        )
        self.calcresult.pack()

        self.equation = ""
        self._build_buttons()

    def show(self, value: str):
        self.equation += value
        self.calcresult.config(text=self.equation if self.equation else "0")

    def clear(self):
        self.equation = ""
        self.calcresult.config(text="0")

    def calculate(self):
        if self.equation.strip():
            try:
                result = evaluate(self.equation)
                self.calcresult.config(text=str(int(result)) if result.is_integer() else str(result))
            except CalcError:
                self.calcresult.config(text="Error")
                self.equation = ""
        else:
            self.calcresult.config(text="0")

    # For integration tests (simulated button presses)
    def press(self, token: str):
        if token == "C":
            self.clear()
        elif token == "=":
            self.calculate()
        else:
            self.show(token)

    def _build_buttons(self):
        Button(self.t1, text="C", width=5, height=1, font=("arial", 30, "bold"),
               bd=9, bg="#321ec7", fg="#000000", command=self.clear).place(x=10, y=100)

        Button(self.t1, text="/", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("/")).place(x=150, y=100)

        Button(self.t1, text="*", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("*")).place(x=430, y=100)

        Button(self.t1, text="7", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("7")).place(x=10, y=200)
        Button(self.t1, text="8", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("8")).place(x=150, y=200)
        Button(self.t1, text="9", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("9")).place(x=290, y=200)
        Button(self.t1, text="-", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("-")).place(x=430, y=200)

        Button(self.t1, text="4", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("4")).place(x=10, y=300)
        Button(self.t1, text="5", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("5")).place(x=150, y=300)
        Button(self.t1, text="6", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("6")).place(x=290, y=300)
        Button(self.t1, text="+", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("+")).place(x=430, y=300)

        Button(self.t1, text="1", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("1")).place(x=10, y=400)
        Button(self.t1, text="2", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("2")).place(x=150, y=400)
        Button(self.t1, text="3", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("3")).place(x=290, y=400)

        Button(self.t1, text="0", width=11, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show("0")).place(x=10, y=500)
        Button(self.t1, text=".", width=5, height=1, font=("arial", 30, "bold"),
               bd=5, bg="#faa507", fg="#000000", command=lambda: self.show(".")).place(x=290, y=500)

        Button(self.t1, text="=", width=5, height=4, font=("arial", 30, "bold"),
               bd=6, fg="#ffffff", bg="#000000", command=self.calculate).place(x=430, y=400)

    def run(self):
        self.t1.mainloop()

def main():
    QuickCalcApp().run()

if __name__ == "__main__":
    main()