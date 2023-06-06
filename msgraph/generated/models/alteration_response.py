from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import search_alteration, search_alteration_type

@dataclass
class AlterationResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Defines the original user query string.
    original_query_string: Optional[str] = None
    # Defines the details of alteration information for the spelling correction.
    query_alteration: Optional[search_alteration.SearchAlteration] = None
    # Defines the type of the spelling correction. Possible values are suggestion, modification.
    query_alteration_type: Optional[search_alteration_type.SearchAlterationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlterationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlterationResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlterationResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import search_alteration, search_alteration_type

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "originalQueryString": lambda n : setattr(self, 'original_query_string', n.get_str_value()),
            "queryAlteration": lambda n : setattr(self, 'query_alteration', n.get_object_value(search_alteration.SearchAlteration)),
            "queryAlterationType": lambda n : setattr(self, 'query_alteration_type', n.get_enum_value(search_alteration_type.SearchAlterationType)),
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
        writer.write_str_value("originalQueryString", self.original_query_string)
        writer.write_object_value("queryAlteration", self.query_alteration)
        writer.write_enum_value("queryAlterationType", self.query_alteration_type)
        writer.write_additional_data_value(self.additional_data)
    

