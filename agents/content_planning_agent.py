import logging

class ContentPlanningAgent:
    def create_outline(self, topic, detailed=False):
        """
        Generates an outline for a blog post based on the given topic.

        :param topic: The main topic of the blog post.
        :param detailed: If True, generates a more detailed outline with additional sections.
        :return: Dictionary containing title and sections of the blog.
        """
        outline = {
            "title": f"Exploring the Latest Trends in HR: {topic}",
            "subtitle": f"Understanding the Impact of {topic} on Workplace Dynamics",
            "sections": [
                "Introduction",
                "Current Key Trends in HR",
                "Impact of These Trends on the Workplace",
                "Challenges and Considerations",
                "Future Predictions for HR Trends",
                "Conclusion & Key Takeaways",
            ]
        }

        if detailed:
            # Add extra sections for an in-depth blog
            outline["sections"].insert(3, "Case Studies and Real-World Examples")
            outline["sections"].insert(5, "Best Practices for HR Professionals")

        logging.info(f"✅ Blog outline created for topic: {topic}")
        return outline
