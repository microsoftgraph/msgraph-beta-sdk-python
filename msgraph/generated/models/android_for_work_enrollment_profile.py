from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mime_content = lazy_import('msgraph.generated.models.mime_content')

class AndroidForWorkEnrollmentProfile(entity.Entity):
    """
    Enrollment Profile used to enroll COSU devices using Google's Cloud Management.
    """
    @property
    def account_id(self,) -> Optional[str]:
        """
        Gets the accountId property value. Tenant GUID the enrollment profile belongs to.
        Returns: Optional[str]
        """
        return self._account_id
    
    @account_id.setter
    def account_id(self,value: Optional[str] = None) -> None:
        """
        Sets the accountId property value. Tenant GUID the enrollment profile belongs to.
        Args:
            value: Value to set for the accountId property.
        """
        self._account_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new androidForWorkEnrollmentProfile and sets the default values.
        """
        super().__init__()
        # Tenant GUID the enrollment profile belongs to.
        self._account_id: Optional[str] = None
        # Date time the enrollment profile was created.
        self._created_date_time: Optional[datetime] = None
        # Description for the enrollment profile.
        self._description: Optional[str] = None
        # Display name for the enrollment profile.
        self._display_name: Optional[str] = None
        # Total number of Android devices that have enrolled using this enrollment profile.
        self._enrolled_device_count: Optional[int] = None
        # Date time the enrollment profile was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # String used to generate a QR code for the token.
        self._qr_code_content: Optional[str] = None
        # String used to generate a QR code for the token.
        self._qr_code_image: Optional[mime_content.MimeContent] = None
        # Date time the most recently created token will expire.
        self._token_expiration_date_time: Optional[datetime] = None
        # Value of the most recently created token for this enrollment profile.
        self._token_value: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date time the enrollment profile was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date time the enrollment profile was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkEnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidForWorkEnrollmentProfile()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for the enrollment profile.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for the enrollment profile.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for the enrollment profile.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for the enrollment profile.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enrolled_device_count(self,) -> Optional[int]:
        """
        Gets the enrolledDeviceCount property value. Total number of Android devices that have enrolled using this enrollment profile.
        Returns: Optional[int]
        """
        return self._enrolled_device_count
    
    @enrolled_device_count.setter
    def enrolled_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the enrolledDeviceCount property value. Total number of Android devices that have enrolled using this enrollment profile.
        Args:
            value: Value to set for the enrolledDeviceCount property.
        """
        self._enrolled_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_id": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolled_device_count": lambda n : setattr(self, 'enrolled_device_count', n.get_int_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "qr_code_content": lambda n : setattr(self, 'qr_code_content', n.get_str_value()),
            "qr_code_image": lambda n : setattr(self, 'qr_code_image', n.get_object_value(mime_content.MimeContent)),
            "token_expiration_date_time": lambda n : setattr(self, 'token_expiration_date_time', n.get_datetime_value()),
            "token_value": lambda n : setattr(self, 'token_value', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date time the enrollment profile was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date time the enrollment profile was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
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
        Gets the qrCodeImage property value. String used to generate a QR code for the token.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._qr_code_image
    
    @qr_code_image.setter
    def qr_code_image(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the qrCodeImage property value. String used to generate a QR code for the token.
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
        super().serialize(writer)
        writer.write_str_value("accountId", self.account_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("enrolledDeviceCount", self.enrolled_device_count)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("qrCodeContent", self.qr_code_content)
        writer.write_object_value("qrCodeImage", self.qr_code_image)
        writer.write_datetime_value("tokenExpirationDateTime", self.token_expiration_date_time)
        writer.write_str_value("tokenValue", self.token_value)
    
    @property
    def token_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the tokenExpirationDateTime property value. Date time the most recently created token will expire.
        Returns: Optional[datetime]
        """
        return self._token_expiration_date_time
    
    @token_expiration_date_time.setter
    def token_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the tokenExpirationDateTime property value. Date time the most recently created token will expire.
        Args:
            value: Value to set for the tokenExpirationDateTime property.
        """
        self._token_expiration_date_time = value
    
    @property
    def token_value(self,) -> Optional[str]:
        """
        Gets the tokenValue property value. Value of the most recently created token for this enrollment profile.
        Returns: Optional[str]
        """
        return self._token_value
    
    @token_value.setter
    def token_value(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenValue property value. Value of the most recently created token for this enrollment profile.
        Args:
            value: Value to set for the tokenValue property.
        """
        self._token_value = value
    

