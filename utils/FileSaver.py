import os
import logging

class FileSaver:
    @staticmethod
    def save_to_file(content, filename):
        """Saves content to a file, ensuring the directory exists."""
        try:
            if not content:
                logging.warning("⚠️ No content to save. File not created.")
                return
            
            # Ensure the directory exists
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            # Save content to file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)

            logging.info(f"✅ Successfully saved content to {filename}")

        except OSError as e:
            logging.error(f"❌ Error saving file {filename}: {e}")

        except Exception as e:
            logging.error(f"❌ Unexpected error while saving file: {e}")
