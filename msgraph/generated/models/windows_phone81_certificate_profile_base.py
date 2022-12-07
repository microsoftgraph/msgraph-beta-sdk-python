from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

certificate_validity_period_scale = lazy_import('msgraph.generated.models.certificate_validity_period_scale')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
extended_key_usage = lazy_import('msgraph.generated.models.extended_key_usage')
key_storage_provider_option = lazy_import('msgraph.generated.models.key_storage_provider_option')
subject_alternative_name_type = lazy_import('msgraph.generated.models.subject_alternative_name_type')
subject_name_format = lazy_import('msgraph.generated.models.subject_name_format')

class WindowsPhone81CertificateProfileBase(device_configuration.DeviceConfiguration):
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
        Gets the certificateValidityPeriodValue property value. Value for the Certificate Validtiy Period.
        Returns: Optional[int]
        """
        return self._certificate_validity_period_value
    
    @certificate_validity_period_value.setter
    def certificate_validity_period_value(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateValidityPeriodValue property value. Value for the Certificate Validtiy Period.
        Args:
            value: Value to set for the certificateValidityPeriodValue property.
        """
        self._certificate_validity_period_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsPhone81CertificateProfileBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhone81CertificateProfileBase"
        # Certificate Validity Period Options.
        self._certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
        # Value for the Certificate Validtiy Period.
        self._certificate_validity_period_value: Optional[int] = None
        # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        self._extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
        # Key Storage Provider (KSP) Import Options.
        self._key_storage_provider: Optional[key_storage_provider_option.KeyStorageProviderOption] = None
        # Certificate renewal threshold percentage.
        self._renewal_threshold_percentage: Optional[int] = None
        # Subject Alternative Name Options.
        self._subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
        # Subject Name Format Options.
        self._subject_name_format: Optional[subject_name_format.SubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81CertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81CertificateProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhone81CertificateProfileBase()
    
    @property
    def extended_key_usages(self,) -> Optional[List[extended_key_usage.ExtendedKeyUsage]]:
        """
        Gets the extendedKeyUsages property value. Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[extended_key_usage.ExtendedKeyUsage]]
        """
        return self._extended_key_usages
    
    @extended_key_usages.setter
    def extended_key_usages(self,value: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None) -> None:
        """
        Sets the extendedKeyUsages property value. Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the extendedKeyUsages property.
        """
        self._extended_key_usages = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_validity_period_scale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificate_validity_period_value": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extended_key_usages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
            "key_storage_provider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(key_storage_provider_option.KeyStorageProviderOption)),
            "renewal_threshold_percentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "subject_alternative_name_type": lambda n : setattr(self, 'subject_alternative_name_type', n.get_enum_value(subject_alternative_name_type.SubjectAlternativeNameType)),
            "subject_name_format": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(subject_name_format.SubjectNameFormat)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key_storage_provider(self,) -> Optional[key_storage_provider_option.KeyStorageProviderOption]:
        """
        Gets the keyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Returns: Optional[key_storage_provider_option.KeyStorageProviderOption]
        """
        return self._key_storage_provider
    
    @key_storage_provider.setter
    def key_storage_provider(self,value: Optional[key_storage_provider_option.KeyStorageProviderOption] = None) -> None:
        """
        Sets the keyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Args:
            value: Value to set for the keyStorageProvider property.
        """
        self._key_storage_provider = value
    
    @property
    def renewal_threshold_percentage(self,) -> Optional[int]:
        """
        Gets the renewalThresholdPercentage property value. Certificate renewal threshold percentage.
        Returns: Optional[int]
        """
        return self._renewal_threshold_percentage
    
    @renewal_threshold_percentage.setter
    def renewal_threshold_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the renewalThresholdPercentage property value. Certificate renewal threshold percentage.
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
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    
    @property
    def subject_alternative_name_type(self,) -> Optional[subject_alternative_name_type.SubjectAlternativeNameType]:
        """
        Gets the subjectAlternativeNameType property value. Subject Alternative Name Options.
        Returns: Optional[subject_alternative_name_type.SubjectAlternativeNameType]
        """
        return self._subject_alternative_name_type
    
    @subject_alternative_name_type.setter
    def subject_alternative_name_type(self,value: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None) -> None:
        """
        Sets the subjectAlternativeNameType property value. Subject Alternative Name Options.
        Args:
            value: Value to set for the subjectAlternativeNameType property.
        """
        self._subject_alternative_name_type = value
    
    @property
    def subject_name_format(self,) -> Optional[subject_name_format.SubjectNameFormat]:
        """
        Gets the subjectNameFormat property value. Subject Name Format Options.
        Returns: Optional[subject_name_format.SubjectNameFormat]
        """
        return self._subject_name_format
    
    @subject_name_format.setter
    def subject_name_format(self,value: Optional[subject_name_format.SubjectNameFormat] = None) -> None:
        """
        Sets the subjectNameFormat property value. Subject Name Format Options.
        Args:
            value: Value to set for the subjectNameFormat property.
        """
        self._subject_name_format = value
    

