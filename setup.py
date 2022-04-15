import setuptools

setuptools.setup(
    name="simpledemotivators",
    version="2.1.1",
    author="infqq",
    description="Tool for easy demotivators",
    url="https://github.com/Infqq/simpledemotivators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'pillow==9.1.0',
        'requests==2.25.1',
    ],
)
