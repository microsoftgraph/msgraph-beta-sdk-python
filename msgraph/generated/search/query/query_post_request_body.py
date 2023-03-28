from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import search_request

class QueryPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new queryPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The requests property
        self._requests: Optional[List[search_request.SearchRequest]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> QueryPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: QueryPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return QueryPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models import search_request

        fields: Dict[str, Callable[[Any], None]] = {
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(search_request.SearchRequest)),
        }
        return fields
    
    @property
    def requests(self,) -> Optional[List[search_request.SearchRequest]]:
        """
        Gets the requests property value. The requests property
        Returns: Optional[List[search_request.SearchRequest]]
        """
        return self._requests
    
    @requests.setter
    def requests(self,value: Optional[List[search_request.SearchRequest]] = None) -> None:
        """
        Sets the requests property value. The requests property
        Args:
            value: Value to set for the requests property.
        """
        self._requests = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("requests", self.requests)
        writer.write_additional_data_value(self.additional_data)
    

