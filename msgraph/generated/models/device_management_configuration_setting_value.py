from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_value_template_reference = lazy_import('msgraph.generated.models.device_management_configuration_setting_value_template_reference')

class DeviceManagementConfigurationSettingValue(AdditionalDataHolder, Parsable):
    """
    Setting value
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationSettingValue and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Setting value template reference
        self._setting_value_template_reference: Optional[device_management_configuration_setting_value_template_reference.DeviceManagementConfigurationSettingValueTemplateReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "setting_value_template_reference": lambda n : setattr(self, 'setting_value_template_reference', n.get_object_value(device_management_configuration_setting_value_template_reference.DeviceManagementConfigurationSettingValueTemplateReference)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("settingValueTemplateReference", self.setting_value_template_reference)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_value_template_reference(self,) -> Optional[device_management_configuration_setting_value_template_reference.DeviceManagementConfigurationSettingValueTemplateReference]:
        """
        Gets the settingValueTemplateReference property value. Setting value template reference
        Returns: Optional[device_management_configuration_setting_value_template_reference.DeviceManagementConfigurationSettingValueTemplateReference]
        """
        return self._setting_value_template_reference
    
    @setting_value_template_reference.setter
    def setting_value_template_reference(self,value: Optional[device_management_configuration_setting_value_template_reference.DeviceManagementConfigurationSettingValueTemplateReference] = None) -> None:
        """
        Sets the settingValueTemplateReference property value. Setting value template reference
        Args:
            value: Value to set for the settingValueTemplateReference property.
        """
        self._setting_value_template_reference = value
    

