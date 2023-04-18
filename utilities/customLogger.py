import logging
from datetime import time


class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger
        logger = logging.getLogger('ELMS Logger')
        logger.setLevel(logging.DEBUG)

        # create file handler which logs even info messages
        fh = logging.FileHandler('C:\\Users\\surya.n\\PycharmProjects\\ECMS\\logs\\logger.log')
        fh.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add the handlers to logger
        # logger.addHandler(ch)
        logger.addHandler(fh)

        # logger=logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger
