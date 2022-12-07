from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_setting_instance = lazy_import('msgraph.generated.models.device_management_setting_instance')

class DeviceManagementAbstractComplexSettingInstance(device_management_setting_instance.DeviceManagementSettingInstance):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementAbstractComplexSettingInstance and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementAbstractComplexSettingInstance"
        # The definition ID for the chosen implementation of this complex setting
        self._implementation_id: Optional[str] = None
        # The values that make up the complex setting
        self._value: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementAbstractComplexSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementAbstractComplexSettingInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementAbstractComplexSettingInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "implementation_id": lambda n : setattr(self, 'implementation_id', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(device_management_setting_instance.DeviceManagementSettingInstance)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def implementation_id(self,) -> Optional[str]:
        """
        Gets the implementationId property value. The definition ID for the chosen implementation of this complex setting
        Returns: Optional[str]
        """
        return self._implementation_id
    
    @implementation_id.setter
    def implementation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the implementationId property value. The definition ID for the chosen implementation of this complex setting
        Args:
            value: Value to set for the implementationId property.
        """
        self._implementation_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("implementationId", self.implementation_id)
        writer.write_collection_of_object_values("value", self.value)
    
    @property
    def value(self,) -> Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]:
        """
        Gets the value property value. The values that make up the complex setting
        Returns: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None) -> None:
        """
        Sets the value property value. The values that make up the complex setting
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

