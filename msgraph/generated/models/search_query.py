from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SearchQuery(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new searchQuery and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The search query containing the search terms. Required.
        self._query_string: Optional[str] = None
        # Provides a way to decorate the query string. Supports both KQL and query variables. Optional.
        self._query_template: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchQuery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchQuery
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchQuery()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "queryString": lambda n : setattr(self, 'query_string', n.get_str_value()),
            "queryTemplate": lambda n : setattr(self, 'query_template', n.get_str_value()),
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
    def query_string(self,) -> Optional[str]:
        """
        Gets the queryString property value. The search query containing the search terms. Required.
        Returns: Optional[str]
        """
        return self._query_string
    
    @query_string.setter
    def query_string(self,value: Optional[str] = None) -> None:
        """
        Sets the queryString property value. The search query containing the search terms. Required.
        Args:
            value: Value to set for the query_string property.
        """
        self._query_string = value
    
    @property
    def query_template(self,) -> Optional[str]:
        """
        Gets the queryTemplate property value. Provides a way to decorate the query string. Supports both KQL and query variables. Optional.
        Returns: Optional[str]
        """
        return self._query_template
    
    @query_template.setter
    def query_template(self,value: Optional[str] = None) -> None:
        """
        Sets the queryTemplate property value. Provides a way to decorate the query string. Supports both KQL and query variables. Optional.
        Args:
            value: Value to set for the query_template property.
        """
        self._query_template = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("queryString", self.query_string)
        writer.write_str_value("queryTemplate", self.query_template)
        writer.write_additional_data_value(self.additional_data)
    

