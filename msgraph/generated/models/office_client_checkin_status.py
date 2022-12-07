from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OfficeClientCheckinStatus(AdditionalDataHolder, Parsable):
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
    def applied_policies(self,) -> Optional[List[str]]:
        """
        Gets the appliedPolicies property value. List of policies delivered to the device as last checkin.
        Returns: Optional[List[str]]
        """
        return self._applied_policies
    
    @applied_policies.setter
    def applied_policies(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the appliedPolicies property value. List of policies delivered to the device as last checkin.
        Args:
            value: Value to set for the appliedPolicies property.
        """
        self._applied_policies = value
    
    @property
    def checkin_date_time(self,) -> Optional[datetime]:
        """
        Gets the checkinDateTime property value. Last device check-in time in UTC.
        Returns: Optional[datetime]
        """
        return self._checkin_date_time
    
    @checkin_date_time.setter
    def checkin_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the checkinDateTime property value. Last device check-in time in UTC.
        Args:
            value: Value to set for the checkinDateTime property.
        """
        self._checkin_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new officeClientCheckinStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of policies delivered to the device as last checkin.
        self._applied_policies: Optional[List[str]] = None
        # Last device check-in time in UTC.
        self._checkin_date_time: Optional[datetime] = None
        # Device name trying to check-in.
        self._device_name: Optional[str] = None
        # Device platform trying to check-in.
        self._device_platform: Optional[str] = None
        # Device platform version trying to check-in.
        self._device_platform_version: Optional[str] = None
        # Error message if any associated for the last checkin.
        self._error_message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # User identifier using the device.
        self._user_id: Optional[str] = None
        # User principal name using the device.
        self._user_principal_name: Optional[str] = None
        # If the last checkin was successful.
        self._was_successful: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeClientCheckinStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfficeClientCheckinStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OfficeClientCheckinStatus()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name trying to check-in.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name trying to check-in.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_platform(self,) -> Optional[str]:
        """
        Gets the devicePlatform property value. Device platform trying to check-in.
        Returns: Optional[str]
        """
        return self._device_platform
    
    @device_platform.setter
    def device_platform(self,value: Optional[str] = None) -> None:
        """
        Sets the devicePlatform property value. Device platform trying to check-in.
        Args:
            value: Value to set for the devicePlatform property.
        """
        self._device_platform = value
    
    @property
    def device_platform_version(self,) -> Optional[str]:
        """
        Gets the devicePlatformVersion property value. Device platform version trying to check-in.
        Returns: Optional[str]
        """
        return self._device_platform_version
    
    @device_platform_version.setter
    def device_platform_version(self,value: Optional[str] = None) -> None:
        """
        Sets the devicePlatformVersion property value. Device platform version trying to check-in.
        Args:
            value: Value to set for the devicePlatformVersion property.
        """
        self._device_platform_version = value
    
    @property
    def error_message(self,) -> Optional[str]:
        """
        Gets the errorMessage property value. Error message if any associated for the last checkin.
        Returns: Optional[str]
        """
        return self._error_message
    
    @error_message.setter
    def error_message(self,value: Optional[str] = None) -> None:
        """
        Sets the errorMessage property value. Error message if any associated for the last checkin.
        Args:
            value: Value to set for the errorMessage property.
        """
        self._error_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applied_policies": lambda n : setattr(self, 'applied_policies', n.get_collection_of_primitive_values(str)),
            "checkin_date_time": lambda n : setattr(self, 'checkin_date_time', n.get_datetime_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_platform": lambda n : setattr(self, 'device_platform', n.get_str_value()),
            "device_platform_version": lambda n : setattr(self, 'device_platform_version', n.get_str_value()),
            "error_message": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "was_successful": lambda n : setattr(self, 'was_successful', n.get_bool_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("appliedPolicies", self.applied_policies)
        writer.write_datetime_value("checkinDateTime", self.checkin_date_time)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("devicePlatform", self.device_platform)
        writer.write_str_value("devicePlatformVersion", self.device_platform_version)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_bool_value("wasSuccessful", self.was_successful)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User identifier using the device.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User identifier using the device.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User principal name using the device.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User principal name using the device.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def was_successful(self,) -> Optional[bool]:
        """
        Gets the wasSuccessful property value. If the last checkin was successful.
        Returns: Optional[bool]
        """
        return self._was_successful
    
    @was_successful.setter
    def was_successful(self,value: Optional[bool] = None) -> None:
        """
        Sets the wasSuccessful property value. If the last checkin was successful.
        Args:
            value: Value to set for the wasSuccessful property.
        """
        self._was_successful = value
    

