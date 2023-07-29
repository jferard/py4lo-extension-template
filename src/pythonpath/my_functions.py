from lo_dialogs import DialogHelper, MessageBoxType


class MyFunctions:
    def __init__(self, component_ctx):
        self._component_ctx = component_ctx

    def my_method(self):
        helper = DialogHelper(self._component_ctx)
        helper.message_box(
            "It works", "Method `my_method`", MessageBoxType.MESSAGEBOX)
