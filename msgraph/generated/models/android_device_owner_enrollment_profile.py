from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_enrollment_mode = lazy_import('msgraph.generated.models.android_device_owner_enrollment_mode')
android_device_owner_enrollment_token_type = lazy_import('msgraph.generated.models.android_device_owner_enrollment_token_type')
aosp_wifi_security_type = lazy_import('msgraph.generated.models.aosp_wifi_security_type')
entity = lazy_import('msgraph.generated.models.entity')
mime_content = lazy_import('msgraph.generated.models.mime_content')

class AndroidDeviceOwnerEnrollmentProfile(entity.Entity):
    """
    Enrollment Profile used to enroll Android Enterprise devices using Google's Cloud Management.
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
    
    @property
    def configure_wifi(self,) -> Optional[bool]:
        """
        Gets the configureWifi property value. Boolean that indicates that the Wi-Fi network should be configured during device provisioning. When set to TRUE, device provisioning will use Wi-Fi related properties to automatically connect to Wi-Fi networks. When set to FALSE or undefined, other Wi-Fi related properties will be ignored. Default value is TRUE. Returned by default.
        Returns: Optional[bool]
        """
        return self._configure_wifi
    
    @configure_wifi.setter
    def configure_wifi(self,value: Optional[bool] = None) -> None:
        """
        Sets the configureWifi property value. Boolean that indicates that the Wi-Fi network should be configured during device provisioning. When set to TRUE, device provisioning will use Wi-Fi related properties to automatically connect to Wi-Fi networks. When set to FALSE or undefined, other Wi-Fi related properties will be ignored. Default value is TRUE. Returned by default.
        Args:
            value: Value to set for the configureWifi property.
        """
        self._configure_wifi = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new androidDeviceOwnerEnrollmentProfile and sets the default values.
        """
        super().__init__()
        # Tenant GUID the enrollment profile belongs to.
        self._account_id: Optional[str] = None
        # Boolean that indicates that the Wi-Fi network should be configured during device provisioning. When set to TRUE, device provisioning will use Wi-Fi related properties to automatically connect to Wi-Fi networks. When set to FALSE or undefined, other Wi-Fi related properties will be ignored. Default value is TRUE. Returned by default.
        self._configure_wifi: Optional[bool] = None
        # Date time the enrollment profile was created.
        self._created_date_time: Optional[datetime] = None
        # Description for the enrollment profile.
        self._description: Optional[str] = None
        # Display name for the enrollment profile.
        self._display_name: Optional[str] = None
        # Total number of Android devices that have enrolled using this enrollment profile.
        self._enrolled_device_count: Optional[int] = None
        # The enrollment mode for an enrollment profile.
        self._enrollment_mode: Optional[android_device_owner_enrollment_mode.AndroidDeviceOwnerEnrollmentMode] = None
        # The enrollment token type for an enrollment profile.
        self._enrollment_token_type: Optional[android_device_owner_enrollment_token_type.AndroidDeviceOwnerEnrollmentTokenType] = None
        # Total number of AOSP devices that have enrolled using the current token.
        self._enrollment_token_usage_count: Optional[int] = None
        # Date time the enrollment profile was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # String used to generate a QR code for the token.
        self._qr_code_content: Optional[str] = None
        # String used to generate a QR code for the token.
        self._qr_code_image: Optional[mime_content.MimeContent] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # Date time the most recently created token was created.
        self._token_creation_date_time: Optional[datetime] = None
        # Date time the most recently created token will expire.
        self._token_expiration_date_time: Optional[datetime] = None
        # Value of the most recently created token for this enrollment profile.
        self._token_value: Optional[str] = None
        # Boolean that indicates if hidden wifi networks are enabled
        self._wifi_hidden: Optional[bool] = None
        # String that contains the wi-fi login password
        self._wifi_password: Optional[str] = None
        # This enum represents Wi-Fi Security Types for Android Device Owner AOSP Scenarios.
        self._wifi_security_type: Optional[aosp_wifi_security_type.AospWifiSecurityType] = None
        # String that contains the wi-fi login ssid
        self._wifi_ssid: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerEnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerEnrollmentProfile()
    
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
    
    @property
    def enrollment_mode(self,) -> Optional[android_device_owner_enrollment_mode.AndroidDeviceOwnerEnrollmentMode]:
        """
        Gets the enrollmentMode property value. The enrollment mode for an enrollment profile.
        Returns: Optional[android_device_owner_enrollment_mode.AndroidDeviceOwnerEnrollmentMode]
        """
        return self._enrollment_mode
    
    @enrollment_mode.setter
    def enrollment_mode(self,value: Optional[android_device_owner_enrollment_mode.AndroidDeviceOwnerEnrollmentMode] = None) -> None:
        """
        Sets the enrollmentMode property value. The enrollment mode for an enrollment profile.
        Args:
            value: Value to set for the enrollmentMode property.
        """
        self._enrollment_mode = value
    
    @property
    def enrollment_token_type(self,) -> Optional[android_device_owner_enrollment_token_type.AndroidDeviceOwnerEnrollmentTokenType]:
        """
        Gets the enrollmentTokenType property value. The enrollment token type for an enrollment profile.
        Returns: Optional[android_device_owner_enrollment_token_type.AndroidDeviceOwnerEnrollmentTokenType]
        """
        return self._enrollment_token_type
    
    @enrollment_token_type.setter
    def enrollment_token_type(self,value: Optional[android_device_owner_enrollment_token_type.AndroidDeviceOwnerEnrollmentTokenType] = None) -> None:
        """
        Sets the enrollmentTokenType property value. The enrollment token type for an enrollment profile.
        Args:
            value: Value to set for the enrollmentTokenType property.
        """
        self._enrollment_token_type = value
    
    @property
    def enrollment_token_usage_count(self,) -> Optional[int]:
        """
        Gets the enrollmentTokenUsageCount property value. Total number of AOSP devices that have enrolled using the current token.
        Returns: Optional[int]
        """
        return self._enrollment_token_usage_count
    
    @enrollment_token_usage_count.setter
    def enrollment_token_usage_count(self,value: Optional[int] = None) -> None:
        """
        Sets the enrollmentTokenUsageCount property value. Total number of AOSP devices that have enrolled using the current token.
        Args:
            value: Value to set for the enrollmentTokenUsageCount property.
        """
        self._enrollment_token_usage_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_id": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "configure_wifi": lambda n : setattr(self, 'configure_wifi', n.get_bool_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolled_device_count": lambda n : setattr(self, 'enrolled_device_count', n.get_int_value()),
            "enrollment_mode": lambda n : setattr(self, 'enrollment_mode', n.get_enum_value(android_device_owner_enrollment_mode.AndroidDeviceOwnerEnrollmentMode)),
            "enrollment_token_type": lambda n : setattr(self, 'enrollment_token_type', n.get_enum_value(android_device_owner_enrollment_token_type.AndroidDeviceOwnerEnrollmentTokenType)),
            "enrollment_token_usage_count": lambda n : setattr(self, 'enrollment_token_usage_count', n.get_int_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "qr_code_content": lambda n : setattr(self, 'qr_code_content', n.get_str_value()),
            "qr_code_image": lambda n : setattr(self, 'qr_code_image', n.get_object_value(mime_content.MimeContent)),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "token_creation_date_time": lambda n : setattr(self, 'token_creation_date_time', n.get_datetime_value()),
            "token_expiration_date_time": lambda n : setattr(self, 'token_expiration_date_time', n.get_datetime_value()),
            "token_value": lambda n : setattr(self, 'token_value', n.get_str_value()),
            "wifi_hidden": lambda n : setattr(self, 'wifi_hidden', n.get_bool_value()),
            "wifi_password": lambda n : setattr(self, 'wifi_password', n.get_str_value()),
            "wifi_security_type": lambda n : setattr(self, 'wifi_security_type', n.get_enum_value(aosp_wifi_security_type.AospWifiSecurityType)),
            "wifi_ssid": lambda n : setattr(self, 'wifi_ssid', n.get_str_value()),
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
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
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
        writer.write_bool_value("configureWifi", self.configure_wifi)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("enrolledDeviceCount", self.enrolled_device_count)
        writer.write_enum_value("enrollmentMode", self.enrollment_mode)
        writer.write_enum_value("enrollmentTokenType", self.enrollment_token_type)
        writer.write_int_value("enrollmentTokenUsageCount", self.enrollment_token_usage_count)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("qrCodeContent", self.qr_code_content)
        writer.write_object_value("qrCodeImage", self.qr_code_image)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_datetime_value("tokenCreationDateTime", self.token_creation_date_time)
        writer.write_datetime_value("tokenExpirationDateTime", self.token_expiration_date_time)
        writer.write_str_value("tokenValue", self.token_value)
        writer.write_bool_value("wifiHidden", self.wifi_hidden)
        writer.write_str_value("wifiPassword", self.wifi_password)
        writer.write_enum_value("wifiSecurityType", self.wifi_security_type)
        writer.write_str_value("wifiSsid", self.wifi_ssid)
    
    @property
    def token_creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the tokenCreationDateTime property value. Date time the most recently created token was created.
        Returns: Optional[datetime]
        """
        return self._token_creation_date_time
    
    @token_creation_date_time.setter
    def token_creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the tokenCreationDateTime property value. Date time the most recently created token was created.
        Args:
            value: Value to set for the tokenCreationDateTime property.
        """
        self._token_creation_date_time = value
    
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
    
    @property
    def wifi_hidden(self,) -> Optional[bool]:
        """
        Gets the wifiHidden property value. Boolean that indicates if hidden wifi networks are enabled
        Returns: Optional[bool]
        """
        return self._wifi_hidden
    
    @wifi_hidden.setter
    def wifi_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiHidden property value. Boolean that indicates if hidden wifi networks are enabled
        Args:
            value: Value to set for the wifiHidden property.
        """
        self._wifi_hidden = value
    
    @property
    def wifi_password(self,) -> Optional[str]:
        """
        Gets the wifiPassword property value. String that contains the wi-fi login password
        Returns: Optional[str]
        """
        return self._wifi_password
    
    @wifi_password.setter
    def wifi_password(self,value: Optional[str] = None) -> None:
        """
        Sets the wifiPassword property value. String that contains the wi-fi login password
        Args:
            value: Value to set for the wifiPassword property.
        """
        self._wifi_password = value
    
    @property
    def wifi_security_type(self,) -> Optional[aosp_wifi_security_type.AospWifiSecurityType]:
        """
        Gets the wifiSecurityType property value. This enum represents Wi-Fi Security Types for Android Device Owner AOSP Scenarios.
        Returns: Optional[aosp_wifi_security_type.AospWifiSecurityType]
        """
        return self._wifi_security_type
    
    @wifi_security_type.setter
    def wifi_security_type(self,value: Optional[aosp_wifi_security_type.AospWifiSecurityType] = None) -> None:
        """
        Sets the wifiSecurityType property value. This enum represents Wi-Fi Security Types for Android Device Owner AOSP Scenarios.
        Args:
            value: Value to set for the wifiSecurityType property.
        """
        self._wifi_security_type = value
    
    @property
    def wifi_ssid(self,) -> Optional[str]:
        """
        Gets the wifiSsid property value. String that contains the wi-fi login ssid
        Returns: Optional[str]
        """
        return self._wifi_ssid
    
    @wifi_ssid.setter
    def wifi_ssid(self,value: Optional[str] = None) -> None:
        """
        Sets the wifiSsid property value. String that contains the wi-fi login ssid
        Args:
            value: Value to set for the wifiSsid property.
        """
        self._wifi_ssid = value
    

