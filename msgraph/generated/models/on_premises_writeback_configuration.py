from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class OnPremisesWritebackConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The distinguished name of the on-premises container that the customer is using to store unified groups which are created in the cloud.
    unified_group_container: Optional[str] = None
    # The distinguished name of the on-premises container that the customer is using to store users which are created in the cloud.
    user_container: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesWritebackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesWritebackConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesWritebackConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unifiedGroupContainer": lambda n : setattr(self, 'unified_group_container', n.get_str_value()),
            "userContainer": lambda n : setattr(self, 'user_container', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("unifiedGroupContainer", self.unified_group_container)
        writer.write_str_value("userContainer", self.user_container)
        writer.write_additional_data_value(self.additional_data)
    

