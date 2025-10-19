import pwinput
import json
import os
import time
from knight import knight
from thief import thief
from mago import mago


jsonfile= "usuarios.json"

def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")


def load_dados():
    if os.path.exists(jsonfile):
        with open(jsonfile, "r") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}
    return {}

def save_dados(dados):
    with open(jsonfile, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def level_up(heroi):
    level_atual = heroi.get("level", 1)
    xp_atual = heroi.get("xp", 0) 
    xp_need = level_atual*100
    while xp_atual >= xp_need:
        heroi["level"] += 1
        heroi["xp"] -= xp_need
        clear()
        print("="*40)
        print(f"      PARABÉNS {heroi['nome']}! VOCÊ SUBIU DE NÍVEL!")
        print(f"         NÍVEL {heroi['level']} ALCANÇADO!")
        print("="*40)
        time.sleep(3)
        
        xp_atual=heroi["xp"]
        level_atual=heroi["level"]
        xp_need=level_atual*100

def view_hero(user_atual, all_users):
    clear()
    dados_heroi=all_users[user_atual]["heroi"]
    heroname=dados_heroi["nome"]
    classe_heroi=dados_heroi["classe"]
    level=dados_heroi["level"]
    xp=dados_heroi["xp"]
    
    if classe_heroi == "Guerreiro":
        print(f"Nome: {heroname} | Classe: {classe_heroi} | Nível: {level} | XP: {xp}/{level*100}")
        print(knight())
        input("Pressione ENTER para voltar...")
    elif classe_heroi == "Mago":
        print(f"Nome: {heroname} | Classe: {classe_heroi} | Nível: {xp}/{level*100}")
        print(mago())
        input("Pressione ENTER para voltar...")
    else:
        print(f"Nome: {heroname} | Classe: {classe_heroi} | Nível: {xp}/{level*100}")
        print(thief())
        input("Pressione ENTER para voltar...")





def criar_heroi(usuario, all_users):
    clear()
    print(f"Bem-vindo pela primeira vez ao Questify {usuario}!")
    time.sleep(1)
    print("Antes de começar sua jornada, é necessário criar um Herói.")
    time.sleep(2)
    
    while True:
        heroname = input("Qual será o nome do seu Herói?: ")
        if len(heroname) < 3:
            print("O nome do seu Herói precisa ter 3 ou mais caracteres")
            time.sleep(1)
            clear()
        else:
            break    
        
    print(f"Ótimo nome, {heroname}!")
    time.sleep(1)
    print("Escolha a classe do seu Herói: ")
    time.sleep(2)
    
    while True:
        print(knight())
        time.sleep(3)
        clear()
       
        print(mago())
        time.sleep(3)
        clear()
        
        print(thief())
        time.sleep(3)
        clear()
        choice = input("[1] GUERREIRO \n[2] MAGO \n[3] LADRÃO \n[4] VISUALIZAR NOVAMENTE \nQual sua classe?: ")
        classe_heroi = None
        
        if choice == "1":
            classe_heroi = "Guerreiro"
        elif choice == "2":
            classe_heroi = "Mago"
        elif choice == "3":
            classe_heroi = "Ladrão"
        elif choice == "4":
            continue
        else:
            print("Número inválido, tente novamente.")
            continue

        dados_heroi = {
                "nome": heroname,
                "classe": classe_heroi,
                "level": 1,
                "xp": 0,          
                "quests": []     
            }
        all_users[usuario]["heroi"] = dados_heroi
        print(f"Parabéns, seu Herói {heroname}, o {classe_heroi}, foi criado com sucesso.")
        input("Pressione ENTER para continuar...")
        return dados_heroi


def add_quests(user_logado, all_users):
    clear()
    herodata= all_users[user_logado].get("heroi")
    lista_quests= herodata.setdefault("quests", [])
    if len(lista_quests) > 5:
        print("Você adicionou o máximo de Quests de uma vez, complete ou exclua uma e tente novamente!")
        time.sleep(2)
        
    
    while True:
        clear()
        print("=-=-=-=-=-=ADICIONAR QUEST=-=-=-=-=-=-=")
        quest_title=input("Digite o título da sua Quest: ").strip()
        
        if len(quest_title) > 100:
            print("O título está muito grande, tente novamente.")
            time.sleep(2)

        elif len(quest_title) == 0:
            print("O título da Quest não pode estar vazio.")
            time.sleep(2)
        
        else:
            break
            
    dificuldades={
        "1": {"nome": "Fácil", "xp": 30},
        "2": {"nome": "Média", "xp": 60},
        "3": {"nome": "Difícil", "xp": 120}
    }
    
    
    
    while True:
        print(f"Quest:{quest_title} \n[1] FÁCIL (30XP) \n[2] MÉDIA (60XP) \n[3] DIFÍCIL (120XP)")
        diff=input("Escolha o nível de dificuldade que essa tarefa representa para você: ")
        if diff in dificuldades:
            diff_selected= dificuldades[diff]
            break
        else:
            print("Opção inválida, digite 1, 2 ou 3!")
            time.sleep(2)

    new_quest={
        "título": quest_title,
        "dificuldade": diff_selected["nome"],
        "xp": diff_selected["xp"],
        "status": "ativa"
    }
    
    lista_quests.append(new_quest)
    save_dados(all_users)
    print(f"Quest {quest_title} adicionada com sucesso!")
    input("Pressione ENTER para voltar...")


def edit_quests(user_logado, all_users):
    while True:
        clear()
        heroi=all_users[user_logado]["heroi"]
        lista_quests=heroi.get("quests", [])
        if not lista_quests:
            print("Você não possui nenhuma quest ativa no momento.")
            input("Pressione ENTER para voltar...")
            return
        clear()
        print("=-=-=-=-=-=GERENCIAMENTO DE QUESTS=-=-=-=-=-=-=")    
        print("Suas quests: ")
        for a, quest in enumerate(lista_quests, 1):
            print(f"[{a}] {quest['título']} ({quest['dificuldade']}) - ({quest['xp']} XP)")
            
        print("\n\n[C] Concluir quest \n[E] Excluir quest \n[V] Voltar")
        choice=input("O que você deseja fazer?: (C/E/V): ").upper()
        if choice == "V":
            return
     
        elif choice in ["C", "E"]:
            try:
                quest_num= int(input("Digite o número da quest: "))
                if 1 <= quest_num <= len(lista_quests):
                            
                    index_select= quest_num - 1
                    quest_select= lista_quests[index_select]
                    if choice == "C":
                        clear()
                        xp_ganho = quest_select["xp"]
                        print(f"{quest_select['título']} concluída!")
                        lista_quests.pop(index_select)
                        heroi["xp"] += xp_ganho
                        level_up(heroi)
                        save_dados(all_users)
                        time.sleep(2)
                            
                    elif choice == "E":
                        clear()
                        confirm=input(f"Tem certeza que deseja excluir a quest {quest_select['título']}? (S/N): ").upper()
                        if confirm == "S":
                            lista_quests.pop(index_select)
                            save_dados(all_users)
                            print("Quest excluída com sucesso!")
                            input("Pressione ENTER para voltar...")
                        else:
                            print("Operação cancelada")
                            time.sleep(2)
                            
                    elif choice == "V":
                        return
                            
                    else:
                        print("Opção inválida.")
                        time.sleep(1)
                        clear()
                else: 
                    print("Não existe quest com esse número!")
                    time.sleep(2)
            except ValueError:
                print("Entrada inválida, digite um número. ")
                time.sleep(2)


def startgame(user_atual, all_users):
    clear()
    dados_heroi = all_users[user_atual].get("heroi")
    
    if dados_heroi is None:
        dados_heroi = criar_heroi(user_logado, all_users)
        save_dados(all_users)
        
        
    
    else:
        clear()
        print(f"=-=-=-=-=-=-=-=-=-= BEM-VINDO AO QUESTIFY, {user_atual}! =-=-=-=-=-=-=-=-=-=")
        time.sleep(2) 
         
        while True:
            clear()
            heroi=all_users[user_atual]["heroi"]
            heroname= dados_heroi["nome"]
            xp= dados_heroi["xp"]
            level=dados_heroi["level"]
            
            print(f"Painel do Herói {heroname} | Nível: {level} | XP: {xp}/{level*100} \n[1] Adicionar Quest \n[2] Gerenciar Quests \n[3] Visualizar Herói \n[4] Voltar ao Menu")
            ingame=input("Digite a opção que você deseja: ")

            if ingame == "1":
                add_quests(user_atual, all_users)
            
            elif ingame == "2":
                edit_quests(user_atual, all_users)
            
            elif ingame == "3":
                view_hero(user_atual, all_users)
            
            elif ingame == "4":
                print("Voltando ao menu...")
                break
            else:
                print("Opção inválida, tente novamente!")
            
            



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