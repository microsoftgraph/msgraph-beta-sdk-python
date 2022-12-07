from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mac_o_s_software_update_category = lazy_import('msgraph.generated.models.mac_o_s_software_update_category')
mac_o_s_software_update_state_summary = lazy_import('msgraph.generated.models.mac_o_s_software_update_state_summary')

class MacOSSoftwareUpdateCategorySummary(entity.Entity):
    """
    MacOS software update category summary report for a device and user
    """
    def __init__(self,) -> None:
        """
        Instantiates a new macOSSoftwareUpdateCategorySummary and sets the default values.
        """
        super().__init__()
        # The device ID.
        self._device_id: Optional[str] = None
        # The name of the report
        self._display_name: Optional[str] = None
        # Number of failed updates on the device
        self._failed_update_count: Optional[int] = None
        # Last date time the report for this device was updated.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of successful updates on the device
        self._successful_update_count: Optional[int] = None
        # Number of total updates on the device
        self._total_update_count: Optional[int] = None
        # MacOS Software Update Category
        self._update_category: Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory] = None
        # Summary of the update states.
        self._update_state_summaries: Optional[List[mac_o_s_software_update_state_summary.MacOSSoftwareUpdateStateSummary]] = None
        # The user ID.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSoftwareUpdateCategorySummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateCategorySummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSSoftwareUpdateCategorySummary()
    
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
        Gets the failedUpdateCount property value. Number of failed updates on the device
        Returns: Optional[int]
        """
        return self._failed_update_count
    
    @failed_update_count.setter
    def failed_update_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedUpdateCount property value. Number of failed updates on the device
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
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "failed_update_count": lambda n : setattr(self, 'failed_update_count', n.get_int_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "successful_update_count": lambda n : setattr(self, 'successful_update_count', n.get_int_value()),
            "total_update_count": lambda n : setattr(self, 'total_update_count', n.get_int_value()),
            "update_category": lambda n : setattr(self, 'update_category', n.get_enum_value(mac_o_s_software_update_category.MacOSSoftwareUpdateCategory)),
            "update_state_summaries": lambda n : setattr(self, 'update_state_summaries', n.get_collection_of_object_values(mac_o_s_software_update_state_summary.MacOSSoftwareUpdateStateSummary)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("failedUpdateCount", self.failed_update_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_int_value("successfulUpdateCount", self.successful_update_count)
        writer.write_int_value("totalUpdateCount", self.total_update_count)
        writer.write_enum_value("updateCategory", self.update_category)
        writer.write_collection_of_object_values("updateStateSummaries", self.update_state_summaries)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def successful_update_count(self,) -> Optional[int]:
        """
        Gets the successfulUpdateCount property value. Number of successful updates on the device
        Returns: Optional[int]
        """
        return self._successful_update_count
    
    @successful_update_count.setter
    def successful_update_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulUpdateCount property value. Number of successful updates on the device
        Args:
            value: Value to set for the successfulUpdateCount property.
        """
        self._successful_update_count = value
    
    @property
    def total_update_count(self,) -> Optional[int]:
        """
        Gets the totalUpdateCount property value. Number of total updates on the device
        Returns: Optional[int]
        """
        return self._total_update_count
    
    @total_update_count.setter
    def total_update_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUpdateCount property value. Number of total updates on the device
        Args:
            value: Value to set for the totalUpdateCount property.
        """
        self._total_update_count = value
    
    @property
    def update_category(self,) -> Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory]:
        """
        Gets the updateCategory property value. MacOS Software Update Category
        Returns: Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory]
        """
        return self._update_category
    
    @update_category.setter
    def update_category(self,value: Optional[mac_o_s_software_update_category.MacOSSoftwareUpdateCategory] = None) -> None:
        """
        Sets the updateCategory property value. MacOS Software Update Category
        Args:
            value: Value to set for the updateCategory property.
        """
        self._update_category = value
    
    @property
    def update_state_summaries(self,) -> Optional[List[mac_o_s_software_update_state_summary.MacOSSoftwareUpdateStateSummary]]:
        """
        Gets the updateStateSummaries property value. Summary of the update states.
        Returns: Optional[List[mac_o_s_software_update_state_summary.MacOSSoftwareUpdateStateSummary]]
        """
        return self._update_state_summaries
    
    @update_state_summaries.setter
    def update_state_summaries(self,value: Optional[List[mac_o_s_software_update_state_summary.MacOSSoftwareUpdateStateSummary]] = None) -> None:
        """
        Sets the updateStateSummaries property value. Summary of the update states.
        Args:
            value: Value to set for the updateStateSummaries property.
        """
        self._update_state_summaries = value
    
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
    

