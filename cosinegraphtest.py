import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MyMplCanvas, self).__init__(fig)

class MyStaticMplCanvas(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        self.compute_initial_figure()

    def compute_initial_figure(self):
      # Here you can replace this with your own data
      data_sets = {
          'Computer science ': calculate_cosine_similarity(job_skills, resume_skills1),
          'Project manager': calculate_cosine_similarity(job_skills, resume_skills2),
          'Financial Analyst': calculate_cosine_similarity(job_skills, resume_skills3)
      }
      names = list(data_sets.keys())
      scores = list(data_sets.values())
      self.axes.bar(names, scores, color='b')
      self.axes.set_ylim([0, 1])
      self.axes.set_ylabel('Cosine Similarity Score')
      self.axes.set_xticks(range(len(names)))
      self.axes.set_xticklabels(names, rotation=45)


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Resume Matching Scores Graph")

        self.main_widget = QWidget(self)

        layout = QVBoxLayout(self.main_widget)
        static_canvas = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        layout.addWidget(static_canvas)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

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

job_skills = ['job description', 'recruitment software', 'manage market', 'user interface', 'front end', 'user experience', 'version control', 'front end', 'single page application', 'database schema', 'API', 'HTML', 'CSS', 'OOP', 'managers', 'react', 'refinement', 'refinement', 'development processes', 'plans', 'react', 'json', 'ajax', 'bootstrap', 'git', 'semantic', 'based knowledge', 'web development', 'javascript', 'maintain', 'management', 'mysql', 'design experience', 'webpack', 'bash', 'command line']

# Replace these with your actual resume skills
resume_skills1 = ['computer science', 'react redux', 'node js', 'customer experience', 'front end', 'front end', 'a b testing', 'user account', 'com', 'GCP', 'HTML', 'CSS', 'GCP', 'github',  'software developer', 'scalable', 'collaboratively', 'e', 'c', 'science computer', 'python', 'django', 'sql', 'postgresql', 'mysql', 'javascript', 'typescript', 'r', 'e', 'e', 'r', 'e', 'c', 'e', 'software developer', 'quickbooks', 'product team', 'react', 'best practices', 'library', 'web app', 'management platform', 'manage', 'react', 'redux', 'added', 'react', 'redux', 'conversion rate', 'help desk', 'accounts']
resume_skills2 = ['project management', 'agile methodologies', 'scrum', 'software development', 'java', 'python', 'c++', 'html', 'css', 'javascript', 'sql', 'git', 'github', 'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'devops', 'continuous integration', 'continuous deployment', 'unit testing', 'system testing', 'ui/ux design', 'adobe photoshop', 'adobe illustrator', 'sketch', 'figma', 'product management', 'business analysis', 'data analysis', 'machine learning', 'deep learning', 'artificial intelligence', 'big data', 'hadoop', 'spark', 'tableau', 'power bi', 'excel', 'word', 'powerpoint', 'outlook', 'customer service', 'communication', 'leadership', 'teamwork', 'problem solving', 'critical thinking', 'time management', 'adaptability', 'creativity', 'interpersonal skills', 'work ethic', 'reliability']

resume_skills3 = ['financial analysis', 'accounting', 'bookkeeping', 'tax preparation', 'auditing', 'financial reporting', 'budgeting', 'forecasting', 'financial modeling', 'excel', 'quickbooks', 'sage', 'xero', 'financial software', 'data analysis', 'attention to detail', 'organizational skills', 'communication', 'problem solving', 'critical thinking', 'time management', 'adaptability', 'creativity', 'interpersonal skills', 'work ethic', 'reliability', 'leadership', 'teamwork', 'customer service', 'sales', 'marketing', 'business development', 'negotiation', 'public speaking', 'presentation', 'project management', 'strategic planning', 'research', 'report writing', 'social media', 'seo', 'sem', 'google analytics', 'content creation', 'branding', 'public relations', 'event planning', 'email marketing', 'crm']


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ApplicationWindow()
    window.setWindowTitle("Resume Matching Scores Graph")
    window.show()

    sys.exit(app.exec_())
