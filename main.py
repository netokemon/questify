import time

from database import load_dados

from authentication import criar_conta, login, edit_conta
from game import startgame
from utils import clear

userdata=load_dados()
user_logado= None

while True:
    clear()
    if user_logado is None:
        print("""\033[31m

  ___  _   _ _____ ____ _____ ___ _______   __
 / _ \| | | | ____/ ___|_   _|_ _|  ___\ \ / /
| | | | | | |  _| \___ \ | |  | || |_   \ V / 
| |_| | |_| | |___ ___) || |  | ||  _|   | |  
 \__\_\\___/|_____|____/ |_| |___|_|     |_|  

\033[0m""")
        
        
        print("\nBem vindo ao Questify! (Faça Login para entrar no jogo.)")
        print("""=-=-=-=-=-=-=-=-=-=MENU PRINCIPAL=-=-=-=-=-=-=-=-=-=
                
        [1] Login
        [2] Criação de conta de usúario
        [3] Gerenciar conta
        [4] Sair do programa""")

        menu=str(input("Qual das opcões você deseja?: "))
        
        if menu == "1":
            user_logado= login(userdata)
            
            
        elif menu == "2":
            criar_conta(userdata)
            
     
        elif menu == "3":
            edit_conta(userdata)
            
        elif menu == "4":
            print("Finalizando programa...")
            time.sleep(2)
            break
        else:
            print("O valor digitado é inválido, tente novamente")
            time.sleep(2)   
    
    
    else:
    
        clear()
        print("""\033[31m

  ___  _   _ _____ ____ _____ ___ _______   __
 / _ \| | | | ____/ ___|_   _|_ _|  ___\ \ / /
| | | | | | |  _| \___ \ | |  | || |_   \ V / 
| |_| | |_| | |___ ___) || |  | ||  _|   | |  
 \__\_\\___/|_____|____/ |_| |___|_|     |_|  

\033[0m""")
        
        
        
        print(f"\nBem vindo ao Questify {user_logado}!")
        print("""=-=-=-=-=-=-=-=-=-=MENU PRINCIPAL=-=-=-=-=-=-=-=-=-=
                
        [1] Iniciar QUESTIFY
        [2] Criação de conta de usúario
        [3] Logout
        [4] Gerenciar conta
        [5] Sair do programa""")

        menu=str(input("Qual das opcões você deseja?: "))
        
        if menu == "1":
            startgame(user_logado, userdata)
        
        
        elif menu == "2":
            criar_conta(userdata)
        
        elif menu == "3":
            print(f"Fazendo logout de {user_logado}...")
            user_logado = None
            time.sleep(2)
            
        elif menu == "4":
            edit_conta(userdata)
        
        elif menu == "5":
            print("Finalizando programa...")
            time.sleep(2)
            break
        else:
            print("O valor digitado é inválido, tente novamente")
            time.sleep(2)   