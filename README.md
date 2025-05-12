# 🧠 Pi Trainer

**Pi Trainer** est une application interactive en Streamlit conçue pour entraîner ta mémoire à retenir les décimales de π (pi). Génère aléatoirement une suite de chiffres, puis essaie de deviner les 10 décimales suivantes. Ludique, progressif, et sans pression !

---

## 🚀 Fonctionnalités

- 🎲 Génération aléatoire d’une suite de 5 décimales de π
- 🧩 Entrée utilisateur : complète les 10 décimales suivantes
- ✅ Vérification automatique de ta réponse
- 🎉 Animations et messages de feedback
- 📏 Personnalisation de la plage de décimales à mémoriser
- 🎨 Interface propre et interactive via [Streamlit](https://streamlit.io)

---

## 📁 Structure du projet

pi-trainer/
│
├── app.py # Application principale Streamlit
├── pi.txt # Fichier contenant les décimales de π (en une seule ligne)
├── README.md # Ce fichier

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