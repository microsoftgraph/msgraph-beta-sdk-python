from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

query_type = lazy_import('msgraph.generated.models.security.query_type')

class EventQuery(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new eventQuery and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The query property
        self._query: Optional[str] = None
        # The queryType property
        self._query_type: Optional[query_type.QueryType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventQuery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventQuery
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EventQuery()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "query_type": lambda n : setattr(self, 'query_type', n.get_enum_value(query_type.QueryType)),
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
    
    @property
    def query(self,) -> Optional[str]:
        """
        Gets the query property value. The query property
        Returns: Optional[str]
        """
        return self._query
    
    @query.setter
    def query(self,value: Optional[str] = None) -> None:
        """
        Sets the query property value. The query property
        Args:
            value: Value to set for the query property.
        """
        self._query = value
    
    @property
    def query_type(self,) -> Optional[query_type.QueryType]:
        """
        Gets the queryType property value. The queryType property
        Returns: Optional[query_type.QueryType]
        """
        return self._query_type
    
    @query_type.setter
    def query_type(self,value: Optional[query_type.QueryType] = None) -> None:
        """
        Sets the queryType property value. The queryType property
        Args:
            value: Value to set for the queryType property.
        """
        self._query_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("query", self.query)
        writer.write_enum_value("queryType", self.query_type)
        writer.write_additional_data_value(self.additional_data)
    

