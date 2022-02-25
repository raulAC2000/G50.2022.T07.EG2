import json
from datetime import datetime
import pandas

class VaccineRequest:
    """
    @class VaccineRequest
    """

    def __init__(self, id_code, phone_number):
        """
        :param id_code:
        :param phone_number:
        """
        self.__phone_number = phone_number
        self.__id_code = id_code
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def phone_1( self ):
        """
        :return:
        """
        return self.__phone_number
    @phone_1.setter
    def phone_1( self, value ):
        self.__phone_number = value

    @property
    def id_document(self):
        """
        @id_document
        :return:
        """
        return self.__id_code
    @id_document.setter
    def id_document(self,value):
        self.__id_code = value
