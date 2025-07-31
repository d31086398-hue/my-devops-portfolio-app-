from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My DevOps Portfolio App</title>
    <style>
      body { font-family: Arial, sans-serif; background-color: #2c3e50; color: white; text-align: center; padding: 50px; }
      h1 { font-size: 3em; }
      p { font-size: 1.5em; }
      .container { background: #34495e; padding: 20px; border-radius: 10px; display: inline-block; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Hello, I'm a DevOps Engineer!</h1>
      <p>This application is deployed on AWS via a CI/CD pipeline.</p>
      <p>Running on: <strong>{{ hostname }}</strong></p>
      <p>Environment: <strong>{{ environment }}</strong></p>
    </div>
  </body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HTML_TEMPLATE, hostname=os.uname().nodename, environment="Production on AWS EKS")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)