from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_enrollment_configuration, device_enrollment_platform_restriction, enrollment_restriction_platform_type

from . import device_enrollment_configuration

@dataclass
class DeviceEnrollmentPlatformRestrictionConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    odata_type = "#microsoft.graph.deviceEnrollmentPlatformRestrictionConfiguration"
    # Restrictions based on platform, platform operating system version, and device ownership
    platform_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    # This enum indicates the platform type for which the enrollment restriction applies.
    platform_type: Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentPlatformRestrictionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentPlatformRestrictionConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceEnrollmentPlatformRestrictionConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_enrollment_configuration, device_enrollment_platform_restriction, enrollment_restriction_platform_type

        from . import device_enrollment_configuration, device_enrollment_platform_restriction, enrollment_restriction_platform_type

        fields: Dict[str, Callable[[Any], None]] = {
            "platformRestriction": lambda n : setattr(self, 'platform_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("platformRestriction", self.platform_restriction)
        writer.write_enum_value("platformType", self.platform_type)
    

