import sys

def error_message_details(error,error_detail:sys): #this (error_details:sys) gives details with respect to sys
    _,_,exc_tb=error_detail.exc_info() #the first two info is not that imp but last ie (exc_tb) is imp
    file_name=exc_tb.tb_frame.f_code.co_filename #this will give u the filename in which error is there
    error_message="Error occured in python file name[{0}] line number[{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
