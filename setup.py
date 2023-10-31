import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awesome_git_mosaic",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Giovane Costa",                     # Full name of the author
    description="An awesome tool to write small texts on GitHub moaic",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["awesome_git_mosaic"],             # Name of the python package
    package_dir={'':'awesome_git_mosaic/src'},     # Directory of the source code of the package
    install_requires=['unidecode'],                     # Install other dependencies if any
)
