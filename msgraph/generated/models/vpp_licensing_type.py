from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class VppLicensingType(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties for iOS Volume-Purchased Program (Vpp) Licensing Type.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Whether the program supports the device licensing type.
    support_device_licensing: Optional[bool] = None
    # Whether the program supports the user licensing type.
    support_user_licensing: Optional[bool] = None
    # Whether the program supports the device licensing type.
    supports_device_licensing: Optional[bool] = None
    # Whether the program supports the user licensing type.
    supports_user_licensing: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VppLicensingType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VppLicensingType
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VppLicensingType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supportDeviceLicensing": lambda n : setattr(self, 'support_device_licensing', n.get_bool_value()),
            "supportUserLicensing": lambda n : setattr(self, 'support_user_licensing', n.get_bool_value()),
            "supportsDeviceLicensing": lambda n : setattr(self, 'supports_device_licensing', n.get_bool_value()),
            "supportsUserLicensing": lambda n : setattr(self, 'supports_user_licensing', n.get_bool_value()),
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
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_bool_value("supportDeviceLicensing", self.support_device_licensing)
        writer.write_bool_value("supportUserLicensing", self.support_user_licensing)
        writer.write_bool_value("supportsDeviceLicensing", self.supports_device_licensing)
        writer.write_bool_value("supportsUserLicensing", self.supports_user_licensing)
        writer.write_additional_data_value(self.additional_data)
    

