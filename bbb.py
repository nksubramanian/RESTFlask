from flask import Flask, jsonify

app = Flask(__name__)
courses = [{"name": "python",
           "course_id": "0"},
           {"name": "Java",
           "course_id": "1"},
           {"name": "SQL",
           "course_id": "2"},
           {"name": "Mongo",
           "course_id": "3"},
           {"name": "Visual",
           "course_id": "4"}]


@app.route("/")
def index():
    return "Welcome to the course API"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'courses': courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'course': courses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course = {"name": "Audio",
               "course_id": "5"}
    courses.append(course)
    return jsonify({'Created': courses})


@app.route("/courses/<int:course_id>", methods=['PUT'])
def courses_update(course_id):
    courses[course_id]['name'] = "XYZ"
    return jsonify({'course': courses[course_id]})


@app.route("/courses/<int:course_id>", methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})




app.run(debug=True)