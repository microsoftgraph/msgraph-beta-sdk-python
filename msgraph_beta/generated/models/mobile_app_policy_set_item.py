from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .install_intent import InstallIntent
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings
    from .policy_set_item import PolicySetItem

from .policy_set_item import PolicySetItem

@dataclass
class MobileAppPolicySetItem(PolicySetItem, Parsable):
    """
    A class containing the properties used for mobile app PolicySetItem.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mobileAppPolicySetItem"
    # Possible values for the install intent chosen by the admin.
    intent: Optional[InstallIntent] = None
    # Settings of the MobileAppPolicySetItem.
    settings: Optional[MobileAppAssignmentSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppPolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppPolicySetItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppPolicySetItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .install_intent import InstallIntent
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .policy_set_item import PolicySetItem

        from .install_intent import InstallIntent
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .policy_set_item import PolicySetItem

        fields: Dict[str, Callable[[Any], None]] = {
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(InstallIntent)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(MobileAppAssignmentSettings)),
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
        from .install_intent import InstallIntent
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .policy_set_item import PolicySetItem

        writer.write_enum_value("intent", self.intent)
        writer.write_object_value("settings", self.settings)
    

