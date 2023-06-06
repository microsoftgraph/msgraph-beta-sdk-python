from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_built_in_user_flow_attribute, identity_custom_user_flow_attribute, identity_user_flow_attribute_data_type, identity_user_flow_attribute_type

from . import entity

@dataclass
class IdentityUserFlowAttribute(entity.Entity):
    # The dataType property
    data_type: Optional[identity_user_flow_attribute_data_type.IdentityUserFlowAttributeDataType] = None
    # The description of the user flow attribute that's shown to the user at the time of sign-up.
    description: Optional[str] = None
    # The display name of the user flow attribute.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The userFlowAttributeType property
    user_flow_attribute_type: Optional[identity_user_flow_attribute_type.IdentityUserFlowAttributeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityUserFlowAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlowAttribute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.identityBuiltInUserFlowAttribute":
                from . import identity_built_in_user_flow_attribute

                return identity_built_in_user_flow_attribute.IdentityBuiltInUserFlowAttribute()
            if mapping_value == "#microsoft.graph.identityCustomUserFlowAttribute":
                from . import identity_custom_user_flow_attribute

                return identity_custom_user_flow_attribute.IdentityCustomUserFlowAttribute()
        return IdentityUserFlowAttribute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_built_in_user_flow_attribute, identity_custom_user_flow_attribute, identity_user_flow_attribute_data_type, identity_user_flow_attribute_type

        fields: Dict[str, Callable[[Any], None]] = {
            "dataType": lambda n : setattr(self, 'data_type', n.get_enum_value(identity_user_flow_attribute_data_type.IdentityUserFlowAttributeDataType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "userFlowAttributeType": lambda n : setattr(self, 'user_flow_attribute_type', n.get_enum_value(identity_user_flow_attribute_type.IdentityUserFlowAttributeType)),
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
        writer.write_enum_value("dataType", self.data_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("userFlowAttributeType", self.user_flow_attribute_type)
    

