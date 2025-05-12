# 🧠 Pi Trainer

**Pi Trainer** est une application interactive en Streamlit conçue pour entraîner ta mémoire à retenir les décimales de π (pi).  
Elle te propose aléatoirement une suite de 5 chiffres de π, à toi de retrouver les 10 suivants !

---

## 🚀 Fonctionnalités

- 🎲 Génération aléatoire d’une suite de 5 décimales de π
- 🧩 Entrée utilisateur pour compléter les 10 décimales suivantes
- ✅ Vérification instantanée de ta réponse
- 🎉 Feedback visuel (erreurs, réussite, animations)
- 📏 Personnalisation de la plage de décimales à étudier
- 🎨 Interface simple, accessible et agréable via Streamlit

---

## 📁 Structure du projet

```text
pi-trainer/
├── app.py         # Application principale Streamlit
├── pi.txt         # Fichier contenant les décimales de π (en une seule ligne)
├── requirements.txt # Dépendances Python
└── README.md      # Ce fichier de documentation
```

---

## 📝 Pré-requis

- Python 3.7+
- Fichier `pi.txt` avec au moins 100 décimales (ou jusqu'à 100000 si tu veux un vrai défi !)

---

## ⚙️ Installation

1. Clone ce dépôt :

```bash
git clone https://github.com/ton-utilisateur/pi-trainer.git
cd pi-trainer