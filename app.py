from flask import Flask, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps With Cloud</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            text-align: center;
        }

        .container {
            margin-top: 60px;
            padding: 30px;
        }

        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.4);
            backdrop-filter: blur(10px);
            display: inline-block;
        }

        h1 {
            font-size: 32px;
            margin-bottom: 10px;
            color: #FFD700;
        }

        h2 {
            font-weight: normal;
            margin-bottom: 30px;
        }

        .logos img {
            width: 70px;
            margin: 10px;
            transition: transform 0.3s;
        }

        .logos img:hover {
            transform: scale(1.2);
        }

        .footer {
            margin-top: 40px;
            font-size: 18px;
            color: #00ffcc;
        }

        .badge {
            background: #ff4b2b;
            padding: 8px 15px;
            border-radius: 20px;
            display: inline-block;
            margin-top: 15px;
            font-weight: bold;
        }

    </style>
</head>
<body>

    <div class="container">
        <div class="card">
            <h1>🚀 DevOps & Multi Cloud</h1>
            <h2>Traning Present By The Veera Sir</h2>

            <div class="logos">
                <img src="https://cdn.worldvectorlogo.com/logos/aws-2.svg">
                <img src="https://cdn.worldvectorlogo.com/logos/docker.svg">
                <img src="https://cdn.worldvectorlogo.com/logos/kubernetes.svg">
                <img src="https://cdn.worldvectorlogo.com/logos/jenkins-1.svg">
                <img src="https://cdn.worldvectorlogo.com/logos/google-cloud-1.svg">
            </div>

            <div class="badge">
                🔥 AWS | AZURE | GCP | Terraform | CI/CD | Docker | Kubernetes | 
            </div>

            <div class="footer">
                💙 Team VeeraOps
            </div>

        </div>
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
