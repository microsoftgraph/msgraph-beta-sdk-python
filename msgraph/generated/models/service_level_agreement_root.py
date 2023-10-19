from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_a_d_authentication import AzureADAuthentication
    from .entity import Entity

from .entity import Entity

@dataclass
class ServiceLevelAgreementRoot(Entity):
    # Collects the Microsoft Entra SLA attainment for each month for a Microsoft Entra tenant.
    azure_a_d_authentication: Optional[AzureADAuthentication] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceLevelAgreementRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceLevelAgreementRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServiceLevelAgreementRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .azure_a_d_authentication import AzureADAuthentication
        from .entity import Entity

        from .azure_a_d_authentication import AzureADAuthentication
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "azureADAuthentication": lambda n : setattr(self, 'azure_a_d_authentication', n.get_object_value(AzureADAuthentication)),
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
        writer.write_object_value("azureADAuthentication", self.azure_a_d_authentication)
    

