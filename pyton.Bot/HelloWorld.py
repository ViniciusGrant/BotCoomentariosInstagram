from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import schedule

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Vinícius Grant\Desktop\pyton.Bot\geckodriver.exe")


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/p/COJaQCNh0cT/")

        time.sleep(10)

        botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?next=%2F&source=logged_out_half_sheet']")
        botao_login.click()

        time.sleep(10)

        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)

        time.sleep(10)

        # botao_agrNao = driver.find_element_by_xpath("//button[contains(text(),'Agora não')]").click()
        driver.get("https://www.instagram.com/p/COMFZ2tJNX6/?igshid=eqomngdehzx2")

    

        def Comentar():
            driver.find_element_by_class_name('Ypffh').click()
            campo_comentario = driver.find_element_by_class_name('Ypffh')
            campo_comentario.send_keys("Uhul")
            campo_comentario.send_keys(Keys.RETURN)
        
        def Atualizar():
            driver.get("https://www.instagram.com/p/COMFZ2tJNX6/?igshid=eqomngdehzx2")

        schedule.every(63).seconds.do(Comentar)
        schedule.every(5).minutes.do(Atualizar)
        

        while 1:
            schedule.run_pending()
            time.sleep(1)




grantBot = InstagramBot('granolasorteio','RE160756')
grantBot.login()
