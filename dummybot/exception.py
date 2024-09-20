import sys

class customexception(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,exec_tb = error_details.exc_info()

        self.lineno = exec_tb.tb_lineno
        self.filename = exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.lineno
