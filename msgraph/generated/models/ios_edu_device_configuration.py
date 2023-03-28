from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, ios_edu_certificate_settings

from . import device_configuration

class IosEduDeviceConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new IosEduDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosEduDeviceConfiguration"
        # The Trusted Root and PFX certificates for Device
        self._device_certificate_settings: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None
        # The Trusted Root and PFX certificates for Student
        self._student_certificate_settings: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None
        # Trusted Root and PFX certificates for iOS EDU.
        self._teacher_certificate_settings: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None
    
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
    
    @property
    def device_certificate_settings(self,) -> Optional[ios_edu_certificate_settings.IosEduCertificateSettings]:
        """
        Gets the deviceCertificateSettings property value. The Trusted Root and PFX certificates for Device
        Returns: Optional[ios_edu_certificate_settings.IosEduCertificateSettings]
        """
        return self._device_certificate_settings
    
    @device_certificate_settings.setter
    def device_certificate_settings(self,value: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None) -> None:
        """
        Sets the deviceCertificateSettings property value. The Trusted Root and PFX certificates for Device
        Args:
            value: Value to set for the device_certificate_settings property.
        """
        self._device_certificate_settings = value
    
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
    
    @property
    def student_certificate_settings(self,) -> Optional[ios_edu_certificate_settings.IosEduCertificateSettings]:
        """
        Gets the studentCertificateSettings property value. The Trusted Root and PFX certificates for Student
        Returns: Optional[ios_edu_certificate_settings.IosEduCertificateSettings]
        """
        return self._student_certificate_settings
    
    @student_certificate_settings.setter
    def student_certificate_settings(self,value: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None) -> None:
        """
        Sets the studentCertificateSettings property value. The Trusted Root and PFX certificates for Student
        Args:
            value: Value to set for the student_certificate_settings property.
        """
        self._student_certificate_settings = value
    
    @property
    def teacher_certificate_settings(self,) -> Optional[ios_edu_certificate_settings.IosEduCertificateSettings]:
        """
        Gets the teacherCertificateSettings property value. Trusted Root and PFX certificates for iOS EDU.
        Returns: Optional[ios_edu_certificate_settings.IosEduCertificateSettings]
        """
        return self._teacher_certificate_settings
    
    @teacher_certificate_settings.setter
    def teacher_certificate_settings(self,value: Optional[ios_edu_certificate_settings.IosEduCertificateSettings] = None) -> None:
        """
        Sets the teacherCertificateSettings property value. Trusted Root and PFX certificates for iOS EDU.
        Args:
            value: Value to set for the teacher_certificate_settings property.
        """
        self._teacher_certificate_settings = value
    

