from flask import Flask, request, render_template
from hashlib import md5
app = Flask('app')
hashes = {
  "user": "26ed49287e3bbe890bd58ae3b174a91a",
  "pass": "17b525ce8f0f7ecab8e9672152b666c8"
}


@app.route('/', methods=["GET", "POST"])
def main():
  return render_template('index.html')

@app.route('/admin', methods=["GET", "POST"])
def admin():
  if request.method == "POST":
    form = request.form.to_dict()
    if 'user' in form and 'pass' in form:
      print('YASSSSSSS')
      form_type = "login"
    if form_type == "login":
      if md5(form["user"].encode()).hexdigest() == hashes["user"] and md5(form["pass"].encode()).hexdigest() == hashes["pass"]:
        return "WORKING"
      else:
        return render_template('admin.html', errors = "Username or password incorrect.")

  return render_template('admin.html')

app.run(host='0.0.0.0', port=80)
