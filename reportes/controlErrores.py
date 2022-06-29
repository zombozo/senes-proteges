



import logging
import re


logger = logging.getLogger("Logger in reports")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('log_senes_proteges.log')
formater = logging.Formatter('%(astime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)

def get_loggerSenes():
    return logger