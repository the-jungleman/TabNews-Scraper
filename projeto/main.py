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
                self.post_title=element.find(class_="Box-sc-g0xbh4-0 cMZbkX").text.strip()
                self.widget = tk.Frame(master)
                self.widget.pack()
                self.button_post_page=tk.Button(self.widget,text=self.post_title+" - "+tab_coins)
                self.button_post_page.pack()
                self.button_post_page.config(command=lambda x=self.button_post_page.cget("text"): print(x))
    
    def page_set(self,url):
        self.url=str(url)
        self.response=requests.get(url)
        return BeautifulSoup(self.response.content,'html.parser')

    def get_post_url(self):
        self.href_value = self.soup.find('a', string=self.button_text)
        for e   in  self.buttons_post:
            for a_tag in self.soup.find('a'):
                self.href_value = [a_tag.get('href')]   
                print(self.href_value)
        self.button_text = self.button_post_page['text']
        
    # def post_page(self):
        # for widget in self.winfo_children():
            # widget.destroy()
        # self.button_home_page=tk.Button(self, text="Pagina Inicial",  command=print("a")).pack()


if __name__ == "__main__":
    os.system("clear")
    root=tk.Tk()
    main = HomePage(root)
    main.pack(side="left", fill="both", expand=True)
    root.mainloop()