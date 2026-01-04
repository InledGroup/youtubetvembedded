# Youtube Embedded para Kodi 📺

<p align="center">
  <img src="icon.png" width="128" height="128" Alt="Youtube Embedded Icon">
</p>

<p align="center">
  <a href="https://kodi.tv/"><img src="https://img.shields.io/badge/Kodi-v19%2B-blue.svg" alt="Versión de Kodi"></a>
  <a href="https://python.org/"><img src="https://img.shields.io/badge/Python-3.x-yellow.svg" alt="Versión de Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Licencia-GPL--3.0-green.svg" alt="Licencia"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/Language-English-blue.svg" alt="English"></a>
</p>

---

### ⚠️ Aviso de Mantenimiento

<p align="center">
  <img src="pocomantenido.gif" alt="Aviso de mantenimiento" width="400">
</p>

> [!WARNING]
> Este repositorio **no es de los principales** de Inled Group y no se actualiza con frecuencia. Funciona como prueba de concepto y para uso interno. Te animamos a trastear, probar mejoras y enviarnos tus Pull Requests ;)

---

Este addon para Kodi permite ejecutar **Youtube.com/tv** (modo Leanback) directamente en un navegador desde Kodi, proporcionando una experiencia de Smart TV en sistemas basados en Linux.

## ✨ Características

- 🖥️ **Modo TV**: Fuerza la interfaz de YouTube TV emulando el User Agent de una Smart TV.
- 🚀 **Modo Kiosk**: Abre el navegador a pantalla completa para una experiencia integrada.
- 🐧 **Optimizado para Linux**: Diseñado específicamente para distribuciones Linux.

## 🛠️ Requisitos

Para usar este addon, necesitas tener instalado en tu sistema:

- **Python 3.x**
- **Distribución Linux**
- **pynput** (Librería de Python para monitorización de entrada)
- **Navegador Web**: Se recomienda Chrome/Chromium para evitar configuraciones adicionales.

## 🚀 Instalación

1. Descarga este repositorio como un archivo `.zip`.
2. En Kodi, ve a **Ajustes** > **Addons**.
3. Selecciona **Instalar desde un archivo .zip**.
4. Elige el archivo `.zip` descargado.

## 🗺️ Roadmap

- [ ] **Integración HDMI-CEC**: Corregir fallos actuales con el envío de comandos CEC.
- [ ] **Soporte para botón Exit**: Mapear el botón 'Exit' del mando a distancia para cerrar el navegador (evitando usar el teclado/Ctrl+W).

## 🤝 Contribuciones

¡Cualquier Pull Request es bienvenida! Al no ser un proyecto prioritario para nosotros, dependemos de la comunidad para mantenerlo funcional. ¡No dudes en hacer un fork y mejorarlo!

## 📖 Funcionamiento

El addon inicia Chrome/Chromium apuntando a `youtube.com/tv`, forzando un User Agent específico para que Google sirva la interfaz optimizada para TV. 
También intenta capturar las pulsaciones de las teclas de salida/escape para devolver el control a Kodi de forma elegante.

---

*Desarrollado por [Inled Group](https://github.com/inled).*
