# How to contribute


## Useful curl commands
These will be useful when developing for the flask api. 

To list all current jobs:
```sh
curl http://127.0.0.1:5000/api/v0.0/jobs
```
To access a specific job (i.e. job_id = 3):
```sh
curl http://127.0.0.1:5000/api/v0.0/jobs/<int:job_id> 
```
To create a new job and run an analysis ```["asym", "lfh", "ratio1", "ratio2",
ratio3"]```:
```sh
curl -i -H Content-Type: application/json -X POST -d {"analysis":"asym",
"image":"lena.jpg"} http://127.0.0.1:5000/api/v0.0/jobs/new
```

## Reporting Issues

To report an issues or bug please use the [github issues page](https://github.com/maxrousseau/pfla/issues). 

Before opening a new issue make sure that it has not already been mentionned in
a previous thread.

When reporting on a problem make sure that your initial comment includes the
following:
- Short title, and thorough description in the body of the initial comment
- Version of: Python, R, OpenCV 
- Operating system
- Terminal input and output
- List of contents of the directories being fed as input
- Output of the test ([see test section](https://github.com/maxrousseau/pfla))


## Submitting changes

Please send a [GitHub Pull Request to pfla](https://github.com/maxrousseau/flask-pfla/pull/new/master) with a clear list of what you've done (read more about [pull requests](http://help.github.com/pull-requests/)). 
Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."

## Coding conventions

Follow the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) and
[Google R style guide](https://google.github.io/styleguide/Rguide.xml) when writing code for this package.

Additional notes:
- Indent your code with tabs
- Include tests and documentation for your newly implemented features
- Use TravisCI for building
- Use Sphinx for documentation
