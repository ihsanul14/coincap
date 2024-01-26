import logging

class Logger:
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(asctime)s - %(message)s')
    logger = logging.getLogger(__name__)
    def Info(self, error):
        self.logger.info(error)
        
    def Warning(self, error):
        self.logger.warning(error)
        
    def Error(self, error):
        self.logger.error(error)