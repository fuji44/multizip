Multi-Zip
#########

This is a command line tool that creates a zip file based on each directory under the target directory.

If you run against the following target directories.

::

    terget
    +-- dir1
    |   +- file1.txt
    |   ...
    +-- dir2
    |   +-- file2.txt
    |   ...
    +-- file3.txt

A zip file will be created as shown below.

::

    output
    +-- dir1.zip
    +-- dir2.zip

Install
=======

You need to have poetry installed in advance.

.. code-block:: shell

    $ git clone xxx
    $ cd multizip
    $ poetry install
    $ poetry build
    $ pip install dist/multizip-0.1.0.tar.gz


Usege
=====

.. code-block:: shell

    $ mzip archive/target/directory/ -o archive/output/directory/

If the -o option is omitted, the output will be in the current directory.


Test
====

::

    $ poetry run pytest
