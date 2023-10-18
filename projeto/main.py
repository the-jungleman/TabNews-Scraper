from bs4 import BeautifulSoup
import  requests
import  tkinter
url="https://www.tabnews.com.br/"
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')

tempo_post=soup.find(class_="Tooltip__TooltipBase-sc-uha8qm-0 hsZHZO tooltipped-nw").text.strip()
print(tempo_post)
div_post=soup.find(class_='Box-sc-g0xbh4-0 kRPWSL')
div_post_elements=div_post.find_all(class_="Box-sc-g0xbh4-0 fXxQUH")
for elements    in  div_post_elements:
    element_text=elements.text.strip()
    print(element_text)

class   App:
    def __init__(self,master=None):
        pass
root=Tk()
App(root)
root.mainloop()
