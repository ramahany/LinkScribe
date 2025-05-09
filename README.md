# 📄 LinkScribe – AI-Powered Link Summarizer

**LinkScribe** is a simple yet powerful desktop app that takes an Excel sheet filled with URLs, applies a custom prompt to each one using an LLM (via [Groq](https://groq.com/)), and returns an Excel file with summarized content—clean, fast, and customizable.

![image](https://github.com/user-attachments/assets/f813b621-fa7c-4a0d-9ae3-992c3779faa5)
<p align="center">
  <img src="https://github.com/user-attachments/assets/f813b621-fa7c-4a0d-9ae3-992c3779faa5" width="200" />
</p>
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
   
2. Install the required packages:

   ```bash
   pip install -r requirements.txt

3. Get your `Groq API key` and add it in the app when prompted.
4. Run the app:
   ```bash
      python main.py

## 🧠 What I Learned
One major challenge was integrating a live progress bar with `ttk` while running the summarization process. Because `ttk` runs on the main thread, updating the UI while the backend was busy caused the interface to freeze. The solution? Python’s `threading` module.

By offloading the summarization loop to a background thread, I could keep the UI responsive and update the progress bar in real time. This experience helped me understand the crucial interplay between UI responsiveness and background processing.

<details> <summary>💡 Threading Snippet (Click to Expand)</summary>
   ```bash
      threading.Thread(target=process_excel).start()
</details>

## 📌 Future Enhancements

- 📄 Export each summary into a separate PDF
- ☁️ Add cloud storage option for output files
- 🧹 Better error handling for invalid links or failed summaries

## 📌 Future Enhancements
![image](https://github.com/user-attachments/assets/b4fcb6a4-ec18-4aa4-8839-03fc1c5bc7c1)
![image](https://github.com/user-attachments/assets/c3de84db-255c-4ff8-b0c1-a53f9a3978f2)
![image](https://github.com/user-attachments/assets/4071c9e4-641b-4aea-aff7-1fda2ed700db)
![image](https://github.com/user-attachments/assets/840437a6-623d-4761-a30a-339361aa24bb)
![image](https://github.com/user-attachments/assets/434a6d56-30ab-459a-863a-f553958edc3b)
- Main UI
- Prompt input window
- Summary complete notification
- Finished output file

## 📂 Demo


📈 Status
✅ Functional and stable – actively open to feature suggestions!
