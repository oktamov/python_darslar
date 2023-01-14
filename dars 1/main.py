from tkinter import *


def kalkulyator(bosh, side):
    Obj_malumotlar = Frame(bosh, borderwidth=4, bd=4, bg="powder blue")
    Obj_malumotlar.pack(side=side, expand=YES, fill=BOTH)
    return Obj_malumotlar


def button(bosh, side, text, command=None):
    Obj_malumotlar = Button(bosh, text=text, command=command)
    Obj_malumotlar.pack(side=side, expand=YES, fill=BOTH)
    return Obj_malumotlar


class kalkulyator_dastur(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('UDAR KALKULYATOR bro')

        oyna = StringVar()
        Entry(self, relief=RIDGE, textvariable=oyna, justify='right'
              , bd=30, bg="powder blue").pack(side=TOP,
                                              expand=YES, fill=BOTH)

        for tozalash_kinobkasi in (["C"]):
            tozala = kalkulyator(self, TOP)
            for ichar in tozalash_kinobkasi:
                button(tozala, LEFT, ichar, lambda
                    Obj_malumotlar=oyna, q=ichar: Obj_malumotlar.set(''))

        for raqam_kinobka in ("789/", "456*", "123-", "0.+"):
            raqamlar_funksiyasi = kalkulyator(self, TOP)
            for tenglik in raqam_kinobka:
                button(raqamlar_funksiyasi, LEFT, tenglik, lambda
                    Obj_malumotlar=oyna, q=tenglik: Obj_malumotlar
                       .set(Obj_malumotlar.get() + q))

        tenglik_kinobkasi = kalkulyator(self, TOP)
        for tenglik in "=":
            if tenglik == '=':
                btntenglik = button(tenglik_kinobkasi, LEFT, tenglik)
                btntenglik.bind('<ButtonRelease-1>', lambda e, s=self,
                                                            Obj_malumotlar=oyna: s.kalkulyatorim(Obj_malumotlar), '+')


            else:
                btntenglik = button(tenglik_kinobkasi, LEFT, tenglik,
                                    lambda Obj_malumotlar=oyna, s=' %s ' % tenglik: Obj_malumotlar.set
                                    (Obj_malumotlar.get() + s))

    def kalkulyatorim(self, oyna):
        try:
            oyna.set(eval(oyna.get()))
        except:
            oyna.set("NOTOGRI YOZDIZ!")


if __name__ == '__main__':
    kalkulyator_dastur().mainloop()


