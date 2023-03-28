from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_payload_detail, payload_coachmark

class PayloadDetail(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new payloadDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Payload coachmark details.
        self._coachmarks: Optional[List[payload_coachmark.PayloadCoachmark]] = None
        # Payload content details.
        self._content: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The phishing URL used to target a user.
        self._phishing_url: Optional[str] = None
    
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
    
    @property
    def coachmarks(self,) -> Optional[List[payload_coachmark.PayloadCoachmark]]:
        """
        Gets the coachmarks property value. Payload coachmark details.
        Returns: Optional[List[payload_coachmark.PayloadCoachmark]]
        """
        return self._coachmarks
    
    @coachmarks.setter
    def coachmarks(self,value: Optional[List[payload_coachmark.PayloadCoachmark]] = None) -> None:
        """
        Sets the coachmarks property value. Payload coachmark details.
        Args:
            value: Value to set for the coachmarks property.
        """
        self._coachmarks = value
    
    @property
    def content(self,) -> Optional[str]:
        """
        Gets the content property value. Payload content details.
        Returns: Optional[str]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[str] = None) -> None:
        """
        Sets the content property value. Payload content details.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PayloadDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PayloadDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.emailPayloadDetail":
                from . import email_payload_detail

                return email_payload_detail.EmailPayloadDetail()
        return PayloadDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_payload_detail, payload_coachmark

        fields: Dict[str, Callable[[Any], None]] = {
            "coachmarks": lambda n : setattr(self, 'coachmarks', n.get_collection_of_object_values(payload_coachmark.PayloadCoachmark)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phishingUrl": lambda n : setattr(self, 'phishing_url', n.get_str_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def phishing_url(self,) -> Optional[str]:
        """
        Gets the phishingUrl property value. The phishing URL used to target a user.
        Returns: Optional[str]
        """
        return self._phishing_url
    
    @phishing_url.setter
    def phishing_url(self,value: Optional[str] = None) -> None:
        """
        Sets the phishingUrl property value. The phishing URL used to target a user.
        Args:
            value: Value to set for the phishing_url property.
        """
        self._phishing_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("coachmarks", self.coachmarks)
        writer.write_str_value("content", self.content)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("phishingUrl", self.phishing_url)
        writer.write_additional_data_value(self.additional_data)
    

