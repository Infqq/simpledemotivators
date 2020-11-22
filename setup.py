import setuptools

setuptools.setup(
    name="simpledemotivators",
    version="1.1.0",
    author="infqq",
    description="Tool for easy demotivators",
    url="https://github.com/Infqq/simpledemotivators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pillow~=7.1.1"
    ]
)
