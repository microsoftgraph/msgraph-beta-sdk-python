from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

exact_match_job_base = lazy_import('msgraph.generated.models.exact_match_job_base')
lookup_result_row = lazy_import('msgraph.generated.models.lookup_result_row')

class ExactMatchLookupJob(exact_match_job_base.ExactMatchJobBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ExactMatchLookupJob and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.exactMatchLookupJob"
        # The matchingRows property
        self._matching_rows: Optional[List[lookup_result_row.LookupResultRow]] = None
        # The state property
        self._state: Optional[str] = None
    
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
        fields = {
            "matching_rows": lambda n : setattr(self, 'matching_rows', n.get_collection_of_object_values(lookup_result_row.LookupResultRow)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def matching_rows(self,) -> Optional[List[lookup_result_row.LookupResultRow]]:
        """
        Gets the matchingRows property value. The matchingRows property
        Returns: Optional[List[lookup_result_row.LookupResultRow]]
        """
        return self._matching_rows
    
    @matching_rows.setter
    def matching_rows(self,value: Optional[List[lookup_result_row.LookupResultRow]] = None) -> None:
        """
        Sets the matchingRows property value. The matchingRows property
        Args:
            value: Value to set for the matchingRows property.
        """
        self._matching_rows = value
    
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
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state property
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

