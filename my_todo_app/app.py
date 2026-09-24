from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []
next_id = 1


# Home + Get Tasks
@app.route("/")
@app.route("/get")
def home():
    return render_template("home.html", tasks=tasks)


# Add Task
@app.route("/add", methods=["POST"])
def add_task():

    global next_id

    name = request.form["name"]
    status = request.form["status"]
    due_date = request.form["due_date"]

    task = {
        "id": next_id,
        "name": name,
        "status": status,
        "due_date": due_date
    }

    tasks.append(task)

    next_id = next_id + 1

    return redirect("/")


# Delete Task
@app.route("/delete/<int:id>")
def delete_task(id):

    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break

    return redirect("/")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
