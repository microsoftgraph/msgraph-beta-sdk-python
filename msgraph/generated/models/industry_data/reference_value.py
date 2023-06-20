from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identifier_type_reference_value, reference_definition, role_reference_value, user_match_target_reference_value, year_reference_value

@dataclass
class ReferenceValue(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The code of the desired referenceDefinition entry.
    code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The value property
    value: Optional[reference_definition.ReferenceDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReferenceValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReferenceValue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.identifierTypeReferenceValue".casefold():
            from . import identifier_type_reference_value

            return identifier_type_reference_value.IdentifierTypeReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.roleReferenceValue".casefold():
            from . import role_reference_value

            return role_reference_value.RoleReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.userMatchTargetReferenceValue".casefold():
            from . import user_match_target_reference_value

            return user_match_target_reference_value.UserMatchTargetReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.yearReferenceValue".casefold():
            from . import year_reference_value

            return year_reference_value.YearReferenceValue()
        return ReferenceValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identifier_type_reference_value, reference_definition, role_reference_value, user_match_target_reference_value, year_reference_value

        from . import identifier_type_reference_value, reference_definition, role_reference_value, user_match_target_reference_value, year_reference_value

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(reference_definition.ReferenceDefinition)),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

