#!/usr/bin/env python3
###############################################################################%

import sys
import logging
import colorlog

#logging.basicConfig(
#    format="%(levelname)s | %(asctime)s | %(message)s",
#    datefmt="%Y-%m-%dT%H:%M:%SZ",
#)

logger = logging.getLogger(__name__)

stdout = colorlog.StreamHandler(stream=sys.stdout)

fmt = colorlog.ColoredFormatter(
    "%(name)s: %(white)s%(asctime)s%(reset)s | %(log_color)s%(levelname)s%(reset)s | %(blue)s%(filename)s:%(lineno)s%(reset)s | %(process)d >>> %(log_color)s%(message)s%(reset)s"
)

stdout.setFormatter(fmt)
logger.addHandler(stdout)

#stdout.setLevel(logging.INFO)

logger.setLevel(logging.DEBUG)


logger.debug("A debug message")
logger.info("An info message")
logger.warning("A warning message")
logger.error("An error message")
logger.critical("A critical message")

