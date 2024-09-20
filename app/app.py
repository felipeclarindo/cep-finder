from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry
from .modules.search_cep import (
    search_cep,
)
from .modules.cep_gui import CepGUI
from time import sleep


class App(CTk):
    """
    Classe principal da aplicação para busca de CEP.
    Herda a classe CTk para criar uma interface gráfica personalizada.
    """

    def __init__(self) -> None:
        """
        Inicializa a interface gráfica, configura e define os widgets da aplicação.
        """
        super(App, self).__init__()

        self.configure_screen()
        self.create_widgets()

    def configure_screen(self) -> None:
        """
        Configurações da interface gráfica (titulo, resoluçãoo e etc)
        """
        self.title("Cep Finder")
        self.geometry("240x210")
        self.resizable(width=False, height=False)
        self._set_appearance_mode("dark")

    def create_widgets(self) -> None:
        """
        Cria e posiciona os widgets (elementos da interface) na janela.
        """
        self.text_orientation = CTkLabel(self, text="Buscar Cep", bg_color=self.cget("bg"), text_color="white")
        self.text_orientation.pack(pady=13)

        self.cep_input = CTkEntry(self, bg_color=self.cget("bg"), placeholder_text="Digite o cep")
        self.cep_input.pack()

        self.button_search_cep = CTkButton(self, text="Search", command=self.print_cep, bg_color=self.cget("bg"), width=80)
        self.button_search_cep.pack(pady=12)

        self.text_result = CTkLabel(self, text="", bg_color=self.cget("bg"), text_color="white")

        self.loading = CTkLabel(self, text="", bg_color=self.cget("bg"), text_color="white")
        self.loading.pack()

    def print_cep(self) -> None:
        """
        Busca e exibe as informações do CEP inserido pelo usuário. Se o CEP for inválido,
        exibe uma mensagem de erro.
        """
        self.clear()

        # Exibe mensagem de carregamento durante a busca
        self.loading.configure(text="Carregando....")
        self.loading.place(x=85, y=143)
        self.update()

        sleep(1)

        cep_data = search_cep(self.cep_input.get())

        # Verifica se o resultado é um dicionário válido com as informações do CEP
        if isinstance(cep_data, dict):
            self.text_result.configure(text=f"Cep encontrado com sucesso.")
            self.text_result.pack(pady=10)
            self.loading.place_forget()
            self.update()

            self.cep_gui = CepGUI(cep_data)
            self.cep_gui.mainloop()
        else:
            self.text_result.configure(text=cep_data)
        
        self.text_result.pack(pady=10)
        self.loading.place_forget()
        self.update()
        
    def clear(self) -> None:
        self.text_result.configure(text="")
