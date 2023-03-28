from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class RunSummary(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new runSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of failed workflow runs.
        self._failed_runs: Optional[int] = None
        # The number of failed tasks of a workflow.
        self._failed_tasks: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number of successful workflow runs.
        self._successful_runs: Optional[int] = None
        # The total number of runs for a workflow.
        self._total_runs: Optional[int] = None
        # The total number of tasks processed by a workflow.
        self._total_tasks: Optional[int] = None
        # The total number of users processed by a workflow.
        self._total_users: Optional[int] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RunSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RunSummary()
    
    @property
    def failed_runs(self,) -> Optional[int]:
        """
        Gets the failedRuns property value. The number of failed workflow runs.
        Returns: Optional[int]
        """
        return self._failed_runs
    
    @failed_runs.setter
    def failed_runs(self,value: Optional[int] = None) -> None:
        """
        Sets the failedRuns property value. The number of failed workflow runs.
        Args:
            value: Value to set for the failed_runs property.
        """
        self._failed_runs = value
    
    @property
    def failed_tasks(self,) -> Optional[int]:
        """
        Gets the failedTasks property value. The number of failed tasks of a workflow.
        Returns: Optional[int]
        """
        return self._failed_tasks
    
    @failed_tasks.setter
    def failed_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the failedTasks property value. The number of failed tasks of a workflow.
        Args:
            value: Value to set for the failed_tasks property.
        """
        self._failed_tasks = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "failedRuns": lambda n : setattr(self, 'failed_runs', n.get_int_value()),
            "failedTasks": lambda n : setattr(self, 'failed_tasks', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulRuns": lambda n : setattr(self, 'successful_runs', n.get_int_value()),
            "totalRuns": lambda n : setattr(self, 'total_runs', n.get_int_value()),
            "totalTasks": lambda n : setattr(self, 'total_tasks', n.get_int_value()),
            "totalUsers": lambda n : setattr(self, 'total_users', n.get_int_value()),
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
            value: Value to set for the odata_type property.
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
        writer.write_int_value("failedRuns", self.failed_runs)
        writer.write_int_value("failedTasks", self.failed_tasks)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulRuns", self.successful_runs)
        writer.write_int_value("totalRuns", self.total_runs)
        writer.write_int_value("totalTasks", self.total_tasks)
        writer.write_int_value("totalUsers", self.total_users)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def successful_runs(self,) -> Optional[int]:
        """
        Gets the successfulRuns property value. The number of successful workflow runs.
        Returns: Optional[int]
        """
        return self._successful_runs
    
    @successful_runs.setter
    def successful_runs(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulRuns property value. The number of successful workflow runs.
        Args:
            value: Value to set for the successful_runs property.
        """
        self._successful_runs = value
    
    @property
    def total_runs(self,) -> Optional[int]:
        """
        Gets the totalRuns property value. The total number of runs for a workflow.
        Returns: Optional[int]
        """
        return self._total_runs
    
    @total_runs.setter
    def total_runs(self,value: Optional[int] = None) -> None:
        """
        Sets the totalRuns property value. The total number of runs for a workflow.
        Args:
            value: Value to set for the total_runs property.
        """
        self._total_runs = value
    
    @property
    def total_tasks(self,) -> Optional[int]:
        """
        Gets the totalTasks property value. The total number of tasks processed by a workflow.
        Returns: Optional[int]
        """
        return self._total_tasks
    
    @total_tasks.setter
    def total_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the totalTasks property value. The total number of tasks processed by a workflow.
        Args:
            value: Value to set for the total_tasks property.
        """
        self._total_tasks = value
    
    @property
    def total_users(self,) -> Optional[int]:
        """
        Gets the totalUsers property value. The total number of users processed by a workflow.
        Returns: Optional[int]
        """
        return self._total_users
    
    @total_users.setter
    def total_users(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUsers property value. The total number of users processed by a workflow.
        Args:
            value: Value to set for the total_users property.
        """
        self._total_users = value
    

