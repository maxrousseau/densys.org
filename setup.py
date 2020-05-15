from setuptools import setup, find_packages

setup(name='densys',
      version='1.0.0',
      description='densys.org platform for research software',
      classifiers=[
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Medical Science Apps.',
      ],
      url='https://github.com/maxrousseau/densys.org',
      author='Maxime Rousseau',
      author_email='maximerousseau08@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'flask',
      ],
)
