from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class AssignedTrainingInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new assignedTrainingInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of users who were assigned the training in an attack simulation and training campaign.
        self._assigned_user_count: Optional[int] = None
        # Number of users who completed the training in an attack simulation and training campaign.
        self._completed_user_count: Optional[int] = None
        # Display name of the training in an attack simulation and training campaign.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @property
    def assigned_user_count(self,) -> Optional[int]:
        """
        Gets the assignedUserCount property value. Number of users who were assigned the training in an attack simulation and training campaign.
        Returns: Optional[int]
        """
        return self._assigned_user_count
    
    @assigned_user_count.setter
    def assigned_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the assignedUserCount property value. Number of users who were assigned the training in an attack simulation and training campaign.
        Args:
            value: Value to set for the assigned_user_count property.
        """
        self._assigned_user_count = value
    
    @property
    def completed_user_count(self,) -> Optional[int]:
        """
        Gets the completedUserCount property value. Number of users who completed the training in an attack simulation and training campaign.
        Returns: Optional[int]
        """
        return self._completed_user_count
    
    @completed_user_count.setter
    def completed_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completedUserCount property value. Number of users who completed the training in an attack simulation and training campaign.
        Args:
            value: Value to set for the completed_user_count property.
        """
        self._completed_user_count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedTrainingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignedTrainingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignedTrainingInfo()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the training in an attack simulation and training campaign.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the training in an attack simulation and training campaign.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "assignedUserCount": lambda n : setattr(self, 'assigned_user_count', n.get_int_value()),
            "completedUserCount": lambda n : setattr(self, 'completed_user_count', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("assignedUserCount", self.assigned_user_count)
        writer.write_int_value("completedUserCount", self.completed_user_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

