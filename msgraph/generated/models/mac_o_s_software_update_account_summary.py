from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mac_o_s_software_update_category_summary = lazy_import('msgraph.generated.models.mac_o_s_software_update_category_summary')

class MacOSSoftwareUpdateAccountSummary(entity.Entity):
    """
    MacOS software update account summary report for a device and user
    """
    @property
    def category_summaries(self,) -> Optional[List[mac_o_s_software_update_category_summary.MacOSSoftwareUpdateCategorySummary]]:
        """
        Gets the categorySummaries property value. Summary of the updates by category.
        Returns: Optional[List[mac_o_s_software_update_category_summary.MacOSSoftwareUpdateCategorySummary]]
        """
        return self._category_summaries
    
    @category_summaries.setter
    def category_summaries(self,value: Optional[List[mac_o_s_software_update_category_summary.MacOSSoftwareUpdateCategorySummary]] = None) -> None:
        """
        Sets the categorySummaries property value. Summary of the updates by category.
        Args:
            value: Value to set for the categorySummaries property.
        """
        self._category_summaries = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new macOSSoftwareUpdateAccountSummary and sets the default values.
        """
        super().__init__()
        # Summary of the updates by category.
        self._category_summaries: Optional[List[mac_o_s_software_update_category_summary.MacOSSoftwareUpdateCategorySummary]] = None
        # The device ID.
        self._device_id: Optional[str] = None
        # The device name.
        self._device_name: Optional[str] = None
        # The name of the report
        self._display_name: Optional[str] = None
        # Number of failed updates on the device.
        self._failed_update_count: Optional[int] = None
        # Last date time the report for this device was updated.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The OS version.
        self._os_version: Optional[str] = None
        # Number of successful updates on the device.
        self._successful_update_count: Optional[int] = None
        # Number of total updates on the device.
        self._total_update_count: Optional[int] = None
        # The user ID.
        self._user_id: Optional[str] = None
        # The user principal name
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSoftwareUpdateAccountSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateAccountSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSSoftwareUpdateAccountSummary()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The device ID.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The device ID.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the report
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the report
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def failed_update_count(self,) -> Optional[int]:
        """
        Gets the failedUpdateCount property value. Number of failed updates on the device.
        Returns: Optional[int]
        """
        return self._failed_update_count
    
    @failed_update_count.setter
    def failed_update_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedUpdateCount property value. Number of failed updates on the device.
        Args:
            value: Value to set for the failedUpdateCount property.
        """
        self._failed_update_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category_summaries": lambda n : setattr(self, 'category_summaries', n.get_collection_of_object_values(mac_o_s_software_update_category_summary.MacOSSoftwareUpdateCategorySummary)),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "failed_update_count": lambda n : setattr(self, 'failed_update_count', n.get_int_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "successful_update_count": lambda n : setattr(self, 'successful_update_count', n.get_int_value()),
            "total_update_count": lambda n : setattr(self, 'total_update_count', n.get_int_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Last date time the report for this device was updated.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Last date time the report for this device was updated.
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. The OS version.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. The OS version.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("categorySummaries", self.category_summaries)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("failedUpdateCount", self.failed_update_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_int_value("successfulUpdateCount", self.successful_update_count)
        writer.write_int_value("totalUpdateCount", self.total_update_count)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def successful_update_count(self,) -> Optional[int]:
        """
        Gets the successfulUpdateCount property value. Number of successful updates on the device.
        Returns: Optional[int]
        """
        return self._successful_update_count
    
    @successful_update_count.setter
    def successful_update_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulUpdateCount property value. Number of successful updates on the device.
        Args:
            value: Value to set for the successfulUpdateCount property.
        """
        self._successful_update_count = value
    
    @property
    def total_update_count(self,) -> Optional[int]:
        """
        Gets the totalUpdateCount property value. Number of total updates on the device.
        Returns: Optional[int]
        """
        return self._total_update_count
    
    @total_update_count.setter
    def total_update_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUpdateCount property value. Number of total updates on the device.
        Args:
            value: Value to set for the totalUpdateCount property.
        """
        self._total_update_count = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The user ID.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user ID.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

