from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

driver_approval_status = lazy_import('msgraph.generated.models.driver_approval_status')
driver_category = lazy_import('msgraph.generated.models.driver_category')
entity = lazy_import('msgraph.generated.models.entity')

class WindowsDriverUpdateInventory(entity.Entity):
    """
    A new entity to represent driver inventories.
    """
    @property
    def applicable_device_count(self,) -> Optional[int]:
        """
        Gets the applicableDeviceCount property value. The number of devices for which this driver is applicable.
        Returns: Optional[int]
        """
        return self._applicable_device_count
    
    @applicable_device_count.setter
    def applicable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the applicableDeviceCount property value. The number of devices for which this driver is applicable.
        Args:
            value: Value to set for the applicableDeviceCount property.
        """
        self._applicable_device_count = value
    
    @property
    def approval_status(self,) -> Optional[driver_approval_status.DriverApprovalStatus]:
        """
        Gets the approvalStatus property value. An enum type to represent approval status of a driver.
        Returns: Optional[driver_approval_status.DriverApprovalStatus]
        """
        return self._approval_status
    
    @approval_status.setter
    def approval_status(self,value: Optional[driver_approval_status.DriverApprovalStatus] = None) -> None:
        """
        Sets the approvalStatus property value. An enum type to represent approval status of a driver.
        Args:
            value: Value to set for the approvalStatus property.
        """
        self._approval_status = value
    
    @property
    def category(self,) -> Optional[driver_category.DriverCategory]:
        """
        Gets the category property value. An enum type to represent which category a driver belongs to.
        Returns: Optional[driver_category.DriverCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[driver_category.DriverCategory] = None) -> None:
        """
        Sets the category property value. An enum type to represent which category a driver belongs to.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsDriverUpdateInventory and sets the default values.
        """
        super().__init__()
        # The number of devices for which this driver is applicable.
        self._applicable_device_count: Optional[int] = None
        # An enum type to represent approval status of a driver.
        self._approval_status: Optional[driver_approval_status.DriverApprovalStatus] = None
        # An enum type to represent which category a driver belongs to.
        self._category: Optional[driver_category.DriverCategory] = None
        # The date time when a driver should be deployed if approvalStatus is approved.
        self._deploy_date_time: Optional[datetime] = None
        # The class of the driver.
        self._driver_class: Optional[str] = None
        # The manufacturer of the driver.
        self._manufacturer: Optional[str] = None
        # The name of the driver.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The release date time of the driver.
        self._release_date_time: Optional[datetime] = None
        # The version of the driver.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDriverUpdateInventory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDriverUpdateInventory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDriverUpdateInventory()
    
    @property
    def deploy_date_time(self,) -> Optional[datetime]:
        """
        Gets the deployDateTime property value. The date time when a driver should be deployed if approvalStatus is approved.
        Returns: Optional[datetime]
        """
        return self._deploy_date_time
    
    @deploy_date_time.setter
    def deploy_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deployDateTime property value. The date time when a driver should be deployed if approvalStatus is approved.
        Args:
            value: Value to set for the deployDateTime property.
        """
        self._deploy_date_time = value
    
    @property
    def driver_class(self,) -> Optional[str]:
        """
        Gets the driverClass property value. The class of the driver.
        Returns: Optional[str]
        """
        return self._driver_class
    
    @driver_class.setter
    def driver_class(self,value: Optional[str] = None) -> None:
        """
        Sets the driverClass property value. The class of the driver.
        Args:
            value: Value to set for the driverClass property.
        """
        self._driver_class = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_device_count": lambda n : setattr(self, 'applicable_device_count', n.get_int_value()),
            "approval_status": lambda n : setattr(self, 'approval_status', n.get_enum_value(driver_approval_status.DriverApprovalStatus)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(driver_category.DriverCategory)),
            "deploy_date_time": lambda n : setattr(self, 'deploy_date_time', n.get_datetime_value()),
            "driver_class": lambda n : setattr(self, 'driver_class', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "release_date_time": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The manufacturer of the driver.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The manufacturer of the driver.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the driver.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the driver.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def release_date_time(self,) -> Optional[datetime]:
        """
        Gets the releaseDateTime property value. The release date time of the driver.
        Returns: Optional[datetime]
        """
        return self._release_date_time
    
    @release_date_time.setter
    def release_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the releaseDateTime property value. The release date time of the driver.
        Args:
            value: Value to set for the releaseDateTime property.
        """
        self._release_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("applicableDeviceCount", self.applicable_device_count)
        writer.write_enum_value("approvalStatus", self.approval_status)
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("deployDateTime", self.deploy_date_time)
        writer.write_str_value("driverClass", self.driver_class)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("name", self.name)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version of the driver.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version of the driver.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

