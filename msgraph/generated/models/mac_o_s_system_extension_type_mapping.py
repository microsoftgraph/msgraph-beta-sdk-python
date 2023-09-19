from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_system_extension_type import MacOSSystemExtensionType

@dataclass
class MacOSSystemExtensionTypeMapping(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents a mapping between team identifiers for macOS system extensions and system extension types.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Flag enum representing the allowed macOS system extension types.
    allowed_types: Optional[MacOSSystemExtensionType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Gets or sets the team identifier used to sign the system extension.
    team_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSystemExtensionTypeMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSystemExtensionTypeMapping
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSSystemExtensionTypeMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_system_extension_type import MacOSSystemExtensionType

        from .mac_o_s_system_extension_type import MacOSSystemExtensionType

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedTypes": lambda n : setattr(self, 'allowed_types', n.get_collection_of_enum_values(MacOSSystemExtensionType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("allowedTypes", self.allowed_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("teamIdentifier", self.team_identifier)
        writer.write_additional_data_value(self.additional_data)
    

