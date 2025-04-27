from flask import Flask, render_template, request
from database import show_jobs, show_job_details, job_application


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
    job = show_job_details(id)
  
    if not job:
        return "Not Found", 404
    
    return render_template('jobpage.html', job=job)


@app.route("/job/<id>/apply", methods=['POST'])
def apply_page(id):
    data = request.form
    job = show_job_details(id)

    job_application(id, data)
    
    return render_template('application_submitted.html', application=data, job=job)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
