from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_authorization_system_resource import AzureAuthorizationSystemResource
    from .azure_identity import AzureIdentity

from .azure_identity import AzureIdentity

@dataclass
class AzureServerlessFunction(AzureIdentity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.azureServerlessFunction"
    # The resource property
    resource: Optional[AzureAuthorizationSystemResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureServerlessFunction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureServerlessFunction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AzureServerlessFunction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .azure_identity import AzureIdentity

        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .azure_identity import AzureIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(AzureAuthorizationSystemResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("resource", self.resource)
    

