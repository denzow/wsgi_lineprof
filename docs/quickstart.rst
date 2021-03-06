Quickstart
==========

Requirements
------------
* CPython 2.7/3.5/3.6/3.7
* WSGI application

Installation
------------
You can install wsgi_lineprof from PyPI.

::

   $ pip install wsgi_lineprof

We provide wheel packages for some platforms. If your platform is supported,
you don't need to build C extension. Otherwise, you need environment for
building Python C extensions.

Enabling wsgi_lineprof
----------------------
Apply wsgi_lineprof to the existing WSGI web application called ``app``:

.. code-block:: python

   from wsgi_lineprof.middleware import LineProfilerMiddleware

   app = LineProfilerMiddleware(app)

Running wsgi_lineprof
---------------------
Start the web application and access to the application.
wsgi_lineprof writes results to stdout every time an HTTP request is processed by default.
You can see the output like this in your console:

::

   ... (snip) ...

   File: ./app.py
   Name: index
   Total time: 1.00518 [sec]
     Line      Hits         Time  Code
   ===================================
        9                         @app.route('/')
       10                         def index():
       11         1      1005175      time.sleep(1)
       12         1            4      return "Hello world!!"

   ... (snip) ...

Next Steps
----------
* See :doc:`examples` for more examples of integrating wsgi_lineprof with your applications.
* See :doc:`configuration` for advanced usage such as filtering results, writing results to the file, accumulating results, and so on.
