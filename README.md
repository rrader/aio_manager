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
