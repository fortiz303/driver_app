from flask import Flask, request, render_template
app = Flask('app')

@app.route('/', methods=["GET", "POST"])
def main():
  return render_template('index.html')

app.run(host='0.0.0.0', port=80)
