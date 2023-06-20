from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import external_connection
    from ..industry_data import industry_data_root

@dataclass
class External(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The connections property
    connections: Optional[List[external_connection.ExternalConnection]] = None
    # The industryData property
    industry_data: Optional[industry_data_root.IndustryDataRoot] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> External:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: External
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return External()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import external_connection
        from ..industry_data import industry_data_root

        from . import external_connection
        from ..industry_data import industry_data_root

        fields: Dict[str, Callable[[Any], None]] = {
            "connections": lambda n : setattr(self, 'connections', n.get_collection_of_object_values(external_connection.ExternalConnection)),
            "industryData": lambda n : setattr(self, 'industry_data', n.get_object_value(industry_data_root.IndustryDataRoot)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("connections", self.connections)
        writer.write_object_value("industryData", self.industry_data)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

