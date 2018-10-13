#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask, flash, jsonify, abort, make_response, request
from flask import url_for, redirect
from werkzeug.utils import secure_filename
import job
import os

upload_folder = os.path.abspath('./uploads')
allowed_extensions = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)
app.config['upload_folder'] = upload_folder
jobs = [
    {
        'id' : 1,
        'analysis' : 'asym',
        'image' : None,
        'complete' : False
    }
]

def make_public_job(job):
    new_job = {}
    for field in job:
        if field == 'id':
            new_job['uri'] = url_for('get_job', job_id=job['id'], _extrernal=True)
        else:
            new_job[field] = job[field]
    return new_job


# get list of jobs
@app.route('/api/v0.0/jobs', methods=['GET'])
def get_jobs():
    return jsonify({'jobs':[make_public_job(job) for job in jobs]})

# get a specific job 
@app.route('/api/v0.0/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = [job for job in jobs if job['id'] == job_id]
    if len(job) == 0:
        abort(404)
    return jsonify({'job': [make_public_job(job[0])]})

# improved error message
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

# post a new job
@app.route('/api/v0.0/jobs/', methods=['POST'])
def create_job():
    if not request.json or not 'analysis' in request.json:
        abort(400)

    job = {
        'id':jobs[-1]['id']+1,
        'analysis':request.json['analysis'],
        'image': None,
        'complete':False
    }

    jobs.append(job)
    return jsonify({'job':job}), 201

@app.route('/api/v0.0/jobs/', methods=['GET', 'POST'])
def upload_file():
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
            file.save(os.path.join(app.config['upload_folder'], filename))
            return 'successful upload', redirect(url_for('uploaded_file', filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
    </form>
    '''

# update job completion status
@app.route('/api/v0.0/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
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

# delete a job
@app.route('/api/v0.0/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = [job for job in jobs if job['id'] == job_id]
    if len(job) == 0:
        abort(404)
    jobs.remove(job[0])
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(debug=True)
