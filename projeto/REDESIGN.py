import tkinter as tk
from bs4 import BeautifulSoup
import  requests
import  re

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Design de Janela Dinâmico")
        self.geometry("400x300")
        self.current_design = 1
        self.create_design()
        url="https://www.tabnews.com.br/"
        self.response=requests.get(url)
        # return BeautifulSoup(self.response.content,'html.parser')
        soup=BeautifulSoup(self.response.content)
        self.current_page=1
        self.show_page()

    def create_design(self):
        if self.current_design == 1:
            self.create_design1()
        elif self.current_design == 2:
            self.create_design2()

    def create_design1(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()
# 
        # Adicionar widgets ao design 1
        self.div_post=soup.find(class_='Box-sc-g0xbh4-0 kRPWSL')
        self.div_post_elements=self.div_post.find_all(class_="Box-sc-g0xbh4-0 fXxQUH")
        for element in  self.div_post_elements:
            for tab_coins   in  self.div_post_elements:
                tab_coins=element.find(class_="Text-sc-17v1xeu-0 bLDAWn").text.strip()
                self.regex_syntax = r"\D"
                self.num_str = re.sub(self.regex_syntax, "", tab_coins)
                self.tab_coins_num = int(self.num_str)
            if  self.tab_coins_num>10:
                self.post_title=element.find(class_="Box-sc-g0xbh4-0 cMZbkX").text.strip()
                # self.widget = tk.Frame(master)
                # self.widget.pack()
                self.button_post_page=tk.Button(self.widget,text=post_title+" - "+tab_coins,command=self.show_page).pack()
        # label = tk.Label(self, text="Design 1")
        # label.pack(pady=20)
        button_change_design = tk.Button(self, text="Mudar Design", command=self.change_design)
        button_change_design.pack()

    def create_design2(self):
        # Limpar a janela
        for widget in self.winfo_children():
            widget.destroy()
        self.button_home_page=tk.Button(self, text="Pagina Inicial",  command=self.back_to_home_page).pack()
        self.label=tk.Label(self,    text="AAAAAAA")
        self.label.pack(side="top",fill="both",expand=True)
# 
        # Adicionar widgets ao design 2
        # label = tk.Label(self, text="Design 2", font=("Arial", 24))
        # label.pack(pady=50)
        entry = tk.Entry(self)
        entry.pack(pady=20)
        button_change_design = tk.Button(self, text="Mudar Design", command=self.change_design)
        button_change_design.pack()

    def change_design(self):
        # Alternar entre designs
        if self.current_design == 1:
            self.current_design = 2
        else:
            self.current_design = 1
        # Criar o novo design
        self.create_design()

if __name__ == "__main__":
    app = App()
    app.mainloop()
