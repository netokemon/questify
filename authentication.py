import pwinput
import time
from database import save_dados
from utils import clear

def email_valido(email):
    return "@" in email and "." in email


def email_existe(email, usuarios):
    for user_info in usuarios.values():
        if user_info["email"] == email:
            return True
    return False         


def criar_conta(usuarios):
    clear()
    time.sleep(0.2)
    print("=-=-=-=-=-=-=-=-=-=CRIACÃO DE CONTA=-=-=-=-=-=-=-=-=-=")
    
    while True:
        user=str(input("Digite um nome de usuário: ")).strip()
        if len(user) < 5:
            clear() 
            print("Seu nome de usúario tem menos de 5 caracteres, tente novamente ")
            
        elif user in usuarios:
            clear()
            print("Esse usúario já existe, tente novamente.")
            
        else:
            break   

    while True: 
        email=input("Digite seu email: ").strip()
        
        if not email_valido(email):
            print("Email inválido, tente novamente.")
        
        elif email_existe(email, usuarios):
            print("Esse email ja está em uso, tente novamente")
        else:
            break
            
    while True:   
        pswd=pwinput.pwinput("Digite sua senha:", mask='*')
        rpt=pwinput.pwinput("Repita sua senha:", mask='*')

        if pswd == rpt and len(user) >= 5 and len(pswd) >= 5:
            clear()
            print("Você criou sua conta com sucesso!")
            input("Pressione ENTER para voltar ao Menu Principal...")
            break
        elif len(pswd) < 5:
            clear()
            print("Sua senha precisa ter 5 ou mais caracteres.")

        else:
            clear()
            print("As senhas não se batem, tente novamente ")
    usuarios[user] = {
        "senha": pswd,
        "email": email,
        "heroi": None
    }
    
    save_dados(usuarios)

def login(usuarios):
    clear()
    if not usuarios:
        print("Nenhuma conta foi criada ainda, crie sua conta e tente novamente.")
        input("Pressione ENTER para voltar ao Menu Principal:")
        return None
    else: 
        print("=-=-=-=-=-=-=-=-=-=LOGIN=-=-=-=-=-=-=-=-=-=")
        
        while True:
            user=input("Digite seu nome de usúario: ").strip()
            pswd=pwinput.pwinput("Digite sua senha: ", mask="*").strip()
            if user in usuarios and usuarios[user]["senha"] == pswd:
                print(f"Login bem-sucedido, Bem-vindo {user}!")
                input("Pressione ENTER para voltar ao Menu Principal:")
                return user
            else:
                print("Seu nome de usuário ou senha estão incorretos")
                time.sleep(2)
                return None


def edit_conta(usuarios):
    clear()
    print("=-=-=-=-=-=-=-=-=-=GERENCIAMENTO DE CONTAS=-=-=-=-=-=-=-=-=-=")
    

    choice=input("[1] Alterar senha \n[2] Excluir conta \nQual das opções você deseja? ")
            
    while True:
        if choice == "1":
            clear()
            user=input("Digite o usuário que você deseja alterar:")
            if user not in usuarios:
                clear()
                print("Esse usuário não existe, operação cancelada.")
                time.sleep(2)
                break
                
                
            pswd=pwinput.pwinput("Digite a senha atual da conta: ", mask="*")
            if usuarios[user]["senha"] == pswd:
                clear()
                print(f"Identidade de {user} validadada com sucesso.")
                  
                    
                while True:
                    newpswd=pwinput.pwinput("Digite a sua nova senha: ")
                    newpswd2=pwinput.pwinput("Repita a sua nova senha: ")

                    if newpswd == newpswd2:
                        print("Senha alterada com sucesso!")
                        input("Pressione ENTER para voltar para o Menu Principal")
                        usuarios[user]["senha"]=newpswd
                        save_dados(usuarios)  
                        return
                    else:
                        print("As senhas não coincidem, tente novamente")
            else:
                clear()
                print("Senha incorreta, operação cancelada.")
                time.sleep(2)
                break
            
            
        elif choice == "2":
            while True:
                clear()
                user=input("Digite o usuário que você deseja exluir:")
                    
                if user not in usuarios:
                    print("Esse usuário não existe, tente novamente.")
                    time.sleep(1)
                    break
                else:
                    
                    email=input("Digite seu email: ")
                    
                    if usuarios[user]["email"] == email:
                        clear()
                        pswd=pwinput.pwinput("Digite sua senha para continuar com a exclusão da conta: ", mask="*")
                        if usuarios[user]["senha"] == pswd:
                            while True:
                                clear()
                                print(f"Identidade de {user} validada com sucesso.")
                                sure=input("Tem certeza que deseja excluir sua conta? S/N: ").upper()
                                if sure == "S":
                                    print("Sua conta foi excluida com sucesso.")
                                    del usuarios[user]
                                    save_dados(usuarios)
                                    time.sleep(2)
                                    return
                                elif sure == "N":
                                    print("Operação cancelada, voltando ao Menu Principal...")
                                    time.sleep(2)
                                    return
                                else:
                                    clear()
                                    print("Por favor, digite 'S' ou 'N'")
                                    time.sleep(2)
                        else:   
                            clear()
                            print("Senha incorreta, tente novamente.")            
                            time.sleep(1)
                    else:
                        clear()
                        print("Esse email não existe, tente novamente.")
                        time.sleep(1)
