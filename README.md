# AI WhatsApp Replier 🤖📱

An intelligent WhatsApp automation bot that reads messages from WhatsApp Web and generates smart, human-like replies using Google Gemini AI.

---

## 🚀 About The Project

AI WhatsApp Replier is a Python-based automation project that integrates:

- Selenium for WhatsApp Web automation  
- Google Gemini AI for intelligent responses  
- Python scripting for message processing  

The bot reads the latest message from a selected WhatsApp chat, sends it to Gemini AI, and automatically replies in real time.

---

## ✨ Features

- Automatically opens WhatsApp Web  
- Reads incoming messages from a selected contact  
- Generates AI-powered replies using Gemini  
- Sends replies automatically  
- Handles emojis and special characters safely  
- Simple and easy to configure  

---

## 🛠 Technologies Used

- **Python**  
- **Selenium WebDriver** – for browser automation  
- **Google Gemini AI SDK** – for generating replies  
- **WebDriver Manager** – automatic ChromeDriver setup  
- **python-dotenv** – to manage API keys securely  

---

## 📂 Project Structure

ai-whatsapp-replier/
│
├── newmain.py # Main automation script
├── checkmodels.py # Script to verify Gemini AI models
├── .env # API key storage (ignored by Git)
├── .gitignore # Files to be ignored by Git
├── pycache/ # Compiled Python files
└── README.md # Project documentation


---

## ⚙ Installation Guide

### 1. Clone the Repository

git clone https://github.com/ana61012/ai-whatsapp-replier.git

2 . Navigate to the Project Folder
cd ai-whatsapp-replier

3. Install Required Libraries

Install the required Python packages:
pip install selenium
pip install webdriver-manager
pip install python-dotenv
pip install google-genai

Configuration

Create a .env file in the project folder with the following content:
GEMINI_KEY=your_api_key_here

How to Run

Run the main script using:
python newmain.py

Program Workflow
Chrome opens WhatsApp Web
You scan the QR code
Enter the contact name
The bot reads the latest message
Message is sent to Gemini AI
AI generates a smart reply
The reply is automatically sent back on WhatsApp

🧠 How It Works
Selenium automates WhatsApp Web
Extracts the most recent message
Sends it to Gemini AI as a prompt
Cleans the AI response to remove unsupported characters
Sends the reply automatically

🚧 Future Enhancements

Planned improvements:
Continuous monitoring for new messages
Support for group chats
GUI interface using Streamlit
Multi-contact support
Chat history logging
Custom reply styles

⚠ Security Notice

API keys are stored in .env
The .env file is ignored using .gitignore
Never upload API keys to GitHub

📄 License

This project is open-source and free to use for learning and development.

👩‍💻 Author

Ananya
GitHub: @ana61012

If you like this project, feel free to give it a star on GitHub!

---
