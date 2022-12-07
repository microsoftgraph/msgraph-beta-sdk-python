from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceConfigurationGroupAssignment(entity.Entity):
    """
    Device configuration group assignment.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceConfigurationGroupAssignment and sets the default values.
        """
        super().__init__()
        # The navigation link to the Device Configuration being targeted.
        self._device_configuration: Optional[device_configuration.DeviceConfiguration] = None
        # Indicates if this group is should be excluded. Defaults that the group should be included
        self._exclude_group: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Id of the AAD group we are targeting the device configuration to.
        self._target_group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfigurationGroupAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationGroupAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceConfigurationGroupAssignment()
    
    @property
    def device_configuration(self,) -> Optional[device_configuration.DeviceConfiguration]:
        """
        Gets the deviceConfiguration property value. The navigation link to the Device Configuration being targeted.
        Returns: Optional[device_configuration.DeviceConfiguration]
        """
        return self._device_configuration
    
    @device_configuration.setter
    def device_configuration(self,value: Optional[device_configuration.DeviceConfiguration] = None) -> None:
        """
        Sets the deviceConfiguration property value. The navigation link to the Device Configuration being targeted.
        Args:
            value: Value to set for the deviceConfiguration property.
        """
        self._device_configuration = value
    
    @property
    def exclude_group(self,) -> Optional[bool]:
        """
        Gets the excludeGroup property value. Indicates if this group is should be excluded. Defaults that the group should be included
        Returns: Optional[bool]
        """
        return self._exclude_group
    
    @exclude_group.setter
    def exclude_group(self,value: Optional[bool] = None) -> None:
        """
        Sets the excludeGroup property value. Indicates if this group is should be excluded. Defaults that the group should be included
        Args:
            value: Value to set for the excludeGroup property.
        """
        self._exclude_group = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_configuration": lambda n : setattr(self, 'device_configuration', n.get_object_value(device_configuration.DeviceConfiguration)),
            "exclude_group": lambda n : setattr(self, 'exclude_group', n.get_bool_value()),
            "target_group_id": lambda n : setattr(self, 'target_group_id', n.get_str_value()),
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
        writer.write_object_value("deviceConfiguration", self.device_configuration)
        writer.write_bool_value("excludeGroup", self.exclude_group)
        writer.write_str_value("targetGroupId", self.target_group_id)
    
    @property
    def target_group_id(self,) -> Optional[str]:
        """
        Gets the targetGroupId property value. The Id of the AAD group we are targeting the device configuration to.
        Returns: Optional[str]
        """
        return self._target_group_id
    
    @target_group_id.setter
    def target_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetGroupId property value. The Id of the AAD group we are targeting the device configuration to.
        Args:
            value: Value to set for the targetGroupId property.
        """
        self._target_group_id = value
    

