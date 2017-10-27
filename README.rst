.. image:: https://img.shields.io/pypi/v/aio_manager.svg
   :target: https://pypi.org/project/aio_manager

.. image:: https://img.shields.io/travis/rrader/aio_manager/master.svg
   :target: http://travis-ci.org/rrader/aio_manager

.. image:: https://img.shields.io/pypi/pyversions/aio_manager.svg


Script manager for aiohttp.
========

Quick Start
------------------

Install from PYPI:

.. code:: shell

    pip install aio_manager

For optional features, feel free to depend on extras:

.. code:: shell

    pip install aio_manager[mysql,postgres]
    pip install aio_manager[sa]

OR (less popular) via ``setup.py``:

.. code:: shell

    python -m setup install

Example
------------------

.. code:: python
   :number-lines:

    app = build_application()
    manager = Manager(app)

    sqlalchemy.configure_manager(manager, app, Base,
                                 DATABASE_USERNAME,
                                 DATABASE_NAME,
                                 DATABASE_HOST,
                                 DATABASE_PASSWORD)
