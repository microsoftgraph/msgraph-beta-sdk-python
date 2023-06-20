from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import weak_algorithms

@dataclass
class RequestSignatureVerification(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies whether this application accepts weak algorithms.  The possible values are: rsaSha1, unknownFutureValue.
    allowed_weak_algorithms: Optional[weak_algorithms.WeakAlgorithms] = None
    # Specifies whether signed authentication requests for this application should be required.
    is_signed_request_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequestSignatureVerification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequestSignatureVerification
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RequestSignatureVerification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import weak_algorithms

        from . import weak_algorithms

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedWeakAlgorithms": lambda n : setattr(self, 'allowed_weak_algorithms', n.get_enum_value(weak_algorithms.WeakAlgorithms)),
            "isSignedRequestRequired": lambda n : setattr(self, 'is_signed_request_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("allowedWeakAlgorithms", self.allowed_weak_algorithms)
        writer.write_bool_value("isSignedRequestRequired", self.is_signed_request_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

