from setuptools import setup

setup(
    name="scryer",
    version="0.1",
    author="Vince Rosso",
    author_email="v@grepnull.com",
    description="RESTful frontend to Find My iPhone.",
    license="BSD",
    url="http://github.com/grepnull/scryer",
    packages=['scryer'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    requires=['flask==0.10.1',
              'pyicloud==0.3.0']
)
