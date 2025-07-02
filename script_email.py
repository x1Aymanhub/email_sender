import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Paramètres du serveur SMTP (exemple avec Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "tonemail@gmail.com"
app_password = "tonmotdepasseapplication"

# Liste des destinataires
recipient_emails = ["email1@example.com", "email2@example.com", "email3@example.com"]

# Contenu de l'email
subject = "Sujet de l'email"
body = """
Bonjour,

Ceci est un message envoyé automatiquement via un script Python.

Cordialement,
Ton Nom
"""

# Configuration du serveur SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, app_password)

# Boucle pour envoyer à chaque destinataire
for recipient in recipient_emails:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server.sendmail(sender_email, recipient, msg.as_string())
    print(f"Email envoyé à {recipient}")

# Fermeture de la connexion
server.quit()
print("Tous les emails ont été envoyés.")