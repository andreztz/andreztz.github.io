How to build and install Wxpython Phoenix.
##########################################

:date: 2017-01-30 00:25
:category: python
:tags: python3, wxpython,


.. code-block:: python

    $ wget -c wget -c https://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev2755+968784d.tar.gz

.. code-block:: python

    $ tar -vzxf wxPython_Phoenix-3.0.3.dev2759+07a7440.tar.gz

.. code-block:: python

    $ cd wxPython_Phoenix-3.0.3.dev2759+07a7440

.. code-block:: python

    $ sudo pip install -r requirements.txt

.. code-block:: python

    $ sudo python3.6 build.py build install --python=/usr/bin/python3.6

.. code-block:: python

    $ sudo chmod o+r /usr/lib/python3.6/site-packages/wxPython_Phoenix-3.0.3.dev2759+07a7440-py3.6.egg-info/PKG-INFO


`snapshot-builds <https://wxpython.org/Phoenix/snapshot-builds/>`_
