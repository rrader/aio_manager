import logging
from aio_manager import Manager
from aioapp.app import build_application

logging.basicConfig(level=logging.WARNING)

app = build_application()
manager = Manager(app)

# To support SQLAlchemy commands, use this
#
# from aio_manager.commands.ext import sqlalchemy
# [from aiopg.sa import create_engine]
# sqlalchemy.configure_manager(manager, app, Base,
#                              settings.DATABASE_USERNAME,
#                              settings.DATABASE_PASSWORD,
#                              settings.DATABASE_NAME,
#                              settings.DATABASE_HOST,
#                              settings.DATABASE_PORT[,
#                              create_engine])

if __name__ == '__main__':
    manager.run()
