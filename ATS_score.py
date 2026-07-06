import fitz  # PyMuPDF for PDF text extraction
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download NLTK resources if not already available
nltk.download('punkt')
nltk.download('stopwords')

# Define a function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Define a function to preprocess text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Join tokens back to form the processed text
    return " ".join(tokens)

# Extract skills from a text using a predefined list of common skills
def extract_skills(text, skills_list):
    found_skills = []
    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)
    return found_skills

# Function to calculate a score based on skill matching
def skill_matching_score(resume_text, job_description_text, skills_list):
    resume_skills = extract_skills(resume_text, skills_list)
    job_skills = extract_skills(job_description_text, skills_list)
    matching_skills = set(resume_skills).intersection(set(job_skills))
    if len(job_skills) == 0:
        return 0
    return len(matching_skills) / len(job_skills)

# Function to calculate a score based on achievements (using action verbs)
def achievement_score(resume_text, action_verbs):
    achievements = [verb for verb in action_verbs if verb in resume_text]
    return len(achievements) / len(action_verbs) if len(action_verbs) > 0 else 0

# Function to calculate similarity score between resume and job description
def calculate_similarity(resume_text, job_description_text):
    # Vectorize the texts using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description_text])

    # Calculate cosine similarity
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_score[0][0]

# Main function to calculate ATS score of a resume
def calculate_ats_score(pdf_path, job_description):
    # Extract and preprocess resume text
    resume_text = extract_text_from_pdf(pdf_path)
    preprocessed_resume = preprocess_text(resume_text)

    # Preprocess job description
    preprocessed_job_description = preprocess_text(job_description)

    # Define important lists for scoring
    skills_list = [
        "python", "javascript", "sql", "aws", "azure", "tensorflow", "flask", "django",
        "react.js", "machine learning", "data analysis", "pandas", "numpy"
    ]
    action_verbs = [
        "led", "managed", "developed", "improved", "created", "built", "integrated",
        "analyzed", "optimized", "streamlined"
    ]

    # Calculate similarity score using TF-IDF
    similarity_score = calculate_similarity(preprocessed_resume, preprocessed_job_description)

    # Calculate skill matching score
    skill_score = skill_matching_score(preprocessed_resume, preprocessed_job_description, skills_list)

    # Calculate achievement score
    achievement_score_value = achievement_score(preprocessed_resume, action_verbs)

    # Weigh each component and compute a final ATS score
    final_score = (
        0.5 * similarity_score +  # General content match
        0.3 * skill_score +       # Skill matching
        0.2 * achievement_score_value  # Achievements and experience indications
    )

    # Convert score to percentage
    return round(final_score * 100, 2)

# Example usage
# Note: Function calls are commented out to prevent execution without valid input files
pdf_path = "C:\\Users\\priyanshu kumar\\Desktop\\fake_resume.pdf"
job_description = """
We are looking for a software engineer with experience in Python, data analysis, and machine learning.
Knowledge of cloud services such as AWS or Azure is a plus. The candidate should have led projects, optimized applications, and created effective solutions.
"""
ats_score = calculate_ats_score(pdf_path, job_description)
print(f"The ATS score for the resume is: {ats_score}%")
