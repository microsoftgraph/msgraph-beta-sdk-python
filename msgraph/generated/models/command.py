from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
payload_request = lazy_import('msgraph.generated.models.payload_request')
payload_response = lazy_import('msgraph.generated.models.payload_response')

class Command(entity.Entity):
    """
    Casts the previous resource to device.
    """
    @property
    def app_service_name(self,) -> Optional[str]:
        """
        Gets the appServiceName property value. The appServiceName property
        Returns: Optional[str]
        """
        return self._app_service_name
    
    @app_service_name.setter
    def app_service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appServiceName property value. The appServiceName property
        Args:
            value: Value to set for the appServiceName property.
        """
        self._app_service_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new command and sets the default values.
        """
        super().__init__()
        # The appServiceName property
        self._app_service_name: Optional[str] = None
        # The error property
        self._error: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The packageFamilyName property
        self._package_family_name: Optional[str] = None
        # The payload property
        self._payload: Optional[payload_request.PayloadRequest] = None
        # The permissionTicket property
        self._permission_ticket: Optional[str] = None
        # The postBackUri property
        self._post_back_uri: Optional[str] = None
        # The responsepayload property
        self._responsepayload: Optional[payload_response.PayloadResponse] = None
        # The status property
        self._status: Optional[str] = None
        # The type property
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Command:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Command
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Command()
    
    @property
    def error(self,) -> Optional[str]:
        """
        Gets the error property value. The error property
        Returns: Optional[str]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[str] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_service_name": lambda n : setattr(self, 'app_service_name', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "package_family_name": lambda n : setattr(self, 'package_family_name', n.get_str_value()),
            "payload": lambda n : setattr(self, 'payload', n.get_object_value(payload_request.PayloadRequest)),
            "permission_ticket": lambda n : setattr(self, 'permission_ticket', n.get_str_value()),
            "post_back_uri": lambda n : setattr(self, 'post_back_uri', n.get_str_value()),
            "responsepayload": lambda n : setattr(self, 'responsepayload', n.get_object_value(payload_response.PayloadResponse)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def package_family_name(self,) -> Optional[str]:
        """
        Gets the packageFamilyName property value. The packageFamilyName property
        Returns: Optional[str]
        """
        return self._package_family_name
    
    @package_family_name.setter
    def package_family_name(self,value: Optional[str] = None) -> None:
        """
        Sets the packageFamilyName property value. The packageFamilyName property
        Args:
            value: Value to set for the packageFamilyName property.
        """
        self._package_family_name = value
    
    @property
    def payload(self,) -> Optional[payload_request.PayloadRequest]:
        """
        Gets the payload property value. The payload property
        Returns: Optional[payload_request.PayloadRequest]
        """
        return self._payload
    
    @payload.setter
    def payload(self,value: Optional[payload_request.PayloadRequest] = None) -> None:
        """
        Sets the payload property value. The payload property
        Args:
            value: Value to set for the payload property.
        """
        self._payload = value
    
    @property
    def permission_ticket(self,) -> Optional[str]:
        """
        Gets the permissionTicket property value. The permissionTicket property
        Returns: Optional[str]
        """
        return self._permission_ticket
    
    @permission_ticket.setter
    def permission_ticket(self,value: Optional[str] = None) -> None:
        """
        Sets the permissionTicket property value. The permissionTicket property
        Args:
            value: Value to set for the permissionTicket property.
        """
        self._permission_ticket = value
    
    @property
    def post_back_uri(self,) -> Optional[str]:
        """
        Gets the postBackUri property value. The postBackUri property
        Returns: Optional[str]
        """
        return self._post_back_uri
    
    @post_back_uri.setter
    def post_back_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the postBackUri property value. The postBackUri property
        Args:
            value: Value to set for the postBackUri property.
        """
        self._post_back_uri = value
    
    @property
    def responsepayload(self,) -> Optional[payload_response.PayloadResponse]:
        """
        Gets the responsepayload property value. The responsepayload property
        Returns: Optional[payload_response.PayloadResponse]
        """
        return self._responsepayload
    
    @responsepayload.setter
    def responsepayload(self,value: Optional[payload_response.PayloadResponse] = None) -> None:
        """
        Sets the responsepayload property value. The responsepayload property
        Args:
            value: Value to set for the responsepayload property.
        """
        self._responsepayload = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appServiceName", self.app_service_name)
        writer.write_str_value("error", self.error)
        writer.write_str_value("packageFamilyName", self.package_family_name)
        writer.write_object_value("payload", self.payload)
        writer.write_str_value("permissionTicket", self.permission_ticket)
        writer.write_str_value("postBackUri", self.post_back_uri)
        writer.write_object_value("responsepayload", self.responsepayload)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

