from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome ENSIA Students from Flask!"

@app.route('/news')
def get_news():
    news_list = [
        {"title": "AI Revolution in ENSIA", "content": "Students are learning to build intelligent systems."},
        {"title": "Tech Fair 2025", "content": "ENSIA students showcased amazing AI projects!"},
        {"title": "New Lab Opened", "content": "ENSIA just launched a state-of-the-art robotics lab."}
    ]
    return jsonify(news_list)

# 🌸 NEW ROUTE: Candidates
@app.route('/candidates')
def get_candidates():
    candidates = [
        {
            "name": "Lina A.",
            "email": "lina.a@ensia.dz",
            "education_level": "3rd Year Bachelor",
            "university": "ENSIA",
            "major": "Artificial Intelligence",
            "experience": "Intern at SONATRACH - Developed an AI-based safety alert system",
            "skills": ["Python", "Machine Learning", "Flask", "TensorFlow"]
        },
        {
            "name": "Sara M.",
            "email": "sara.m@ensia.dz",
            "education_level": "2nd Year Master",
            "university": "ENSIA",
            "major": "Data Science",
            "experience": "Worked on a predictive model for stock prices",
            "skills": ["Pandas", "NumPy", "Data Visualization", "APIs"]
        },
        {
            "name": "Amine K.",
            "email": "amine.k@ensia.dz",
            "education_level": "3rd Year Bachelor",
            "university": "ENSIA",
            "major": "Software Engineering",
            "experience": "Built mobile apps using Flutter and Firebase",
            "skills": ["Flutter", "Dart", "Firebase", "UI/UX"]
        }
    ]
    return jsonify(candidates)


if __name__ == '__main__':
    app.run(debug=True)
