from guizero import (
    App,
    Text,
    TextBox,
    PushButton,
    MenuBar,
    CheckBox,
    ButtonGroup,
    ListBox,
    Slider,
    Combo,
)

app = App(title="Menu Demo", bg="cadetblue")
chkbx = CheckBox(app, text="Python")
slider = Slider(app)
combo = Combo(app, options=["SDLC", "HTML", "CSS", "NoSQL"])
lstBox = ListBox(app, items=["Cheese", "Salad", "Yoghurt", "Pasta"])
choice = ButtonGroup(
    app, options=["SDLC", "SDLC", "HTML", "HTML", "CSS", "NoSQL" "CSS", "NoSQL"]
)


def fileFunction():
    print("File Option")


def editFunction():
    print("Edit Option")


menubar = MenuBar(
    app,
    toplevel=["File", "Edit"],
    options=[
        [["File Option1", fileFunction], ["File Option2", fileFunction]],
        [["Edit Option1", editFunction], ["Edit Option2", editFunction]],
    ],
)


app.display()
