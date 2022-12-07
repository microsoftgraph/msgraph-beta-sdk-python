from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_script_assignment = lazy_import('msgraph.generated.models.device_management_script_assignment')
device_management_script_group_assignment = lazy_import('msgraph.generated.models.device_management_script_group_assignment')

class AssignPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the assign method.
    """
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
        Instantiates a new assignPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceManagementScriptAssignments property
        self._device_management_script_assignments: Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]] = None
        # The deviceManagementScriptGroupAssignments property
        self._device_management_script_group_assignments: Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]] = None
    
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
    def device_management_script_assignments(self,) -> Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]]:
        """
        Gets the deviceManagementScriptAssignments property value. The deviceManagementScriptAssignments property
        Returns: Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]]
        """
        return self._device_management_script_assignments
    
    @device_management_script_assignments.setter
    def device_management_script_assignments(self,value: Optional[List[device_management_script_assignment.DeviceManagementScriptAssignment]] = None) -> None:
        """
        Sets the deviceManagementScriptAssignments property value. The deviceManagementScriptAssignments property
        Args:
            value: Value to set for the deviceManagementScriptAssignments property.
        """
        self._device_management_script_assignments = value
    
    @property
    def device_management_script_group_assignments(self,) -> Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]]:
        """
        Gets the deviceManagementScriptGroupAssignments property value. The deviceManagementScriptGroupAssignments property
        Returns: Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]]
        """
        return self._device_management_script_group_assignments
    
    @device_management_script_group_assignments.setter
    def device_management_script_group_assignments(self,value: Optional[List[device_management_script_group_assignment.DeviceManagementScriptGroupAssignment]] = None) -> None:
        """
        Sets the deviceManagementScriptGroupAssignments property value. The deviceManagementScriptGroupAssignments property
        Args:
            value: Value to set for the deviceManagementScriptGroupAssignments property.
        """
        self._device_management_script_group_assignments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_management_script_assignments": lambda n : setattr(self, 'device_management_script_assignments', n.get_collection_of_object_values(device_management_script_assignment.DeviceManagementScriptAssignment)),
            "device_management_script_group_assignments": lambda n : setattr(self, 'device_management_script_group_assignments', n.get_collection_of_object_values(device_management_script_group_assignment.DeviceManagementScriptGroupAssignment)),
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
        writer.write_collection_of_object_values("deviceManagementScriptAssignments", self.device_management_script_assignments)
        writer.write_collection_of_object_values("deviceManagementScriptGroupAssignments", self.device_management_script_group_assignments)
        writer.write_additional_data_value(self.additional_data)
    

