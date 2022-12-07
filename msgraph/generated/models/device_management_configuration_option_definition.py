from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_dependent_on = lazy_import('msgraph.generated.models.device_management_configuration_dependent_on')
device_management_configuration_setting_depended_on_by = lazy_import('msgraph.generated.models.device_management_configuration_setting_depended_on_by')
device_management_configuration_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_setting_value')

class DeviceManagementConfigurationOptionDefinition(AdditionalDataHolder, Parsable):
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
        Instantiates a new deviceManagementConfigurationOptionDefinition and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of Settings that depends on this option
        self._depended_on_by: Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]] = None
        # List of dependent settings for this option
        self._dependent_on: Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]] = None
        # Description of the option
        self._description: Optional[str] = None
        # Friendly name of the option
        self._display_name: Optional[str] = None
        # Help text of the option
        self._help_text: Optional[str] = None
        # Identifier of option
        self._item_id: Optional[str] = None
        # Name of the option
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Value of the option
        self._option_value: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationOptionDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationOptionDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationOptionDefinition()
    
    @property
    def depended_on_by(self,) -> Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]]:
        """
        Gets the dependedOnBy property value. List of Settings that depends on this option
        Returns: Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]]
        """
        return self._depended_on_by
    
    @depended_on_by.setter
    def depended_on_by(self,value: Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]] = None) -> None:
        """
        Sets the dependedOnBy property value. List of Settings that depends on this option
        Args:
            value: Value to set for the dependedOnBy property.
        """
        self._depended_on_by = value
    
    @property
    def dependent_on(self,) -> Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]]:
        """
        Gets the dependentOn property value. List of dependent settings for this option
        Returns: Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]]
        """
        return self._dependent_on
    
    @dependent_on.setter
    def dependent_on(self,value: Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]] = None) -> None:
        """
        Sets the dependentOn property value. List of dependent settings for this option
        Args:
            value: Value to set for the dependentOn property.
        """
        self._dependent_on = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the option
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the option
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Friendly name of the option
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Friendly name of the option
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "depended_on_by": lambda n : setattr(self, 'depended_on_by', n.get_collection_of_object_values(device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy)),
            "dependent_on": lambda n : setattr(self, 'dependent_on', n.get_collection_of_object_values(device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "help_text": lambda n : setattr(self, 'help_text', n.get_str_value()),
            "item_id": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "option_value": lambda n : setattr(self, 'option_value', n.get_object_value(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue)),
        }
        return fields
    
    @property
    def help_text(self,) -> Optional[str]:
        """
        Gets the helpText property value. Help text of the option
        Returns: Optional[str]
        """
        return self._help_text
    
    @help_text.setter
    def help_text(self,value: Optional[str] = None) -> None:
        """
        Sets the helpText property value. Help text of the option
        Args:
            value: Value to set for the helpText property.
        """
        self._help_text = value
    
    @property
    def item_id(self,) -> Optional[str]:
        """
        Gets the itemId property value. Identifier of option
        Returns: Optional[str]
        """
        return self._item_id
    
    @item_id.setter
    def item_id(self,value: Optional[str] = None) -> None:
        """
        Sets the itemId property value. Identifier of option
        Args:
            value: Value to set for the itemId property.
        """
        self._item_id = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the option
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the option
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    
    @property
    def option_value(self,) -> Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue]:
        """
        Gets the optionValue property value. Value of the option
        Returns: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue]
        """
        return self._option_value
    
    @option_value.setter
    def option_value(self,value: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue] = None) -> None:
        """
        Sets the optionValue property value. Value of the option
        Args:
            value: Value to set for the optionValue property.
        """
        self._option_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("dependedOnBy", self.depended_on_by)
        writer.write_collection_of_object_values("dependentOn", self.dependent_on)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpText", self.help_text)
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("optionValue", self.option_value)
        writer.write_additional_data_value(self.additional_data)
    

