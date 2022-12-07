from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_and_app_management_assignment_filter = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter')

class ValidateFilterPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the validateFilter method.
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
        Instantiates a new validateFilterPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceAndAppManagementAssignmentFilter property
        self._device_and_app_management_assignment_filter: Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateFilterPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidateFilterPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidateFilterPostRequestBody()
    
    @property
    def device_and_app_management_assignment_filter(self,) -> Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]:
        """
        Gets the deviceAndAppManagementAssignmentFilter property value. The deviceAndAppManagementAssignmentFilter property
        Returns: Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]
        """
        return self._device_and_app_management_assignment_filter
    
    @device_and_app_management_assignment_filter.setter
    def device_and_app_management_assignment_filter(self,value: Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter] = None) -> None:
        """
        Sets the deviceAndAppManagementAssignmentFilter property value. The deviceAndAppManagementAssignmentFilter property
        Args:
            value: Value to set for the deviceAndAppManagementAssignmentFilter property.
        """
        self._device_and_app_management_assignment_filter = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_and_app_management_assignment_filter": lambda n : setattr(self, 'device_and_app_management_assignment_filter', n.get_object_value(device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter)),
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
        writer.write_object_value("deviceAndAppManagementAssignmentFilter", self.device_and_app_management_assignment_filter)
        writer.write_additional_data_value(self.additional_data)
    

