DENSYS.ORG
==========

This web applications aims at making the analyses from the [pfla
package](<https://github.com/maxrousseau/flask-pfla) accessible and easy to use
for non-programmers.

Requirements and Dependencies
-----------------------------

-   Python 3.5
-   Python packages: opencv-python, dlib, numpy 
-   Linux operating system

Testing
-------

To run all tests on the python source files, enter the following in the cloned
directory:

```shell
pytest
```

To execute the api tests begin by deploying the the backend locally:

```shell
python app.py
```

Then follow up by executing the shell script:

```shell
./api-test.sh
```


Documentation
-------------
Under development.

Contribute
----------

Use conda to reproduce the development environment:
```sh
conda env create -f environment-dev.yml
```

-   Refer to the contribution guidelines: <https://github.com/maxrousseau/densys.org/blob/master/contributing.md> 
-   Issue Tracker: <https://github.com/maxrousseau/densys.org/issues>
-   Source Code: <https://github.com/maxrousseau/densys.org>

TODO
----
- [x] complete all analysis functions
- [x] draw, save and display resulting image
- [ ] tests for jobs.py, app.py and linear.py
- [ ] documentation generation with sphinx and RTD hosting
- [ ] travisCI
- [x] deployment on heroku

Deployment commands
------------------
```sh
sudo heroku container:push web
sudo heroku container:release web
heroku open
```

License
-------
The project is licensed under the MIT license.

Contact
-------
Maxime Rousseau, DMD III McGill University, Faculty of Dentistry
- Email: <maximerousseau08@gmail.com>

