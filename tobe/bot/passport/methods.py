from ..methods import BaseMethod


class setPassportDataErrors(BaseMethod):
    """Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

    Parameters
    ----------
    user_id : Integer
         User identifier
    errors : Array of PassportElementError
         A JSON-serialized array describing the errors
    """

    def __init__(self, user_id,
                 errors,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.errors = errors
