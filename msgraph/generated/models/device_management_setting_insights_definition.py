from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_setting_value

class DeviceManagementSettingInsightsDefinition(AdditionalDataHolder, Parsable):
    """
    Setting Insights
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettingInsightsDefinition and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Setting definition id that is being referred to a setting.
        self._setting_definition_id: Optional[str] = None
        # Data Insights Target Value
        self._setting_insight: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingInsightsDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingInsightsDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingInsightsDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_setting_value

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingDefinitionId": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "settingInsight": lambda n : setattr(self, 'setting_insight', n.get_object_value(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue)),
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
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_object_value("settingInsight", self.setting_insight)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_definition_id(self,) -> Optional[str]:
        """
        Gets the settingDefinitionId property value. Setting definition id that is being referred to a setting.
        Returns: Optional[str]
        """
        return self._setting_definition_id
    
    @setting_definition_id.setter
    def setting_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDefinitionId property value. Setting definition id that is being referred to a setting.
        Args:
            value: Value to set for the setting_definition_id property.
        """
        self._setting_definition_id = value
    
    @property
    def setting_insight(self,) -> Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue]:
        """
        Gets the settingInsight property value. Data Insights Target Value
        Returns: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue]
        """
        return self._setting_insight
    
    @setting_insight.setter
    def setting_insight(self,value: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue] = None) -> None:
        """
        Sets the settingInsight property value. Data Insights Target Value
        Args:
            value: Value to set for the setting_insight property.
        """
        self._setting_insight = value
    

