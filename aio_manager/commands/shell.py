import code
import os

from aio_manager import Command


class Shell(Command):
    """
    Command to run the shell.
    """

    banner = 'AIOManager Shell. The "app" variable is available in the context.'

    def __init__(self, app):
        super().__init__('shell', app)

    def run(self, app, args):
        """
        Logic copied from https://github.com/smurfix/flask-script/blob/master/flask_script/commands.py
        """
        context = self.create_context(app)

        if not args.no_ptipython:
            # Try PtIPython
            try:
                from ptpython.ipython import embed
                history_filename = os.path.expanduser('~/.ptpython_history')
                embed(banner1=self.banner, user_ns=context, history_filename=history_filename)
                return
            except ImportError:
                pass

        if not args.no_ptpython:
            # Try PtPython
            try:
                from ptpython.repl import embed
                history_filename = os.path.expanduser('~/.ptpython_history')
                embed(globals=context, history_filename=history_filename)
                return
            except ImportError:
                pass

        if not args.no_bpython:
            # Try BPython
            try:
                from bpython import embed
                embed(banner=self.banner, locals_=context)
                return
            except ImportError:
                pass

        if not args.no_ipython:
            # Try IPython
            try:
                from IPython import embed
                embed(banner1=self.banner, user_ns=context)
                return
            except ImportError:
                pass

        code.interact(self.banner, local=context)

    def create_context(self, app):
        return {'app': app}

    def configure_parser(self, parser):
        super().configure_parser(parser)
        parser.add_argument('--no-ipython',
                            action='store_true',
                            dest='no_ipython',
                            help='Do not use the IPython shell')
        parser.add_argument('--no-bpython',
                            action='store_true',
                            dest='no_bpython',
                            help='Do not use the BPython shell')
        parser.add_argument('--no-ptipython',
                            action='store_true',
                            dest='no_ptipython',
                            help='Do not use the PtIPython shell')
        parser.add_argument('--no-ptpython',
                            action='store_true',
                            dest='no_ptpython',
                            help='Do not use the PtPython shell')
