from setuptools import setup

setup(
    name="ncviewer",
    version="0.0",
    py_modules=["__init__", "src"],
    install_requires=["numpy", "scipy", "ncfiles @ git+https://github.com/nramirez-f/NcFiles.git@main#egg=ncfiles"],
    author="Nramirez",
    description="Module to visualize NetCDF files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nramirez-f/NcViewer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)