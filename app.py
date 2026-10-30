from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Veda Cloud Internship - Task 30</h1>
    <h2>Flask Application Deployed Successfully!</h2>
    <p>Hosted on an AWS EC2 Ubuntu Virtual Machine.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
