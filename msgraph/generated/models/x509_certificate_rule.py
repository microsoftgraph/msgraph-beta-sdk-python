from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
    from .x509_certificate_rule_type import X509CertificateRuleType

@dataclass
class X509CertificateRule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The identifier of the X.509 certificate. Required.
    identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue. Required.
    x509_certificate_authentication_mode: Optional[X509CertificateAuthenticationMode] = None
    # The type of the X.509 certificate mode configuration rule. The possible values are: issuerSubject, policyOID, unknownFutureValue. Required.
    x509_certificate_rule_type: Optional[X509CertificateRuleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> X509CertificateRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
        from .x509_certificate_rule_type import X509CertificateRuleType

        from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
        from .x509_certificate_rule_type import X509CertificateRuleType

        fields: Dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "x509CertificateAuthenticationMode": lambda n : setattr(self, 'x509_certificate_authentication_mode', n.get_enum_value(X509CertificateAuthenticationMode)),
            "x509CertificateRuleType": lambda n : setattr(self, 'x509_certificate_rule_type', n.get_enum_value(X509CertificateRuleType)),
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
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("x509CertificateAuthenticationMode", self.x509_certificate_authentication_mode)
        writer.write_enum_value("x509CertificateRuleType", self.x509_certificate_rule_type)
        writer.write_additional_data_value(self.additional_data)
    

