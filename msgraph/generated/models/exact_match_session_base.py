from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

exact_match_job_base = lazy_import('msgraph.generated.models.exact_match_job_base')

class ExactMatchSessionBase(exact_match_job_base.ExactMatchJobBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ExactMatchSessionBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.exactMatchSessionBase"
        # The dataStoreId property
        self._data_store_id: Optional[str] = None
        # The processingCompletionDateTime property
        self._processing_completion_date_time: Optional[datetime] = None
        # The remainingBlockCount property
        self._remaining_block_count: Optional[int] = None
        # The remainingJobCount property
        self._remaining_job_count: Optional[int] = None
        # The state property
        self._state: Optional[str] = None
        # The totalBlockCount property
        self._total_block_count: Optional[int] = None
        # The totalJobCount property
        self._total_job_count: Optional[int] = None
        # The uploadCompletionDateTime property
        self._upload_completion_date_time: Optional[datetime] = None
    
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
        return ExactMatchSessionBase()
    
    @property
    def data_store_id(self,) -> Optional[str]:
        """
        Gets the dataStoreId property value. The dataStoreId property
        Returns: Optional[str]
        """
        return self._data_store_id
    
    @data_store_id.setter
    def data_store_id(self,value: Optional[str] = None) -> None:
        """
        Sets the dataStoreId property value. The dataStoreId property
        Args:
            value: Value to set for the dataStoreId property.
        """
        self._data_store_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_store_id": lambda n : setattr(self, 'data_store_id', n.get_str_value()),
            "processing_completion_date_time": lambda n : setattr(self, 'processing_completion_date_time', n.get_datetime_value()),
            "remaining_block_count": lambda n : setattr(self, 'remaining_block_count', n.get_int_value()),
            "remaining_job_count": lambda n : setattr(self, 'remaining_job_count', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "total_block_count": lambda n : setattr(self, 'total_block_count', n.get_int_value()),
            "total_job_count": lambda n : setattr(self, 'total_job_count', n.get_int_value()),
            "upload_completion_date_time": lambda n : setattr(self, 'upload_completion_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def processing_completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the processingCompletionDateTime property value. The processingCompletionDateTime property
        Returns: Optional[datetime]
        """
        return self._processing_completion_date_time
    
    @processing_completion_date_time.setter
    def processing_completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the processingCompletionDateTime property value. The processingCompletionDateTime property
        Args:
            value: Value to set for the processingCompletionDateTime property.
        """
        self._processing_completion_date_time = value
    
    @property
    def remaining_block_count(self,) -> Optional[int]:
        """
        Gets the remainingBlockCount property value. The remainingBlockCount property
        Returns: Optional[int]
        """
        return self._remaining_block_count
    
    @remaining_block_count.setter
    def remaining_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remainingBlockCount property value. The remainingBlockCount property
        Args:
            value: Value to set for the remainingBlockCount property.
        """
        self._remaining_block_count = value
    
    @property
    def remaining_job_count(self,) -> Optional[int]:
        """
        Gets the remainingJobCount property value. The remainingJobCount property
        Returns: Optional[int]
        """
        return self._remaining_job_count
    
    @remaining_job_count.setter
    def remaining_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remainingJobCount property value. The remainingJobCount property
        Args:
            value: Value to set for the remainingJobCount property.
        """
        self._remaining_job_count = value
    
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
    
    @property
    def total_block_count(self,) -> Optional[int]:
        """
        Gets the totalBlockCount property value. The totalBlockCount property
        Returns: Optional[int]
        """
        return self._total_block_count
    
    @total_block_count.setter
    def total_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalBlockCount property value. The totalBlockCount property
        Args:
            value: Value to set for the totalBlockCount property.
        """
        self._total_block_count = value
    
    @property
    def total_job_count(self,) -> Optional[int]:
        """
        Gets the totalJobCount property value. The totalJobCount property
        Returns: Optional[int]
        """
        return self._total_job_count
    
    @total_job_count.setter
    def total_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalJobCount property value. The totalJobCount property
        Args:
            value: Value to set for the totalJobCount property.
        """
        self._total_job_count = value
    
    @property
    def upload_completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the uploadCompletionDateTime property value. The uploadCompletionDateTime property
        Returns: Optional[datetime]
        """
        return self._upload_completion_date_time
    
    @upload_completion_date_time.setter
    def upload_completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the uploadCompletionDateTime property value. The uploadCompletionDateTime property
        Args:
            value: Value to set for the uploadCompletionDateTime property.
        """
        self._upload_completion_date_time = value
    

