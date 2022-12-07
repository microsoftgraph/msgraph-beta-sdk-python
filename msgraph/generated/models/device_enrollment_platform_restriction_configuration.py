from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')
device_enrollment_platform_restriction = lazy_import('msgraph.generated.models.device_enrollment_platform_restriction')
enrollment_restriction_platform_type = lazy_import('msgraph.generated.models.enrollment_restriction_platform_type')

class DeviceEnrollmentPlatformRestrictionConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceEnrollmentPlatformRestrictionConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceEnrollmentPlatformRestrictionConfiguration"
        # Restrictions based on platform, platform operating system version, and device ownership
        self._platform_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # This enum indicates the platform type for which the enrollment restriction applies.
        self._platform_type: Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentPlatformRestrictionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentPlatformRestrictionConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentPlatformRestrictionConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "platform_restriction": lambda n : setattr(self, 'platform_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def platform_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the platformRestriction property value. Restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._platform_restriction
    
    @platform_restriction.setter
    def platform_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the platformRestriction property value. Restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the platformRestriction property.
        """
        self._platform_restriction = value
    
    @property
    def platform_type(self,) -> Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType]:
        """
        Gets the platformType property value. This enum indicates the platform type for which the enrollment restriction applies.
        Returns: Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType]
        """
        return self._platform_type
    
    @platform_type.setter
    def platform_type(self,value: Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType] = None) -> None:
        """
        Sets the platformType property value. This enum indicates the platform type for which the enrollment restriction applies.
        Args:
            value: Value to set for the platformType property.
        """
        self._platform_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("platformRestriction", self.platform_restriction)
        writer.write_enum_value("platformType", self.platform_type)
    

