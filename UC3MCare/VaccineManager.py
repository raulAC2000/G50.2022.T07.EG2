import json
from UC3MCare import VaccineManagementException
from .VaccineRequest import VaccineRequest

class VaccineManager:
    def __init__(self):
        pass

    def ValidateGUID( self, GUID ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        import re
        r = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$')
        res = r.search(GUID)
        if res is None:
            return False
        else:
            return True
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE

        return True

    def ReadaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise VaccineManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            Guid = DATA["id"]
            Zip = DATA["phoneNumber"]
            req = VaccineRequest(Guid, Zip)
        except KeyError as e:
            raise VaccineManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateGUID(Guid):
            raise VaccineManagementException("Invalid GUID")

        # Close the file
        return req