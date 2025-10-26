from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome ENSIA Students from Flask!"

@app.route('/news')
def get_news():
    # Example of fake data
    news_list = [
        {"title": "AI Revolution in ENSIA", "content": "Students are learning to build intelligent systems."},
        {"title": "Tech Fair 2025", "content": "ENSIA students showcased amazing AI projects!"},
        {"title": "New Lab Opened", "content": "ENSIA just launched a state-of-the-art robotics lab."}
    ]
    return jsonify(news_list)

if __name__ == '__main__':
    app.run(debug=True)
