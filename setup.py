import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as requirements_file:
    requirements = [line.rstrip('\n') for line in requirements_file]

setuptools.setup(
    name="sac_utils",
    version="0.0.1",
    author="Satellite Applications Catapult",
    #author_email="author@example.com",
    description="A collection of utility functions for use in Jupyter Notebooks and other geo processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SatelliteApplicationsCatapult/sac_utils",
    packages=setuptools.find_packages(include=['sac_utils']),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <3.7',
)
