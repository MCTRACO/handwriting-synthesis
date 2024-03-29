import PySimpleGUI as Sg


def create_layout():
    return [[Sg.Text("Input:"), Sg.Input(key="input")],
            [Sg.Text("Style:"), Sg.Input(key="style", default_text="3")],

            [Sg.Text("Readability:"),
             Sg.Slider(range=(0.15, 2.5), default_value=2.5, orientation="h", resolution=0.02, key="bias")],
            [Sg.Text("Width:"),
             Sg.Slider(range=(0.1, 1.5), default_value=0.1, orientation="h", size=(15, 15), key="width")],
            [Sg.Button("OK")]]


layout = create_layout()

window = Sg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == Sg.WIN_CLOSED:
        break

window.close()

print("Input:", values["input"])
print("Style:", values["style"])
print("Bias:", values["bias"])
print("Width:", values["width"])
