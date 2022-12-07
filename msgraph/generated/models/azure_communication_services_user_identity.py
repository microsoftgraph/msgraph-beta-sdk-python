from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class AzureCommunicationServicesUserIdentity(identity.Identity):
    @property
    def azure_communication_services_resource_id(self,) -> Optional[str]:
        """
        Gets the azureCommunicationServicesResourceId property value. The Azure Communication Services resource ID associated with the user.
        Returns: Optional[str]
        """
        return self._azure_communication_services_resource_id
    
    @azure_communication_services_resource_id.setter
    def azure_communication_services_resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureCommunicationServicesResourceId property value. The Azure Communication Services resource ID associated with the user.
        Args:
            value: Value to set for the azureCommunicationServicesResourceId property.
        """
        self._azure_communication_services_resource_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AzureCommunicationServicesUserIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.azureCommunicationServicesUserIdentity"
        # The Azure Communication Services resource ID associated with the user.
        self._azure_communication_services_resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureCommunicationServicesUserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AzureCommunicationServicesUserIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AzureCommunicationServicesUserIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_communication_services_resource_id": lambda n : setattr(self, 'azure_communication_services_resource_id', n.get_str_value()),
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
        writer.write_str_value("azureCommunicationServicesResourceId", self.azure_communication_services_resource_id)
    

