from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class VerifiedCustomDomainCertificatesMetadata(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The expiry date of the custom domain certificate. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiry_date: Optional[datetime.datetime] = None
    # The issue date of the custom domain. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    issue_date: Optional[datetime.datetime] = None
    # The issuer name of the custom domain certificate.
    issuer_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The subject name of the custom domain certificate.
    subject_name: Optional[str] = None
    # The thumbprint associated with the custom domain certificate.
    thumbprint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerifiedCustomDomainCertificatesMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedCustomDomainCertificatesMetadata
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VerifiedCustomDomainCertificatesMetadata()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "expiryDate": lambda n : setattr(self, 'expiry_date', n.get_datetime_value()),
            "issueDate": lambda n : setattr(self, 'issue_date', n.get_datetime_value()),
            "issuerName": lambda n : setattr(self, 'issuer_name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subjectName": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("expiryDate", self.expiry_date)
        writer.write_datetime_value("issueDate", self.issue_date)
        writer.write_str_value("issuerName", self.issuer_name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_additional_data_value(self.additional_data)
    

