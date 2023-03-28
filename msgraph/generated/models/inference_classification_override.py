from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_address, entity, inference_classification_type

from . import entity

class InferenceClassificationOverride(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new inferenceClassificationOverride and sets the default values.
        """
        super().__init__()
        # Specifies how incoming messages from a specific sender should always be classified as. Possible values are: focused, other.
        self._classify_as: Optional[inference_classification_type.InferenceClassificationType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The email address information of the sender for whom the override is created.
        self._sender_email_address: Optional[email_address.EmailAddress] = None
    
    @property
    def classify_as(self,) -> Optional[inference_classification_type.InferenceClassificationType]:
        """
        Gets the classifyAs property value. Specifies how incoming messages from a specific sender should always be classified as. Possible values are: focused, other.
        Returns: Optional[inference_classification_type.InferenceClassificationType]
        """
        return self._classify_as
    
    @classify_as.setter
    def classify_as(self,value: Optional[inference_classification_type.InferenceClassificationType] = None) -> None:
        """
        Sets the classifyAs property value. Specifies how incoming messages from a specific sender should always be classified as. Possible values are: focused, other.
        Args:
            value: Value to set for the classify_as property.
        """
        self._classify_as = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceClassificationOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InferenceClassificationOverride
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InferenceClassificationOverride()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_address, entity, inference_classification_type

        fields: Dict[str, Callable[[Any], None]] = {
            "classifyAs": lambda n : setattr(self, 'classify_as', n.get_enum_value(inference_classification_type.InferenceClassificationType)),
            "senderEmailAddress": lambda n : setattr(self, 'sender_email_address', n.get_object_value(email_address.EmailAddress)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def sender_email_address(self,) -> Optional[email_address.EmailAddress]:
        """
        Gets the senderEmailAddress property value. The email address information of the sender for whom the override is created.
        Returns: Optional[email_address.EmailAddress]
        """
        return self._sender_email_address
    
    @sender_email_address.setter
    def sender_email_address(self,value: Optional[email_address.EmailAddress] = None) -> None:
        """
        Sets the senderEmailAddress property value. The email address information of the sender for whom the override is created.
        Args:
            value: Value to set for the sender_email_address property.
        """
        self._sender_email_address = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("classifyAs", self.classify_as)
        writer.write_object_value("senderEmailAddress", self.sender_email_address)
    

