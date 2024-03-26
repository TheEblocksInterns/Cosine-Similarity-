from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def calculate_cosine_similarity(list1, list2):
    # Combine the two lists
    combined = [' '.join(list1), ' '.join(list2)]

    # Initialize the CountVectorizer
    vectorizer = CountVectorizer().fit_transform(combined)

    # Calculate the cosine similarity
    vectors = vectorizer.toarray()
    csim = cosine_similarity(vectors)

    # Get the similarity score for the first document (list1) compared to the second document (list2)
    score = csim[0][1]

    return score

def find_common_skills(list1, list2):
    # Convert the lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Find the intersection of the two sets
    common_skills = set1.intersection(set2)

    return common_skills

job_skills = ['job description', 'recruitment software', 'manage market', 'user interface', 'front end', 'user experience', 'version control', 'front end', 'single page application', 'database schema', 'API', 'HTML', 'CSS', 'OOP', 'managers', 'react', 'refinement', 'refinement', 'development processes', 'plans', 'react', 'json', 'ajax', 'bootstrap', 'git', 'semantic', 'based knowledge', 'web development', 'javascript', 'maintain', 'management', 'mysql', 'design experience', 'webpack', 'bash', 'command line']

resume_skills = ['computer science', 'react redux', 'node js', 'customer experience', 'front end', 'front end', 'a b testing', 'user account', 'com', 'GCP', 'HTML', 'CSS', 'GCP', 'github',  'software developer', 'scalable', 'collaboratively', 'e', 'c', 'science computer', 'python', 'django', 'sql', 'postgresql', 'mysql', 'javascript', 'typescript', 'r', 'e', 'e', 'r', 'e', 'c', 'e', 'software developer', 'quickbooks', 'product team', 'react', 'best practices', 'library', 'web app', 'management platform', 'manage', 'react', 'redux', 'added', 'react', 'redux', 'conversion rate', 'help desk', 'accounts']

similarity_score = calculate_cosine_similarity(job_skills, resume_skills)
print("The cosine similarity score is:", similarity_score)
common_skills = find_common_skills(job_skills, resume_skills)
print("The common skills are:", common_skills)