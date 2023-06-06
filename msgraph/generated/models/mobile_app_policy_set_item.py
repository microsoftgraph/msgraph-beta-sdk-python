from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import install_intent, mobile_app_assignment_settings, policy_set_item

from . import policy_set_item

@dataclass
class MobileAppPolicySetItem(policy_set_item.PolicySetItem):
    odata_type = "#microsoft.graph.mobileAppPolicySetItem"
    # Possible values for the install intent chosen by the admin.
    intent: Optional[install_intent.InstallIntent] = None
    # Settings of the MobileAppPolicySetItem.
    settings: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppPolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppPolicySetItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppPolicySetItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import install_intent, mobile_app_assignment_settings, policy_set_item

        fields: Dict[str, Callable[[Any], None]] = {
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(install_intent.InstallIntent)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(mobile_app_assignment_settings.MobileAppAssignmentSettings)),
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
        writer.write_enum_value("intent", self.intent)
        writer.write_object_value("settings", self.settings)
    

