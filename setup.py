from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().split("\n")

setup(
    name="audico",
    version="0.0.1",
    description="Audico helps train audio detection models.",
    package_dir={"": "audico"},
    packages=find_packages(where="audico"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ricerob/audico",
    author="Robby Rice",
    author_email="riceslif@gmail.com",
    license="Apache License",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3"
    ],
    install_requires=install_requires,
    python_requires=">=3.10"
)