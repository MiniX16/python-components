import logging
from time import sleep
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

logging.basicConfig(format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)

class ConstrainedDeviceApp:
    """
    Definition of the ConstrainedDeviceApp class.
    """

    def __init__(self):
        logging.info("Initializing CDA...")
        self.sysPerfMgr = SystemPerformanceManager()

    def startApp(self):
        logging.info("Starting CDA...")
        self.sysPerfMgr.startManager()
        logging.info("CDA started.")

    def stopApp(self, code: int):
        logging.info("CDA stopping...")
        self.sysPerfMgr.stopManager()
        logging.info("CDA stopped with exit code %s.", str(code))

    def parseArgs(self, args):
        """
        Parse command line args.
        
        @param args: The arguments to parse.
        """
        logging.info("Parsing command line args...")


def main():
    """
    Main function definition for running client as application.

    Current implementation runs for 65 seconds then exits.
    """
    cda = ConstrainedDeviceApp()
    cda.startApp()

    # Run for 65 seconds - this can be changed as needed
    sleep(65)

    # Optionally stop the app - this can be removed if needed
    cda.stopApp(0)


if __name__ == '__main__':
    """
    Attribute definition for when invoking as app via command line.
    """
    main()
