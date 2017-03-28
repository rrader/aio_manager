import logging

from colorama import Style, Fore

from sqlalchemy import event
from sqlalchemy.engine import engine_from_config

from aio_manager import Command  # noqa: E402

logger = logging.getLogger(__name__)


class SACommand(Command):
    cmd_name = None
    cmd_action = None
    cmd_action_desc = None
    sql_event = None
    sql_action_callable = None

    def __init__(self, app, declarative_base, url):
        if not (self.cmd_name and self.cmd_action and
                self.cmd_action_desc and self.sql_event):
            raise NotImplementedError(
                'Programmer error: '
                'cmd_name string must be set and represent CLI command name; '
                'cmd_action string must be set and represent command action; '
                'cmd_action_desc string must be set and describe command action; '
                'sql_event string must be set and be sqlalchemy.event; '
                "sql_action_callable string must be set and be metadata's method."
            )

        super().__init__(self.cmd_name, app)
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

    def __get_sql_callable(self):
        return getattr(self._declarative_base.metadata, self.sql_action_callable)

    def __receive_after_event(self, target, connection, **kw):
        print('  ' + target.name + Fore.GREEN + ' ' + self.cmd_action + ' ' + Style.RESET_ALL)

    def _sql_action(self):
        for name, table in self._declarative_base.metadata.tables.items():
            event.listen(table, self.sql_event, self.__receive_after_event)

        print(Fore.GREEN + self.cmd_action_desc + Style.RESET_ALL)
        engine = self.create_engine()
        self.__get_sql_callable()(engine)

    def run(self, app, args):
        self._sql_action()


class CreateTables(SACommand):
    """Creates DB tables for all models."""
    cmd_name = 'create_tables'
    cmd_action = 'created'
    cmd_action_desc = 'Creating all tables'
    sql_event = 'after_create'
    sql_action_callable = 'create_all'


class DropTables(SACommand):
    """Drops DB tables for all models."""
    cmd_name = 'drop_tables'
    cmd_action = 'dropped'
    cmd_action_desc = 'Dropping all tables'
    sql_event = 'after_drop'
    sql_action_callable = 'drop_all'


def configure_manager(manager, app, declarative_base, url):
    manager.add_command(CreateTables(app, declarative_base, url=url))
    manager.add_command(DropTables(app, declarative_base, url=url))
