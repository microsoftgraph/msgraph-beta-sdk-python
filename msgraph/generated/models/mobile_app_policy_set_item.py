from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

install_intent = lazy_import('msgraph.generated.models.install_intent')
mobile_app_assignment_settings = lazy_import('msgraph.generated.models.mobile_app_assignment_settings')
policy_set_item = lazy_import('msgraph.generated.models.policy_set_item')

class MobileAppPolicySetItem(policy_set_item.PolicySetItem):
    def __init__(self,) -> None:
        """
        Instantiates a new MobileAppPolicySetItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.mobileAppPolicySetItem"
        # Possible values for the install intent chosen by the admin.
        self._intent: Optional[install_intent.InstallIntent] = None
        # Settings of the MobileAppPolicySetItem.
        self._settings: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings] = None
    
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
        fields = {
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(install_intent.InstallIntent)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(mobile_app_assignment_settings.MobileAppAssignmentSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def intent(self,) -> Optional[install_intent.InstallIntent]:
        """
        Gets the intent property value. Possible values for the install intent chosen by the admin.
        Returns: Optional[install_intent.InstallIntent]
        """
        return self._intent
    
    @intent.setter
    def intent(self,value: Optional[install_intent.InstallIntent] = None) -> None:
        """
        Sets the intent property value. Possible values for the install intent chosen by the admin.
        Args:
            value: Value to set for the intent property.
        """
        self._intent = value
    
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
    
    @property
    def settings(self,) -> Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings]:
        """
        Gets the settings property value. Settings of the MobileAppPolicySetItem.
        Returns: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings] = None) -> None:
        """
        Sets the settings property value. Settings of the MobileAppPolicySetItem.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

