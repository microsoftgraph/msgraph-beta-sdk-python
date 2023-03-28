from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UserSummary(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new userSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of failed tasks for users in a user summary.
        self._failed_tasks: Optional[int] = None
        # The number of failed users in a user summary.
        self._failed_users: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number of successful users in a user summary.
        self._successful_users: Optional[int] = None
        # The total tasks of users in a user summary.
        self._total_tasks: Optional[int] = None
        # The total number of users in a user summary
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSummary()
    
    @property
    def failed_tasks(self,) -> Optional[int]:
        """
        Gets the failedTasks property value. The number of failed tasks for users in a user summary.
        Returns: Optional[int]
        """
        return self._failed_tasks
    
    @failed_tasks.setter
    def failed_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the failedTasks property value. The number of failed tasks for users in a user summary.
        Args:
            value: Value to set for the failed_tasks property.
        """
        self._failed_tasks = value
    
    @property
    def failed_users(self,) -> Optional[int]:
        """
        Gets the failedUsers property value. The number of failed users in a user summary.
        Returns: Optional[int]
        """
        return self._failed_users
    
    @failed_users.setter
    def failed_users(self,value: Optional[int] = None) -> None:
        """
        Sets the failedUsers property value. The number of failed users in a user summary.
        Args:
            value: Value to set for the failed_users property.
        """
        self._failed_users = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "failedTasks": lambda n : setattr(self, 'failed_tasks', n.get_int_value()),
            "failedUsers": lambda n : setattr(self, 'failed_users', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulUsers": lambda n : setattr(self, 'successful_users', n.get_int_value()),
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
        writer.write_int_value("failedTasks", self.failed_tasks)
        writer.write_int_value("failedUsers", self.failed_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulUsers", self.successful_users)
        writer.write_int_value("totalTasks", self.total_tasks)
        writer.write_int_value("totalUsers", self.total_users)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def successful_users(self,) -> Optional[int]:
        """
        Gets the successfulUsers property value. The number of successful users in a user summary.
        Returns: Optional[int]
        """
        return self._successful_users
    
    @successful_users.setter
    def successful_users(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulUsers property value. The number of successful users in a user summary.
        Args:
            value: Value to set for the successful_users property.
        """
        self._successful_users = value
    
    @property
    def total_tasks(self,) -> Optional[int]:
        """
        Gets the totalTasks property value. The total tasks of users in a user summary.
        Returns: Optional[int]
        """
        return self._total_tasks
    
    @total_tasks.setter
    def total_tasks(self,value: Optional[int] = None) -> None:
        """
        Sets the totalTasks property value. The total tasks of users in a user summary.
        Args:
            value: Value to set for the total_tasks property.
        """
        self._total_tasks = value
    
    @property
    def total_users(self,) -> Optional[int]:
        """
        Gets the totalUsers property value. The total number of users in a user summary
        Returns: Optional[int]
        """
        return self._total_users
    
    @total_users.setter
    def total_users(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUsers property value. The total number of users in a user summary
        Args:
            value: Value to set for the total_users property.
        """
        self._total_users = value
    

