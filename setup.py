from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0',
        'numpy==1.21.2',
    ],
)

