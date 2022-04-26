from ast import While
from guizero import App, Text, TextBox, PushButton

app = App(title="Addition", bg="cadetblue")

lblTxt1 = Text(app, text="Enter your first number:")
num1Box = TextBox(app)

lblTxt2 = Text(app, text="Enter your second number:")
num2Box = TextBox(app, width=25)

showAnswer = Text(app, text="Answer will be displayed here", color="white", bg="black")


def addNums():
    # Use the value property to capture value/data entered in the textbox
    num1 = num1Box.value
    num2 = num2Box.value

    # create variable to hold/store answer of num1 + num2
    answer = int(num1) + int(num2)

    # pass answer value to show answer on display
    showAnswer.value = answer


btnAdd = PushButton(app, command=addNums, text="+")


app.display()
