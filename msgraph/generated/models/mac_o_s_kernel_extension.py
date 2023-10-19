from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class MacOSKernelExtension(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents a specific macOS kernel extension. A macOS kernel extension can be described by its team identifier plus its bundle identifier.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Bundle ID of the kernel extension.
    bundle_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The team identifier that was used to sign the kernel extension.
    team_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSKernelExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSKernelExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSKernelExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "teamIdentifier": lambda n : setattr(self, 'team_identifier', n.get_str_value()),
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
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("teamIdentifier", self.team_identifier)
        writer.write_additional_data_value(self.additional_data)
    

