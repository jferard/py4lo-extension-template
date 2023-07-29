import logging

try:
    # noinspection PyUnresolvedReferences
    from com.sun.star.awt import (MessageBoxType, MessageBoxButtons)
except (ModuleNotFoundError, ImportError):
    class MessageBoxType:
        MESSAGEBOX = 0
        INFOBOX = 1
        WARNINGBOX = 2
        ERRORBOX = 3
        QUERYBOX = 4

    class MessageBoxButtons:
        BUTTONS_OK = 1
        BUTTONS_OK_CANCEL = 2


class DialogHelper:
    _logger = logging.getLogger(__name__)

    def __init__(self, component_ctx):
        self.component_ctx = component_ctx
        self.sm = self.component_ctx.ServiceManager

    def message_box(
            self, msg_title: str, msg_text: str,
            msg_type: MessageBoxType = MessageBoxType.MESSAGEBOX,
            msg_buttons: MessageBoxButtons = MessageBoxButtons.BUTTONS_OK,
            parent_win=None) -> int:
        # from https://forum.openoffice.org/fr/forum/viewtopic.php?f=15&t=47603
        # (thanks Bernard !)
        toolkit = self.sm.createInstanceWithContext(
            "com.sun.star.awt.Toolkit", self.component_ctx)
        if parent_win is None:
            oDesktop = self.component_ctx.getByName(
                "/singletons/com.sun.star.frame.theDesktop")
            oDoc = oDesktop.getCurrentComponent()
            controller = oDoc.CurrentController
            frame = controller.Frame
            parent_win = frame.ContainerWindow
        mb = toolkit.createMessageBox(
            parent_win, msg_type, msg_buttons, msg_title, msg_text)
        return mb.execute()
