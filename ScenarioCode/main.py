def Menu_main ():
    argument = GetArg()
    switcher = {
        "1": "Op",
        "2": "Det",
        "3": "Eig",
        "4": exit()
    }

    return switcher.get(argument, "Invalid, please retry")

def Menu_operation ():
    argument = GetArg()
    switcher = {
        "1": "Add",
        "2": "Minus",
        "3": "Multiply",
        "4": "Divide",
        "5": "Break"
    }

    return switcher.get(argument, "Invalid, please retry")

def Menu_Det():
    argument = GetArg()
    switcher = {
        "1": "2x2",
        "2": "3x3",
        "3": "Break"
    }

    return switcher.get(argument, "Invalid, please retry")


def Menu_eigenvalue():
    argument = GetArg()
    switcher = {
        "1": "EigenValue",
        "2": "EigenVector",
        "3": "Break"
    }

    return switcher.get(argument, "Invalid, please retry")


def Go ():
    while True:
        printMenu_main()
        if Menu_main() == "Op":
            while True:
                printMenu_op()
                if Menu_operation() == "Break":
                    break
                elif Menu_operation() == "Invalid, please retry":
                    print(Menu_operation())
        if Menu_main() == "Det":
            while True:
                printMenu_Det()
                if Menu_Det() == "Break":
                    break
                elif Menu_Det() == "Invalid, please retry":
                    print(Menu_Det())
        if Menu_main() == "Eig":
            while True:
                printMenu_Eig()
                if Menu_eigenvalue() == "Break":
                    break
                elif Menu_eigenvalue() == "Invalid, please retry":
                    print(Menu_eigenvalue())
        if Menu_main() == "Invalid, please retry":
            print("Invalid, please retry")



def printMenu_main():
    print("Welcome to Matrix Practice system Ver 1.0.0")
    print("1: Basic Matrix Operation Practice")
    print("2: Determinant Operation Practice")
    print("3: File IO Function Menu")
    print("4: Quit the System")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to main menu")
    return

def printMenu_op():
    print("This is the sub menu of operation practice")
    print("1: Do Add Operation")
    print("2: Do Minus Operation")
    print("3: Do Multiply Operation")
    print("4: Do Devide Operation")
    print("5: Quit to Main Menu")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to this menu")
    return

def printMenu_Det():
    print("This is the sub menu of operation practice")
    print("1: Do 2x2 Determinant Operation")
    print("2: Do 3x3 Determinant Operation")
    print("3: Quit to Main Menu")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to this menu")
    return

def printMenu_Eig():
    print("This is the sub menu of operation practice")
    print("1: Do Eigenvalue Operation")
    print("2: Do Eigenvector Operation")
    print("3: Quit to Main Menu")
    print("Enter number to start corresponding practice")
    print("Invalid number will loop back to this menu")
    return

def GetArg():
    value = input("Please enter a number:\n")
    return value

Go()