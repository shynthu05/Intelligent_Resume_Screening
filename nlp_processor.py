import spacy
import re


nlp = spacy.load("en_core_web_sm")


def extract_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities


def extract_email(text):

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    result = re.search(
        pattern,
        text
    )

    if result:

        return result.group()

    return "Not Found"


def extract_phone(text):

    pattern = r'(\+?\d{1,3}[-.\s]?)?\d{10}'

    result = re.search(
        pattern,
        text
    )

    if result:

        return result.group()

    return "Not Found"


def extract_skills(text):

    skills_database = [

        "python",
        "java",
        "c",
        "c++",
        "sql",
        "html",
        "css",
        "javascript",
        "react",
        "node.js",

        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",

        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "spacy",

        "cyber security",
        "cloud computing",

        "aws",
        "azure",
        "git",
        "docker"

    ]

    text_lower = text.lower()

    found_skills = []

    for skill in skills_database:

        if skill.lower() in text_lower:

            found_skills.append(skill)

    return found_skills