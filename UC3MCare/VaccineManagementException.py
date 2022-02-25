"""
@description: Archivo de excepción para VaccineManagementException
@author: UC3M
@email:
@version: 0.1.0
@date: 25/02/22
@warning:
"""

class VaccineManagementException(Exception):
    """
    @description: Crea una nueva excepción para la gestión de vacunas
    """
    def __init__(self, message):
        """
        @description: Inicia una instancia de la excepción VaccineManagementException
        @param: self
        @param: message
        :rtype: object
        """
        self.__message__ = message
        super().__init__(self.message)

    @property
    def message(self):
        """
        @description: Getter del mensaje de la excepción
        @param: self
        @return: message
        """
        return self.__message__

    @message.setter
    def message(self, value):
        """
        @description: Setter el mensaje de la excepción
        @param: self
        @param: value
        """
        self.__message__ = value
