from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .exact_match_job_base import ExactMatchJobBase
    from .lookup_result_row import LookupResultRow

from .exact_match_job_base import ExactMatchJobBase

@dataclass
class ExactMatchLookupJob(ExactMatchJobBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.exactMatchLookupJob"
    # The matchingRows property
    matching_rows: Optional[List[LookupResultRow]] = None
    # The state property
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchLookupJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchLookupJob
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExactMatchLookupJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .exact_match_job_base import ExactMatchJobBase
        from .lookup_result_row import LookupResultRow

        from .exact_match_job_base import ExactMatchJobBase
        from .lookup_result_row import LookupResultRow

        fields: Dict[str, Callable[[Any], None]] = {
            "matchingRows": lambda n : setattr(self, 'matching_rows', n.get_collection_of_object_values(LookupResultRow)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_collection_of_object_values("matchingRows", self.matching_rows)
        writer.write_str_value("state", self.state)
    

