from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_policy, entity

from . import entity

class DeviceCompliancePolicyGroupAssignment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceCompliancePolicyGroupAssignment and sets the default values.
        """
        super().__init__()
        # The navigation link to the  device compliance polic targeted.
        self._device_compliance_policy: Optional[device_compliance_policy.DeviceCompliancePolicy] = None
        # Indicates if this group is should be excluded. Defaults that the group should be included
        self._exclude_group: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Id of the AAD group we are targeting the device compliance policy to.
        self._target_group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyGroupAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyGroupAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicyGroupAssignment()
    
    @property
    def device_compliance_policy(self,) -> Optional[device_compliance_policy.DeviceCompliancePolicy]:
        """
        Gets the deviceCompliancePolicy property value. The navigation link to the  device compliance polic targeted.
        Returns: Optional[device_compliance_policy.DeviceCompliancePolicy]
        """
        return self._device_compliance_policy
    
    @device_compliance_policy.setter
    def device_compliance_policy(self,value: Optional[device_compliance_policy.DeviceCompliancePolicy] = None) -> None:
        """
        Sets the deviceCompliancePolicy property value. The navigation link to the  device compliance polic targeted.
        Args:
            value: Value to set for the device_compliance_policy property.
        """
        self._device_compliance_policy = value
    
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
            value: Value to set for the exclude_group property.
        """
        self._exclude_group = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_policy, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCompliancePolicy": lambda n : setattr(self, 'device_compliance_policy', n.get_object_value(device_compliance_policy.DeviceCompliancePolicy)),
            "excludeGroup": lambda n : setattr(self, 'exclude_group', n.get_bool_value()),
            "targetGroupId": lambda n : setattr(self, 'target_group_id', n.get_str_value()),
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
        writer.write_object_value("deviceCompliancePolicy", self.device_compliance_policy)
        writer.write_bool_value("excludeGroup", self.exclude_group)
        writer.write_str_value("targetGroupId", self.target_group_id)
    
    @property
    def target_group_id(self,) -> Optional[str]:
        """
        Gets the targetGroupId property value. The Id of the AAD group we are targeting the device compliance policy to.
        Returns: Optional[str]
        """
        return self._target_group_id
    
    @target_group_id.setter
    def target_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetGroupId property value. The Id of the AAD group we are targeting the device compliance policy to.
        Args:
            value: Value to set for the target_group_id property.
        """
        self._target_group_id = value
    

