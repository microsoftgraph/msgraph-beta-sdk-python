from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cross_tenant_access_policy_b2_b_setting = lazy_import('msgraph.generated.models.cross_tenant_access_policy_b2_b_setting')
devices_filter = lazy_import('msgraph.generated.models.devices_filter')

class CrossTenantAccessPolicyTenantRestrictions(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting):
    def __init__(self,) -> None:
        """
        Instantiates a new CrossTenantAccessPolicyTenantRestrictions and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.crossTenantAccessPolicyTenantRestrictions"
        # The devices property
        self._devices: Optional[devices_filter.DevicesFilter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyTenantRestrictions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyTenantRestrictions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicyTenantRestrictions()
    
    @property
    def devices(self,) -> Optional[devices_filter.DevicesFilter]:
        """
        Gets the devices property value. The devices property
        Returns: Optional[devices_filter.DevicesFilter]
        """
        return self._devices
    
    @devices.setter
    def devices(self,value: Optional[devices_filter.DevicesFilter] = None) -> None:
        """
        Sets the devices property value. The devices property
        Args:
            value: Value to set for the devices property.
        """
        self._devices = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "devices": lambda n : setattr(self, 'devices', n.get_object_value(devices_filter.DevicesFilter)),
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
        writer.write_object_value("devices", self.devices)
    

