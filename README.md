# Youtube Embedded for Kodi 📺

<p align="center">
  <img src="icon.png" width="128" height="128" Alt="Youtube Embedded Icon">
</p>

<p align="center">
  <a href="https://kodi.tv/"><img src="https://img.shields.io/badge/Kodi-v19%2B-blue.svg" alt="Kodi Version"></a>
  <a href="https://python.org/"><img src="https://img.shields.io/badge/Python-3.x-yellow.svg" alt="Python Version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-green.svg" alt="License"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/Language-Español-red.svg" alt="Español"></a>
</p>

---

### ⚠️ Maintenance Notice

<p align="center">
  <img src="pocomantenido.gif" alt="Maintenance Warning" width="400">
</p>

> [!WARNING]
> This repository is **not actively maintained** by the Inled Group core team. It works as a proof of concept and we use it internally, but updates are infrequent. We highly encourage you to tinker with it and submit Pull Requests if you find ways to improve it!

---

This Kodi addon allows you to run **Youtube.com/tv** (Leanback mode) directly in a web browser from within Kodi, providing a seamless Smart TV experience on Linux-based systems.

## ✨ Features

- 🖥️ **TV Mode**: Forces the YouTube TV interface by emulating a Smart TV User Agent.
- 🚀 **Kiosk Mode**: Opens the browser in full-screen kiosk mode for a native feel.
- 🐧 **Linux Optimized**: Tailored for Linux distributions.

## 🛠️ Requirements

To use this addon, you need to have the following installed on your system:

- **Python 3.x**
- **Linux Distribution**
- **pynput** (Python library for input monitoring)
- **Web Browser**: Chrome/Chromium is highly recommended for out-of-the-box compatibility.

## 🚀 Installation

1. Download this repository as a `.zip` file.
2. In Kodi, navigate to **Settings** > **Add-ons**.
3. Select **Install from zip file**.
4. Choose the downloaded `.zip` file.

## 🗺️ Roadmap

- [ ] **HDMI-CEC Integration**: Fix current issues with CEC commands passing correctly.
- [ ] **Remote Exit Support**: Map the 'Exit' button on remote controls to close the browser (avoiding the need for a keyboard/Ctrl+W).

## 🤝 Contributing

Every Pull Request is welcome! Since this is not a priority project for us, we rely on the community to keep it functional and polished. Feel free to fork it, break it, and fix it!

## 📖 How it Works

The addon launches Chrome/Chromium pointing to `youtube.com/tv`, forcing a specific User Agent so Google serves the TV-optimized interface. 
It also attempts to capture exit/escape key presses to return control to Kodi gracefully.

---

*Developed by [Inled Group](https://inled.es).*
