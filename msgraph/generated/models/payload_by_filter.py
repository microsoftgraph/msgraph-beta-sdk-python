from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import associated_assignment_payload_type, device_and_app_management_assignment_filter_type

@dataclass
class PayloadByFilter(AdditionalDataHolder, Parsable):
    """
    This entity represents a single payload with requested assignment filter Id
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Represents type of the assignment filter.
    assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
    # The Azure AD security group ID
    group_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy identifier
    payload_id: Optional[str] = None
    # This enum represents associated assignment payload type
    payload_type: Optional[associated_assignment_payload_type.AssociatedAssignmentPayloadType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PayloadByFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PayloadByFilter
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PayloadByFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import associated_assignment_payload_type, device_and_app_management_assignment_filter_type

        from . import associated_assignment_payload_type, device_and_app_management_assignment_filter_type

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentFilterType": lambda n : setattr(self, 'assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payloadId": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "payloadType": lambda n : setattr(self, 'payload_type', n.get_enum_value(associated_assignment_payload_type.AssociatedAssignmentPayloadType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("assignmentFilterType", self.assignment_filter_type)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_enum_value("payloadType", self.payload_type)
        writer.write_additional_data_value(self.additional_data)
    

