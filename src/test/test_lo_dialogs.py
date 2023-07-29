import unittest
from unittest import mock

from src.pythonpath.lo_dialogs import DialogHelper


class DialogsTestCase(unittest.TestCase):
    def test_message_box(self):
        # arrange
        component_ctx = mock.Mock()

        # act
        helper = DialogHelper(component_ctx)
        helper.message_box("title", "text")

        # assert
        self.assertEqual([
            mock.call.ServiceManager.createInstanceWithContext('com.sun.star.awt.Toolkit', mock.ANY),
            mock.call.getByName('/singletons/com.sun.star.frame.theDesktop'),
            mock.call.getByName().getCurrentComponent(),
            mock.call.ServiceManager.createInstanceWithContext().createMessageBox(mock.ANY, 0, 1, 'title', 'text'),
            mock.call.ServiceManager.createInstanceWithContext().createMessageBox().execute()
        ], component_ctx.mock_calls)


if __name__ == '__main__':
    unittest.main()
