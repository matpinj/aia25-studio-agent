from server.config import *


def classify_input(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        Your task is to classify if the user message is related to co-living, buildings and architecture or not.
                        Output only the classification string.
                        If it is related, output "Related", if not, output "Refuse to answer".

                        # Example #
                        User message: "How do I bake cookies?"
                        Output: "Refuse to answer"

                        User message: "What is the tallest skyscrapper in the world?"
                        Output: "Related"
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def generate_concept(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are a visionary intern at a leading architecture firm.
                        Your task is to craft a short, poetic, and highly imaginative concept for a co-living building design.
                        Weave the initial information naturally into your idea, letting it inspire creative associations and unexpected imagery.
                        Your concept should feel bold, evocative, and memorable — like the opening lines of a story.
                        Keep your response to a maximum of one paragraph.
                        Avoid generic descriptions; instead, focus on mood, atmosphere, and emotional resonance.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        What is the concept for this building? 
                        Initial information: {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def extract_attributes(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """

                        # Instructions #
                        You are a keyword extraction assistant.
                        Your task is to read a given text and extract relevant keywords according to three categories: spatial_features, lifestyle_themes, and target_users.
                        Only output a JSON object in the following format:
                        {
                            "spatial_features": "keyword1, keyword2",
                            "lifestyle_themes": "keyword3, keyword4",
                            "target_users": "keyword5, keyword6"
                        }

                        # Rules #
                        If a category has no relevant keywords, write "None" for that field.
                        Separate multiple keywords in the same field by commas without any additional text.
                        Do not include explanations, introductions, or any extra information—only output the JSON.
                        Focus on concise, meaningful keywords directly related to the given categories.
                        Do not try to format the json output with characters like ```json

                        # Category guidelines #
                        Spatial Features: Types of spaces, layout qualities, or design elements (e.g., shared kitchen, private pod, coworking zone).
                        Lifestyle Themes: Ideas or values related to how people live or interact (e.g., community, flexibility, sustainability, work-life balance).
                        Target Users: Specific groups the space is designed for (e.g., digital nomads, students, freelancers, remote workers).
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        # GIVEN TEXT # 
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def create_question(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        # Instruction #
                        You are a thoughtful research assistant specializing in contemporary housing trends.
                        Your task is to create an open-ended question based on the given text.
                        Your question should invite an answer that refers to specific co-living projects, housing models, or social experiments.
                        Imagine the question will be answered using a detailed text about co-living and shared housing.
                        The question should feel exploratory and intellectually curious.
                        Output only the question, without any extra text.

                        # Examples #
                        - What are some notable co-living projects that successfully balance privacy and community?
                        - How have co-living spaces evolved to support the changing lifestyles of young professionals?
                        - Which co-living models address both affordability and social connection in urban environments?
                        - What examples exist of co-living developments that integrate workspaces into residential settings?
                        - How do different co-living initiatives reinterpret traditional ideas of home and domestic life?

                        # Important #
                        Keep the question open-ended, inviting multiple references or examples.
                        The question must be naturally connected to the themes present in the input text.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content
