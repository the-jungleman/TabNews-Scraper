from bs4 import BeautifulSoup
import  requests
import  tkinter as  tk
from tkinter.ttk import *
from tkhtmlview import HTMLLabel,HTMLText
import re
import html2text
import  os,sys

class Page(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master=None)
    
    def close_window(self):
        self.master.destroy()

class   HomePage(Page,tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)

        url=("https://www.tabnews.com.br/")
        self.response=requests.get(url)
        self.soup=BeautifulSoup(self.response.content,'html.parser')


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
        
            self.url_lambda_function()
        
    def url_lambda_function(self):
        self.url_lambda=lambda x=self.soup.find('a', string=self.post_title): self.get_lambda_url(x)
        self.post_url=self.button_post_page.config(command=self.url_lambda)
        self.buttons=[self.button_post_page]
        self.button_id=str(self.buttons)

    def get_lambda_url(self,url):
        self.urls=[url]
        self.url_list=[link['href'] for link in self.urls]
        self.url_string=str(self.url_list).strip('[]').strip("'")
        self.new_window()

    def new_window(self):
        self.new_window=tk.Toplevel(self.master)
        self.app=PostPage(self.new_window,)
    
    def close_hp_window(self):
        self.root.destroy()

class PostPage(HomePage,tk.Frame,tk.Toplevel):
    def __init__(self, master,):
        self.master=master
        self.frame=tk.Frame(master)
        master.title("a")

        # self.home_page=HomePage(self)
        # self.home_page.close_hp_window()

        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_window)
        self.quitButton.pack()

        self.frame.pack()

        self.post_link=f"https://www.tabnews.com.br{main.url_string}"
        self.response=requests.get(self.post_link)
        html_content=self.response.content
        soup=BeautifulSoup(html_content,'html.parser')
        
        rendered_html=html2text.html2text(str(soup))

        self.html_text_label=tk.Label(self.frame,text=rendered_html,width=80, height=20)

        self.html_label=HTMLLabel(self.frame,html="")
        self.html_label.pack(expand=True, fill='both')
        self.html_label.set_html(rendered_html)

    # def close_window_post(self):
        # self.master.destroy()
        # self.top=tk.Toplevel(self.master)
        # top.HomePage(self)
        # HomePage.tk.Toplevel(self.master)

if __name__ == "__main__":
    os.system("clear")
    root=tk.Tk()
    main = HomePage(root)
    main.pack(side="left", fill="both", expand=True)
    root.mainloop()