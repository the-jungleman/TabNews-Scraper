from bs4 import BeautifulSoup
import  requests
import  tkinter as  tk
import re
import  os,sys

class Page(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master=None)

    def show(self):
        self.lift()

class   HomePage(Page):
    def __init__(self,master=None):
        tk.Frame.__init__(self, master=None)
        self.soup=self.page_set("https://www.tabnews.com.br/")
        self.div_post=self.soup.find(class_='Box-sc-g0xbh4-0 kRPWSL')
        self.div_post_elements=self.div_post.find_all(class_="Box-sc-g0xbh4-0 fXxQUH")

        for element in  self.div_post_elements:
            for tab_coins   in  self.div_post_elements:
                tab_coins=element.find(class_="Text-sc-17v1xeu-0 bLDAWn").text.strip()
                self.regex_syntax = r"\D"
                self.num_str = re.sub(self.regex_syntax, "", tab_coins)
                self.tab_coins_num = int(self.num_str)
            if  self.tab_coins_num>10:
                self.widget = tk.Frame(master)
                self.widget.pack()
                self.post_title=element.find(class_="Box-sc-g0xbh4-0 cMZbkX").text.strip()
                self.button_post_page=tk.Button(self.widget,text=self.post_title+" - "+tab_coins)
                
                self.home_page_index()

    def home_page_index(self):
        self.button_post_page.pack()
        self.url_lambda=lambda x=self.soup.find('a', string=self.post_title): self.get_lambda_url(x)
        self.post_url=self.button_post_page.config(command=self.url_lambda)
        self.buttons=[self.button_post_page]
        self.button_id=str(self.buttons)

    def get_lambda_url(self,url):
        self.clear_frame()
        self.urls=[url]
        self.url_list=[link['href'] for link in self.urls]
        self.url_string=str(self.url_list).strip('[]').strip("'")
        print(self.url_string)
        self.post_page()
        
    def post_page(self):
        self.clear_frame()
        self.page_set("https://www.tabnews.com.br"+self.url_string)
        # self.button_home_page=tk.Button(self, text="Pagina Inicial",  command=print("a")).pack()
        return  self.soup.get_text()

    def clear_frame(self):
        for widget in main.winfo_children():
            widget.destroy()
        main.pack_forget()

    def page_set(self,url):
        self.response=requests.get(url)
        return BeautifulSoup(self.response.content,'html.parser')

if __name__ == "__main__":
    os.system("clear")
    root=tk.Tk()
    main = HomePage(root)
    main.pack(side="left", fill="both", expand=True)
    root.mainloop()