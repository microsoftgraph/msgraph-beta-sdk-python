from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class InferenceData(AdditionalDataHolder, Parsable):
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
    def confidence_score(self,) -> Optional[float]:
        """
        Gets the confidenceScore property value. Confidence score reflecting the accuracy of the data inferred about the user.
        Returns: Optional[float]
        """
        return self._confidence_score
    
    @confidence_score.setter
    def confidence_score(self,value: Optional[float] = None) -> None:
        """
        Sets the confidenceScore property value. Confidence score reflecting the accuracy of the data inferred about the user.
        Args:
            value: Value to set for the confidenceScore property.
        """
        self._confidence_score = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new inferenceData and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Confidence score reflecting the accuracy of the data inferred about the user.
        self._confidence_score: Optional[float] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Records if the user has confirmed this inference as being True or False.
        self._user_has_verified_accuracy: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InferenceData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InferenceData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "confidence_score": lambda n : setattr(self, 'confidence_score', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_has_verified_accuracy": lambda n : setattr(self, 'user_has_verified_accuracy', n.get_bool_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_float_value("confidenceScore", self.confidence_score)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("userHasVerifiedAccuracy", self.user_has_verified_accuracy)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_has_verified_accuracy(self,) -> Optional[bool]:
        """
        Gets the userHasVerifiedAccuracy property value. Records if the user has confirmed this inference as being True or False.
        Returns: Optional[bool]
        """
        return self._user_has_verified_accuracy
    
    @user_has_verified_accuracy.setter
    def user_has_verified_accuracy(self,value: Optional[bool] = None) -> None:
        """
        Sets the userHasVerifiedAccuracy property value. Records if the user has confirmed this inference as being True or False.
        Args:
            value: Value to set for the userHasVerifiedAccuracy property.
        """
        self._user_has_verified_accuracy = value
    

