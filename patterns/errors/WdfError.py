from patterns.errors.Error import Error


class WdfError(Error):
    """Exception raised for errors instantiating a WebDriver.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self,  message):
        self.message = message
