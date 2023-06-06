from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ediscovery_custodian, ediscovery_review_tag, file

from . import file

@dataclass
class EdiscoveryFile(file.File):
    # Custodians associated with the file.
    custodian: Optional[ediscovery_custodian.EdiscoveryCustodian] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Tags associated with the file.
    tags: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ediscovery_custodian, ediscovery_review_tag, file

        fields: Dict[str, Callable[[Any], None]] = {
            "custodian": lambda n : setattr(self, 'custodian', n.get_object_value(ediscovery_custodian.EdiscoveryCustodian)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(ediscovery_review_tag.EdiscoveryReviewTag)),
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
        writer.write_object_value("custodian", self.custodian)
        writer.write_collection_of_object_values("tags", self.tags)
    

