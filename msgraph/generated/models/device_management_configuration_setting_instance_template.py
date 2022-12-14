from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceManagementConfigurationSettingInstanceTemplate(AdditionalDataHolder, Parsable):
    """
    Setting Instance Template
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
        Instantiates a new deviceManagementConfigurationSettingInstanceTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates if a policy must specify this setting.
        self._is_required: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Setting Definition Id
        self._setting_definition_id: Optional[str] = None
        # Setting Instance Template Id
        self._setting_instance_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingInstanceTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_required": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "setting_definition_id": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "setting_instance_template_id": lambda n : setattr(self, 'setting_instance_template_id', n.get_str_value()),
        }
        return fields
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. Indicates if a policy must specify this setting.
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. Indicates if a policy must specify this setting.
        Args:
            value: Value to set for the isRequired property.
        """
        self._is_required = value
    
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
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_str_value("settingInstanceTemplateId", self.setting_instance_template_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_definition_id(self,) -> Optional[str]:
        """
        Gets the settingDefinitionId property value. Setting Definition Id
        Returns: Optional[str]
        """
        return self._setting_definition_id
    
    @setting_definition_id.setter
    def setting_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDefinitionId property value. Setting Definition Id
        Args:
            value: Value to set for the settingDefinitionId property.
        """
        self._setting_definition_id = value
    
    @property
    def setting_instance_template_id(self,) -> Optional[str]:
        """
        Gets the settingInstanceTemplateId property value. Setting Instance Template Id
        Returns: Optional[str]
        """
        return self._setting_instance_template_id
    
    @setting_instance_template_id.setter
    def setting_instance_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingInstanceTemplateId property value. Setting Instance Template Id
        Args:
            value: Value to set for the settingInstanceTemplateId property.
        """
        self._setting_instance_template_id = value
    

