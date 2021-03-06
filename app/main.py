import os

from view.menus import main_menu, authentication_menu
from utils.controller import sair, actions
from utils.controller.authentication import login, logout, signup
from utils.colors import bcolors


if __name__ == "__main__":
    os.system("clear")
    try:
        while True:
            user = None
            while not user:
                try:
                    option = authentication_menu()
                    os.system("clear")
                    if option == "x":
                        sair()
                    elif option == "l":
                        user = login()
                    elif option == "c":
                        user = signup()
                except ValueError as e:
                    os.system("clear")
                    print(bcolors.WARNING
                          + f"A opção deve ser c, l ou x!"
                            f" Opção {e} inválida!" + bcolors.ENDC)
            os.system("clear")
            print(bcolors.OKGREEN+"Autenticado!"+bcolors.ENDC)
            action = ''
            while user:
                try:
                    action = main_menu(user)
                    os.system("clear")
                    if action not in actions.keys():
                        raise ValueError(action)
                    user = actions[action].get("function", logout)(user)
                except ValueError as e:
                    os.system("clear")
                    print(bcolors.WARNING
                          + f"A opção deve ser uma das disponíveis!"
                            f" Opção {e} inválida!" + bcolors.ENDC)
                except KeyboardInterrupt as e:
                    os.system("clear")
                    user = logout(user)
    except KeyboardInterrupt:
        sair()
