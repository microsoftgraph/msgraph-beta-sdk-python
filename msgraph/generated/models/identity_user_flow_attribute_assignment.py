from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_user_flow_attribute, identity_user_flow_attribute_input_type, user_attribute_values_item

from . import entity

@dataclass
class IdentityUserFlowAttributeAssignment(entity.Entity):
    # The display name of the identityUserFlowAttribute within a user flow.
    display_name: Optional[str] = None
    # Determines whether the identityUserFlowAttribute is optional. true means the user doesn't have to provide a value. false means the user cannot complete sign-up without providing a value.
    is_optional: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Determines whether the identityUserFlowAttribute requires verification. This is only used for verifying the user's phone number or email address.
    requires_verification: Optional[bool] = None
    # The user attribute that you want to add to your user flow.
    user_attribute: Optional[identity_user_flow_attribute.IdentityUserFlowAttribute] = None
    # The input options for the user flow attribute. Only applicable when the userInputType is radioSingleSelect, dropdownSingleSelect, or checkboxMultiSelect.
    user_attribute_values: Optional[List[user_attribute_values_item.UserAttributeValuesItem]] = None
    # The userInputType property
    user_input_type: Optional[identity_user_flow_attribute_input_type.IdentityUserFlowAttributeInputType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityUserFlowAttributeAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlowAttributeAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IdentityUserFlowAttributeAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_user_flow_attribute, identity_user_flow_attribute_input_type, user_attribute_values_item

        from . import entity, identity_user_flow_attribute, identity_user_flow_attribute_input_type, user_attribute_values_item

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isOptional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "requiresVerification": lambda n : setattr(self, 'requires_verification', n.get_bool_value()),
            "userAttribute": lambda n : setattr(self, 'user_attribute', n.get_object_value(identity_user_flow_attribute.IdentityUserFlowAttribute)),
            "userAttributeValues": lambda n : setattr(self, 'user_attribute_values', n.get_collection_of_object_values(user_attribute_values_item.UserAttributeValuesItem)),
            "userInputType": lambda n : setattr(self, 'user_input_type', n.get_enum_value(identity_user_flow_attribute_input_type.IdentityUserFlowAttributeInputType)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_bool_value("requiresVerification", self.requires_verification)
        writer.write_object_value("userAttribute", self.user_attribute)
        writer.write_collection_of_object_values("userAttributeValues", self.user_attribute_values)
        writer.write_enum_value("userInputType", self.user_input_type)
    

