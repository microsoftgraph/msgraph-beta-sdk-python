from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_abstract_complex_setting_instance, device_management_boolean_setting_instance, device_management_collection_setting_instance, device_management_complex_setting_instance, device_management_integer_setting_instance, device_management_string_setting_instance, entity

from . import entity

class DeviceManagementSettingInstance(entity.Entity):
    """
    Base type for a setting instance
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettingInstance and sets the default values.
        """
        super().__init__()
        # The ID of the setting definition for this instance
        self._definition_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # JSON representation of the value
        self._value_json: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementAbstractComplexSettingInstance":
                from . import device_management_abstract_complex_setting_instance

                return device_management_abstract_complex_setting_instance.DeviceManagementAbstractComplexSettingInstance()
            if mapping_value == "#microsoft.graph.deviceManagementBooleanSettingInstance":
                from . import device_management_boolean_setting_instance

                return device_management_boolean_setting_instance.DeviceManagementBooleanSettingInstance()
            if mapping_value == "#microsoft.graph.deviceManagementCollectionSettingInstance":
                from . import device_management_collection_setting_instance

                return device_management_collection_setting_instance.DeviceManagementCollectionSettingInstance()
            if mapping_value == "#microsoft.graph.deviceManagementComplexSettingInstance":
                from . import device_management_complex_setting_instance

                return device_management_complex_setting_instance.DeviceManagementComplexSettingInstance()
            if mapping_value == "#microsoft.graph.deviceManagementIntegerSettingInstance":
                from . import device_management_integer_setting_instance

                return device_management_integer_setting_instance.DeviceManagementIntegerSettingInstance()
            if mapping_value == "#microsoft.graph.deviceManagementStringSettingInstance":
                from . import device_management_string_setting_instance

                return device_management_string_setting_instance.DeviceManagementStringSettingInstance()
        return DeviceManagementSettingInstance()
    
    @property
    def definition_id(self,) -> Optional[str]:
        """
        Gets the definitionId property value. The ID of the setting definition for this instance
        Returns: Optional[str]
        """
        return self._definition_id
    
    @definition_id.setter
    def definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the definitionId property value. The ID of the setting definition for this instance
        Args:
            value: Value to set for the definition_id property.
        """
        self._definition_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_abstract_complex_setting_instance, device_management_boolean_setting_instance, device_management_collection_setting_instance, device_management_complex_setting_instance, device_management_integer_setting_instance, device_management_string_setting_instance, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "definitionId": lambda n : setattr(self, 'definition_id', n.get_str_value()),
            "valueJson": lambda n : setattr(self, 'value_json', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("valueJson", self.value_json)
    
    @property
    def value_json(self,) -> Optional[str]:
        """
        Gets the valueJson property value. JSON representation of the value
        Returns: Optional[str]
        """
        return self._value_json
    
    @value_json.setter
    def value_json(self,value: Optional[str] = None) -> None:
        """
        Sets the valueJson property value. JSON representation of the value
        Args:
            value: Value to set for the value_json property.
        """
        self._value_json = value
    

