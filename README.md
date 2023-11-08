[![codecov](https://codecov.io/gh/justgigio/awesome-git-mosaic/graph/badge.svg?token=0ON0YL8EAH)](https://codecov.io/gh/justgigio/awesome-git-mosaic)
![build](https://github.com/justgigio/awesome-git-mosaic/actions/workflows/build.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/awesome-git-mosaic.svg)](https://badge.fury.io/py/awesome-git-mosaic)
![Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![License](https://img.shields.io/pypi/l/awesome-git-mosaic)
[![Documentation Status](https://readthedocs.org/projects/awesome-git-mosaic/badge/?version=latest)](https://awesome-git-mosaic.readthedocs.io/en/latest/?badge=latest)

# awesome-git-mosaic
A simple tool to make cool tricks with your Github activity mosaic

# Install
Just create a new repo on Github and install like any python lib

`pip install awesome-git-mosaic`

or

`poetry add awesome-git-mosaic`

# Usage

It comes ready to be used out of the box with dafault settings or you can use its full functionalities by importing on code

> **Warning**\
> It is recommended to create an empty repo for this purpose only. A lot of files will be created and so a lot of commits (which can be problematic to revert in a working repo). See [Reseting](#reseting).

## Default
After installation, you can use with default parameter by running

`python -m awesome_git_mosaic <your_text_here[A-Za-z0-9# ]+>`

> **Note**\
> With default params, each character have 5 squares wide plus 1 square of space between letters. So, only 8 characters will appear at time.

## Importing on console (or anywhere)

```python
from awesome_git_mosaic.usecases.write_mosaic import WriteMosaic

wm = WriteMosaic()

wm.write('numenor', 50, 2, True, False, True)
```
Method signature:

```python
def write(
    self,
    message: str,  # what you want to write
    strength: int = 15,  # how many commits each pixel will have (more details in "How it works" section)
    multiply: int = 1,  # number of times to write the message consecutive like "MSGMSGMSG" (more details in "How it works" section)
    with_spaces: bool = True,  # put or not spaces between characters
    background: bool = False,  # put background or not
    inverted: bool = False,  # invert pixels or not
):
```
# How it works
Git allow us to [set the date and time](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---dateltdategt) of a commit, so, we can do it in retrspective or even in the future.

By understanding how Github activity mosaic works, we can figure out wich time correlates to each pixel and translate a matrix of pixels in a list of datetimes. So, for each datetime a commit is made modifying or create an unique file.

Days with more contribution have a lighter green and the light intensity will be dynamic according to the day you have more contributions in the period of time showing in the mosaic. So, to have a good highlighted message, it is recommended to set `strength` at least as two times the number of max contributions you have in the period.

Each week the leftmost column will disappear. So to make the mosaic looks like a veeeery slow scrolling text, you can set `multiply` to more than `1`.

> **Warning**\
> Commits and pushes are made automatically by the code. It is HIGHLY RECOMMENDED to create a repo specially for this purpose.

## Reseting
You can easily remove everything by deleting the repo where you made the commits.

# About
After watch [this video](https://www.youtube.com/watch?app=desktop&v=2q--gA97caM) from [@akshaymarch7](https://github.com/akshaymarch7) i´ve just had an ideia to play around with the pixels instead of just make it random.

So, why not draw or write something? A few days later and i had a working prototype. Now it is a lib for anyone who want to have fun or contribute with more ideas.

If you enjoyed enough, consider

[![buy me a coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/justgigio)

# Contributing
