from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_type import DeviceType

@dataclass
class MobileAppSupportedDeviceType(AdditionalDataHolder, BackedModel, Parsable):
    """
    Device properties
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Maximum OS version
    maximum_operating_system_version: Optional[str] = None
    # Minimum OS version
    minimum_operating_system_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device type.
    type: Optional[DeviceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppSupportedDeviceType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppSupportedDeviceType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppSupportedDeviceType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_type import DeviceType

        from .device_type import DeviceType

        fields: Dict[str, Callable[[Any], None]] = {
            "maximumOperatingSystemVersion": lambda n : setattr(self, 'maximum_operating_system_version', n.get_str_value()),
            "minimumOperatingSystemVersion": lambda n : setattr(self, 'minimum_operating_system_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(DeviceType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("maximumOperatingSystemVersion", self.maximum_operating_system_version)
        writer.write_str_value("minimumOperatingSystemVersion", self.minimum_operating_system_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

