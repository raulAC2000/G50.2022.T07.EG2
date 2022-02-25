"""
@description: Archivo de gestión de la clase VaccineManager
@author: UC3M
@email:
@version: 0.1.0
@date: 25/02/22
@warning:
"""

import json
import re
from .VaccineRequest import VaccineRequest
from .VaccineManagementException import VaccineManagementException

class VaccineManager:
    """
    @description: Gestiona los GUID de los usuarios para su vacunación
    @throw: VaccineManagementException
    """
    def __init__(self):
        """
        @description: Inicia una instancia de la clase VaccineManager
        @param: self
        """
        self.__result__ = False

    def validateGUID(self, guid):
        """
        @description: Valida un GUID de usuario
        @param: self
        @param: guid
        @return: True Si el GUID es correcto
        @return: False Si el GUID es incorrecto
        """
        regex = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB]'
                           r'[0-9A-F]{3}-[0-9A-F]{12}$')
        result = regex.search(guid)
        if result is None:
            return False
        self.__result__ = result
        return True

    def readAccessRequestFromJSON(self, input_file):
        """
        @description: Lee
        @param: self
        @param: input_file
        @return: True Si el GUID es correcto
        @return: False Si el GUID es incorrecto
        """
        try:
            with open(input_file, encoding="utf8") as file:
                data = json.load(file)
        except FileNotFoundError as exception:
            raise VaccineManagementException("Wrong file or file path") from exception
        except json.JSONDecodeError as exception:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format")\
                from exception

        try:
            guid = data["id"]
            phone_number = data["phoneNumber"]
            request = VaccineRequest(guid, phone_number)
        except KeyError as exception:
            raise VaccineManagementException("JSON Decode Error - Invalid JSON Key") \
                from exception
        if not self.validateGUID(guid):
            raise VaccineManagementException("Invalid GUID")

        # Close the file
        return request
