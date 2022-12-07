from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_configured_peripheral = lazy_import('msgraph.generated.models.teamwork_configured_peripheral')
teamwork_display_screen_configuration = lazy_import('msgraph.generated.models.teamwork_display_screen_configuration')

class TeamworkDisplayConfiguration(AdditionalDataHolder, Parsable):
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
    
    @property
    def configured_displays(self,) -> Optional[List[teamwork_configured_peripheral.TeamworkConfiguredPeripheral]]:
        """
        Gets the configuredDisplays property value. The list of configured displays. Applicable only for Microsoft Teams Rooms devices.
        Returns: Optional[List[teamwork_configured_peripheral.TeamworkConfiguredPeripheral]]
        """
        return self._configured_displays
    
    @configured_displays.setter
    def configured_displays(self,value: Optional[List[teamwork_configured_peripheral.TeamworkConfiguredPeripheral]] = None) -> None:
        """
        Sets the configuredDisplays property value. The list of configured displays. Applicable only for Microsoft Teams Rooms devices.
        Args:
            value: Value to set for the configuredDisplays property.
        """
        self._configured_displays = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDisplayConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The list of configured displays. Applicable only for Microsoft Teams Rooms devices.
        self._configured_displays: Optional[List[teamwork_configured_peripheral.TeamworkConfiguredPeripheral]] = None
        # Total number of connected displays, including the inbuilt display. Applicable only for Teams Rooms devices.
        self._display_count: Optional[int] = None
        # Configuration for the inbuilt display. Not applicable for Teams Rooms devices.
        self._in_built_display_screen_configuration: Optional[teamwork_display_screen_configuration.TeamworkDisplayScreenConfiguration] = None
        # True if content duplication is allowed. Applicable only for Teams Rooms devices.
        self._is_content_duplication_allowed: Optional[bool] = None
        # True if dual display mode is enabled. If isDualDisplayModeEnabled is true, then the content will be displayed on both front of room screens instead of just the one screen, when it is shared via the HDMI ingest module on the Microsoft Teams Rooms device. Applicable only for Teams Rooms devices.
        self._is_dual_display_mode_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDisplayConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDisplayConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDisplayConfiguration()
    
    @property
    def display_count(self,) -> Optional[int]:
        """
        Gets the displayCount property value. Total number of connected displays, including the inbuilt display. Applicable only for Teams Rooms devices.
        Returns: Optional[int]
        """
        return self._display_count
    
    @display_count.setter
    def display_count(self,value: Optional[int] = None) -> None:
        """
        Sets the displayCount property value. Total number of connected displays, including the inbuilt display. Applicable only for Teams Rooms devices.
        Args:
            value: Value to set for the displayCount property.
        """
        self._display_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configured_displays": lambda n : setattr(self, 'configured_displays', n.get_collection_of_object_values(teamwork_configured_peripheral.TeamworkConfiguredPeripheral)),
            "display_count": lambda n : setattr(self, 'display_count', n.get_int_value()),
            "in_built_display_screen_configuration": lambda n : setattr(self, 'in_built_display_screen_configuration', n.get_object_value(teamwork_display_screen_configuration.TeamworkDisplayScreenConfiguration)),
            "is_content_duplication_allowed": lambda n : setattr(self, 'is_content_duplication_allowed', n.get_bool_value()),
            "is_dual_display_mode_enabled": lambda n : setattr(self, 'is_dual_display_mode_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def in_built_display_screen_configuration(self,) -> Optional[teamwork_display_screen_configuration.TeamworkDisplayScreenConfiguration]:
        """
        Gets the inBuiltDisplayScreenConfiguration property value. Configuration for the inbuilt display. Not applicable for Teams Rooms devices.
        Returns: Optional[teamwork_display_screen_configuration.TeamworkDisplayScreenConfiguration]
        """
        return self._in_built_display_screen_configuration
    
    @in_built_display_screen_configuration.setter
    def in_built_display_screen_configuration(self,value: Optional[teamwork_display_screen_configuration.TeamworkDisplayScreenConfiguration] = None) -> None:
        """
        Sets the inBuiltDisplayScreenConfiguration property value. Configuration for the inbuilt display. Not applicable for Teams Rooms devices.
        Args:
            value: Value to set for the inBuiltDisplayScreenConfiguration property.
        """
        self._in_built_display_screen_configuration = value
    
    @property
    def is_content_duplication_allowed(self,) -> Optional[bool]:
        """
        Gets the isContentDuplicationAllowed property value. True if content duplication is allowed. Applicable only for Teams Rooms devices.
        Returns: Optional[bool]
        """
        return self._is_content_duplication_allowed
    
    @is_content_duplication_allowed.setter
    def is_content_duplication_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isContentDuplicationAllowed property value. True if content duplication is allowed. Applicable only for Teams Rooms devices.
        Args:
            value: Value to set for the isContentDuplicationAllowed property.
        """
        self._is_content_duplication_allowed = value
    
    @property
    def is_dual_display_mode_enabled(self,) -> Optional[bool]:
        """
        Gets the isDualDisplayModeEnabled property value. True if dual display mode is enabled. If isDualDisplayModeEnabled is true, then the content will be displayed on both front of room screens instead of just the one screen, when it is shared via the HDMI ingest module on the Microsoft Teams Rooms device. Applicable only for Teams Rooms devices.
        Returns: Optional[bool]
        """
        return self._is_dual_display_mode_enabled
    
    @is_dual_display_mode_enabled.setter
    def is_dual_display_mode_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDualDisplayModeEnabled property value. True if dual display mode is enabled. If isDualDisplayModeEnabled is true, then the content will be displayed on both front of room screens instead of just the one screen, when it is shared via the HDMI ingest module on the Microsoft Teams Rooms device. Applicable only for Teams Rooms devices.
        Args:
            value: Value to set for the isDualDisplayModeEnabled property.
        """
        self._is_dual_display_mode_enabled = value
    
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
            value: Value to set for the OdataType property.
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
        writer.write_collection_of_object_values("configuredDisplays", self.configured_displays)
        writer.write_int_value("displayCount", self.display_count)
        writer.write_object_value("inBuiltDisplayScreenConfiguration", self.in_built_display_screen_configuration)
        writer.write_bool_value("isContentDuplicationAllowed", self.is_content_duplication_allowed)
        writer.write_bool_value("isDualDisplayModeEnabled", self.is_dual_display_mode_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

