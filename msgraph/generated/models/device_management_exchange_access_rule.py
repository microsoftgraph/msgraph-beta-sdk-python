from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
    from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass

@dataclass
class DeviceManagementExchangeAccessRule(AdditionalDataHolder, BackedModel, Parsable):
    """
    Device Access Rules in Exchange.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Access Level in Exchange.
    access_level: Optional[DeviceManagementExchangeAccessLevel] = None
    # Device Class which will be impacted by this rule.
    device_class: Optional[DeviceManagementExchangeDeviceClass] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementExchangeAccessRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExchangeAccessRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementExchangeAccessRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
        from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass

        from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
        from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass

        fields: Dict[str, Callable[[Any], None]] = {
            "accessLevel": lambda n : setattr(self, 'access_level', n.get_enum_value(DeviceManagementExchangeAccessLevel)),
            "deviceClass": lambda n : setattr(self, 'device_class', n.get_object_value(DeviceManagementExchangeDeviceClass)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("accessLevel", self.access_level)
        writer.write_object_value("deviceClass", self.device_class)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

