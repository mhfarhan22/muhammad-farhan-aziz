import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                  layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                   font=("Arial"))],
                          [sg.Text("NPM  : 2210010317 " )],        
                          [sg.Text("Nama  : Farhan AZIZ ")],
                          [sg.Text("Kelas : 5M Regular Banjarmasin ")]
],
                  size=(400,200),
                  font=("Times", 18))

window()
window.close()