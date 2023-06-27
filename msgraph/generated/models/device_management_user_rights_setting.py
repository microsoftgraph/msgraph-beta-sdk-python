from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_user_rights_local_user_or_group import DeviceManagementUserRightsLocalUserOrGroup
    from .state_management_setting import StateManagementSetting

@dataclass
class DeviceManagementUserRightsSetting(AdditionalDataHolder, Parsable):
    """
    Represents a user rights setting.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Representing a collection of local users or groups which will be set on device if the state of this setting is Allowed. This collection can contain a maximum of 500 elements.
    local_users_or_groups: Optional[List[DeviceManagementUserRightsLocalUserOrGroup]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # State Management Setting.
    state: Optional[StateManagementSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementUserRightsSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementUserRightsSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementUserRightsSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_user_rights_local_user_or_group import DeviceManagementUserRightsLocalUserOrGroup
        from .state_management_setting import StateManagementSetting

        from .device_management_user_rights_local_user_or_group import DeviceManagementUserRightsLocalUserOrGroup
        from .state_management_setting import StateManagementSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "localUsersOrGroups": lambda n : setattr(self, 'local_users_or_groups', n.get_collection_of_object_values(DeviceManagementUserRightsLocalUserOrGroup)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(StateManagementSetting)),
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
        writer.write_collection_of_object_values("localUsersOrGroups", self.local_users_or_groups)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

