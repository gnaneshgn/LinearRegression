import os
import sys


class LinearRegressionException(Exception):

   def __init__(self,error_message:Exception,error_details:sys):
    super().__init__(error_message)


    @staticmethod
    def get_detialed_message(error_message:Exception,error_details:sys):
        """
        error_message : Exception object
        error_detial : object of sys module
        """
        _,_,exec_line=error_details.exc_info()
        line_number=exec_line.tb_frame.f_lineno
        file_name=exec_line.tb_frame.f_code.co_filename
        error_message=f"Error occured in script[{file_name}] at line number [{line_number}] error message:[{error_message}] "       
        return error_message

    def __str__(self)->str:
        return self.error_message
    
    def __repr__(self) -> str:
        return LinearRegressionException.__name__.str()