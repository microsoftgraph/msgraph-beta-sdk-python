from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ControlScore(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new controlScore and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The controlCategory property
        self._control_category: Optional[str] = None
        # The controlName property
        self._control_name: Optional[str] = None
        # The description property
        self._description: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The score property
        self._score: Optional[float] = None
    
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
    def control_category(self,) -> Optional[str]:
        """
        Gets the controlCategory property value. The controlCategory property
        Returns: Optional[str]
        """
        return self._control_category
    
    @control_category.setter
    def control_category(self,value: Optional[str] = None) -> None:
        """
        Sets the controlCategory property value. The controlCategory property
        Args:
            value: Value to set for the control_category property.
        """
        self._control_category = value
    
    @property
    def control_name(self,) -> Optional[str]:
        """
        Gets the controlName property value. The controlName property
        Returns: Optional[str]
        """
        return self._control_name
    
    @control_name.setter
    def control_name(self,value: Optional[str] = None) -> None:
        """
        Sets the controlName property value. The controlName property
        Args:
            value: Value to set for the control_name property.
        """
        self._control_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ControlScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ControlScore
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ControlScore()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "controlCategory": lambda n : setattr(self, 'control_category', n.get_str_value()),
            "controlName": lambda n : setattr(self, 'control_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "score": lambda n : setattr(self, 'score', n.get_float_value()),
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
    def score(self,) -> Optional[float]:
        """
        Gets the score property value. The score property
        Returns: Optional[float]
        """
        return self._score
    
    @score.setter
    def score(self,value: Optional[float] = None) -> None:
        """
        Sets the score property value. The score property
        Args:
            value: Value to set for the score property.
        """
        self._score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("controlCategory", self.control_category)
        writer.write_str_value("controlName", self.control_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("score", self.score)
        writer.write_additional_data_value(self.additional_data)
    

