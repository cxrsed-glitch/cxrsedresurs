name1 = ("Евгений")
name = input("Как вас зовут?")
def authoriz():
    if name == name1:
        print("Вас зовут Евгений:")
        print("Вы преподователь")
    elif name == name:
        print("Ваше имя:",name)
        print("Вы ученик")