from flask import Flask, render_template_string, request

app = Flask(__name__)
appointments = []

template = """
<h2>🩺 Doctor Appointment Booking System</h2>
<form method="post">
  Name: <input type="text" name="name" required><br><br>
  Age: <input type="number" name="age" required><br><br>
  Date: <input type="date" name="date" required><br><br>
  <button type="submit">Book Appointment</button>
</form>

<h3>Booked Appointments</h3>
<ul>
{% for a in appointments %}
  <li>{{a['name']}} ({{a['age']}} yrs) - {{a['date']}}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        date = request.form["date"]
        appointments.append({"name": name, "age": age, "date": date})
    return render_template_string(template, appointments=appointments)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)