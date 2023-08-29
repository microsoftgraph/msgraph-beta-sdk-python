from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ediscovery_custodian import EdiscoveryCustodian
    from .ediscovery_review_tag import EdiscoveryReviewTag
    from .file import File

from .file import File

@dataclass
class EdiscoveryFile(File):
    # Custodians associated with the file.
    custodian: Optional[EdiscoveryCustodian] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Tags associated with the file.
    tags: Optional[List[EdiscoveryReviewTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryFile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ediscovery_custodian import EdiscoveryCustodian
        from .ediscovery_review_tag import EdiscoveryReviewTag
        from .file import File

        from .ediscovery_custodian import EdiscoveryCustodian
        from .ediscovery_review_tag import EdiscoveryReviewTag
        from .file import File

        fields: Dict[str, Callable[[Any], None]] = {
            "custodian": lambda n : setattr(self, 'custodian', n.get_object_value(EdiscoveryCustodian)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(EdiscoveryReviewTag)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("custodian", self.custodian)
        writer.write_collection_of_object_values("tags", self.tags)
    

