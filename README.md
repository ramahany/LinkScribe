# 📄 LinkScribe – AI-Powered Link Summarizer

**LinkScribe** is a simple yet powerful desktop app that takes an Excel sheet filled with URLs, applies a custom prompt to each one using an LLM (via [Groq](https://groq.com/)), and returns an Excel file with summarized content—clean, fast, and customizable.

![app-preview](screenshots/app-main-window.png)

---

## 🚀 Features

- 🔗 Process and summarize content from a list of links in Excel
- ✍️ Use your own custom prompt
- 📊 Clean UI with real-time progress bar (built with `ttkbootstrap`)
- 🧠 Powered by Groq's LLM API
- 📁 Export results to a new Excel file
- ⚙️ Threaded processing for a smooth user experience

---

## 🛠 Tech Stack

- 🐍 Python
- 🖼 `tkinter` & `ttkbootstrap` for UI
- 📊 `pandas` for Excel file handling
- 🔌 `threading` for background summarization
- 🤖 Groq API for AI summarization

---

## 📦 Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/yourusername/LinkScribe.git
   cd LinkScribe
