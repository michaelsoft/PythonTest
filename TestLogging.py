import logging
import logging.config

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = logging.FileHandler(filename=r"c:\temp\test.log", encoding="utf-8")
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

logger.warning("Warning")
logger.info("It is an info")
logger.error("Error occured")