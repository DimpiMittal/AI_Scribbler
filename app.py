import logging
import os
import cohere
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load API Key from .env
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    logging.error("❌ API Key not found. Please check your .env file.")
    exit(1)  # Exit program if no API key

# Initialize Flask App
app = Flask(__name__)

# Initialize Cohere API Client
co = cohere.Client(api_key)

def generate_blog_content(topic):
    """Generates a blog using Cohere AI."""
    try:
        logging.info(f"🚀 Generating blog for topic: {topic}")

        response = co.generate(
            model='command',
            prompt=f"Write a detailed, SEO-optimized blog on '{topic}' with headings, subheadings, and structured content.",
            max_tokens=2000
        )

        content = response.generations[0].text

        if not content:
            logging.error("❌ Failed to generate content.")
            return None

        return content

    except Exception as e:
        logging.error(f"❌ Cohere API error: {e}")
        return None

# ====================== Flask Routes ======================

@app.route("/")
def index():
    """Serves the main homepage."""
    return render_template("index.html")

@app.route("/about")
def about():
    """Serves the About page."""
    return render_template("about.html")

@app.route("/blog")
def blog():
    """Serves the Blog page."""
    return render_template("blog.html")

@app.route("/contact")
def contact():
    """Serves the Contact page."""
    return render_template("contact.html")

@app.route("/sign")
def sign():
    """Serves the Sign-in page."""
    return render_template("sign.html")

@app.route("/generate_blog", methods=["POST"])
def generate_blog():
    """Handles blog generation requests."""
    data = request.get_json()
    topic = data.get("topic")

    if not topic:
        return jsonify({"success": False, "error": "No topic provided."})

    content = generate_blog_content(topic)
    
    if content:
        return jsonify({"success": True, "content": content})
    else:

        return jsonify({"success": False, "error": "Failed to generate content."})

        

@app.route("/process-voice", methods=["POST"])
def process_voice():
    """Handles voice recognition input and generates AI response."""
    data = request.get_json()
    user_text = data.get("text")

    if not user_text:
        return jsonify({"error": "No text received!"}), 400

    try:
        response = co.generate(
            model="command",
            prompt=f"Respond to this: {user_text}",
            max_tokens=50
        )

        return jsonify({"response": response.generations[0].text})

    except Exception as e:
        logging.error(f"❌ Cohere API error: {e}")
        return jsonify({"error": "Failed to process request."}), 500

if __name__ == "__main__":
    app.run(debug=True)
