from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import exact_match_job_base, exact_match_session

from . import exact_match_job_base

@dataclass
class ExactMatchSessionBase(exact_match_job_base.ExactMatchJobBase):
    odata_type = "#microsoft.graph.exactMatchSessionBase"
    # The dataStoreId property
    data_store_id: Optional[str] = None
    # The processingCompletionDateTime property
    processing_completion_date_time: Optional[datetime] = None
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
    upload_completion_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchSessionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchSessionBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.exactMatchSession":
                from . import exact_match_session

                return exact_match_session.ExactMatchSession()
        return ExactMatchSessionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import exact_match_job_base, exact_match_session

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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("dataStoreId", self.data_store_id)
        writer.write_datetime_value("processingCompletionDateTime", self.processing_completion_date_time)
        writer.write_int_value("remainingBlockCount", self.remaining_block_count)
        writer.write_int_value("remainingJobCount", self.remaining_job_count)
        writer.write_str_value("state", self.state)
        writer.write_int_value("totalBlockCount", self.total_block_count)
        writer.write_int_value("totalJobCount", self.total_job_count)
        writer.write_datetime_value("uploadCompletionDateTime", self.upload_completion_date_time)
    

