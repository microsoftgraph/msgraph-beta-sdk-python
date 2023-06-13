from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, ios_edu_certificate_settings

from . import device_configuration

@dataclass
class IosEduDeviceConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.iosEduDeviceConfiguration"
    # The Trusted Root and PFX certificates for Device
    device_certificate_settings: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None
    # The Trusted Root and PFX certificates for Student
    student_certificate_settings: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None
    # Trusted Root and PFX certificates for iOS EDU.
    teacher_certificate_settings: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosEduDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosEduDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosEduDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, ios_edu_certificate_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCertificateSettings": lambda n : setattr(self, 'device_certificate_settings', n.get_object_value(ios_edu_certificate_settings.IosEduCertificateSettings)),
            "studentCertificateSettings": lambda n : setattr(self, 'student_certificate_settings', n.get_object_value(ios_edu_certificate_settings.IosEduCertificateSettings)),
            "teacherCertificateSettings": lambda n : setattr(self, 'teacher_certificate_settings', n.get_object_value(ios_edu_certificate_settings.IosEduCertificateSettings)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("deviceCertificateSettings", self.device_certificate_settings)
        writer.write_object_value("studentCertificateSettings", self.student_certificate_settings)
        writer.write_object_value("teacherCertificateSettings", self.teacher_certificate_settings)
    

