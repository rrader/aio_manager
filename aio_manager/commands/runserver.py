import asyncio
from aio_manager import Command
import logging


class RunServer(Command):
    """
    Creates aiohttp server coroutine and executes event loop
    """
    def __init__(self, app):
        super().__init__('run_server', app)

    async def run_server(self, app, loop, host, port):
        handler = app.make_handler()
        srv = await loop.create_server(handler, host, port)
        logging.getLogger().info('Server started at http://{}:{}'.format(host, port))
        return srv, handler

    def run(self, app, args):
        logging.basicConfig(level=args.level)
        logging.getLogger().setLevel(args.level)

        loop = asyncio.get_event_loop()
        srv, handler = loop.run_until_complete(self.run_server(app, loop, args.hostname, args.port))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            try:
                """
                ``finish_connection()`` is deprecated since aiohttp v1.2
                It's fully removed from aiohttp >= v2.3:
                https://github.com/aio-libs/aiohttp/pull/2006
                """
                shutdown_coro = handler.finish_connections()
            except AttributeError:
                """
                ``finish_connection()`` is an alias
                for ``shutdown()`` in aiohttp >=1.2,<2.3.
                """
                shutdown_coro = handler.shutdown()
            loop.run_until_complete(shutdown_coro)

    def configure_parser(self, parser):
        super().configure_parser(parser)
        parser.add_argument('--hostname', metavar='HOST',
                            help='host or ip to listen on')
        parser.add_argument('--port', type=int, metavar='PORT',
                            help='port to listening')
        parser.add_argument('--level', type=str, metavar='LEVEL',
                            help='logging level')
        parser.set_defaults(hostname='127.0.0.1', port=5000, level='INFO')
