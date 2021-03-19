import logging
import logging.config
import yaml

with open(file=r"logging.config.yaml", mode="r", encoding="utf-8") as config_file:
    config_file_content = yaml.load(stream=config_file, Loader=yaml.FullLoader)

logging.config.dictConfig(config=config_file_content)

# create logger
logger = logging.getLogger('simple_example')

logger.warning("Warning")
logger.info("It is an info")
logger.error("Error occured")