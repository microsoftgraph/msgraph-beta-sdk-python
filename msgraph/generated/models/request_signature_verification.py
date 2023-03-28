from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import weak_algorithms

class RequestSignatureVerification(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new requestSignatureVerification and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether this application accepts weak algorithms.  The possible values are: rsaSha1, unknownFutureValue.
        self._allowed_weak_algorithms: Optional[weak_algorithms.WeakAlgorithms] = None
        # Specifies whether signed authentication requests for this application should be required.
        self._is_signed_request_required: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def allowed_weak_algorithms(self,) -> Optional[weak_algorithms.WeakAlgorithms]:
        """
        Gets the allowedWeakAlgorithms property value. Specifies whether this application accepts weak algorithms.  The possible values are: rsaSha1, unknownFutureValue.
        Returns: Optional[weak_algorithms.WeakAlgorithms]
        """
        return self._allowed_weak_algorithms
    
    @allowed_weak_algorithms.setter
    def allowed_weak_algorithms(self,value: Optional[weak_algorithms.WeakAlgorithms] = None) -> None:
        """
        Sets the allowedWeakAlgorithms property value. Specifies whether this application accepts weak algorithms.  The possible values are: rsaSha1, unknownFutureValue.
        Args:
            value: Value to set for the allowed_weak_algorithms property.
        """
        self._allowed_weak_algorithms = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequestSignatureVerification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequestSignatureVerification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RequestSignatureVerification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import weak_algorithms

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedWeakAlgorithms": lambda n : setattr(self, 'allowed_weak_algorithms', n.get_enum_value(weak_algorithms.WeakAlgorithms)),
            "isSignedRequestRequired": lambda n : setattr(self, 'is_signed_request_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_signed_request_required(self,) -> Optional[bool]:
        """
        Gets the isSignedRequestRequired property value. Specifies whether signed authentication requests for this application should be required.
        Returns: Optional[bool]
        """
        return self._is_signed_request_required
    
    @is_signed_request_required.setter
    def is_signed_request_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSignedRequestRequired property value. Specifies whether signed authentication requests for this application should be required.
        Args:
            value: Value to set for the is_signed_request_required property.
        """
        self._is_signed_request_required = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("allowedWeakAlgorithms", self.allowed_weak_algorithms)
        writer.write_bool_value("isSignedRequestRequired", self.is_signed_request_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

