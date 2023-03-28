from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import software_update_catalog_entry

from . import software_update_catalog_entry

class DriverUpdateCatalogEntry(software_update_catalog_entry.SoftwareUpdateCatalogEntry):
    def __init__(self,) -> None:
        """
        Instantiates a new DriverUpdateCatalogEntry and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry"
        # The description of the content.
        self._description: Optional[str] = None
        # The classification of the driver.
        self._driver_class: Optional[str] = None
        # The manufacturer of the driver.
        self._manufacturer: Optional[str] = None
        # The provider of the driver.
        self._provider: Optional[str] = None
        # The setup information file of the driver.
        self._setup_information_file: Optional[str] = None
        # The unique version of the content.
        self._version: Optional[str] = None
        # The date and time when a new version of content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._version_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DriverUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DriverUpdateCatalogEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DriverUpdateCatalogEntry()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the content.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the content.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def driver_class(self,) -> Optional[str]:
        """
        Gets the driverClass property value. The classification of the driver.
        Returns: Optional[str]
        """
        return self._driver_class
    
    @driver_class.setter
    def driver_class(self,value: Optional[str] = None) -> None:
        """
        Sets the driverClass property value. The classification of the driver.
        Args:
            value: Value to set for the driver_class property.
        """
        self._driver_class = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import software_update_catalog_entry

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "driverClass": lambda n : setattr(self, 'driver_class', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "setupInformationFile": lambda n : setattr(self, 'setup_information_file', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "versionDateTime": lambda n : setattr(self, 'version_date_time', n.get_datetime_value()),
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
    def provider(self,) -> Optional[str]:
        """
        Gets the provider property value. The provider of the driver.
        Returns: Optional[str]
        """
        return self._provider
    
    @provider.setter
    def provider(self,value: Optional[str] = None) -> None:
        """
        Sets the provider property value. The provider of the driver.
        Args:
            value: Value to set for the provider property.
        """
        self._provider = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("driverClass", self.driver_class)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("setupInformationFile", self.setup_information_file)
        writer.write_str_value("version", self.version)
        writer.write_datetime_value("versionDateTime", self.version_date_time)
    
    @property
    def setup_information_file(self,) -> Optional[str]:
        """
        Gets the setupInformationFile property value. The setup information file of the driver.
        Returns: Optional[str]
        """
        return self._setup_information_file
    
    @setup_information_file.setter
    def setup_information_file(self,value: Optional[str] = None) -> None:
        """
        Sets the setupInformationFile property value. The setup information file of the driver.
        Args:
            value: Value to set for the setup_information_file property.
        """
        self._setup_information_file = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The unique version of the content.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The unique version of the content.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    
    @property
    def version_date_time(self,) -> Optional[datetime]:
        """
        Gets the versionDateTime property value. The date and time when a new version of content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._version_date_time
    
    @version_date_time.setter
    def version_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the versionDateTime property value. The date and time when a new version of content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the version_date_time property.
        """
        self._version_date_time = value
    

