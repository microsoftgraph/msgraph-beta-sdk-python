from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')
service_information = lazy_import('msgraph.generated.models.service_information')

class WebAccount(item_facet.ItemFacet):
    def __init__(self,) -> None:
        """
        Instantiates a new WebAccount and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.webAccount"
        # Contains the description the user has provided for the account on the service being referenced.
        self._description: Optional[str] = None
        # The service property
        self._service: Optional[service_information.ServiceInformation] = None
        # Contains a status message from the cloud service if provided or synchronized.
        self._status_message: Optional[str] = None
        # The thumbnailUrl property
        self._thumbnail_url: Optional[str] = None
        # The user name  displayed for the webaccount.
        self._user_id: Optional[str] = None
        # Contains a link to the user's profile on the cloud service if one exists.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebAccount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebAccount()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Contains the description the user has provided for the account on the service being referenced.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Contains the description the user has provided for the account on the service being referenced.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_object_value(service_information.ServiceInformation)),
            "status_message": lambda n : setattr(self, 'status_message', n.get_str_value()),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_object_value("service", self.service)
        writer.write_str_value("statusMessage", self.status_message)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def service(self,) -> Optional[service_information.ServiceInformation]:
        """
        Gets the service property value. The service property
        Returns: Optional[service_information.ServiceInformation]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[service_information.ServiceInformation] = None) -> None:
        """
        Sets the service property value. The service property
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def status_message(self,) -> Optional[str]:
        """
        Gets the statusMessage property value. Contains a status message from the cloud service if provided or synchronized.
        Returns: Optional[str]
        """
        return self._status_message
    
    @status_message.setter
    def status_message(self,value: Optional[str] = None) -> None:
        """
        Sets the statusMessage property value. Contains a status message from the cloud service if provided or synchronized.
        Args:
            value: Value to set for the statusMessage property.
        """
        self._status_message = value
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. The thumbnailUrl property
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. The thumbnailUrl property
        Args:
            value: Value to set for the thumbnailUrl property.
        """
        self._thumbnail_url = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The user name  displayed for the webaccount.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user name  displayed for the webaccount.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Contains a link to the user's profile on the cloud service if one exists.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Contains a link to the user's profile on the cloud service if one exists.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

