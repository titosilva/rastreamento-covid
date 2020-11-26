from datetime import date, datetime
from os import system

from utils.colors import bcolors
from utils.input import read_simple_string
from utils.database.emailDAO import EmailDAO
from utils.database.usuarioDAO import UsuarioDAO
from utils.entity.email import Email
from utils.entity.usuario import Usuario


def add_email(user: Usuario):
    new_email_addr = read_simple_string("Novo email")
    new_email = Email(email=new_email_addr,
                      usuario_id_=user.id_, primario=False)

    dao = None
    try:
        dao = EmailDAO()
        dao.create(new_email)
        system("clear")
        print(
            f"{bcolors.OKGREEN}Novo email inserido com sucesso!{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Ocorreu um erro ao inserir o novo email... "
              f"Por favor tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()

    user.emails.append(new_email)


def remove_email(user: Usuario):
    print("Qual email você gostaria de remover?")
    print("\nEmails:")
    for index, email in enumerate(user.emails):
        print(f"\t{index} - {email.email}{'*' if email.primario else ''}")

    choice = -1
    while choice not in range(len(user.emails)):
        try:
            choice = int(input(">> "))
        except:
            print(f"{bcolors.FAIL}Opção inválida!{bcolors.ENDC}")

    email = user.emails.pop(choice)

    dao = None
    try:
        dao = EmailDAO()
        dao.remove(email)
        if email.primario:
            user.emails[0].primario = True
            dao.update(user.emails[0])
        system("clear")
        print(
            f"{bcolors.OKGREEN}Email removido com sucesso!{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Ocorreu um erro ao remover o email... "
              f"Por favor tente novamente.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()


def change_birthday(user: Usuario):
    system("clear")

    birthday = ""
    while not isinstance(birthday, date):
        date_input = read_simple_string(
            "Data de nascimento (dd/mm/AAAA)")
        try:
            birthday = datetime.strptime(date_input, "%d/%m/%Y")
            if birthday.timestamp() > datetime.now().timestamp():
                birthday = ""
                raise ValueError
        except ValueError:
            print(f"{bcolors.FAIL}Data inválida!{bcolors.ENDC}")

    dao = None
    try:
        user.data_nascimento = birthday
        dao = UsuarioDAO()
        dao.update(user)
        system("clear")
        print(f"{bcolors.OKGREEN}Data de nascimento atualizada"
              f" com sucesso!{bcolors.ENDC}")
    except:
        system("clear")
        print(f"{bcolors.FAIL}Não foi possível atualizar a data de"
              f" nascimento... Tente novamente mais tarde.{bcolors.ENDC}")
    finally:
        if dao:
            dao.close()