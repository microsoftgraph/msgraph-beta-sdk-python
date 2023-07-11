from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

@dataclass
class DeviceManagementPartnerAssignment(AdditionalDataHolder, Parsable):
    """
    User group targeting for Device Management Partner
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # User groups targeting for devices to be enrolled through partner.
    target: Optional[DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementPartnerAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementPartnerAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementPartnerAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(DeviceAndAppManagementAssignmentTarget)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

