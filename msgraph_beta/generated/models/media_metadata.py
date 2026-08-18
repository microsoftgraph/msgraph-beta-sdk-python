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
    # Audio-specific encoding details. Nullable. Set when the analyzed content is audio or multimodal.
    audio_metadata: Optional[AudioMetadata] = None
    # Size of the content in bytes. Set this value to 0 for live streams where the total size is unknown; for recorded files, specify the actual size.
    byte_size: Optional[int] = None
    # Duration of the analyzed content in whole seconds. Sub-second or millisecond windows are rounded to the nearest second. For a continuous live stream, set this value to the length of the analysis window.
    duration: Optional[int] = None
    # Indicates whether the analysis was performed in real time on a live stream.
    is_real_time: Optional[bool] = None
    # MIME type of the analyzed content. Common values for Teams media include audio/pcm, video/mp4, and video/h264.
    mime_type: Optional[str] = None
    # The modality property
    modality: Optional[ContentModality] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Network and real-time streaming quality metrics. Nullable. Set when the analyzed content was streamed in real time.
    streaming_metadata: Optional[StreamingMetadata] = None
    # Video-specific encoding and quality details. Nullable. Set when the analyzed content is video or multimodal.
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
    

