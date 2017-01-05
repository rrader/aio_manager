.. image:: https://img.shields.io/pypi/v/aio_manager.svg
   :target: https://pypi.org/project/aio_manager

.. image:: https://img.shields.io/travis/rrader/aio_manager/master.svg
   :target: http://travis-ci.org/rrader/aio_manager

.. image:: https://img.shields.io/pypi/pyversions/aio_manager.svg

.. image:: https://img.shields.io/pypi/dm/aio_manager.svg


Script manager for aiohttp.

Example
=======

    app = build_application()
    manager = Manager(app)

    sqlalchemy.configure_manager(manager, app, Base,
                                 DATABASE_USERNAME,
                                 DATABASE_NAME,
                                 DATABASE_HOST,
                                 DATABASE_PASSWORD)
