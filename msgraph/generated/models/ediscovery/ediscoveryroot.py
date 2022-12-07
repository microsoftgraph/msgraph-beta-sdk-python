from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
case = lazy_import('msgraph.generated.models.ediscovery.case')

class Ediscoveryroot(entity.Entity):
    @property
    def cases(self,) -> Optional[List[case.Case]]:
        """
        Gets the cases property value. The cases property
        Returns: Optional[List[case.Case]]
        """
        return self._cases
    
    @cases.setter
    def cases(self,value: Optional[List[case.Case]] = None) -> None:
        """
        Sets the cases property value. The cases property
        Args:
            value: Value to set for the cases property.
        """
        self._cases = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ediscoveryroot and sets the default values.
        """
        super().__init__()
        # The cases property
        self._cases: Optional[List[case.Case]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Ediscoveryroot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Ediscoveryroot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Ediscoveryroot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cases": lambda n : setattr(self, 'cases', n.get_collection_of_object_values(case.Case)),
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
        writer.write_collection_of_object_values("cases", self.cases)
    

