import PySimpleGUI as sg 

layout = [
    [sg.Text("Ar siandien sninga", font="times new roman 12")],
    [sg.Input(key= "-NAME-", font= "terminal 15")],
    [
        sg.Button("Noreciau paklausti", key="-HELLO-"),
        sg.Button("Dekoju", key= "-BYE-")
        ],
    [sg.Text(size=(40, 1)), key == "-OUTPUT-", font == "Verdana 15"]
]

window = sg.Window("Oras", layout)
sg.DEFAULT_FONT

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "-HELLO-":
        window ["-OUTPUT-"].update(
            f"Sveiki {values["-NAME-"]}",
            text_color= "#99ff99"
        )

    if event == "-BYE":
        window ["-OUTPUT-"].update(
            f"Sveiki {values["-NAME-"]}",
            text_color= "#99rr99"
        )