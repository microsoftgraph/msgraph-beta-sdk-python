from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

media_info = lazy_import('msgraph.generated.models.media_info')
prompt = lazy_import('msgraph.generated.models.prompt')

class MediaPrompt(prompt.Prompt):
    def __init__(self,) -> None:
        """
        Instantiates a new MediaPrompt and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.mediaPrompt"
        # The loop property
        self._loop: Optional[int] = None
        # The mediaInfo property
        self._media_info: Optional[media_info.MediaInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MediaPrompt:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MediaPrompt
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MediaPrompt()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "loop": lambda n : setattr(self, 'loop', n.get_int_value()),
            "media_info": lambda n : setattr(self, 'media_info', n.get_object_value(media_info.MediaInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def loop(self,) -> Optional[int]:
        """
        Gets the loop property value. The loop property
        Returns: Optional[int]
        """
        return self._loop
    
    @loop.setter
    def loop(self,value: Optional[int] = None) -> None:
        """
        Sets the loop property value. The loop property
        Args:
            value: Value to set for the loop property.
        """
        self._loop = value
    
    @property
    def media_info(self,) -> Optional[media_info.MediaInfo]:
        """
        Gets the mediaInfo property value. The mediaInfo property
        Returns: Optional[media_info.MediaInfo]
        """
        return self._media_info
    
    @media_info.setter
    def media_info(self,value: Optional[media_info.MediaInfo] = None) -> None:
        """
        Sets the mediaInfo property value. The mediaInfo property
        Args:
            value: Value to set for the mediaInfo property.
        """
        self._media_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("loop", self.loop)
        writer.write_object_value("mediaInfo", self.media_info)
    

