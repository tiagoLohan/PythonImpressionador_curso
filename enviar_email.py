import smtplib
import email.message

def enviar_email():
  msg = email.message.Message()
  msg["Subject"] = "Email enviado com Python"
  msg["From"] = "tiiagolohan@gmail.com"
  msg["To"] = "tiago.radinterv@gmail.com"
  msg["Cc"] = "tiiagolohan+copia@gmail.com"

  corpo_email = '''<p>Boa tarde.
  </p><p>Esse é meu primeiro email com Python usando smtplib</p>
  <p>Att., Tiago Lohan</p>'''

  corpo_email = corpo_email.encode("utf-8")

  msg.add_header("Content-Type", "text/html")
  msg.set_payload(corpo_email)

  servidor = smtplib.SMTP("smtp.gmail.com", 587)
  servidor.starttls()
  servidor.login(msg["From"], "rttn lksp nhbp upqy")
  servidor.send_message(msg)
  servidor.quit()
  print("E-mail enviado!")


enviar_email()
