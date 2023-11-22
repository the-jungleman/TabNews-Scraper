from bs4 import BeautifulSoup
import  requests
import  tkinter as  tk
from tkinter.ttk import *
import re
import  os,sys
import  asyncio

class Page(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master=None)

    async   def show(self):
        self.lift()

    def page_set(self,url):
        self.response=requests.get(url)
        return BeautifulSoup(self.response.content,'html.parser')

class   HomePage(Page,tk.Frame):
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
                self.button_post_page.pack()
                
                self.button_post_page.config(command=self.url_lambda_function)
        
    def url_lambda_function(self):
        self.url_lambda=lambda x=self.soup.find('a', string=self.post_title): self.get_lambda_url(x)
        PostPage(root, url_string=self.url_lambda())

    def get_lambda_url(self,url):
        self.urls=[url]
        self.url_list=[link['href'] for link in self.urls]
        self.url_string=str(self.url_list).strip('[]').strip("'")
        return  self.url_string

class PostPage(HomePage,tk.Frame,tk.Toplevel):
    def __init__(self, master = None,url_string=None):
        tk.Frame.__init__(self, master=None,)
        self.soup = self.page_set(f"https://www.tabnews.com.br{url_string}")
        self.post_page_window = tk.Toplevel(root)

        self.widget = tk.Frame(master)
        self.widget.pack()
        self.button_aa=tk.Button(self.widget, text="aaa").pack


if __name__ == "__main__":
    os.system("clear")
    root=tk.Tk()
    main = HomePage(root)
    main.pack(side="left", fill="both", expand=True)
    root.mainloop()