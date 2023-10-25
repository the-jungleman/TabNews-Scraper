from    main import*
class   PostPage(Page):
    def __init__(self,  master=None):
        Page.__init__(self,master=None)
        tk.Button(self, text="Pagina Inicial",  command=self.back_to_home_page).pack()
        label=tk.Label(self,    text="AAAAAAA")
        label.pack(side="top",fill="both",expand=True)

    def back_to_home_page(self):
        HomePage(self).lift()
