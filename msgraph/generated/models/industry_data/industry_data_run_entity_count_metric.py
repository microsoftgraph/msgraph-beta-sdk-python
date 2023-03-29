from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class IndustryDataRunEntityCountMetric(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new industryDataRunEntityCountMetric and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The count of entries for the entity marked as Active.
        self._active: Optional[int] = None
        # The count of entries for the entity marked as Inactive.
        self._inactive: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total count of the entity.
        self._total: Optional[int] = None
    
    @property
    def active(self,) -> Optional[int]:
        """
        Gets the active property value. The count of entries for the entity marked as Active.
        Returns: Optional[int]
        """
        return self._active
    
    @active.setter
    def active(self,value: Optional[int] = None) -> None:
        """
        Sets the active property value. The count of entries for the entity marked as Active.
        Args:
            value: Value to set for the active property.
        """
        self._active = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataRunEntityCountMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRunEntityCountMetric
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IndustryDataRunEntityCountMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_int_value()),
            "inactive": lambda n : setattr(self, 'inactive', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
        }
        return fields
    
    @property
    def inactive(self,) -> Optional[int]:
        """
        Gets the inactive property value. The count of entries for the entity marked as Inactive.
        Returns: Optional[int]
        """
        return self._inactive
    
    @inactive.setter
    def inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the inactive property value. The count of entries for the entity marked as Inactive.
        Args:
            value: Value to set for the inactive property.
        """
        self._inactive = value
    
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total(self,) -> Optional[int]:
        """
        Gets the total property value. Total count of the entity.
        Returns: Optional[int]
        """
        return self._total
    
    @total.setter
    def total(self,value: Optional[int] = None) -> None:
        """
        Sets the total property value. Total count of the entity.
        Args:
            value: Value to set for the total property.
        """
        self._total = value
    

