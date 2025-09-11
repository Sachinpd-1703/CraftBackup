<p align="center">
  <h1 align="center">MineSave</h1>
  <p align="center">
    A simple command-line tool to automatically backup your Minecraft worlds to Google Drive.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/MineSave?style=for-the-badge&logo=github" alt="Stars">
</p>

---

## 📌 Overview

Minecraft worlds are stored locally on your computer. If your hard drive fails, the world file gets corrupted, or a creeper ruins your masterpiece during LAN play, all your hard work can be lost forever.

**MineSave** solves this problem by creating a timestamped `.zip` backup of your Minecraft world and securely uploading it to your personal **Google Drive**. You can restore any backup with a simple command, ensuring your creations are always safe.

---

## ✨ Features

-   📂 **One-Command Backup:** Save your entire Minecraft world folder with a single command.
-   🔒 **Secure Google Drive Upload:** Uses the official Google Drive API with OAuth2 for secure authentication.
-   🕒 **Timestamped Archives:** Each backup is named with the current date and time (e.g., `MyWorld_2025-09-11_09-30-00.zip`) to prevent overwriting.
-   📥 **Easy Restore:** Lists all available backups and lets you download and restore your chosen version.
-   ⚡ **Cross-Platform:** Built with Python, it works on Windows, macOS, and Linux.

---

## 🚀 Installation & Configuration

Follow these steps to get MineSave up and running.

### Step 1: Clone the Repository
First, clone this repository to your local machine.
```bash
git clone [https://github.com/YOUR_USERNAME/MineSave.git](https://github.com/YOUR_USERNAME/MineSave.git)
cd MineSave