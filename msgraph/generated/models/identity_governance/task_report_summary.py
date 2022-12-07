from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TaskReportSummary(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new taskReportSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of failed tasks in a report.
        self._failed_tasks: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The total number of successful tasks in a report.
        self._successful_tasks: Optional[int] = None
        # The total number of tasks in a report.
        self._total_tasks: Optional[int] = None
        # The number of unprocessed tasks in a report.
        self._unprocessed_tasks: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TaskReportSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TaskReportSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TaskReportSummary()
    
    @property
    def failed_tasks(self,) -> Optional[int]:
        """
        Gets the failedTasks property value. The number of failed tasks in a report.
        Returns: Optional[int]
        """
        return self._failed_tasks
    
    @failed_tasks.setter
    def failed_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the failedTasks property value. The number of failed tasks in a report.
        Args:
            value: Value to set for the failedTasks property.
        """
        self._failed_tasks = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "failed_tasks": lambda n : setattr(self, 'failed_tasks', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successful_tasks": lambda n : setattr(self, 'successful_tasks', n.get_int_value()),
            "total_tasks": lambda n : setattr(self, 'total_tasks', n.get_int_value()),
            "unprocessed_tasks": lambda n : setattr(self, 'unprocessed_tasks', n.get_int_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("failedTasks", self.failed_tasks)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulTasks", self.successful_tasks)
        writer.write_int_value("totalTasks", self.total_tasks)
        writer.write_int_value("unprocessedTasks", self.unprocessed_tasks)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def successful_tasks(self,) -> Optional[int]:
        """
        Gets the successfulTasks property value. The total number of successful tasks in a report.
        Returns: Optional[int]
        """
        return self._successful_tasks
    
    @successful_tasks.setter
    def successful_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulTasks property value. The total number of successful tasks in a report.
        Args:
            value: Value to set for the successfulTasks property.
        """
        self._successful_tasks = value
    
    @property
    def total_tasks(self,) -> Optional[int]:
        """
        Gets the totalTasks property value. The total number of tasks in a report.
        Returns: Optional[int]
        """
        return self._total_tasks
    
    @total_tasks.setter
    def total_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the totalTasks property value. The total number of tasks in a report.
        Args:
            value: Value to set for the totalTasks property.
        """
        self._total_tasks = value
    
    @property
    def unprocessed_tasks(self,) -> Optional[int]:
        """
        Gets the unprocessedTasks property value. The number of unprocessed tasks in a report.
        Returns: Optional[int]
        """
        return self._unprocessed_tasks
    
    @unprocessed_tasks.setter
    def unprocessed_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the unprocessedTasks property value. The number of unprocessed tasks in a report.
        Args:
            value: Value to set for the unprocessedTasks property.
        """
        self._unprocessed_tasks = value
    

