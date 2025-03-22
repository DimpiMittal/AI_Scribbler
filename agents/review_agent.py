import language_tool_python
import logging

class ReviewAgent:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')

    def review_content(self, content):
        try:
            matches = self.tool.check(content)
            corrected_content = language_tool_python.utils.correct(content, matches)
            logging.info("Content review completed.")
            return corrected_content
        except Exception as e:
            logging.error(f"Error in content review: {e}")
            return content
