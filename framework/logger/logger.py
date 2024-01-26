import logging

class Logger:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    def Info(self, error):
        self.logger.info(error)
    def Warning(self, error):
        self.logger.warn(error)
    def Error(self, error):
        self.logger.error(error)