from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

associated_assignment_payload_type = lazy_import('msgraph.generated.models.associated_assignment_payload_type')
device_and_app_management_assignment_filter_type = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter_type')

class PayloadByFilter(AdditionalDataHolder, Parsable):
    """
    This entity represents a single payload with requested assignment filter Id
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
    def assignment_filter_type(self,) -> Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]:
        """
        Gets the assignmentFilterType property value. Represents type of the assignment filter.
        Returns: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]
        """
        return self._assignment_filter_type
    
    @assignment_filter_type.setter
    def assignment_filter_type(self,value: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None) -> None:
        """
        Sets the assignmentFilterType property value. Represents type of the assignment filter.
        Args:
            value: Value to set for the assignmentFilterType property.
        """
        self._assignment_filter_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new payloadByFilter and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents type of the assignment filter.
        self._assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
        # The Azure AD security group ID
        self._group_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The policy identifier
        self._payload_id: Optional[str] = None
        # This enum represents associated assignment payload type
        self._payload_type: Optional[associated_assignment_payload_type.AssociatedAssignmentPayloadType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PayloadByFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PayloadByFilter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PayloadByFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_filter_type": lambda n : setattr(self, 'assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "group_id": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payload_id": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "payload_type": lambda n : setattr(self, 'payload_type', n.get_enum_value(associated_assignment_payload_type.AssociatedAssignmentPayloadType)),
        }
        return fields
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The Azure AD security group ID
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The Azure AD security group ID
        Args:
            value: Value to set for the groupId property.
        """
        self._group_id = value
    
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
    
    @property
    def payload_id(self,) -> Optional[str]:
        """
        Gets the payloadId property value. The policy identifier
        Returns: Optional[str]
        """
        return self._payload_id
    
    @payload_id.setter
    def payload_id(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadId property value. The policy identifier
        Args:
            value: Value to set for the payloadId property.
        """
        self._payload_id = value
    
    @property
    def payload_type(self,) -> Optional[associated_assignment_payload_type.AssociatedAssignmentPayloadType]:
        """
        Gets the payloadType property value. This enum represents associated assignment payload type
        Returns: Optional[associated_assignment_payload_type.AssociatedAssignmentPayloadType]
        """
        return self._payload_type
    
    @payload_type.setter
    def payload_type(self,value: Optional[associated_assignment_payload_type.AssociatedAssignmentPayloadType] = None) -> None:
        """
        Sets the payloadType property value. This enum represents associated assignment payload type
        Args:
            value: Value to set for the payloadType property.
        """
        self._payload_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("assignmentFilterType", self.assignment_filter_type)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_enum_value("payloadType", self.payload_type)
        writer.write_additional_data_value(self.additional_data)
    

