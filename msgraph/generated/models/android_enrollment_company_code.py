from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mime_content import MimeContent

@dataclass
class AndroidEnrollmentCompanyCode(AdditionalDataHolder, BackedModel, Parsable):
    """
    A class to hold specialty enrollment data used for enrolling via Google's Android Management API, such as Token, Url, and QR code content
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Enrollment Token used by the User to enroll their device.
    enrollment_token: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # String used to generate a QR code for the token.
    qr_code_content: Optional[str] = None
    # Generated QR code for the token.
    qr_code_image: Optional[MimeContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidEnrollmentCompanyCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidEnrollmentCompanyCode
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidEnrollmentCompanyCode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mime_content import MimeContent

        from .mime_content import MimeContent

        fields: Dict[str, Callable[[Any], None]] = {
            "enrollmentToken": lambda n : setattr(self, 'enrollment_token', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "qrCodeContent": lambda n : setattr(self, 'qr_code_content', n.get_str_value()),
            "qrCodeImage": lambda n : setattr(self, 'qr_code_image', n.get_object_value(MimeContent)),
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
        writer.write_str_value("enrollmentToken", self.enrollment_token)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("qrCodeContent", self.qr_code_content)
        writer.write_object_value("qrCodeImage", self.qr_code_image)
        writer.write_additional_data_value(self.additional_data)
    

