from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AudioMetadata(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Bit depth of the audio samples (for example, 16, 24).
    bit_depth: Optional[int] = None
    # Number of audio channels (for example, 1 for mono, 2 for stereo).
    channels: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Sample rate in Hertz (for example, 16000, 48000).
    sample_rate_hz: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AudioMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AudioMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AudioMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bitDepth": lambda n : setattr(self, 'bit_depth', n.get_int_value()),
            "channels": lambda n : setattr(self, 'channels', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sampleRateHz": lambda n : setattr(self, 'sample_rate_hz', n.get_int_value()),
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
        writer.write_int_value("bitDepth", self.bit_depth)
        writer.write_int_value("channels", self.channels)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("sampleRateHz", self.sample_rate_hz)
        writer.write_additional_data_value(self.additional_data)
    

