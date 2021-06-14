from setuptools import setup

setup(
    name='jackie-python-challenges',
    author='Jacqueline Shrader',
    version='1.0.0',
    description='A series of short challenges completed using python. completed 1, 4 and 5',
    url='https://github.com/JackieShrader/PythonChallenges',

    python_requires=">=3.8",

    packages=["my_project"],

    install_requires=[
        'pandas == 1.2.4',
        'requests == 2.25.1',
        'psutil == 5.8.0',
    ],

    entry_points={
        "console_scripts": [
            "my_project = my_project.__main__:main",
            "challenge-1 = my_project.challenge_1:main",
            "challenge-4 = my_project.challenge_4:main",
            "challenge-5 = my_project.challenge_5:main"

        ]
    },



)
