# AI Scribbler - Multi-Agent SEO Blog Generator

![AI Scribbler](https://your-image-url.com) <!-- Add an image banner if available -->

## 🚀 About AI Scribbler
**AI Scribbler** is a powerful multi-agent **SEO blog generator** that automates content creation using AI. It leverages **Cohere AI**, **web scraping**, and **voice recognition** to generate high-quality, optimized blog content efficiently. The project is built using **Python (Flask)** and integrates multiple AI tools to enhance content generation and SEO effectiveness.

## ✨ Features
- **AI-Powered Blog Generation**: Uses **Cohere AI** to generate high-quality blog posts.
- **Web Scraping**: Gathers relevant data using **BeautifulSoup**.
- **Voice Recognition System**: Converts speech to text for seamless content creation.
- **SEO Optimization**: Enhances blog content for better search engine ranking.
- **User-Friendly UI**: Built with **HTML, CSS, and JavaScript**.
- **API Integration**: Collects and processes data through APIs.
- **Logging Mechanism**: Tracks and manages system activities efficiently.

## 🛠️ Tech Stack
| Technology      | Usage |
|---------------|----------------|
| **Python** | Core programming language |
| **Flask** | Web framework for backend |
| **Cohere AI** | AI-powered text generation |
| **BeautifulSoup** | Web scraping for data collection |
| **JavaScript** | Enhances interactivity |
| **HTML & CSS** | UI/UX styling |
| **Logging** | Tracks and manages system logs |
| **API Integration** | Fetches external data sources |

## 📂 Project Structure
```
AI_Scribbler/
│── app.py               # Main Flask backend
│── requirements.txt     # Required dependencies
│── static/              # CSS, JS, Images
│── templates/           # HTML templates
│── .env                 # API keys & sensitive data (ignored in Git)
│── .gitignore           # Files to ignore in Git
│── README.md            # Project documentation
```

## 📝 Installation & Setup
Follow these steps to set up and run AI Scribbler locally.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/DimpiMittal/AI_Scribbler.git
cd AI_Scribbler
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```
COHERE_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

### 5️⃣ Run the Application
```sh
python app.py
```
Your application should now be running at `http://127.0.0.1:5000/`

## 🚀 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request!

## 🛡️ License
This project is **open-source** and available under the [MIT License](LICENSE).

## 🙌 Acknowledgments
- [Cohere AI](https://cohere.com/) for text generation.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
- Flask and Python Community for development support.

---
🔥 **AI Scribbler** - Your AI-powered content creation assistant!

