from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_security_attribute_comparison_operator import CustomSecurityAttributeComparisonOperator
    from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomSecurityAttributeExemption(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The operator property
    operator: Optional[CustomSecurityAttributeComparisonOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomSecurityAttributeExemption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomSecurityAttributeExemption
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customSecurityAttributeStringValueExemption".casefold():
            from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption

            return CustomSecurityAttributeStringValueExemption()
        return CustomSecurityAttributeExemption()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_security_attribute_comparison_operator import CustomSecurityAttributeComparisonOperator
        from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption
        from .entity import Entity

        from .custom_security_attribute_comparison_operator import CustomSecurityAttributeComparisonOperator
        from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(CustomSecurityAttributeComparisonOperator)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .custom_security_attribute_comparison_operator import CustomSecurityAttributeComparisonOperator
        from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption
        from .entity import Entity

        writer.write_enum_value("operator", self.operator)
    

