# email_sender
---

## 📨 Objectif du script :
Envoyer un email personnalisé à une liste de destinataires à partir d’un seul compte email (exemple : Gmail).

---

## ✅ Étapes avant de commencer

### 1. Activer l’accès SMTP sur ton compte
- Si tu utilises **Gmail**, active l'**authentification à deux facteurs** si ce n’est pas déjà fait.
- Ensuite, génère un **mot de passe d’application** (App Password) dans tes paramètres Google :
  - [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
  - Sélectionne "Autre" comme application et copie le mot de passe généré.

> Tu auras besoin de :
> - Ton adresse email (ex: `tonemail@gmail.com`)
> - Le mot de passe d’application généré

---


## 🔧 Étapes à suivre :

1. **Installe Python** sur ton ordinateur si ce n’est pas encore fait.
2. **Ouvre un éditeur de texte** ou IDE (VSCode, Thonny, IDLE…).
3. **Copie-colle** le script ci-dessus.
4. **Modifie les variables** :
   - `sender_email`
   - `app_password`
   - `recipient_emails`
   - `subject` et `body`
5. **Exécute le script** :
   ```bash
   python script_email.py