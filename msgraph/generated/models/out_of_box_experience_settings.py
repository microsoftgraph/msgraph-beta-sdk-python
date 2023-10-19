from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_device_usage_type import WindowsDeviceUsageType
    from .windows_user_type import WindowsUserType

@dataclass
class OutOfBoxExperienceSettings(AdditionalDataHolder, BackedModel, Parsable):
    """
    Out of box experience setting
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The deviceUsageType property
    device_usage_type: Optional[WindowsDeviceUsageType] = None
    # Show or hide EULA to user
    hide_e_u_l_a: Optional[bool] = None
    # If set to true, then the user can't start over with different account, on company sign-in
    hide_escape_link: Optional[bool] = None
    # Show or hide privacy settings to user
    hide_privacy_settings: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If set, then skip the keyboard selection page if Language and Region are set
    skip_keyboard_selection_page: Optional[bool] = None
    # The userType property
    user_type: Optional[WindowsUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutOfBoxExperienceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutOfBoxExperienceSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OutOfBoxExperienceSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_device_usage_type import WindowsDeviceUsageType
        from .windows_user_type import WindowsUserType

        from .windows_device_usage_type import WindowsDeviceUsageType
        from .windows_user_type import WindowsUserType

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceUsageType": lambda n : setattr(self, 'device_usage_type', n.get_enum_value(WindowsDeviceUsageType)),
            "hideEULA": lambda n : setattr(self, 'hide_e_u_l_a', n.get_bool_value()),
            "hideEscapeLink": lambda n : setattr(self, 'hide_escape_link', n.get_bool_value()),
            "hidePrivacySettings": lambda n : setattr(self, 'hide_privacy_settings', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skipKeyboardSelectionPage": lambda n : setattr(self, 'skip_keyboard_selection_page', n.get_bool_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(WindowsUserType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("deviceUsageType", self.device_usage_type)
        writer.write_bool_value("hideEULA", self.hide_e_u_l_a)
        writer.write_bool_value("hideEscapeLink", self.hide_escape_link)
        writer.write_bool_value("hidePrivacySettings", self.hide_privacy_settings)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_bool_value("skipKeyboardSelectionPage", self.skip_keyboard_selection_page)
        writer.write_enum_value("userType", self.user_type)
        writer.write_additional_data_value(self.additional_data)
    

