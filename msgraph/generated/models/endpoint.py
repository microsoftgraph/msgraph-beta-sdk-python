from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')

class Endpoint(directory_object.DirectoryObject):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def capability(self,) -> Optional[str]:
        """
        Gets the capability property value. Describes the capability that is associated with this resource. (e.g. Messages, Conversations, etc.) Not nullable. Read-only.
        Returns: Optional[str]
        """
        return self._capability
    
    @capability.setter
    def capability(self,value: Optional[str] = None) -> None:
        """
        Sets the capability property value. Describes the capability that is associated with this resource. (e.g. Messages, Conversations, etc.) Not nullable. Read-only.
        Args:
            value: Value to set for the capability property.
        """
        self._capability = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new endpoint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.endpoint"
        # Describes the capability that is associated with this resource. (e.g. Messages, Conversations, etc.) Not nullable. Read-only.
        self._capability: Optional[str] = None
        # Application id of the publishing underlying service. Not nullable. Read-only.
        self._provider_id: Optional[str] = None
        # Name of the publishing underlying service. Read-only.
        self._provider_name: Optional[str] = None
        # For Microsoft 365 groups, this is set to a well-known name for the resource (e.g. Yammer.FeedURL etc.). Not nullable. Read-only.
        self._provider_resource_id: Optional[str] = None
        # URL of the published resource. Not nullable. Read-only.
        self._uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Endpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Endpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Endpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "capability": lambda n : setattr(self, 'capability', n.get_str_value()),
            "provider_id": lambda n : setattr(self, 'provider_id', n.get_str_value()),
            "provider_name": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "provider_resource_id": lambda n : setattr(self, 'provider_resource_id', n.get_str_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def provider_id(self,) -> Optional[str]:
        """
        Gets the providerId property value. Application id of the publishing underlying service. Not nullable. Read-only.
        Returns: Optional[str]
        """
        return self._provider_id
    
    @provider_id.setter
    def provider_id(self,value: Optional[str] = None) -> None:
        """
        Sets the providerId property value. Application id of the publishing underlying service. Not nullable. Read-only.
        Args:
            value: Value to set for the providerId property.
        """
        self._provider_id = value
    
    @property
    def provider_name(self,) -> Optional[str]:
        """
        Gets the providerName property value. Name of the publishing underlying service. Read-only.
        Returns: Optional[str]
        """
        return self._provider_name
    
    @provider_name.setter
    def provider_name(self,value: Optional[str] = None) -> None:
        """
        Sets the providerName property value. Name of the publishing underlying service. Read-only.
        Args:
            value: Value to set for the providerName property.
        """
        self._provider_name = value
    
    @property
    def provider_resource_id(self,) -> Optional[str]:
        """
        Gets the providerResourceId property value. For Microsoft 365 groups, this is set to a well-known name for the resource (e.g. Yammer.FeedURL etc.). Not nullable. Read-only.
        Returns: Optional[str]
        """
        return self._provider_resource_id
    
    @provider_resource_id.setter
    def provider_resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the providerResourceId property value. For Microsoft 365 groups, this is set to a well-known name for the resource (e.g. Yammer.FeedURL etc.). Not nullable. Read-only.
        Args:
            value: Value to set for the providerResourceId property.
        """
        self._provider_resource_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("capability", self.capability)
        writer.write_str_value("providerId", self.provider_id)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_str_value("providerResourceId", self.provider_resource_id)
        writer.write_str_value("uri", self.uri)
    
    @property
    def uri(self,) -> Optional[str]:
        """
        Gets the uri property value. URL of the published resource. Not nullable. Read-only.
        Returns: Optional[str]
        """
        return self._uri
    
    @uri.setter
    def uri(self,value: Optional[str] = None) -> None:
        """
        Sets the uri property value. URL of the published resource. Not nullable. Read-only.
        Args:
            value: Value to set for the uri property.
        """
        self._uri = value
    

