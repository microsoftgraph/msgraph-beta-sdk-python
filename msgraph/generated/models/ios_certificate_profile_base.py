from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_subject_name_format = lazy_import('msgraph.generated.models.apple_subject_name_format')
certificate_validity_period_scale = lazy_import('msgraph.generated.models.certificate_validity_period_scale')
ios_certificate_profile = lazy_import('msgraph.generated.models.ios_certificate_profile')
subject_alternative_name_type = lazy_import('msgraph.generated.models.subject_alternative_name_type')

class IosCertificateProfileBase(ios_certificate_profile.IosCertificateProfile):
    @property
    def certificate_validity_period_scale(self,) -> Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]:
        """
        Gets the certificateValidityPeriodScale property value. Certificate Validity Period Options.
        Returns: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]
        """
        return self._certificate_validity_period_scale
    
    @certificate_validity_period_scale.setter
    def certificate_validity_period_scale(self,value: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None) -> None:
        """
        Sets the certificateValidityPeriodScale property value. Certificate Validity Period Options.
        Args:
            value: Value to set for the certificateValidityPeriodScale property.
        """
        self._certificate_validity_period_scale = value
    
    @property
    def certificate_validity_period_value(self,) -> Optional[int]:
        """
        Gets the certificateValidityPeriodValue property value. Value for the Certificate Validity Period.
        Returns: Optional[int]
        """
        return self._certificate_validity_period_value
    
    @certificate_validity_period_value.setter
    def certificate_validity_period_value(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateValidityPeriodValue property value. Value for the Certificate Validity Period.
        Args:
            value: Value to set for the certificateValidityPeriodValue property.
        """
        self._certificate_validity_period_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosCertificateProfileBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosCertificateProfileBase"
        # Certificate Validity Period Options.
        self._certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
        # Value for the Certificate Validity Period.
        self._certificate_validity_period_value: Optional[int] = None
        # Certificate renewal threshold percentage. Valid values 1 to 99
        self._renewal_threshold_percentage: Optional[int] = None
        # Certificate Subject Alternative Name type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        self._subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
        # Subject Name Format Options for Apple devices.
        self._subject_name_format: Optional[apple_subject_name_format.AppleSubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosCertificateProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosCertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_validity_period_scale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificate_validity_period_value": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "renewal_threshold_percentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "subject_alternative_name_type": lambda n : setattr(self, 'subject_alternative_name_type', n.get_enum_value(subject_alternative_name_type.SubjectAlternativeNameType)),
            "subject_name_format": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(apple_subject_name_format.AppleSubjectNameFormat)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def renewal_threshold_percentage(self,) -> Optional[int]:
        """
        Gets the renewalThresholdPercentage property value. Certificate renewal threshold percentage. Valid values 1 to 99
        Returns: Optional[int]
        """
        return self._renewal_threshold_percentage
    
    @renewal_threshold_percentage.setter
    def renewal_threshold_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the renewalThresholdPercentage property value. Certificate renewal threshold percentage. Valid values 1 to 99
        Args:
            value: Value to set for the renewalThresholdPercentage property.
        """
        self._renewal_threshold_percentage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    
    @property
    def subject_alternative_name_type(self,) -> Optional[subject_alternative_name_type.SubjectAlternativeNameType]:
        """
        Gets the subjectAlternativeNameType property value. Certificate Subject Alternative Name type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        Returns: Optional[subject_alternative_name_type.SubjectAlternativeNameType]
        """
        return self._subject_alternative_name_type
    
    @subject_alternative_name_type.setter
    def subject_alternative_name_type(self,value: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None) -> None:
        """
        Sets the subjectAlternativeNameType property value. Certificate Subject Alternative Name type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        Args:
            value: Value to set for the subjectAlternativeNameType property.
        """
        self._subject_alternative_name_type = value
    
    @property
    def subject_name_format(self,) -> Optional[apple_subject_name_format.AppleSubjectNameFormat]:
        """
        Gets the subjectNameFormat property value. Subject Name Format Options for Apple devices.
        Returns: Optional[apple_subject_name_format.AppleSubjectNameFormat]
        """
        return self._subject_name_format
    
    @subject_name_format.setter
    def subject_name_format(self,value: Optional[apple_subject_name_format.AppleSubjectNameFormat] = None) -> None:
        """
        Sets the subjectNameFormat property value. Subject Name Format Options for Apple devices.
        Args:
            value: Value to set for the subjectNameFormat property.
        """
        self._subject_name_format = value
    

