from setuptools import setup, find_packages

setup(
    name="NcViewer",
    version="0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "xarray",
        "plotly",
    ],
    author="Nramirez",
    description="A NetCDF viewer using Plotly",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nramirez-f/NcViewer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)