
import logging
import re


# logging.basicConfig(filename='senes.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log_senes_proteges.log')
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)

def get_loggerSenes():
    return logger