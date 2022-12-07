from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceManagementConfigurationSettingValueTemplateReference(AdditionalDataHolder, Parsable):
    """
    Setting value template reference information
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
        Instantiates a new deviceManagementConfigurationSettingValueTemplateReference and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Setting value template id
        self._setting_value_template_id: Optional[str] = None
        # Indicates whether to update policy setting value to match template setting default value
        self._use_template_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingValueTemplateReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingValueTemplateReference
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingValueTemplateReference()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "setting_value_template_id": lambda n : setattr(self, 'setting_value_template_id', n.get_str_value()),
            "use_template_default": lambda n : setattr(self, 'use_template_default', n.get_bool_value()),
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
        writer.write_str_value("settingValueTemplateId", self.setting_value_template_id)
        writer.write_bool_value("useTemplateDefault", self.use_template_default)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_value_template_id(self,) -> Optional[str]:
        """
        Gets the settingValueTemplateId property value. Setting value template id
        Returns: Optional[str]
        """
        return self._setting_value_template_id
    
    @setting_value_template_id.setter
    def setting_value_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingValueTemplateId property value. Setting value template id
        Args:
            value: Value to set for the settingValueTemplateId property.
        """
        self._setting_value_template_id = value
    
    @property
    def use_template_default(self,) -> Optional[bool]:
        """
        Gets the useTemplateDefault property value. Indicates whether to update policy setting value to match template setting default value
        Returns: Optional[bool]
        """
        return self._use_template_default
    
    @use_template_default.setter
    def use_template_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the useTemplateDefault property value. Indicates whether to update policy setting value to match template setting default value
        Args:
            value: Value to set for the useTemplateDefault property.
        """
        self._use_template_default = value
    

