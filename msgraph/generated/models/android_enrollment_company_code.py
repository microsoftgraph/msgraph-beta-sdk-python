from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mime_content = lazy_import('msgraph.generated.models.mime_content')

class AndroidEnrollmentCompanyCode(AdditionalDataHolder, Parsable):
    """
    A class to hold specialty enrollment data used for enrolling via Google's Android Management API, such as Token, Url, and QR code content
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new androidEnrollmentCompanyCode and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Enrollment Token used by the User to enroll their device.
        self._enrollment_token: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # String used to generate a QR code for the token.
        self._qr_code_content: Optional[str] = None
        # Generated QR code for the token.
        self._qr_code_image: Optional[mime_content.MimeContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidEnrollmentCompanyCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidEnrollmentCompanyCode
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidEnrollmentCompanyCode()
    
    @property
    def enrollment_token(self,) -> Optional[str]:
        """
        Gets the enrollmentToken property value. Enrollment Token used by the User to enroll their device.
        Returns: Optional[str]
        """
        return self._enrollment_token
    
    @enrollment_token.setter
    def enrollment_token(self,value: Optional[str] = None) -> None:
        """
        Sets the enrollmentToken property value. Enrollment Token used by the User to enroll their device.
        Args:
            value: Value to set for the enrollmentToken property.
        """
        self._enrollment_token = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enrollment_token": lambda n : setattr(self, 'enrollment_token', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "qr_code_content": lambda n : setattr(self, 'qr_code_content', n.get_str_value()),
            "qr_code_image": lambda n : setattr(self, 'qr_code_image', n.get_object_value(mime_content.MimeContent)),
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
    def qr_code_content(self,) -> Optional[str]:
        """
        Gets the qrCodeContent property value. String used to generate a QR code for the token.
        Returns: Optional[str]
        """
        return self._qr_code_content
    
    @qr_code_content.setter
    def qr_code_content(self,value: Optional[str] = None) -> None:
        """
        Sets the qrCodeContent property value. String used to generate a QR code for the token.
        Args:
            value: Value to set for the qrCodeContent property.
        """
        self._qr_code_content = value
    
    @property
    def qr_code_image(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the qrCodeImage property value. Generated QR code for the token.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._qr_code_image
    
    @qr_code_image.setter
    def qr_code_image(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the qrCodeImage property value. Generated QR code for the token.
        Args:
            value: Value to set for the qrCodeImage property.
        """
        self._qr_code_image = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("enrollmentToken", self.enrollment_token)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qrCodeContent", self.qr_code_content)
        writer.write_object_value("qrCodeImage", self.qr_code_image)
        writer.write_additional_data_value(self.additional_data)
    

