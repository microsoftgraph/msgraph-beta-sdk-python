from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class MoveAction(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new moveAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the location the item was moved from.
        self._from_: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The name of the location the item was moved to.
        self._to: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MoveAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MoveAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MoveAction()
    
    @property
    def from_(self,) -> Optional[str]:
        """
        Gets the from property value. The name of the location the item was moved from.
        Returns: Optional[str]
        """
        return self._from_
    
    @from_.setter
    def from_(self,value: Optional[str] = None) -> None:
        """
        Sets the from property value. The name of the location the item was moved from.
        Args:
            value: Value to set for the from_ property.
        """
        self._from_ = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "from": lambda n : setattr(self, 'from_', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "to": lambda n : setattr(self, 'to', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("from", self.from_)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("to", self.to)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def to(self,) -> Optional[str]:
        """
        Gets the to property value. The name of the location the item was moved to.
        Returns: Optional[str]
        """
        return self._to
    
    @to.setter
    def to(self,value: Optional[str] = None) -> None:
        """
        Sets the to property value. The name of the location the item was moved to.
        Args:
            value: Value to set for the to property.
        """
        self._to = value
    

