import unittest
from unittest import mock

from src.pythonpath.my_functions import MyFunctions


class MyfunctionsTestCase(unittest.TestCase):
    def test_my_functions(self):
        # arrange
        component_ctx = mock.Mock()

        # act
        helper = MyFunctions(component_ctx)
        helper.my_method()

        # assert
        self.assertEqual([
            mock.call.ServiceManager.createInstanceWithContext('com.sun.star.awt.Toolkit', mock.ANY),
            mock.call.getByName('/singletons/com.sun.star.frame.theDesktop'),
            mock.call.getByName().getCurrentComponent(),
            mock.call.ServiceManager.createInstanceWithContext().createMessageBox(mock.ANY, 0, 1, 'It works', 'Method `my_method`'),
            mock.call.ServiceManager.createInstanceWithContext().createMessageBox().execute()
        ], component_ctx.mock_calls)


if __name__ == '__main__':
    unittest.main()
