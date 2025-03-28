from flask import Flask, render_template, jsonify, request
from database import show_jobs, show_jobdetails, job_application

app = Flask(__name__)

@app.route("/")
def home_page():
    jobs = show_jobs()
    return render_template('home.html', jobs=jobs)
    

@app.route("/jobs")
def jobs_page():
    jobs = show_jobs()
    return render_template('home.html', jobs=jobs)



@app.route("/job/<id>")
def jobdetails_page(id):
    job = show_jobdetails(id)
  
    if not job:
        return "Not Found", 404
  
    return render_template('jobpage.html', job=job)



@app.route("/job/<id>/apply", methods=['post'])
def apply_page(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html', application=data, job=job)





if __name__ == '__main__':
    app.run(host='localhost', debug=True)