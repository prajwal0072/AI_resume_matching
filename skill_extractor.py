SKILLS = [

    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "go", "rust", "php", "ruby", "swift", "kotlin", "r",

    # Web Development
    "html", "css", "react", "angular", "vue", "nodejs",
    "express", "django", "flask", "fastapi",
    "spring", "spring boot",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "sqlite",
    "oracle", "redis", "dynamodb", "cassandra",

    # Data Science & ML
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit learn", "xgboost",
    "tensorflow", "pytorch",

    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes",
    "linux", "terraform", "jenkins",

    # Analytics & BI
    "data analysis", "power bi", "tableau", "excel",

    # Tools
    "git", "github", "gitlab", "jira"
]

def extract_skills(tokens):
   
    text = " ".join(tokens)
    found_skills = {skill for skill in SKILLS if skill in text}
    return sorted(found_skills)
