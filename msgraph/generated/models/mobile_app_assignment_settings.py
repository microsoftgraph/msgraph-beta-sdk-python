from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_managed_store_app_assignment_settings, ios_lob_app_assignment_settings, ios_store_app_assignment_settings, ios_vpp_app_assignment_settings, mac_os_lob_app_assignment_settings, mac_os_vpp_app_assignment_settings, microsoft_store_for_business_app_assignment_settings, win32_lob_app_assignment_settings, windows_app_x_app_assignment_settings, windows_universal_app_x_app_assignment_settings, win_get_app_assignment_settings

class MobileAppAssignmentSettings(AdditionalDataHolder, Parsable):
    """
    Abstract class to contain properties used to assign a mobile app to a group.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppAssignmentSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidManagedStoreAppAssignmentSettings":
                from . import android_managed_store_app_assignment_settings

                return android_managed_store_app_assignment_settings.AndroidManagedStoreAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.iosLobAppAssignmentSettings":
                from . import ios_lob_app_assignment_settings

                return ios_lob_app_assignment_settings.IosLobAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.iosStoreAppAssignmentSettings":
                from . import ios_store_app_assignment_settings

                return ios_store_app_assignment_settings.IosStoreAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.iosVppAppAssignmentSettings":
                from . import ios_vpp_app_assignment_settings

                return ios_vpp_app_assignment_settings.IosVppAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.macOsLobAppAssignmentSettings":
                from . import mac_os_lob_app_assignment_settings

                return mac_os_lob_app_assignment_settings.MacOsLobAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.macOsVppAppAssignmentSettings":
                from . import mac_os_vpp_app_assignment_settings

                return mac_os_vpp_app_assignment_settings.MacOsVppAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.microsoftStoreForBusinessAppAssignmentSettings":
                from . import microsoft_store_for_business_app_assignment_settings

                return microsoft_store_for_business_app_assignment_settings.MicrosoftStoreForBusinessAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.win32LobAppAssignmentSettings":
                from . import win32_lob_app_assignment_settings

                return win32_lob_app_assignment_settings.Win32LobAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.windowsAppXAppAssignmentSettings":
                from . import windows_app_x_app_assignment_settings

                return windows_app_x_app_assignment_settings.WindowsAppXAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.windowsUniversalAppXAppAssignmentSettings":
                from . import windows_universal_app_x_app_assignment_settings

                return windows_universal_app_x_app_assignment_settings.WindowsUniversalAppXAppAssignmentSettings()
            if mapping_value == "#microsoft.graph.winGetAppAssignmentSettings":
                from . import win_get_app_assignment_settings

                return win_get_app_assignment_settings.WinGetAppAssignmentSettings()
        return MobileAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_managed_store_app_assignment_settings, ios_lob_app_assignment_settings, ios_store_app_assignment_settings, ios_vpp_app_assignment_settings, mac_os_lob_app_assignment_settings, mac_os_vpp_app_assignment_settings, microsoft_store_for_business_app_assignment_settings, win32_lob_app_assignment_settings, windows_app_x_app_assignment_settings, windows_universal_app_x_app_assignment_settings, win_get_app_assignment_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

