from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_filter import ConditionalAccessFilter

@dataclass
class ConditionalAccessDevices(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Filter that defines the dynamic-device-syntax rule to include/exclude devices. A filter can use device properties (such as extension attributes) to include/exclude them. Cannot be set if includeDevices or excludeDevices is set.
    device_filter: Optional[ConditionalAccessFilter] = None
    # The excludeDeviceStates property
    exclude_device_states: Optional[List[str]] = None
    # States excluded from the scope of the policy. Possible values: Compliant, DomainJoined. Cannot be set if deviceFIlter is set.
    exclude_devices: Optional[List[str]] = None
    # The includeDeviceStates property
    include_device_states: Optional[List[str]] = None
    # States in the scope of the policy. All is the only allowed value. Cannot be set if deviceFilter is set.
    include_devices: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessDevices:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessDevices
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessDevices()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_filter import ConditionalAccessFilter

        from .conditional_access_filter import ConditionalAccessFilter

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceFilter": lambda n : setattr(self, 'device_filter', n.get_object_value(ConditionalAccessFilter)),
            "excludeDeviceStates": lambda n : setattr(self, 'exclude_device_states', n.get_collection_of_primitive_values(str)),
            "excludeDevices": lambda n : setattr(self, 'exclude_devices', n.get_collection_of_primitive_values(str)),
            "includeDeviceStates": lambda n : setattr(self, 'include_device_states', n.get_collection_of_primitive_values(str)),
            "includeDevices": lambda n : setattr(self, 'include_devices', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("deviceFilter", self.device_filter)
        writer.write_collection_of_primitive_values("excludeDeviceStates", self.exclude_device_states)
        writer.write_collection_of_primitive_values("excludeDevices", self.exclude_devices)
        writer.write_collection_of_primitive_values("includeDeviceStates", self.include_device_states)
        writer.write_collection_of_primitive_values("includeDevices", self.include_devices)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

