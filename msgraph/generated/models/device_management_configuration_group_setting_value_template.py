from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')

class DeviceManagementConfigurationGroupSettingValueTemplate(AdditionalDataHolder, Parsable):
    """
    Group Setting Value Template
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
    
    @property
    def children(self,) -> Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]]:
        """
        Gets the children property value. Group setting value children
        Returns: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]] = None) -> None:
        """
        Sets the children property value. Group setting value children
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationGroupSettingValueTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Group setting value children
        self._children: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Setting Value Template Id
        self._setting_value_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationGroupSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingValueTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationGroupSettingValueTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "setting_value_template_id": lambda n : setattr(self, 'setting_value_template_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("settingValueTemplateId", self.setting_value_template_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_value_template_id(self,) -> Optional[str]:
        """
        Gets the settingValueTemplateId property value. Setting Value Template Id
        Returns: Optional[str]
        """
        return self._setting_value_template_id
    
    @setting_value_template_id.setter
    def setting_value_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingValueTemplateId property value. Setting Value Template Id
        Args:
            value: Value to set for the settingValueTemplateId property.
        """
        self._setting_value_template_id = value
    

