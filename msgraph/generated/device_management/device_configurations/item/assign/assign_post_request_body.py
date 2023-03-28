from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import device_configuration_assignment, device_configuration_group_assignment

class AssignPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new assignPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignments property
        self._assignments: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None
        # The deviceConfigurationGroupAssignments property
        self._device_configuration_group_assignments: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]] = None
    
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
    def assignments(self,) -> Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]:
        """
        Gets the assignments property value. The assignments property
        Returns: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The assignments property
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignPostRequestBody()
    
    @property
    def device_configuration_group_assignments(self,) -> Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]]:
        """
        Gets the deviceConfigurationGroupAssignments property value. The deviceConfigurationGroupAssignments property
        Returns: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]]
        """
        return self._device_configuration_group_assignments
    
    @device_configuration_group_assignments.setter
    def device_configuration_group_assignments(self,value: Optional[List[device_configuration_group_assignment.DeviceConfigurationGroupAssignment]] = None) -> None:
        """
        Sets the deviceConfigurationGroupAssignments property value. The deviceConfigurationGroupAssignments property
        Args:
            value: Value to set for the device_configuration_group_assignments property.
        """
        self._device_configuration_group_assignments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import device_configuration_assignment, device_configuration_group_assignment

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_configuration_assignment.DeviceConfigurationAssignment)),
            "deviceConfigurationGroupAssignments": lambda n : setattr(self, 'device_configuration_group_assignments', n.get_collection_of_object_values(device_configuration_group_assignment.DeviceConfigurationGroupAssignment)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("deviceConfigurationGroupAssignments", self.device_configuration_group_assignments)
        writer.write_additional_data_value(self.additional_data)
    

