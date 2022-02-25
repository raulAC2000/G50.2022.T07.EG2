"""
@description: Código de gestión de peticiones de vacunación
@author: UC3M
@email:
@version: 0.1.0
@date: 25/02/22
@warning:
"""

import json
from datetime import datetime

class VaccineRequest:
    """
    @description: Modela las peticiones de vacunación
    """

    def __init__(self, identifier, phone_number):
        """
        @description: instancia la clase
        @param self
        @param id_code:
        @param phone_number:
        """
        self.__phone_number__ = phone_number
        self.__identifier__= identifier
        justnow = datetime.utcnow()
        self.__time_stamp__ = datetime.time_stamp(justnow)

    def __str__(self):
        """
        @description: Devuelve un string con información del objeto
        @param self
        @return string con la información
        """
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def phone( self ):
        """
        @description: getter del número de teléfono
        @param self
        @return El número de teléfono de la petición
        """
        return self.__phone_number__

    @phone.setter
    def phone( self, phone_number ):
        """
        @description: setter del número de teléfono
        @param self
        @param phone_number
        """
        self.__phone_number__ = phone_number

    @property
    def identifier(self):
        """
        @description: getter del identificador
        @param self
        @return El identificador
        """

        return self.__identifier__

    @identifier.setter
    def identifier(self, identifier):
        self.__identifier__ = identifier
