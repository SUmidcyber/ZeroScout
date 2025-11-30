from setuptools import setup, find_packages

setup(
    name="zeroscout",
    version="1.0.0",
    description="ZeroScout - The Autonomous Local & Cloud Threat Hunter",
    author="Umid Mammadov",
    author_email="umid.cybersec@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "pefile",
    ],
    entry_points={
        "console_scripts": [
            "zeroscout=zeroscout.cli:main", 
        ],
    },
)