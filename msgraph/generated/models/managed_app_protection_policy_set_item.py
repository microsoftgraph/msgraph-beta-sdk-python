from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_set_item = lazy_import('msgraph.generated.models.policy_set_item')

class ManagedAppProtectionPolicySetItem(policy_set_item.PolicySetItem):
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedAppProtectionPolicySetItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedAppProtectionPolicySetItem"
        # TargetedAppManagementLevels of the ManagedAppPolicySetItem.
        self._targeted_app_management_levels: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppProtectionPolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppProtectionPolicySetItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppProtectionPolicySetItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "targeted_app_management_levels": lambda n : setattr(self, 'targeted_app_management_levels', n.get_str_value()),
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
        writer.write_str_value("targetedAppManagementLevels", self.targeted_app_management_levels)
    
    @property
    def targeted_app_management_levels(self,) -> Optional[str]:
        """
        Gets the targetedAppManagementLevels property value. TargetedAppManagementLevels of the ManagedAppPolicySetItem.
        Returns: Optional[str]
        """
        return self._targeted_app_management_levels
    
    @targeted_app_management_levels.setter
    def targeted_app_management_levels(self,value: Optional[str] = None) -> None:
        """
        Sets the targetedAppManagementLevels property value. TargetedAppManagementLevels of the ManagedAppPolicySetItem.
        Args:
            value: Value to set for the targetedAppManagementLevels property.
        """
        self._targeted_app_management_levels = value
    

