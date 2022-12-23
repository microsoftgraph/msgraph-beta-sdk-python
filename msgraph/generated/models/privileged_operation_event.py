from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class PrivilegedOperationEvent(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def additional_information(self,) -> Optional[str]:
        """
        Gets the additionalInformation property value. Detailed human readable information for the event.
        Returns: Optional[str]
        """
        return self._additional_information
    
    @additional_information.setter
    def additional_information(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInformation property value. Detailed human readable information for the event.
        Args:
            value: Value to set for the additionalInformation property.
        """
        self._additional_information = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedOperationEvent and sets the default values.
        """
        super().__init__()
        # Detailed human readable information for the event.
        self._additional_information: Optional[str] = None
        # Indicates the time when the event is created.
        self._creation_date_time: Optional[datetime] = None
        # This is only used when the requestType is Activate, and it indicates the expiration time for the role activation.
        self._expiration_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Incident/Request ticket number during role activation. The value is presented only if the ticket number is provided during role activation.
        self._reference_key: Optional[str] = None
        # Incident/Request ticketing system provided during tole activation. The value is presented only if the ticket system is provided during role activation.
        self._reference_system: Optional[str] = None
        # The user id of the requestor who initiates the operation.
        self._requestor_id: Optional[str] = None
        # The user name of the requestor who initiates the operation.
        self._requestor_name: Optional[str] = None
        # The request operation type. The requestType value can be: Assign (role assignment), Activate (role activation), Unassign (remove role assignment), Deactivate (role deactivation), ScanAlertsNow (scan security alerts), DismissAlert (dismiss security alert), FixAlertItem (fix a security alert issue),  AccessReview_Review (review an Access Review), AccessReview_Create (create an Access Review) , AccessReview_Update (update an Access Review), AccessReview_Delete (delete an Access Review).
        self._request_type: Optional[str] = None
        # The id of the role that is associated with the operation.
        self._role_id: Optional[str] = None
        # The name of the role.
        self._role_name: Optional[str] = None
        # The tenant (organization) id.
        self._tenant_id: Optional[str] = None
        # The id of the user that is associated with the operation.
        self._user_id: Optional[str] = None
        # The user's email.
        self._user_mail: Optional[str] = None
        # The user's display name.
        self._user_name: Optional[str] = None
    
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
        Gets the creationDateTime property value. Indicates the time when the event is created.
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. Indicates the time when the event is created.
        Args:
            value: Value to set for the creationDateTime property.
        """
        self._creation_date_time = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. This is only used when the requestType is Activate, and it indicates the expiration time for the role activation.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. This is only used when the requestType is Activate, and it indicates the expiration time for the role activation.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_information": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "reference_key": lambda n : setattr(self, 'reference_key', n.get_str_value()),
            "reference_system": lambda n : setattr(self, 'reference_system', n.get_str_value()),
            "requestor_id": lambda n : setattr(self, 'requestor_id', n.get_str_value()),
            "requestor_name": lambda n : setattr(self, 'requestor_name', n.get_str_value()),
            "request_type": lambda n : setattr(self, 'request_type', n.get_str_value()),
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_name": lambda n : setattr(self, 'role_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_mail": lambda n : setattr(self, 'user_mail', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reference_key(self,) -> Optional[str]:
        """
        Gets the referenceKey property value. Incident/Request ticket number during role activation. The value is presented only if the ticket number is provided during role activation.
        Returns: Optional[str]
        """
        return self._reference_key
    
    @reference_key.setter
    def reference_key(self,value: Optional[str] = None) -> None:
        """
        Sets the referenceKey property value. Incident/Request ticket number during role activation. The value is presented only if the ticket number is provided during role activation.
        Args:
            value: Value to set for the referenceKey property.
        """
        self._reference_key = value
    
    @property
    def reference_system(self,) -> Optional[str]:
        """
        Gets the referenceSystem property value. Incident/Request ticketing system provided during tole activation. The value is presented only if the ticket system is provided during role activation.
        Returns: Optional[str]
        """
        return self._reference_system
    
    @reference_system.setter
    def reference_system(self,value: Optional[str] = None) -> None:
        """
        Sets the referenceSystem property value. Incident/Request ticketing system provided during tole activation. The value is presented only if the ticket system is provided during role activation.
        Args:
            value: Value to set for the referenceSystem property.
        """
        self._reference_system = value
    
    @property
    def requestor_id(self,) -> Optional[str]:
        """
        Gets the requestorId property value. The user id of the requestor who initiates the operation.
        Returns: Optional[str]
        """
        return self._requestor_id
    
    @requestor_id.setter
    def requestor_id(self,value: Optional[str] = None) -> None:
        """
        Sets the requestorId property value. The user id of the requestor who initiates the operation.
        Args:
            value: Value to set for the requestorId property.
        """
        self._requestor_id = value
    
    @property
    def requestor_name(self,) -> Optional[str]:
        """
        Gets the requestorName property value. The user name of the requestor who initiates the operation.
        Returns: Optional[str]
        """
        return self._requestor_name
    
    @requestor_name.setter
    def requestor_name(self,value: Optional[str] = None) -> None:
        """
        Sets the requestorName property value. The user name of the requestor who initiates the operation.
        Args:
            value: Value to set for the requestorName property.
        """
        self._requestor_name = value
    
    @property
    def request_type(self,) -> Optional[str]:
        """
        Gets the requestType property value. The request operation type. The requestType value can be: Assign (role assignment), Activate (role activation), Unassign (remove role assignment), Deactivate (role deactivation), ScanAlertsNow (scan security alerts), DismissAlert (dismiss security alert), FixAlertItem (fix a security alert issue),  AccessReview_Review (review an Access Review), AccessReview_Create (create an Access Review) , AccessReview_Update (update an Access Review), AccessReview_Delete (delete an Access Review).
        Returns: Optional[str]
        """
        return self._request_type
    
    @request_type.setter
    def request_type(self,value: Optional[str] = None) -> None:
        """
        Sets the requestType property value. The request operation type. The requestType value can be: Assign (role assignment), Activate (role activation), Unassign (remove role assignment), Deactivate (role deactivation), ScanAlertsNow (scan security alerts), DismissAlert (dismiss security alert), FixAlertItem (fix a security alert issue),  AccessReview_Review (review an Access Review), AccessReview_Create (create an Access Review) , AccessReview_Update (update an Access Review), AccessReview_Delete (delete an Access Review).
        Args:
            value: Value to set for the requestType property.
        """
        self._request_type = value
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. The id of the role that is associated with the operation.
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. The id of the role that is associated with the operation.
        Args:
            value: Value to set for the roleId property.
        """
        self._role_id = value
    
    @property
    def role_name(self,) -> Optional[str]:
        """
        Gets the roleName property value. The name of the role.
        Returns: Optional[str]
        """
        return self._role_name
    
    @role_name.setter
    def role_name(self,value: Optional[str] = None) -> None:
        """
        Sets the roleName property value. The name of the role.
        Args:
            value: Value to set for the roleName property.
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
        Gets the tenantId property value. The tenant (organization) id.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenant (organization) id.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The id of the user that is associated with the operation.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The id of the user that is associated with the operation.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_mail(self,) -> Optional[str]:
        """
        Gets the userMail property value. The user's email.
        Returns: Optional[str]
        """
        return self._user_mail
    
    @user_mail.setter
    def user_mail(self,value: Optional[str] = None) -> None:
        """
        Sets the userMail property value. The user's email.
        Args:
            value: Value to set for the userMail property.
        """
        self._user_mail = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The user's display name.
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The user's display name.
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    

