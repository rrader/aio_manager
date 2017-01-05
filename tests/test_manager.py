import unittest

from aio_manager import BaseManager, Command


class HelloCommand(Command):
    def run(self, app, args):
        print('world')


class HelloManager(BaseManager):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.add_command(HelloCommand('hello', app))


class TestManager(unittest.TestCase):
    def setUp(self):
        self.app = object()

    def test_base(self):
        manager = BaseManager()
        self.assertEqual(0, len(manager.commands))

    def test_hello(self):
        manager = HelloManager(self.app)
        self.assertEqual(1, len(manager.commands))
        self.assertIsInstance(manager.commands[0], HelloCommand)

        argparser = manager.create_parser()
        parsed = argparser.parse_args(['hello'])
        self.assertIn('command', parsed)
        self.assertIsInstance(parsed.command, HelloCommand)

    def test_unknown(self):
        manager = HelloManager(self.app)

        argparser = manager.create_parser()
        with self.assertRaises(SystemExit):
            argparser.parse_args(['unknown'])


if __name__ == '__main__':
    unittest.main()
