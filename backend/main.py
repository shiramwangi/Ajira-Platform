# main.py
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions

# Dummy user (for testing only)
USER = {"username": "admin", "password": "1234"}

# Login page template
login_page = """
<!DOCTYPE html>
<html>
<head>
  <title>Login Test</title>
  <style>
    body { font-family: Arial; background: #f4f4f4; display:flex; justify-content:center; align-items:center; height:100vh; }
    .box { background: white; padding: 20px; border-radius: 8px; width: 300px; box-shadow: 0 0 10px rgba(0,0,0,0.2); }
    input { width: 100%; padding: 10px; margin: 8px 0; border-radius: 5px; border: 1px solid #ccc; }
    button { background: #3b82f6; color: white; border: none; padding: 10px; width: 100%; border-radius: 5px; cursor: pointer; }
    button:hover { background: #2563eb; }
    .error { color: red; font-size: 14px; }
  </style>
</head>
<body>
  <div class="box">
    <h2>Login</h2>
    {% if error %}<p class="error">{{ error }}</p>{% endif %}
    <form method="POST">
      <input type="text" name="username" placeholder="Username" required><br>
      <input type="password" name="password" placeholder="Password" required><br>
      <button type="submit">Login</button>
    </form>
  </div>
</body>
</html>
"""

# Dashboard page
dashboard_page = """
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body style="font-family: Arial; text-align:center; padding:50px;">
  <h1>Welcome, {{ user }} 🎉</h1>
  <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USER["username"] and password == USER["password"]:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid credentials, try again."
    return render_template_string(login_page, error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template_string(dashboard_page, user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
