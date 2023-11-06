from bs4 import BeautifulSoup
import  requests
import  tkinter as  tk
import re

def page_set(url):
    url=str(url)
    response=requests.get(url)
    return BeautifulSoup(response.content,'html.parser')

class Page(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master=None)
        global  current_page

    def show(self):
        self.lift()

class   HomePage(Page):
    def __init__(self,master=None):
        tk.Frame.__init__(self, master=None)
        soup=page_set("https://www.tabnews.com.br/")
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
                self.widget = tk.Frame(master)
                self.widget.pack()
                self.button_post_page=tk.Button(self.widget,text=self.post_title+" - "+tab_coins,command=print("a")).pack()

    def post_page(self):
        self.button_home_page=tk.Button(self, text="Pagina Inicial",  command=print(a)).pack()
        self.label=tk.Label(self,    text="AAAAAAA")
        self.label.pack(side="top",fill="both",expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    main = HomePage(root)
    main.pack(side="left", fill="both", expand=True)
    root.mainloop()