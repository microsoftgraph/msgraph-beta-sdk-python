from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio_metadata import AudioMetadata
    from .content_modality import ContentModality
    from .streaming_metadata import StreamingMetadata
    from .video_metadata import VideoMetadata

@dataclass
class MediaMetadata(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The audioMetadata property
    audio_metadata: Optional[AudioMetadata] = None
    # The byteSize property
    byte_size: Optional[int] = None
    # The duration property
    duration: Optional[int] = None
    # The isRealTime property
    is_real_time: Optional[bool] = None
    # The mimeType property
    mime_type: Optional[str] = None
    # The modality property
    modality: Optional[ContentModality] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The streamingMetadata property
    streaming_metadata: Optional[StreamingMetadata] = None
    # The videoMetadata property
    video_metadata: Optional[VideoMetadata] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MediaMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MediaMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MediaMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .audio_metadata import AudioMetadata
        from .content_modality import ContentModality
        from .streaming_metadata import StreamingMetadata
        from .video_metadata import VideoMetadata

        from .audio_metadata import AudioMetadata
        from .content_modality import ContentModality
        from .streaming_metadata import StreamingMetadata
        from .video_metadata import VideoMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "audioMetadata": lambda n : setattr(self, 'audio_metadata', n.get_object_value(AudioMetadata)),
            "byteSize": lambda n : setattr(self, 'byte_size', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "isRealTime": lambda n : setattr(self, 'is_real_time', n.get_bool_value()),
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
            "modality": lambda n : setattr(self, 'modality', n.get_enum_value(ContentModality)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "streamingMetadata": lambda n : setattr(self, 'streaming_metadata', n.get_object_value(StreamingMetadata)),
            "videoMetadata": lambda n : setattr(self, 'video_metadata', n.get_object_value(VideoMetadata)),
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
        writer.write_object_value("audioMetadata", self.audio_metadata)
        writer.write_int_value("byteSize", self.byte_size)
        writer.write_int_value("duration", self.duration)
        writer.write_bool_value("isRealTime", self.is_real_time)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_enum_value("modality", self.modality)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("streamingMetadata", self.streaming_metadata)
        writer.write_object_value("videoMetadata", self.video_metadata)
        writer.write_additional_data_value(self.additional_data)
    

