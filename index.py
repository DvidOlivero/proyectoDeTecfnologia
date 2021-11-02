from tkinter import *
from tkinter import messagebox
from time import sleep
from selenium import webdriver
import pyttsx3
from pathlib import Path
import threading


class HooverButton(threading.Thread):  # Clase para aplicar efecto hoover
    def __init__(self, window, colorOne, colorThwo, command, text=None, iPadx=None, iPady=None,
                 Pady=None, sizeX=None, sizeY=None, borderWidth=None):
        threading.Thread.__init__(self)

        # Iniciación de variables
        self.window = window
        self.colorOne = colorOne
        self.colorThwo = colorThwo
        self.command = command
        self.text = text
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.iPadx = iPadx
        self.iPady = iPady
        self.borderWidth = borderWidth
        self.Pady = Pady

        self.button = Button(self.window, text=self.text,
                             borderwidth=self.borderWidth, command=self.command)
        self.button.configure(width=self.sizeX, height=self.sizeY)
        self.button.bind('<Enter>', lambda e: e.widget.config(bg=self.colorOne))
        self.button.bind('<Leave>', lambda e: e.widget.config(bg=self.colorThwo))
        self.button.pack(expand=True, pady=self.Pady, ipadx=self.iPadx, ipady=self.iPady)


class WindowPrincipal(threading.Thread):  # Clase principal
    def __init__(self, run):  # Función de inicio -> creación de la ventana principal
        threading.Thread.__init__(self)
        # Iniciando la variable run
        self.window = run
        # Ícono de la ventana
        self.Icon(self.window)
        # Título de la ventana
        self.window.title("Instagram Security")
        self.window.geometry("300x500")  # Tamaño de la ventana
        self.window.configure(bg="dark turquoise")  # Color de la ventana
        # Botón asegurar con efecto hoover
        self.buttonAsegurar = HooverButton(self.window, 'pale turquoise', 'white', self.LogIn_with_Instagram,
                                           'Asegurar', sizeX=14, sizeY=4, Pady=170, borderWidth=2)

    def LogIn_with_Instagram(self):
        self.window2 = Toplevel()  # Generar ventana de LogIn with Instagram
        self.Icon(self.window2)  # Ícono de la ventana
        self.window2.title('Acceder')  # Título de la ventana
        self.window2.geometry('300x200')  # Tamaño de la ventana
        self.window2.configure(bg='pale goldenrod')  # Color de la ventana

        self.labelTitle = Label(self.window2, text='Acceder', font=('System', 11,
                                                                    'bold'), bg='pale goldenrod')  # Título "Acceder"
        self.labelTitle.pack()

        # Bloque username
        self.labelUsername = Label(self.window2, bg='pale goldenrod',
                                   text='Correo o celular')  # Título de el imput username
        self.labelUsername.pack()
        # Imput username
        self.entryUsername = Entry(self.window2)
        self.entryUsername.focus()
        self.entryUsername.pack(ipadx=20, pady=10)

        # Bloque password
        self.labelPassword = Label(self.window2, bg='pale goldenrod',
                                   text='Contraseña')  # Título de imput password
        self.labelPassword.pack()
        # Imput password
        self.entryPassword = Entry(self.window2, show='*')
        self.entryPassword.pack(ipadx=20, pady=10)

        # Opción del check para iniciar con facebook
        self.selfacebook = IntVar()
        self.checkFace = Checkbutton(self.window2,
                                     text='Solo usasar mi cuenta de facebook',
                                     variable=self.selfacebook, onvalue=1, offvalue=0)
        self.checkFace.configure(bg='pale goldenrod')
        self.checkFace.pack()

        self.buttonNext = HooverButton(self.window2, 'pale goldenrod', 'white',
                                       self.Get_instagram, 'Siguiente', iPadx=10, iPady=5).start()

    def LogIn_with_Facebook(self):
        self.window2.destroy()
        self.window3 = Toplevel()
        self.Icon(self.window3)
        self.window3.title('Acceder')
        self.window3.geometry('300x200')
        self.window3.configure(bg='dodger blue')
        self.labelTitle2 = Label(self.window3, text='Acceder', font=('System', 11,
                                                                     'bold'),
                                 bg='dodger blue')
        self.labelTitle2.pack()
        self.labelUsername2 = Label(self.window3, bg='dodger blue',
                                    text='Correo o celular')
        self.labelUsername2.pack()
        self.entryUsername2 = Entry(self.window3)
        self.entryUsername2.focus()
        self.entryUsername2.pack(ipadx=20, pady=10)
        self.labelPassword2 = Label(self.window3, bg='dodger blue', text='Contraseña')
        self.labelPassword2.pack()
        self.entryPassword2 = Entry(self.window3, show='*')
        self.entryPassword2.pack(ipadx=20, pady=10)
        self.buttonFacebook = HooverButton(self.window3, 'dodger blue', 'white', self.Get_facebook,
                                           'Siguiente', iPadx=10, iPady=5).start()


    def CkeckingLogin(self):
        if checkFace.get() == 0:
            self.Get_Instagram()

        else:
            self.LogIn_with_Facebook()
    
    
    def GetWebs(self, mail, password):
        self.mail = mail
        self.password = password
        self.linkTiwitter = "https://www.instagram.com/"
        self.entrys = False
        self.value = False
        while True:
            try:
                self.driver = webdriver.Firefox()
                break
            except Exception:
                pass

        if self.selfacebook.get() != 1:
            self.window2.destroy()
            self.entrys = True
            while True:
                try:
                    self.driver.get(self.linkTiwitter)
                    break
                except Exception:
                    pass
            while True:
                try:
                    sleep(2)
                    self.camposemailorcel = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/'
                                                                              'div[2]/div[1]/div/form/div/div[1]/'
                                                                              'div/label/input')
                    self.camposemailorcel.send_keys(self.mail)
                    self.campospassword = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/'
                                                                            'div[2]/div[1]/div/form/div/div[2]/div/'
                                                                            'label/input')
                    self.campospassword.send_keys(self.password)
                    self.buttonnext = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/'
                                                                        'div[2]/div[1]/div/form/div/div[3]/button/'
                                                                        'div')
                    self.buttonnext.click()
                    break
                except Exception:
                    pass

            try:
                sleep(3)
                self.buttonnext = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                                                    '/div[2]/div[1]/div/form/div[1]/div[3]/'
                                                                    'button/div')
                self.buttonnext.click()
                self.messageImportant('El usuario o contraseña ingresado es incorrecto. Inténtelo de nuevo')
                quit()
            except Exception:
                pass
            try:
                sleep(11)
                self.buttonNone = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div'
                                                                    '/div/div/button')
                self.buttonNone.click()
            except Exception:
                pass

        else:
            while True:
                try:
                    self.driver.get(self.linkTiwitter)
                    break
                except Exception:
                    pass
            sleep(2)
            self.accessWithFacebook = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/'
                                                                        'article/div[2]/div[1]/div/form/div/'
                                                                        'div[5]/button/span[2]')
            self.accessWithFacebook.click()
            while True:
                try:
                    sleep(1)
                    self.usernameFacebook = self.driver.find_element_by_xpath('//*[@id="email"]')
                    self.usernameFacebook.send_keys(self.mail)
                    break
                except AttributeError:
                    pass
            self.passwordFacebook = self.driver.find_element_by_xpath('//*[@id="pass"]')
            self.passwordFacebook.send_keys(self.password)
            self.buttonNextFacebook = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
            self.buttonNextFacebook.click()

        while True:
            try:
                sleep(3)
                self.notNotification = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div['
                                                                         '3]/button[2]')
                self.notNotification.click()
                break
            except Exception as error:
                print(error)
                try:
                    self.notNotification = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div['
                                                                             '3]/button[2]')
                    self.notNotification.click()
                except Exception:
                    try:
                        sleep(3)
                        self.acount = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div['
                                                                        '3]/div[1]/div/div/div[2]/div[1]/div/div/a')
                        self.acount.click()
                        self.value = True
                        break
                    except Exception:
                        pass
        if not self.value:
            sleep(2)
            self.acount = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div['
                                                            '1]/div/div/div[2]/div[1]/div/div/a')
            self.acount.click()
        while True:
            try:
                sleep(2)
                self.settings = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section'
                                                                  '/div[1]/div[1]/div/a')
                self.settings.click()
                break
            except Exception:
                pass
        if self.entrys and not self.securityPassword:
            sleep(2)
            self.passwordAcount = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/'
                                                                    'li[2]/a')
            self.passwordAcount.click()
            sleep(3)
            self.passworvieja = self.driver.find_element_by_xpath('//*[@id="cppOldPassword"]')
            self.passworvieja.send_keys(self.passwordInstagram)
            self.messageImportant('A continuación coloque su contraseña nueva más segura cuando termines'
                                  'cliquea terminé')
            self.EndWindow(self.EndPassword)
        else:
            sleep(2)
            try:
                self.privacity = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[7]/a')
                self.privacity.click()
            except Exception:
                self.privacity.click()
            while True:
                try:
                    sleep(2)
                    self.acontPrivacity = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/'
                                                                            'article/main/section[1]/div[2]/div/'
                                                                            'div/label/div')
                    self.acontPrivacity.click()
                    break
                except Exception:
                    pass
            sleep(2)
            try:
                self.cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/button[2]')
                self.cancel.click()
            except Exception:
                pass

            self.startOfSesion = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[8]'
                                                                   '/a')
            self.startOfSesion.click()
            self.messageImportant('A continuación se presentan todos los lugares donde has iniciado sesión.Por'
                                  'favor cliquea No he sido yo o cerrar seción en los lugares donde tu no hallas'
                                  'iniciado seción. Cuando hallas terminado cliquea terminé')
            self.EndWindow(self.EndProgram)

    def Get_instagram(self):
        self.mailInstagram = self.entryUsername.get()
        self.passwordInstagram = self.entryPassword.get()
        self.securityPassword = False
        self.parameters = {'later': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                                     'Ñ' 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                           'numbers': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                           'caracter': ['!', '#', '$', '%', '&', '/', '*', '-', '_']
                           }

        if len(self.entryUsername.get()) != 0 and len(self.entryPassword.get()) == 0 \
                or len(self.entryUsername.get()) == 0 and len(self.entryPassword.get()) != 0 \
                or len(self.entryUsername.get()) == 0 and len(self.entryPassword.get()) == 0:
            self.message = messagebox.showwarning('Advertencia',
                                                  'Se necesita completar todos los campos'
                                                  'para continuar')

        else:
            for comprobate in self.passwordInstagram:
                if comprobate in self.parameters['later'] and comprobate in self.parameters['later'.lower()] \
                        and comprobate in self.parameters['numbers'] and comprobate in self.parameters['caracter']:
                    self.securityPassword = True

                else:
                    self.securityPassword = False

            if not self.securityPassword:
                self.messageImportant('Su contraseña no es segura, debe contener por lo menos una letra'
                                      'mayúscula, un caracter y un número. Al final podrá cambiar su'
                                      'contraseña')

            self.GetWebs(self.mailInstagram, self.passwordInstagram)

    def Get_facebook(self):
        if len(self.entryUsername2.get()) != 0 and len(self.entryPassword2.get()) == 0 \
                or len(self.entryUsername2.get()) == 0 and len(self.entryPassword2.get()) != 0 \
                or len(self.entryUsername2.get()) == 0 and len(self.entryPassword2.get()) == 0:
            self.message = messagebox.showwarning('Advertencia',
                                                  'Se necesita completar todos los campos para continuar')

        else:
            self.mailf = self.entryUsername2.get()
            self.passwordf = self.entryPassword2.get()
            self.window3.destroy()
            self.GetWebs(self.mailf, self.passwordf)

    def EndPassword(self):
        self.window4.destroy()
        sleep(2)
        try:
            self.privacity = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[7]'
                                                               '/a')
            self.privacity.click()
        except Exception:
            self.privacity.click()
        sleep(2)
        self.acontPrivacity = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article'
                                                                '/main/section[1]/div[2]/div/div/label/div')
        self.acontPrivacity.click()
        sleep(2)
        try:
            self.cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/button[2]')
            self.cancel.click()
        except Exception:
            pass

        self.startOfSesion = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[8]'
                                                               '/a')
        self.startOfSesion.click()
        self.messageImportant('A continuación se presentan todos los lugares donde has iniciado sesión.Por'
                              'favor cliquea No he sido yo o cerrar seción en los lugares donde tu no hallas'
                              'iniciado seción. Cuando hallas terminado cliquea terminé')

        self.EndWindow(self.EndProgram)

    def Icon(self, window):
        self.window = window
        self.window.iconbitmap(r"{}\Documents\Instagram Security\icon.ico".format(Path.home()))
        return self.window

    def EndWindow(self, porpouse):
        self.porpouse = porpouse
        self.window4 = Toplevel()
        self.Icon(self.window4)
        self.window4.title('Finalizar')
        self.window4.geometry('200x200')
        self.buttonFinished = HooverButton(self.window4, 'orange', 'blue',
                                           self.porpouse, 'Terminé', 30, 30).start()

    def EndProgram(self):
        self.window.quit()
        self.window4.destroy()

    def messageImportant(self, text):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("voice", "spanish")

        engine.say(text)
        engine.runAndWait()


def main():
    run = Tk()
    WindowPrincipal(run).start()
    run.mainloop()


if __name__ == "__main__":
    main()
