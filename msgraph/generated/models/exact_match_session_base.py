from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .exact_match_job_base import ExactMatchJobBase
    from .exact_match_session import ExactMatchSession

from .exact_match_job_base import ExactMatchJobBase

@dataclass
class ExactMatchSessionBase(ExactMatchJobBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.exactMatchSessionBase"
    # The dataStoreId property
    data_store_id: Optional[str] = None
    # The processingCompletionDateTime property
    processing_completion_date_time: Optional[datetime.datetime] = None
    # The remainingBlockCount property
    remaining_block_count: Optional[int] = None
    # The remainingJobCount property
    remaining_job_count: Optional[int] = None
    # The state property
    state: Optional[str] = None
    # The totalBlockCount property
    total_block_count: Optional[int] = None
    # The totalJobCount property
    total_job_count: Optional[int] = None
    # The uploadCompletionDateTime property
    upload_completion_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchSessionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchSessionBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchSession".casefold():
            from .exact_match_session import ExactMatchSession

            return ExactMatchSession()
        return ExactMatchSessionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .exact_match_job_base import ExactMatchJobBase
        from .exact_match_session import ExactMatchSession

        from .exact_match_job_base import ExactMatchJobBase
        from .exact_match_session import ExactMatchSession

        fields: Dict[str, Callable[[Any], None]] = {
            "dataStoreId": lambda n : setattr(self, 'data_store_id', n.get_str_value()),
            "processingCompletionDateTime": lambda n : setattr(self, 'processing_completion_date_time', n.get_datetime_value()),
            "remainingBlockCount": lambda n : setattr(self, 'remaining_block_count', n.get_int_value()),
            "remainingJobCount": lambda n : setattr(self, 'remaining_job_count', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "totalBlockCount": lambda n : setattr(self, 'total_block_count', n.get_int_value()),
            "totalJobCount": lambda n : setattr(self, 'total_job_count', n.get_int_value()),
            "uploadCompletionDateTime": lambda n : setattr(self, 'upload_completion_date_time', n.get_datetime_value()),
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
        writer.write_str_value("dataStoreId", self.data_store_id)
        writer.write_datetime_value("processingCompletionDateTime", self.processing_completion_date_time)
        writer.write_int_value("remainingBlockCount", self.remaining_block_count)
        writer.write_int_value("remainingJobCount", self.remaining_job_count)
        writer.write_str_value("state", self.state)
        writer.write_int_value("totalBlockCount", self.total_block_count)
        writer.write_int_value("totalJobCount", self.total_job_count)
        writer.write_datetime_value("uploadCompletionDateTime", self.upload_completion_date_time)
    

