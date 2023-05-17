from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class PrivilegedOperationEvent(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedOperationEvent and sets the default values.
        """
        super().__init__()
        # The additionalInformation property
        self._additional_information: Optional[str] = None
        # The creationDateTime property
        self._creation_date_time: Optional[datetime] = None
        # The expirationDateTime property
        self._expiration_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The referenceKey property
        self._reference_key: Optional[str] = None
        # The referenceSystem property
        self._reference_system: Optional[str] = None
        # The requestType property
        self._request_type: Optional[str] = None
        # The requestorId property
        self._requestor_id: Optional[str] = None
        # The requestorName property
        self._requestor_name: Optional[str] = None
        # The roleId property
        self._role_id: Optional[str] = None
        # The roleName property
        self._role_name: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The userId property
        self._user_id: Optional[str] = None
        # The userMail property
        self._user_mail: Optional[str] = None
        # The userName property
        self._user_name: Optional[str] = None
    
    @property
    def additional_information(self,) -> Optional[str]:
        """
        Gets the additionalInformation property value. The additionalInformation property
        Returns: Optional[str]
        """
        return self._additional_information
    
    @additional_information.setter
    def additional_information(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInformation property value. The additionalInformation property
        Args:
            value: Value to set for the additional_information property.
        """
        self._additional_information = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedOperationEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedOperationEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedOperationEvent()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. The creationDateTime property
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. The creationDateTime property
        Args:
            value: Value to set for the creation_date_time property.
        """
        self._creation_date_time = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expirationDateTime property
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expirationDateTime property
        Args:
            value: Value to set for the expiration_date_time property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "referenceKey": lambda n : setattr(self, 'reference_key', n.get_str_value()),
            "referenceSystem": lambda n : setattr(self, 'reference_system', n.get_str_value()),
            "requestorId": lambda n : setattr(self, 'requestor_id', n.get_str_value()),
            "requestorName": lambda n : setattr(self, 'requestor_name', n.get_str_value()),
            "requestType": lambda n : setattr(self, 'request_type', n.get_str_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleName": lambda n : setattr(self, 'role_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userMail": lambda n : setattr(self, 'user_mail', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reference_key(self,) -> Optional[str]:
        """
        Gets the referenceKey property value. The referenceKey property
        Returns: Optional[str]
        """
        return self._reference_key
    
    @reference_key.setter
    def reference_key(self,value: Optional[str] = None) -> None:
        """
        Sets the referenceKey property value. The referenceKey property
        Args:
            value: Value to set for the reference_key property.
        """
        self._reference_key = value
    
    @property
    def reference_system(self,) -> Optional[str]:
        """
        Gets the referenceSystem property value. The referenceSystem property
        Returns: Optional[str]
        """
        return self._reference_system
    
    @reference_system.setter
    def reference_system(self,value: Optional[str] = None) -> None:
        """
        Sets the referenceSystem property value. The referenceSystem property
        Args:
            value: Value to set for the reference_system property.
        """
        self._reference_system = value
    
    @property
    def request_type(self,) -> Optional[str]:
        """
        Gets the requestType property value. The requestType property
        Returns: Optional[str]
        """
        return self._request_type
    
    @request_type.setter
    def request_type(self,value: Optional[str] = None) -> None:
        """
        Sets the requestType property value. The requestType property
        Args:
            value: Value to set for the request_type property.
        """
        self._request_type = value
    
    @property
    def requestor_id(self,) -> Optional[str]:
        """
        Gets the requestorId property value. The requestorId property
        Returns: Optional[str]
        """
        return self._requestor_id
    
    @requestor_id.setter
    def requestor_id(self,value: Optional[str] = None) -> None:
        """
        Sets the requestorId property value. The requestorId property
        Args:
            value: Value to set for the requestor_id property.
        """
        self._requestor_id = value
    
    @property
    def requestor_name(self,) -> Optional[str]:
        """
        Gets the requestorName property value. The requestorName property
        Returns: Optional[str]
        """
        return self._requestor_name
    
    @requestor_name.setter
    def requestor_name(self,value: Optional[str] = None) -> None:
        """
        Sets the requestorName property value. The requestorName property
        Args:
            value: Value to set for the requestor_name property.
        """
        self._requestor_name = value
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. The roleId property
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. The roleId property
        Args:
            value: Value to set for the role_id property.
        """
        self._role_id = value
    
    @property
    def role_name(self,) -> Optional[str]:
        """
        Gets the roleName property value. The roleName property
        Returns: Optional[str]
        """
        return self._role_name
    
    @role_name.setter
    def role_name(self,value: Optional[str] = None) -> None:
        """
        Sets the roleName property value. The roleName property
        Args:
            value: Value to set for the role_name property.
        """
        self._role_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("referenceKey", self.reference_key)
        writer.write_str_value("referenceSystem", self.reference_system)
        writer.write_str_value("requestorId", self.requestor_id)
        writer.write_str_value("requestorName", self.requestor_name)
        writer.write_str_value("requestType", self.request_type)
        writer.write_str_value("roleId", self.role_id)
        writer.write_str_value("roleName", self.role_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userMail", self.user_mail)
        writer.write_str_value("userName", self.user_name)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The userId property
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The userId property
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_mail(self,) -> Optional[str]:
        """
        Gets the userMail property value. The userMail property
        Returns: Optional[str]
        """
        return self._user_mail
    
    @user_mail.setter
    def user_mail(self,value: Optional[str] = None) -> None:
        """
        Sets the userMail property value. The userMail property
        Args:
            value: Value to set for the user_mail property.
        """
        self._user_mail = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The userName property
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The userName property
        Args:
            value: Value to set for the user_name property.
        """
        self._user_name = value
    

