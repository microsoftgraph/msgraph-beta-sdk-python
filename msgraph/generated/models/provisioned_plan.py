from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ProvisionedPlan(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # For example, 'Enabled'.
    capability_status: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # For example, 'Success'.
    provisioning_status: Optional[str] = None
    # The name of the service; for example, 'AccessControlS2S'
    service: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisionedPlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisionedPlan
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProvisionedPlan()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "capabilityStatus": lambda n : setattr(self, 'capability_status', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioningStatus": lambda n : setattr(self, 'provisioning_status', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("capabilityStatus", self.capability_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("provisioningStatus", self.provisioning_status)
        writer.write_str_value("service", self.service)
        writer.write_additional_data_value(self.additional_data)
    

