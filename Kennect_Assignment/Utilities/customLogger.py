
import logging

class logGen():
    @staticmethod
    def logGen():
        logging.basicConfig(level=logging.INFO, force=True,
                            filename="logs/Automation.log",
                            format="%(asctime)s %(levelname)s %(message)s",
                            datefmt="%d/%m/%Y %I:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger