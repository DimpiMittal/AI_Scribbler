import logging
import cohere
import os
from dotenv import load_dotenv

class ContentGenerationAgent:
    def __init__(self):
        """Initialize the content generation agent and load the API key."""
        load_dotenv()  # Load environment variables from .env
        api_key = os.getenv("COHERE_API_KEY")  # Fetch API key

        if not api_key:
            logging.error("❌ API Key not found. Please check your .env file.")
            raise ValueError("Missing COHERE_API_KEY in .env file")

        self.client = cohere.Client(api_key)  # Initialize Cohere API client

    def generate_content(self, topic):
        """Generates short blog content (~500 words) based on the input topic."""
        try:
            response = self.client.generate(
                model="command",  
                prompt=f"Write a blog on the topic: {topic}\n",  # Use user-input topic
                max_tokens=500
            )
            generated_text = response.generations[0].text.strip()
            
            if not generated_text:
                logging.warning("⚠️ No content generated. Cohere API might have returned an empty response.")
                return None
            
            logging.info("✅ Short content generated successfully.")
            return generated_text

        except cohere.CohereError as e:
            logging.error(f"❌ Cohere API error: {e.message}")
        except Exception as e:
            logging.error(f"❌ Unexpected error: {str(e)}")

        return None
    
    def generate_long_content(self, topic, word_target=2000):
        """Generates long blog content (~2000 words) based on the input topic."""
        total_content = []
        max_tokens_per_request = 1000  # Cohere's per-request token limit
        total_words = 0

        while total_words < word_target:
            try:
                response = self.client.generate(
                    model="command",
                    prompt=f"Write a detailed blog (~{word_target} words) on the topic: {topic}\n",
                    max_tokens=max_tokens_per_request,
                    temperature=0.7,
                )
                
                new_text = response.generations[0].text.strip()
                if not new_text:
                    logging.warning("⚠️ No content generated in this request. Stopping further requests.")
                    break

                total_content.append(new_text)
                total_words = sum(len(part.split()) for part in total_content)

                logging.info(f"📌 Generated {total_words} words so far...")

                if total_words >= word_target:
                    break

            except cohere.CohereError as e:
                logging.error(f"❌ Cohere API error: {e.message}")
                break
            except Exception as e:
                logging.error(f"❌ Unexpected error: {str(e)}")
                break

        final_content = "\n\n".join(total_content)

        if final_content:
            logging.info("✅ Long content generated successfully.")
        else:
            logging.error("❌ Failed to generate any content.")

        return final_content
