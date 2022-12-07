from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class GetAssignmentFiltersStatusDetailsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getAssignmentFiltersStatusDetails method.
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
    
    @property
    def assignment_filter_ids(self,) -> Optional[List[str]]:
        """
        Gets the assignmentFilterIds property value. The assignmentFilterIds property
        Returns: Optional[List[str]]
        """
        return self._assignment_filter_ids
    
    @assignment_filter_ids.setter
    def assignment_filter_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the assignmentFilterIds property value. The assignmentFilterIds property
        Args:
            value: Value to set for the assignmentFilterIds property.
        """
        self._assignment_filter_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new getAssignmentFiltersStatusDetailsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignmentFilterIds property
        self._assignment_filter_ids: Optional[List[str]] = None
        # The managedDeviceId property
        self._managed_device_id: Optional[str] = None
        # The payloadId property
        self._payload_id: Optional[str] = None
        # The skip property
        self._skip: Optional[int] = None
        # The top property
        self._top: Optional[int] = None
        # The userId property
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetAssignmentFiltersStatusDetailsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetAssignmentFiltersStatusDetailsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetAssignmentFiltersStatusDetailsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_filter_ids": lambda n : setattr(self, 'assignment_filter_ids', n.get_collection_of_primitive_values(str)),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "payload_id": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "skip": lambda n : setattr(self, 'skip', n.get_int_value()),
            "top": lambda n : setattr(self, 'top', n.get_int_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        return fields
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The managedDeviceId property
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The managedDeviceId property
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def payload_id(self,) -> Optional[str]:
        """
        Gets the payloadId property value. The payloadId property
        Returns: Optional[str]
        """
        return self._payload_id
    
    @payload_id.setter
    def payload_id(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadId property value. The payloadId property
        Args:
            value: Value to set for the payloadId property.
        """
        self._payload_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("assignmentFilterIds", self.assignment_filter_ids)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_int_value("skip", self.skip)
        writer.write_int_value("top", self.top)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def skip(self,) -> Optional[int]:
        """
        Gets the skip property value. The skip property
        Returns: Optional[int]
        """
        return self._skip
    
    @skip.setter
    def skip(self,value: Optional[int] = None) -> None:
        """
        Sets the skip property value. The skip property
        Args:
            value: Value to set for the skip property.
        """
        self._skip = value
    
    @property
    def top(self,) -> Optional[int]:
        """
        Gets the top property value. The top property
        Returns: Optional[int]
        """
        return self._top
    
    @top.setter
    def top(self,value: Optional[int] = None) -> None:
        """
        Sets the top property value. The top property
        Args:
            value: Value to set for the top property.
        """
        self._top = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The userId property
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The userId property
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

