from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

dlp_notification = lazy_import('msgraph.generated.models.dlp_notification')

class DlpWindowsDevicesNotification(dlp_notification.DlpNotification):
    def __init__(self,) -> None:
        """
        Instantiates a new DlpWindowsDevicesNotification and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.dlpWindowsDevicesNotification"
        # The contentName property
        self._content_name: Optional[str] = None
        # The lastModfiedBy property
        self._last_modfied_by: Optional[str] = None
    
    @property
    def content_name(self,) -> Optional[str]:
        """
        Gets the contentName property value. The contentName property
        Returns: Optional[str]
        """
        return self._content_name
    
    @content_name.setter
    def content_name(self,value: Optional[str] = None) -> None:
        """
        Sets the contentName property value. The contentName property
        Args:
            value: Value to set for the contentName property.
        """
        self._content_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DlpWindowsDevicesNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DlpWindowsDevicesNotification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DlpWindowsDevicesNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_name": lambda n : setattr(self, 'content_name', n.get_str_value()),
            "last_modfied_by": lambda n : setattr(self, 'last_modfied_by', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modfied_by(self,) -> Optional[str]:
        """
        Gets the lastModfiedBy property value. The lastModfiedBy property
        Returns: Optional[str]
        """
        return self._last_modfied_by
    
    @last_modfied_by.setter
    def last_modfied_by(self,value: Optional[str] = None) -> None:
        """
        Sets the lastModfiedBy property value. The lastModfiedBy property
        Args:
            value: Value to set for the lastModfiedBy property.
        """
        self._last_modfied_by = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("contentName", self.content_name)
        writer.write_str_value("lastModfiedBy", self.last_modfied_by)
    

