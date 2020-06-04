import logging
import time
import traceback

from patterns.util import custom_logger as cl


class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Sleep utility method
        """
        if info is not None:
            self.log.info("Waiting '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def verify_text_contains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual is " + actualText)
        self.log.info("Expected is " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match
        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual is " + actualText)
        self.log.info("Expected is " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches
        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list
        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True
