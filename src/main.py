from customtkinter import * # Importa a biblioteca customtkinter para a interface gráfica personalizada
from modules.search_cep import search_cep # Importa a função searchCep do módulo functions para buscar informações de CEP
from time import sleep # Importa a função sleep da biblioteca time para adicionar um atraso visual

# Função para limpar os campos de texto da interface
def clear():
    text.configure(text="")
    text_cep.configure(text="")
    text_rua.configure(text="")
    text_bairro.configure(text="")
    text_cidade.configure(text="")
    text_ddd.configure(text="")

# Função para buscar e exibir as informações do CEP digitado pelo usuário
def print_cep():
    clear()  # Limpa os campos de texto

    # Exibe a mensagem de carregamento
    loading.configure(text="Carregando....")
    loading.place(x=115, y=165)  # Posiciona a mensagem no centro da tela
    tela.update()  # Atualiza a interface para exibir a mensagem

    sleep(1)  # Aguarda 1 segundo para simular um carregamento

    cep = search_cep(cep_input.get())  # Busca as informações do CEP

    if isinstance(cep, dict):
        # Se as informações do CEP foram obtidas com sucesso, exibe os dados nos campos de texto
        text.pack_forget()  # Esconde o texto padrão
        text_cep.configure(text=f"Cep: {cep['Cep']}")
        text_rua.configure(text=f"Rua: {cep['Rua']}")
        text_bairro.configure(text=f"Bairro: {cep['Bairro']}")
        text_cidade.configure(text=f"Cidade: {cep['Cidade']}")
        text_ddd.configure(text=f"DDD: {cep['DDD']}")
    else:
        # Se houve algum erro na busca do CEP, exibe a mensagem de erro
        text.configure(text=cep, pady = 4)

    loading.place_forget()  # Esconde a mensagem de carregamento
    tela.update()  # Atualiza a interface para refletir as mudanças

# Cria a janela principal da aplicação
tela = CTk()
tela.title("Buscar Cep") # Define o titulo
tela.geometry("300x350") # Define a resolução da janela
tela.resizable(width=False, height=False) # Define a redimencão da janela
tela._set_appearance_mode("dark")  # Define o modo escuro para a interface

# Cria e posiciona os elementos da interface
text_orientation = CTkLabel(tela, text="Buscar Cep")
text_orientation.pack(padx=10, pady=5)

cep_input = CTkEntry(tela)
cep_input.pack(padx=10, pady=5)

button_search_cep = CTkButton(tela, text="Search", command=print_cep)
button_search_cep.pack(padx=10, pady=5)

button_clear = CTkButton(tela, text="Clear", command=clear)
button_clear.pack(pady = 5)

loading = CTkLabel(tela, text="")

text = CTkLabel(tela, text="")
text.pack(pady=15)

text_cep = CTkLabel(tela, text="")
text_cep.pack(pady=(15,1))  # Adiciona espaço extra acima e abaixo do texto

text_rua = CTkLabel(tela, text="")
text_rua.pack()

text_bairro = CTkLabel(tela, text="")
text_bairro.pack()

text_cidade = CTkLabel(tela, text="")
text_cidade.pack()

text_ddd = CTkLabel(tela, text="")
text_ddd.pack()

tela.mainloop()  # Inicia o loop principal da interface gráfica
