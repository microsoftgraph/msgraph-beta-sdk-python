from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_enrollment_mode, android_device_owner_enrollment_token_type, aosp_wifi_security_type, entity, mime_content

from . import entity

@dataclass
class AndroidDeviceOwnerEnrollmentProfile(entity.Entity):
    """
    Enrollment Profile used to enroll Android Enterprise devices using Google's Cloud Management.
    """
    # Tenant GUID the enrollment profile belongs to.
    account_id: Optional[str] = None
    # Boolean that indicates that the Wi-Fi network should be configured during device provisioning. When set to TRUE, device provisioning will use Wi-Fi related properties to automatically connect to Wi-Fi networks. When set to FALSE or undefined, other Wi-Fi related properties will be ignored. Default value is TRUE. Returned by default.
    configure_wifi: Optional[bool] = None
    # Date time the enrollment profile was created.
    created_date_time: Optional[datetime] = None
    # Description for the enrollment profile.
    description: Optional[str] = None
    # Display name for the enrollment profile.
    display_name: Optional[str] = None
    # Total number of Android devices that have enrolled using this enrollment profile.
    enrolled_device_count: Optional[int] = None
    # The enrollment mode for an enrollment profile.
    enrollment_mode: Optional[android_device_owner_enrollment_mode.AndroidDeviceOwnerEnrollmentMode] = None
    # The enrollment token type for an enrollment profile.
    enrollment_token_type: Optional[android_device_owner_enrollment_token_type.AndroidDeviceOwnerEnrollmentTokenType] = None
    # Total number of AOSP devices that have enrolled using the current token.
    enrollment_token_usage_count: Optional[int] = None
    # Boolean indicating if this profile is an Android AOSP for Teams device profile.
    is_teams_device_profile: Optional[bool] = None
    # Date time the enrollment profile was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # String used to generate a QR code for the token.
    qr_code_content: Optional[str] = None
    # String used to generate a QR code for the token.
    qr_code_image: Optional[mime_content.MimeContent] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # Date time the most recently created token was created.
    token_creation_date_time: Optional[datetime] = None
    # Date time the most recently created token will expire.
    token_expiration_date_time: Optional[datetime] = None
    # Value of the most recently created token for this enrollment profile.
    token_value: Optional[str] = None
    # Boolean that indicates if hidden wifi networks are enabled
    wifi_hidden: Optional[bool] = None
    # String that contains the wi-fi login password
    wifi_password: Optional[str] = None
    # This enum represents Wi-Fi Security Types for Android Device Owner AOSP Scenarios.
    wifi_security_type: Optional[aosp_wifi_security_type.AospWifiSecurityType] = None
    # String that contains the wi-fi login ssid
    wifi_ssid: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_enrollment_mode, android_device_owner_enrollment_token_type, aosp_wifi_security_type, entity, mime_content

        fields: Dict[str, Callable[[Any], None]] = {
            "accountId": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "configureWifi": lambda n : setattr(self, 'configure_wifi', n.get_bool_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolledDeviceCount": lambda n : setattr(self, 'enrolled_device_count', n.get_int_value()),
            "enrollmentMode": lambda n : setattr(self, 'enrollment_mode', n.get_enum_value(android_device_owner_enrollment_mode.AndroidDeviceOwnerEnrollmentMode)),
            "enrollmentTokenType": lambda n : setattr(self, 'enrollment_token_type', n.get_enum_value(android_device_owner_enrollment_token_type.AndroidDeviceOwnerEnrollmentTokenType)),
            "enrollmentTokenUsageCount": lambda n : setattr(self, 'enrollment_token_usage_count', n.get_int_value()),
            "isTeamsDeviceProfile": lambda n : setattr(self, 'is_teams_device_profile', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "qrCodeContent": lambda n : setattr(self, 'qr_code_content', n.get_str_value()),
            "qrCodeImage": lambda n : setattr(self, 'qr_code_image', n.get_object_value(mime_content.MimeContent)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "tokenCreationDateTime": lambda n : setattr(self, 'token_creation_date_time', n.get_datetime_value()),
            "tokenExpirationDateTime": lambda n : setattr(self, 'token_expiration_date_time', n.get_datetime_value()),
            "tokenValue": lambda n : setattr(self, 'token_value', n.get_str_value()),
            "wifiHidden": lambda n : setattr(self, 'wifi_hidden', n.get_bool_value()),
            "wifiPassword": lambda n : setattr(self, 'wifi_password', n.get_str_value()),
            "wifiSecurityType": lambda n : setattr(self, 'wifi_security_type', n.get_enum_value(aosp_wifi_security_type.AospWifiSecurityType)),
            "wifiSsid": lambda n : setattr(self, 'wifi_ssid', n.get_str_value()),
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
        writer.write_str_value("accountId", self.account_id)
        writer.write_bool_value("configureWifi", self.configure_wifi)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("enrolledDeviceCount", self.enrolled_device_count)
        writer.write_enum_value("enrollmentMode", self.enrollment_mode)
        writer.write_enum_value("enrollmentTokenType", self.enrollment_token_type)
        writer.write_int_value("enrollmentTokenUsageCount", self.enrollment_token_usage_count)
        writer.write_bool_value("isTeamsDeviceProfile", self.is_teams_device_profile)
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
    

