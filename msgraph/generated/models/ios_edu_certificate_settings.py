from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

certificate_validity_period_scale = lazy_import('msgraph.generated.models.certificate_validity_period_scale')

class IosEduCertificateSettings(AdditionalDataHolder, Parsable):
    """
    Trusted Root and PFX certificates for iOS EDU.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def cert_file_name(self,) -> Optional[str]:
        """
        Gets the certFileName property value. File name to display in UI.
        Returns: Optional[str]
        """
        return self._cert_file_name
    
    @cert_file_name.setter
    def cert_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certFileName property value. File name to display in UI.
        Args:
            value: Value to set for the certFileName property.
        """
        self._cert_file_name = value
    
    @property
    def certificate_template_name(self,) -> Optional[str]:
        """
        Gets the certificateTemplateName property value. PKCS Certificate Template Name.
        Returns: Optional[str]
        """
        return self._certificate_template_name
    
    @certificate_template_name.setter
    def certificate_template_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateTemplateName property value. PKCS Certificate Template Name.
        Args:
            value: Value to set for the certificateTemplateName property.
        """
        self._certificate_template_name = value
    
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
    
    @property
    def certification_authority(self,) -> Optional[str]:
        """
        Gets the certificationAuthority property value. PKCS Certification Authority.
        Returns: Optional[str]
        """
        return self._certification_authority
    
    @certification_authority.setter
    def certification_authority(self,value: Optional[str] = None) -> None:
        """
        Sets the certificationAuthority property value. PKCS Certification Authority.
        Args:
            value: Value to set for the certificationAuthority property.
        """
        self._certification_authority = value
    
    @property
    def certification_authority_name(self,) -> Optional[str]:
        """
        Gets the certificationAuthorityName property value. PKCS Certification Authority Name.
        Returns: Optional[str]
        """
        return self._certification_authority_name
    
    @certification_authority_name.setter
    def certification_authority_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certificationAuthorityName property value. PKCS Certification Authority Name.
        Args:
            value: Value to set for the certificationAuthorityName property.
        """
        self._certification_authority_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosEduCertificateSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # File name to display in UI.
        self._cert_file_name: Optional[str] = None
        # PKCS Certificate Template Name.
        self._certificate_template_name: Optional[str] = None
        # Certificate Validity Period Options.
        self._certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
        # Value for the Certificate Validity Period.
        self._certificate_validity_period_value: Optional[int] = None
        # PKCS Certification Authority.
        self._certification_authority: Optional[str] = None
        # PKCS Certification Authority Name.
        self._certification_authority_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Certificate renewal threshold percentage. Valid values 1 to 99
        self._renewal_threshold_percentage: Optional[int] = None
        # Trusted Root Certificate.
        self._trusted_root_certificate: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosEduCertificateSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosEduCertificateSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosEduCertificateSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cert_file_name": lambda n : setattr(self, 'cert_file_name', n.get_str_value()),
            "certificate_template_name": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certificate_validity_period_scale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificate_validity_period_value": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "certification_authority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certification_authority_name": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "renewal_threshold_percentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "trusted_root_certificate": lambda n : setattr(self, 'trusted_root_certificate', n.get_bytes_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
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
        writer.write_str_value("certFileName", self.cert_file_name)
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_object_value("trustedRootCertificate", self.trusted_root_certificate)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def trusted_root_certificate(self,) -> Optional[bytes]:
        """
        Gets the trustedRootCertificate property value. Trusted Root Certificate.
        Returns: Optional[bytes]
        """
        return self._trusted_root_certificate
    
    @trusted_root_certificate.setter
    def trusted_root_certificate(self,value: Optional[bytes] = None) -> None:
        """
        Sets the trustedRootCertificate property value. Trusted Root Certificate.
        Args:
            value: Value to set for the trustedRootCertificate property.
        """
        self._trusted_root_certificate = value
    

