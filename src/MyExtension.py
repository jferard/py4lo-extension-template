import logging
import os
import platform
from pathlib import Path

from typing import Tuple

from lo_dialogs import DialogHelper, MessageBoxType
from lo_helper import init_logger
from my_functions import MyFunctions

try:
    # noinspection PyUnresolvedReferences
    import uno
except (ModuleNotFoundError, ImportError):
    class uno:
        pass

try:
    # noinspection PyUnresolvedReferences
    import unohelper
except (ModuleNotFoundError, ImportError):
    class unohelper:
        class Base:
            pass

        @staticmethod
        def ImplementationHelper():
            class C:
                @staticmethod
                def addImplementation(c, a, b): return None

            return C

try:
    # noinspection PyUnresolvedReferences
    from com.sun.star.task import XJobExecutor
except (ModuleNotFoundError, ImportError):
    class XJobExecutor:
        pass

IMPLEMENTATION_NAME = "com.github.myself.MyExtension"
system = platform.system()
if system == "Windows":
    try:
        LOG_PATH = Path(os.environ["appdata"]) / "myextension.log"
    except KeyError:
        LOG_PATH = None
elif system == "Linux":
    LOG_PATH = Path("/var/log/myextension.log") # sudo touch /var/log/myextension.log
else:
    LOG_PATH = None


class MyExtension(unohelper.Base, XJobExecutor):
    _inited = False
    _logger = logging.getLogger(__name__)

    def __init__(self, component_ctx):
        self._component_ctx = component_ctx
        self._oDesktop = self._component_ctx.getByName(
            "/singletons/com.sun.star.frame.theDesktop")
        self._oDoc = self._oDesktop.getCurrentComponent()
        if not MyExtension._inited:
            init_logger(LOG_PATH)
            self._logger.debug("Start of %s", self.__class__.__name__)
            MyExtension._inited = True

        self._service_manager = self._component_ctx.getServiceManager()
        self._logger.debug("New %s instance", self.__class__.__name__)

    # XJobExecutor / void 	trigger ([in] string Event)
    def trigger(self, event: str):
        self._logger.debug("Function call: %s", event)
        # noinspection PyBroadException
        try:
            self._trigger(event.strip())
        except Exception:
            self._logger.exception("General error")

    # XServiceName /
    def getServiceName(self) -> str:
        return IMPLEMENTATION_NAME

    # XServiceInfo / string 	getImplementationName ()
    def getImplementationName(self) -> str:
        return IMPLEMENTATION_NAME

    # XServiceInfo / boolean 	supportsService ([in] string ServiceName)
    def supportsService(self, service_name: str) -> bool:
        return service_name in self.getSupportedServiceNames()

    # XServiceInfo / sequence< string > 	getSupportedServiceNames ()
    def getSupportedServiceNames(self) -> Tuple[str, ...]:
        return IMPLEMENTATION_NAME,

    def _trigger(self, func_name: str):
        try:
            func = METHOD_BY_NAME[func_name]
            func(self)
        except KeyError:
            helper = DialogHelper(self._component_ctx)
            helper.message_box(
                "Missing function",
                "Function `{}` is missing".format(func_name),
                MessageBoxType.ERRORBOX)

    def my_method(self):
        MyFunctions(self._component_ctx).my_method()


METHOD_BY_NAME = {
    "myMethod": MyExtension.my_method
}

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    MyExtension, IMPLEMENTATION_NAME, ('com.sun.star.task.Job',))
