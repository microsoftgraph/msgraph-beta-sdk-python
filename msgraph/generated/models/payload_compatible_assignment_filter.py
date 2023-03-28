from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assignment_filter_payload_type, device_and_app_management_assignment_filter

from . import device_and_app_management_assignment_filter

class PayloadCompatibleAssignmentFilter(device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter):
    def __init__(self,) -> None:
        """
        Instantiates a new PayloadCompatibleAssignmentFilter and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.payloadCompatibleAssignmentFilter"
        # Represents the payload type AssignmentFilter is being assigned to.
        self._payload_type: Optional[assignment_filter_payload_type.AssignmentFilterPayloadType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PayloadCompatibleAssignmentFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PayloadCompatibleAssignmentFilter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PayloadCompatibleAssignmentFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import assignment_filter_payload_type, device_and_app_management_assignment_filter

        fields: Dict[str, Callable[[Any], None]] = {
            "payloadType": lambda n : setattr(self, 'payload_type', n.get_enum_value(assignment_filter_payload_type.AssignmentFilterPayloadType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def payload_type(self,) -> Optional[assignment_filter_payload_type.AssignmentFilterPayloadType]:
        """
        Gets the payloadType property value. Represents the payload type AssignmentFilter is being assigned to.
        Returns: Optional[assignment_filter_payload_type.AssignmentFilterPayloadType]
        """
        return self._payload_type
    
    @payload_type.setter
    def payload_type(self,value: Optional[assignment_filter_payload_type.AssignmentFilterPayloadType] = None) -> None:
        """
        Sets the payloadType property value. Represents the payload type AssignmentFilter is being assigned to.
        Args:
            value: Value to set for the payload_type property.
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
        super().serialize(writer)
        writer.write_enum_value("payloadType", self.payload_type)
    

