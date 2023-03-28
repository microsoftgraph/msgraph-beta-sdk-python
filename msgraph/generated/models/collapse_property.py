from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class CollapseProperty(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new collapseProperty and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Defines the collapse group to trim results. The properties in this collection must be sortable/refinable properties. Required.
        self._fields: Optional[List[str]] = None
        # Defines a maximum limit count for this field. This numeric value must be a positive integer. Required.
        self._limit: Optional[int] = None
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CollapseProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CollapseProperty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CollapseProperty()
    
    @property
    def fields(self,) -> Optional[List[str]]:
        """
        Gets the fields property value. Defines the collapse group to trim results. The properties in this collection must be sortable/refinable properties. Required.
        Returns: Optional[List[str]]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the fields property value. Defines the collapse group to trim results. The properties in this collection must be sortable/refinable properties. Required.
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def limit(self,) -> Optional[int]:
        """
        Gets the limit property value. Defines a maximum limit count for this field. This numeric value must be a positive integer. Required.
        Returns: Optional[int]
        """
        return self._limit
    
    @limit.setter
    def limit(self,value: Optional[int] = None) -> None:
        """
        Sets the limit property value. Defines a maximum limit count for this field. This numeric value must be a positive integer. Required.
        Args:
            value: Value to set for the limit property.
        """
        self._limit = value
    
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
        writer.write_collection_of_primitive_values("fields", self.fields)
        writer.write_int_value("limit", self.limit)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

