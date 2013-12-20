import zope.interface


AUTHENTICATED = '\x04'
ERROR = '\x10'
HEARTBEAT = '\x06'
HELLO = '\x02'
OK = '\x01'
UNAUTHORIZED = '\x11'
WORK = '\x03'

VERSION = 'v1'


class ServiceNotFoundError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class IAuthenticationBackend(zope.interface.Interface):

    def configure():
        """
        Hook to adapt your RPC peer.
        Must be used to start any service like a zap_handler
        """

    def stop():
        """
        Hook to stop any service running in background.
        Can be either IOLoop, threading, or multiprocess.
        """

    def handle_hello(message, peer_id, message_uuid):
        """
        """

    def handle_authenticated(message):
        """
        """

    def save_last_work(message):
        """
        """

    def is_authenticated(peer_id):
        """
        """


class BaseRPC(zope.interface.Interface):
    """
    """


class IClient(BaseRPC):
    """
    Interface for Clients
    """


class IServer(BaseRPC):
    """
    Interface for Servers
    """


class IHeartbeatBackend(zope.interface.Interface):
    """
    Interface for heartbeat backend
    """
    def handle_heartbeat(peer_id):
        """
        """

    def handle_timeout(peer_id):
        """
        """

    def configure():
        """
        """

    def stop():
        """
        """


class IRPCCallable(zope.interface.Interface):
    """
    """
    def __call__(*args, **kw):
        """
        """

    def test(*args, **kw):
        """
        """


class IRPCRoute(zope.interface.Interface):
    """
    """


class IPredicate(zope.interface.Interface):
    """
    """
    def test(*args, **kw):
        """
        """