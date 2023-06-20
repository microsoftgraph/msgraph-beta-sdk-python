from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_user_initiated_enrollment_type, managed_device_owner_type

@dataclass
class AppleOwnerTypeEnrollmentType(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The enrollmentType property
    enrollment_type: Optional[apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Owner type of device.
    owner_type: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleOwnerTypeEnrollmentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleOwnerTypeEnrollmentType
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppleOwnerTypeEnrollmentType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_user_initiated_enrollment_type, managed_device_owner_type

        from . import apple_user_initiated_enrollment_type, managed_device_owner_type

        fields: Dict[str, Callable[[Any], None]] = {
            "enrollmentType": lambda n : setattr(self, 'enrollment_type', n.get_enum_value(apple_user_initiated_enrollment_type.AppleUserInitiatedEnrollmentType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_enum_value(managed_device_owner_type.ManagedDeviceOwnerType)),
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
        writer.write_enum_value("enrollmentType", self.enrollment_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_additional_data_value(self.additional_data)
    

