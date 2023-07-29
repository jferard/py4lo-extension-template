import os
import unittest
import platform
from pathlib import Path

from lo_helper import init_logger


class LOHelperTestCase(unittest.TestCase):
    def test_init_logger(self):
        system = platform.system()
        if system == "Windows":
            try:
                log_path = Path(os.environ["appdata"]) / "myextension.log"
            except KeyError:
                log_path = None
        elif system == "Linux":
            log_path = Path("/var/log/myextension.log")
        else:
            log_path = None
        init_logger(log_path)


if __name__ == '__main__':
    unittest.main()
