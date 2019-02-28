#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from flask import Flask, flash, jsonify, abort, make_response, request
from flask import url_for, redirect, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from modules import job

upload_folder = os.path.abspath('./uploads')
allowed_extensions = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)
CORS(app)
app.config['upload_folder'] = upload_folder
jobs = []

def allowed_FILE(FILEName):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in allowed_extensions

def make_public_job(job):
    new_job = {}
    for field in job:
        if field == 'id':
            new_job['uri'] = url_for('get_job', job_id=job['id'], _extrernal=True)
        else:
            new_job[field] = job[field]
    return new_job

def run_analysis(image, task):
    """Create a job and call analysis
    This method will create a job object and call the analysis on the
    uploaded image

    Parameters
    ----------
    image : path
        path to the uploaded image
    task : string
        type of analysis to be run on the uploaded image

    Returns
    ------
    result : string
        result from the anlysis in question
    """
    new_job = job.Job(image, task)
    result = new_job.execute()
    hash_id = new_job.json_obj['hash']
    resultimg_path = new_job.json_obj['resultimg_path']
    b64_img = new_job.json_obj['b64_img']
    return result, hash_id, resultimg_path, b64_img

@app.route('/index')
def dis_index():
    return render_template("index.html")

@app.route('/analyses')
def dis_analyses():
    return render_template("analyses.html")

@app.route('/about')
def dis_about():
    return render_template("about.html")

@app.route('/papers')
def dis_papers():
    return render_template("papers.html")

@app.route('/api/v0.0/jobs', methods=['GET'])
def get_jobs():
    """list current jobs
    This method will list the current jobs as JSON format

    Parameters
    ----------
    None

    Returns
    ------
    jobs : JSON object
    """
    return render_template("home.html")
    return jsonify({'jobs':[make_public_job(job) for job in jobs]})

@app.route('/api/v0.0/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """fetch a specific job
    This method will fetch a specific job from the job list.

    Parameters
    ----------
    job_id : int
        identifier of the job being fetched

    Returns
    ------
    job : JSON entry
    """
    job = [job for job in jobs if job['id'] == job_id]
    if len(job) == 0:
        abort(404)
    return jsonify({'job': [make_public_job(job[0])]})

@app.route('/api/v0.0/jobs/new', methods=['POST'])
def create_job():
    """create a job entry
    This method will create a job method to be executed.

    Parameters
    ----------
    None

    Requests
    --------
    'analysis' : string
        analysis to be conducted on image
    'image' : path
        path to image

    Returns
    ------
    job : JSON entry
    """
    # verify request
    if not request.json or not 'analysis' or not 'image' in request.json:
        abort(400)

    # run analysis on the new job
    global new_result, new_hash, resultimg_path
    new_result, new_hash, resultimg_path, b64_img = run_analysis(request.json['image'],
                                                        request.json['analysis'])

    # add a JSON entry
    if not len(jobs) == 0:
        job = {
            'id':jobs[-1]['id']+1,
            'analysis':request.json['analysis'],
            'image': request.json['image'],
            'hash' : new_hash,
            'result' : new_result,
            'resultimg_path' : resultimg_path,
            'b64_img' : b64_img,
            'complete':False
        }
    else:
        job = {
            'id':0,
            'analysis':request.json['analysis'],
            'image': request.json['image'],
            'hash' : new_hash,
            'result' : new_result,
            'resultimg_path' : resultimg_path,
            'b64_img' : b64_img,
            'complete':False
        }

    jobs.append(job)

    # change job status and delete once the job will have been delivered to
    # user

    return jsonify({'job':job}), 201

#@app.route('/images/<int:pid>.jpg', methods=['GET'])
@app.route('/images')
#def get_image(pid)
def get_image():
    #img_hash = pid
    #file_path = os.path.join()

    return '''
    <!doctype html>
    <h1>lakjdfhblaksjhdf<\h1>
    '''

@app.route('/api/v0.0/upload', methods=['GET', 'POST'])
def upload_file():
    """upload an image to the platform
    This methods allows the selection of a file to upload to the platform via
    the html form.

    Parameters
    ----------
    None

    Returns
    ------
    form : html
    """
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_image = os.path.join(app.config['upload_folder'], filename)
            file.save(new_image)

            return redirect(url_for('uploaded_file', filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
    </form>
    '''
@app.route('/api/v0.0/<string:img_id>')
def image_display(img_id):
    processed_img_path = os.path.abspath(os.path.join('db', 'img', img_id))
    print('this is my path: ' + processed_img_path)
    return render_template("image_display.html", user_image =
                           processed_img_path)

@app.route('/api/v0.0/uploaded_file', methods=['GET'])
def uploaded_file():
    """uploaded file redirection
    This method will display a success message once the upload has been
    completed.

    Parameters
    ----------
    None

    Returns
    ------
    'succes' : string
    """
    return "success"

@app.route('/api/v0.0/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    """update job completion status
    This method will update a job's completion status.

    Parameters
    ----------
    job_id : int

    Returns
    -------
    job : JSON entry
    """
    job = [job for job in jobs if job['id'] == job_id]
    if len(job) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'analysis' in request.json and type(request.json['analysis']) != unicode:
        abort(400)
    if 'complete' in request.json and type(request.json['complete']) is not bool:
        abort(400)
    job[0]['analysis'] = request.json.get('analysis', job[0]['analysis'])
    job[0]['complete'] = request.json.get('complete', job[0]['complete'])

    return jsonify({'job':[make_public_job(job[0])]})

@app.route('/api/v0.0/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    """deletes a job
    This method will delete a job entry from the jobs JSON object.

    Parameters
    ----------
    job_id : int

    Returns
    ------
    result : JSON entry
    """

    job = [job for job in jobs if job['id'] == job_id]
    if len(job) == 0:
        abort(404)
    jobs.remove(job[0])

    return jsonify({'result':True})

@app.errorhandler(404)
def not_found(error):
    """improved error message
    This method will returns an error message.

    Parameters
    ----------
    error : string

    Returns
    ------
    make_response : JSON entry
    """
    return make_response(jsonify({'error':'Not found'}), 404)

if __name__ == '__main__':
    # for local development
    app.run(debug=True)
    # use when building docker images
    # app.run(host='0.0.0.0', port=80)
