from easygui import *

while True:
    interface = buttonbox(
        "Выберите действия",
        "тестовый GUI",
        ["Кава", "Чай", "Выход"]
    )

    if interface == "Кава":
        msgbox("Кава капучино \n цена-4€", image = "2.gif")
    elif interface == "Чай":
        msgbox("Зеленый чай \n цена-3€", image = "4.gif")
    else:
        msgbox("Ой на и ладно больно надо было:(")
        break
