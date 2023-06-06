from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import exact_match_job_base, lookup_result_row

from . import exact_match_job_base

@dataclass
class ExactMatchLookupJob(exact_match_job_base.ExactMatchJobBase):
    odata_type = "#microsoft.graph.exactMatchLookupJob"
    # The matchingRows property
    matching_rows: Optional[List[lookup_result_row.LookupResultRow]] = None
    # The state property
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchLookupJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchLookupJob
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactMatchLookupJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import exact_match_job_base, lookup_result_row

        fields: Dict[str, Callable[[Any], None]] = {
            "matchingRows": lambda n : setattr(self, 'matching_rows', n.get_collection_of_object_values(lookup_result_row.LookupResultRow)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_collection_of_object_values("matchingRows", self.matching_rows)
        writer.write_str_value("state", self.state)
    

