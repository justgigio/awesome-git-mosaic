Usage
=====

.. _installation:

Installation
------------

Just create a new repo on Github and install like any python lib:

.. code-block:: console

   (.venv) $ pip install awesome-git-mosaic

Default usage
-------------

After installation, you can use with default parameter by running:

.. code-block:: console

    (.venv) $ python -m awesome_git_mosaic <your_text_here[A-Za-z0-9# ]+>


Importing on console (or anywhere)
----------------------------------

.. autofunction:: awesome_git_mosaic.usecases.write_mosaic.WriteMosaic.write

>>> from awesome_git_mosaic.usecases.write_mosaic import WriteMosaic
>>> wm = WriteMosaic()
>>> wm.write('numenor', 50, 2, True, False, True)
