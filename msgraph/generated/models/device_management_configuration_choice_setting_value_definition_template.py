from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_option_definition_template

class DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate(AdditionalDataHolder, Parsable):
    """
    Choice Setting Value Definition Template
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationChoiceSettingValueDefinitionTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Choice Setting Allowed Options
        self._allowed_options: Optional[List[device_management_configuration_option_definition_template.DeviceManagementConfigurationOptionDefinitionTemplate]] = None
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
    
    @property
    def allowed_options(self,) -> Optional[List[device_management_configuration_option_definition_template.DeviceManagementConfigurationOptionDefinitionTemplate]]:
        """
        Gets the allowedOptions property value. Choice Setting Allowed Options
        Returns: Optional[List[device_management_configuration_option_definition_template.DeviceManagementConfigurationOptionDefinitionTemplate]]
        """
        return self._allowed_options
    
    @allowed_options.setter
    def allowed_options(self,value: Optional[List[device_management_configuration_option_definition_template.DeviceManagementConfigurationOptionDefinitionTemplate]] = None) -> None:
        """
        Sets the allowedOptions property value. Choice Setting Allowed Options
        Args:
            value: Value to set for the allowed_options property.
        """
        self._allowed_options = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_option_definition_template

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedOptions": lambda n : setattr(self, 'allowed_options', n.get_collection_of_object_values(device_management_configuration_option_definition_template.DeviceManagementConfigurationOptionDefinitionTemplate)),
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
        writer.write_collection_of_object_values("allowedOptions", self.allowed_options)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

