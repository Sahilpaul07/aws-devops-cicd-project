
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS DevOps CI/CD Pipeline is Working 🚀</h1>
    <p>Built with Flask + Docker + Jenkins + Terraform + Kubernetes</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "AWS DevOps CI/CD Pipeline"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
