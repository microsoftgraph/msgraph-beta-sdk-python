from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

visual_properties = lazy_import('msgraph.generated.models.visual_properties')

class PayloadTypes(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new payloadTypes and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The notification content of a raw user notification that will be delivered to and consumed by the app client on all supported platforms (Windows, iOS, Android or WebPush) receiving this notification. At least one of Payload.RawContent or Payload.VisualContent needs to be valid for a POST Notification request.
        self._raw_content: Optional[str] = None
        # The visual content of a visual user notification, which will be consumed by the notification platform on each supported platform (Windows, iOS and Android only) and rendered for the user. At least one of Payload.RawContent or Payload.VisualContent needs to be valid for a POST Notification request.
        self._visual_content: Optional[visual_properties.VisualProperties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PayloadTypes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PayloadTypes
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PayloadTypes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "raw_content": lambda n : setattr(self, 'raw_content', n.get_str_value()),
            "visual_content": lambda n : setattr(self, 'visual_content', n.get_object_value(visual_properties.VisualProperties)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def raw_content(self,) -> Optional[str]:
        """
        Gets the rawContent property value. The notification content of a raw user notification that will be delivered to and consumed by the app client on all supported platforms (Windows, iOS, Android or WebPush) receiving this notification. At least one of Payload.RawContent or Payload.VisualContent needs to be valid for a POST Notification request.
        Returns: Optional[str]
        """
        return self._raw_content
    
    @raw_content.setter
    def raw_content(self,value: Optional[str] = None) -> None:
        """
        Sets the rawContent property value. The notification content of a raw user notification that will be delivered to and consumed by the app client on all supported platforms (Windows, iOS, Android or WebPush) receiving this notification. At least one of Payload.RawContent or Payload.VisualContent needs to be valid for a POST Notification request.
        Args:
            value: Value to set for the rawContent property.
        """
        self._raw_content = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("rawContent", self.raw_content)
        writer.write_object_value("visualContent", self.visual_content)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def visual_content(self,) -> Optional[visual_properties.VisualProperties]:
        """
        Gets the visualContent property value. The visual content of a visual user notification, which will be consumed by the notification platform on each supported platform (Windows, iOS and Android only) and rendered for the user. At least one of Payload.RawContent or Payload.VisualContent needs to be valid for a POST Notification request.
        Returns: Optional[visual_properties.VisualProperties]
        """
        return self._visual_content
    
    @visual_content.setter
    def visual_content(self,value: Optional[visual_properties.VisualProperties] = None) -> None:
        """
        Sets the visualContent property value. The visual content of a visual user notification, which will be consumed by the notification platform on each supported platform (Windows, iOS and Android only) and rendered for the user. At least one of Payload.RawContent or Payload.VisualContent needs to be valid for a POST Notification request.
        Args:
            value: Value to set for the visualContent property.
        """
        self._visual_content = value
    

