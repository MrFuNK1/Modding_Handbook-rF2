# Modding Handbook - rF2

This is the repository of the "Modding Handbook - rF2" source.

# Requirements

The documentation is written in reStructuredText (RST) and generated using Spinx. To work on the source and compile the documentation on your own, you would need at least the following:

- To write documentation or edit RST files, you can use any text editor of your choice. Suggested are Notepad++ https://notepad-plus-plus.org/ and Atom https://atom.io/
- To compile the documentation from source, you need sphinx-doc https://www.sphinx-doc.org

# Packaging scripts

There are a couple of packaging scripts provided. These are very simple bash scripts, intended to work on a Ubuntu Linux OS. Maybe batch scripts for Windows will be added later.

# Generating the documentation locally

The requirements above mention you need sphinx-doc to "compile" the documentation from source on your machine. To use it, you need to install Python on your computer.

## Windows

For Windows the installation for that is described in the [Getting started using Python on Windows for beginners](https://docs.microsoft.com/en-us/windows/python/beginners) guide, where you should follow the steps to install Python, optionally Visual Studio Code, and probably Git (if you have not done so already to clone this repository). This version of Python comes with "pip", a package manager for Python which makes the installation of sphinx-doc easy.

You need to install the following packages:
```
pip install sphinx
pip install sphinx-rtd-theme
pip install sphinxprettysearchresults
pip install readthedocs-sphinx-search
```

If that worked without generating any error messages, you can go to the folder where you've cloned the git repository and then type:
```
make html
```
This will build the whole documentation into a subfolder called `build\html` so to read that type:
```
start build\html\index.html
```
That should open the documentation in your default browser. You can run the `make` command again after every update you do to the documentation.

## Linux

TODO

## Mac OS X

TODO
