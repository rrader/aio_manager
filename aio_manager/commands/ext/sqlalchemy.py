import logging

from colorama import Style, Fore

from sqlalchemy import event
from sqlalchemy.engine import engine_from_config

from aio_manager import Command  # noqa: E402

logger = logging.getLogger(__name__)


class SACommand(Command):
    def __init__(self, name, app, declarative_base, url):
        super().__init__(name, app)
        self._db_url = url
        self._declarative_base = declarative_base

        if self._db_url is None:
            raise AssertionError(
                'db_url must be '
                'passed via url to class constructor.'
            )

    def create_engine(self):
        return engine_from_config(
            {'url': self._db_url, 'pool_recycle': 60},
            prefix=''
        )


class CreateTables(SACommand):
    """Creates DB tables for all models."""

    def __init__(self, *args, **kwargs):
        super().__init__('create_tables', *args, **kwargs)

    def _create_tables(self):
        def receive_after_create(target, connection, **kw):
            print('  ' + target.name + Fore.GREEN + ' created ' + Style.RESET_ALL)

        for name, table in self._declarative_base.metadata.tables.items():
            event.listen(table, 'after_create', receive_after_create)

        print(Fore.GREEN + 'Creating all tables' + Style.RESET_ALL)
        engine = self.create_engine()
        self._declarative_base.metadata.create_all(engine)

    def run(self, app, args):
        self._create_tables()


class DropTables(SACommand):
    """Drops DB tables for all models."""
    def __init__(self, *args, **kwargs):
        super().__init__('drop_tables', *args, **kwargs)

    def _drop_tables(self):
        def receive_after_drop(target, connection, **kw):
            print('  ' + target.name + Fore.RED + ' dropped ' + Style.RESET_ALL)

        for name, table in self._declarative_base.metadata.tables.items():
            event.listen(table, 'after_drop', receive_after_drop)

        print(Fore.RED + 'Dropping all tables' + Style.RESET_ALL)
        engine = self.create_engine()
        self._declarative_base.metadata.drop_all(engine)

    def run(self, app, args):
        self._drop_tables()


def configure_manager(manager, app, declarative_base, url):
    manager.add_command(CreateTables(app, declarative_base, url=url))
    manager.add_command(DropTables(app, declarative_base, url=url))
