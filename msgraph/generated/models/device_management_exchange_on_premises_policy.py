from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_exchange_access_level, device_management_exchange_access_rule, device_management_exchange_device_class, entity, on_premises_conditional_access_settings

from . import entity

@dataclass
class DeviceManagementExchangeOnPremisesPolicy(entity.Entity):
    """
    Singleton entity which represents the Exchange OnPremises policy configured for a tenant.
    """
    # The list of device access rules in Exchange. The access rules apply globally to the entire Exchange organization
    access_rules: Optional[List[device_management_exchange_access_rule.DeviceManagementExchangeAccessRule]] = None
    # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
    conditional_access_settings: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None
    # Access Level in Exchange.
    default_access_level: Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel] = None
    # The list of device classes known to Exchange
    known_device_classes: Optional[List[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass]] = None
    # Notification text that will be sent to users quarantined by this policy. This is UTF8 encoded byte array HTML.
    notification_content: Optional[bytes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementExchangeOnPremisesPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExchangeOnPremisesPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementExchangeOnPremisesPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_exchange_access_level, device_management_exchange_access_rule, device_management_exchange_device_class, entity, on_premises_conditional_access_settings

        from . import device_management_exchange_access_level, device_management_exchange_access_rule, device_management_exchange_device_class, entity, on_premises_conditional_access_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "accessRules": lambda n : setattr(self, 'access_rules', n.get_collection_of_object_values(device_management_exchange_access_rule.DeviceManagementExchangeAccessRule)),
            "conditionalAccessSettings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings)),
            "defaultAccessLevel": lambda n : setattr(self, 'default_access_level', n.get_enum_value(device_management_exchange_access_level.DeviceManagementExchangeAccessLevel)),
            "knownDeviceClasses": lambda n : setattr(self, 'known_device_classes', n.get_collection_of_object_values(device_management_exchange_device_class.DeviceManagementExchangeDeviceClass)),
            "notificationContent": lambda n : setattr(self, 'notification_content', n.get_bytes_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessRules", self.access_rules)
        writer.write_object_value("conditionalAccessSettings", self.conditional_access_settings)
        writer.write_enum_value("defaultAccessLevel", self.default_access_level)
        writer.write_collection_of_object_values("knownDeviceClasses", self.known_device_classes)
        writer.write_object_value("notificationContent", self.notification_content)
    

