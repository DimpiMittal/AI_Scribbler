import logging

class SEOOptimizationAgent:
    def __init__(self, keywords):
        self.keywords = keywords

    def optimize_content(self, content):
        for keyword in self.keywords:
            content = content.replace(keyword, f"<b>{keyword}</b>")
        logging.info("SEO optimization completed.")
        return content
