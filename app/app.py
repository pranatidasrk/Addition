from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Calculator</title>
<h2>Simple Calculator</h2>

<form method="post">
  <input type="number" name="a" step="any" required>
  <input type="number" name="b" step="any" required>
  <br><br>

  <button name="operation" value="add">Add</button>
  <button name="operation" value="sub">Subtract</button>
  <button name="operation" value="mul">Multiply</button>
  <button name="operation" value="div">Divide</button>
</form>

{% if result is not none %}
  <h3>Result: {{ result }}</h3>
{% endif %}

{% if error %}
  <h3 style="color:red;">Error: {{ error }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = request.form["operation"]

            if operation == "add":
                result = a + b
            elif operation == "sub":
                result = a - b
            elif operation == "mul":
                result = a * b
            elif operation == "div":
                if b == 0:
                    error = "Cannot divide by zero!"
                else:
                    result = a / b
        except:
            error = "Invalid input!"

    return render_template_string(HTML, result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)