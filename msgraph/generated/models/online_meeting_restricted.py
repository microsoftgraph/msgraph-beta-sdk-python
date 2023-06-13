from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import online_meeting_content_sharing_disabled_reason, online_meeting_video_disabled_reason

@dataclass
class OnlineMeetingRestricted(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies the reason why shared content from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
    content_sharing_disabled: Optional[online_meeting_content_sharing_disabled_reason.OnlineMeetingContentSharingDisabledReason] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the reason why video from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
    video_disabled: Optional[online_meeting_video_disabled_reason.OnlineMeetingVideoDisabledReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeetingRestricted:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingRestricted
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnlineMeetingRestricted()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import online_meeting_content_sharing_disabled_reason, online_meeting_video_disabled_reason

        fields: Dict[str, Callable[[Any], None]] = {
            "contentSharingDisabled": lambda n : setattr(self, 'content_sharing_disabled', n.get_enum_value(online_meeting_content_sharing_disabled_reason.OnlineMeetingContentSharingDisabledReason)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "videoDisabled": lambda n : setattr(self, 'video_disabled', n.get_enum_value(online_meeting_video_disabled_reason.OnlineMeetingVideoDisabledReason)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("contentSharingDisabled", self.content_sharing_disabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("videoDisabled", self.video_disabled)
        writer.write_additional_data_value(self.additional_data)
    

