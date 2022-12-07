from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_collection_pagination_count_response = lazy_import('msgraph.generated.models.base_collection_pagination_count_response')
custodian = lazy_import('msgraph.generated.models.ediscovery.custodian')

class CustodianCollectionResponse(base_collection_pagination_count_response.BaseCollectionPaginationCountResponse):
    """
    Provides operations to manage the custodians property of the microsoft.graph.ediscovery.case entity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new CustodianCollectionResponse and sets the default values.
        """
        super().__init__()
        # The value property
        self._value: Optional[List[custodian.Custodian]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustodianCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustodianCollectionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustodianCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(custodian.Custodian)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("value", self.value)
    
    @property
    def value(self,) -> Optional[List[custodian.Custodian]]:
        """
        Gets the value property value. The value property
        Returns: Optional[List[custodian.Custodian]]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[List[custodian.Custodian]] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

