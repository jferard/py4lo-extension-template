import logging
from pathlib import Path
from typing import Union, Optional


def init_logger(log_path: Union[str, Path], mode: str = "a",
                level: int = logging.DEBUG,
                log_format: Optional[str] = None):
    logger = logging.getLogger()
    if log_format is None:
        log_format = ('%(asctime)s - %(name)s - %(levelname)s - '
                      '%(module)s -  %(lineno)d - %(funcName)s - %(message)s')

    fh = logging.FileHandler(str(log_path), mode, encoding="utf-8")
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    fh.setLevel(level)
    logger.addHandler(fh)
    logger.setLevel(level)
