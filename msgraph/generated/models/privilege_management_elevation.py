from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, privilege_management_elevation_type, privilege_management_end_user_type

from . import entity

class PrivilegeManagementElevation(entity.Entity):
    """
    The endpoint privilege management elevation result entity representing a single elevation action on a client device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new privilegeManagementElevation and sets the default values.
        """
        super().__init__()
        # The certificate payload of the application. This is computed by hashing the certificate information on the client. Example: `32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a50`
        self._certificate_payload: Optional[str] = None
        # The company name of the application. This value is set by the creator of the application. Example: `Microsoft Corporation`
        self._company_name: Optional[str] = None
        # The Intune deviceId. Unique identifier for the managed device. Example: `92ce5047-9553-4731-817f-9b401a999a1b`
        self._device_id: Optional[str] = None
        # The name associated with the device in the intune database. Example: `JOHNDOE-LAPTOP`.
        self._device_name: Optional[str] = None
        # Indicates the type of elevation occured
        self._elevation_type: Optional[privilege_management_elevation_type.PrivilegeManagementElevationType] = None
        # The date and time when the application was elevated. Example:`2014-01-01T00:00:00Z`
        self._event_date_time: Optional[datetime] = None
        # The file description of the application. This value is set by the creator of the application. Example: `Editor of multiple coding languages.`
        self._file_description: Optional[str] = None
        # The full file path of the application including the filename and file extension. Example: `C:/Program Files/vscode.exe`
        self._file_path: Optional[str] = None
        # The version of the application. This value is set by the creator of the application. Example: `6.2211.1035.1000`
        self._file_version: Optional[str] = None
        # The sha256 hash of the application. Example: `32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a57`
        self._hash: Optional[str] = None
        # The internal name of the application. This value is set by the creator of the application. Example: `VS code`
        self._internal_name: Optional[str] = None
        # The justification to elevate the application. This is an input by the user when the privilegeManagementElevationType is of type userConfirmedElevation or support approved elevation. This will be null in all other scenarios. The length is capped at 256 char, enforced on the client side. Example: `To install debug tool.`.
        self._justification: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The product name of the application. This value is set by the creator of the application. Example: `Visual Studio`
        self._product_name: Optional[str] = None
        # The result of the elevation action with 0 being success, and everything else being exit code if the elevation was unsuccessful. The value will always be 0 on all unmanaged elevation. Example: `0`. Valid values 0 to 2147483647
        self._result: Optional[int] = None
        # The User Principal Name of the user who performed the elevation. Example: `john@domain.com`
        self._upn: Optional[str] = None
        # The type of user account on Windows that was used to performed the elevation.
        self._user_type: Optional[privilege_management_end_user_type.PrivilegeManagementEndUserType] = None
    
    @property
    def certificate_payload(self,) -> Optional[str]:
        """
        Gets the certificatePayload property value. The certificate payload of the application. This is computed by hashing the certificate information on the client. Example: `32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a50`
        Returns: Optional[str]
        """
        return self._certificate_payload
    
    @certificate_payload.setter
    def certificate_payload(self,value: Optional[str] = None) -> None:
        """
        Sets the certificatePayload property value. The certificate payload of the application. This is computed by hashing the certificate information on the client. Example: `32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a50`
        Args:
            value: Value to set for the certificate_payload property.
        """
        self._certificate_payload = value
    
    @property
    def company_name(self,) -> Optional[str]:
        """
        Gets the companyName property value. The company name of the application. This value is set by the creator of the application. Example: `Microsoft Corporation`
        Returns: Optional[str]
        """
        return self._company_name
    
    @company_name.setter
    def company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the companyName property value. The company name of the application. This value is set by the creator of the application. Example: `Microsoft Corporation`
        Args:
            value: Value to set for the company_name property.
        """
        self._company_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegeManagementElevation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegeManagementElevation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegeManagementElevation()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The Intune deviceId. Unique identifier for the managed device. Example: `92ce5047-9553-4731-817f-9b401a999a1b`
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The Intune deviceId. Unique identifier for the managed device. Example: `92ce5047-9553-4731-817f-9b401a999a1b`
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The name associated with the device in the intune database. Example: `JOHNDOE-LAPTOP`.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The name associated with the device in the intune database. Example: `JOHNDOE-LAPTOP`.
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    @property
    def elevation_type(self,) -> Optional[privilege_management_elevation_type.PrivilegeManagementElevationType]:
        """
        Gets the elevationType property value. Indicates the type of elevation occured
        Returns: Optional[privilege_management_elevation_type.PrivilegeManagementElevationType]
        """
        return self._elevation_type
    
    @elevation_type.setter
    def elevation_type(self,value: Optional[privilege_management_elevation_type.PrivilegeManagementElevationType] = None) -> None:
        """
        Sets the elevationType property value. Indicates the type of elevation occured
        Args:
            value: Value to set for the elevation_type property.
        """
        self._elevation_type = value
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. The date and time when the application was elevated. Example:`2014-01-01T00:00:00Z`
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. The date and time when the application was elevated. Example:`2014-01-01T00:00:00Z`
        Args:
            value: Value to set for the event_date_time property.
        """
        self._event_date_time = value
    
    @property
    def file_description(self,) -> Optional[str]:
        """
        Gets the fileDescription property value. The file description of the application. This value is set by the creator of the application. Example: `Editor of multiple coding languages.`
        Returns: Optional[str]
        """
        return self._file_description
    
    @file_description.setter
    def file_description(self,value: Optional[str] = None) -> None:
        """
        Sets the fileDescription property value. The file description of the application. This value is set by the creator of the application. Example: `Editor of multiple coding languages.`
        Args:
            value: Value to set for the file_description property.
        """
        self._file_description = value
    
    @property
    def file_path(self,) -> Optional[str]:
        """
        Gets the filePath property value. The full file path of the application including the filename and file extension. Example: `C:/Program Files/vscode.exe`
        Returns: Optional[str]
        """
        return self._file_path
    
    @file_path.setter
    def file_path(self,value: Optional[str] = None) -> None:
        """
        Sets the filePath property value. The full file path of the application including the filename and file extension. Example: `C:/Program Files/vscode.exe`
        Args:
            value: Value to set for the file_path property.
        """
        self._file_path = value
    
    @property
    def file_version(self,) -> Optional[str]:
        """
        Gets the fileVersion property value. The version of the application. This value is set by the creator of the application. Example: `6.2211.1035.1000`
        Returns: Optional[str]
        """
        return self._file_version
    
    @file_version.setter
    def file_version(self,value: Optional[str] = None) -> None:
        """
        Sets the fileVersion property value. The version of the application. This value is set by the creator of the application. Example: `6.2211.1035.1000`
        Args:
            value: Value to set for the file_version property.
        """
        self._file_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, privilege_management_elevation_type, privilege_management_end_user_type

        fields: Dict[str, Callable[[Any], None]] = {
            "certificatePayload": lambda n : setattr(self, 'certificate_payload', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "elevationType": lambda n : setattr(self, 'elevation_type', n.get_enum_value(privilege_management_elevation_type.PrivilegeManagementElevationType)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "fileDescription": lambda n : setattr(self, 'file_description', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "fileVersion": lambda n : setattr(self, 'file_version', n.get_str_value()),
            "hash": lambda n : setattr(self, 'hash', n.get_str_value()),
            "internalName": lambda n : setattr(self, 'internal_name', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_int_value()),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(privilege_management_end_user_type.PrivilegeManagementEndUserType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hash(self,) -> Optional[str]:
        """
        Gets the hash property value. The sha256 hash of the application. Example: `32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a57`
        Returns: Optional[str]
        """
        return self._hash
    
    @hash.setter
    def hash(self,value: Optional[str] = None) -> None:
        """
        Sets the hash property value. The sha256 hash of the application. Example: `32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a57`
        Args:
            value: Value to set for the hash property.
        """
        self._hash = value
    
    @property
    def internal_name(self,) -> Optional[str]:
        """
        Gets the internalName property value. The internal name of the application. This value is set by the creator of the application. Example: `VS code`
        Returns: Optional[str]
        """
        return self._internal_name
    
    @internal_name.setter
    def internal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the internalName property value. The internal name of the application. This value is set by the creator of the application. Example: `VS code`
        Args:
            value: Value to set for the internal_name property.
        """
        self._internal_name = value
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The justification to elevate the application. This is an input by the user when the privilegeManagementElevationType is of type userConfirmedElevation or support approved elevation. This will be null in all other scenarios. The length is capped at 256 char, enforced on the client side. Example: `To install debug tool.`.
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The justification to elevate the application. This is an input by the user when the privilegeManagementElevationType is of type userConfirmedElevation or support approved elevation. This will be null in all other scenarios. The length is capped at 256 char, enforced on the client side. Example: `To install debug tool.`.
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def product_name(self,) -> Optional[str]:
        """
        Gets the productName property value. The product name of the application. This value is set by the creator of the application. Example: `Visual Studio`
        Returns: Optional[str]
        """
        return self._product_name
    
    @product_name.setter
    def product_name(self,value: Optional[str] = None) -> None:
        """
        Sets the productName property value. The product name of the application. This value is set by the creator of the application. Example: `Visual Studio`
        Args:
            value: Value to set for the product_name property.
        """
        self._product_name = value
    
    @property
    def result(self,) -> Optional[int]:
        """
        Gets the result property value. The result of the elevation action with 0 being success, and everything else being exit code if the elevation was unsuccessful. The value will always be 0 on all unmanaged elevation. Example: `0`. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._result
    
    @result.setter
    def result(self,value: Optional[int] = None) -> None:
        """
        Sets the result property value. The result of the elevation action with 0 being success, and everything else being exit code if the elevation was unsuccessful. The value will always be 0 on all unmanaged elevation. Example: `0`. Valid values 0 to 2147483647
        Args:
            value: Value to set for the result property.
        """
        self._result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("certificatePayload", self.certificate_payload)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("elevationType", self.elevation_type)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("fileDescription", self.file_description)
        writer.write_str_value("filePath", self.file_path)
        writer.write_str_value("fileVersion", self.file_version)
        writer.write_str_value("hash", self.hash)
        writer.write_str_value("internalName", self.internal_name)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("productName", self.product_name)
        writer.write_int_value("result", self.result)
        writer.write_str_value("upn", self.upn)
        writer.write_enum_value("userType", self.user_type)
    
    @property
    def upn(self,) -> Optional[str]:
        """
        Gets the upn property value. The User Principal Name of the user who performed the elevation. Example: `john@domain.com`
        Returns: Optional[str]
        """
        return self._upn
    
    @upn.setter
    def upn(self,value: Optional[str] = None) -> None:
        """
        Sets the upn property value. The User Principal Name of the user who performed the elevation. Example: `john@domain.com`
        Args:
            value: Value to set for the upn property.
        """
        self._upn = value
    
    @property
    def user_type(self,) -> Optional[privilege_management_end_user_type.PrivilegeManagementEndUserType]:
        """
        Gets the userType property value. The type of user account on Windows that was used to performed the elevation.
        Returns: Optional[privilege_management_end_user_type.PrivilegeManagementEndUserType]
        """
        return self._user_type
    
    @user_type.setter
    def user_type(self,value: Optional[privilege_management_end_user_type.PrivilegeManagementEndUserType] = None) -> None:
        """
        Sets the userType property value. The type of user account on Windows that was used to performed the elevation.
        Args:
            value: Value to set for the user_type property.
        """
        self._user_type = value
    

