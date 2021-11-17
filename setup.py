import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eabr-functions",
    version="1.0.0",
    author="Walter José Avelino da Silva",
    author_email="walter.avelin@gmail.com",
    description="EABR Functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walteravelino/eabr-functions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
