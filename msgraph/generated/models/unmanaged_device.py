from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UnmanagedDevice(AdditionalDataHolder, Parsable):
    """
    Unmanaged device discovered in the network.
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
        Instantiates a new unmanagedDevice and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Device name.
        self._device_name: Optional[str] = None
        # Domain.
        self._domain: Optional[str] = None
        # IP address.
        self._ip_address: Optional[str] = None
        # Last logged on user.
        self._last_logged_on_user: Optional[str] = None
        # Last seen date and time.
        self._last_seen_date_time: Optional[datetime] = None
        # Location.
        self._location: Optional[str] = None
        # MAC address.
        self._mac_address: Optional[str] = None
        # Manufacturer.
        self._manufacturer: Optional[str] = None
        # Model.
        self._model: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Operating system.
        self._os: Optional[str] = None
        # Operating system version.
        self._os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnmanagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnmanagedDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnmanagedDevice()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def domain(self,) -> Optional[str]:
        """
        Gets the domain property value. Domain.
        Returns: Optional[str]
        """
        return self._domain
    
    @domain.setter
    def domain(self,value: Optional[str] = None) -> None:
        """
        Sets the domain property value. Domain.
        Args:
            value: Value to set for the domain property.
        """
        self._domain = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "last_logged_on_user": lambda n : setattr(self, 'last_logged_on_user', n.get_str_value()),
            "last_seen_date_time": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "mac_address": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
        }
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. IP address.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. IP address.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    @property
    def last_logged_on_user(self,) -> Optional[str]:
        """
        Gets the lastLoggedOnUser property value. Last logged on user.
        Returns: Optional[str]
        """
        return self._last_logged_on_user
    
    @last_logged_on_user.setter
    def last_logged_on_user(self,value: Optional[str] = None) -> None:
        """
        Sets the lastLoggedOnUser property value. Last logged on user.
        Args:
            value: Value to set for the lastLoggedOnUser property.
        """
        self._last_logged_on_user = value
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. Last seen date and time.
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. Last seen date and time.
        Args:
            value: Value to set for the lastSeenDateTime property.
        """
        self._last_seen_date_time = value
    
    @property
    def location(self,) -> Optional[str]:
        """
        Gets the location property value. Location.
        Returns: Optional[str]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[str] = None) -> None:
        """
        Sets the location property value. Location.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def mac_address(self,) -> Optional[str]:
        """
        Gets the macAddress property value. MAC address.
        Returns: Optional[str]
        """
        return self._mac_address
    
    @mac_address.setter
    def mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the macAddress property value. MAC address.
        Args:
            value: Value to set for the macAddress property.
        """
        self._mac_address = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
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
    def os(self,) -> Optional[str]:
        """
        Gets the os property value. Operating system.
        Returns: Optional[str]
        """
        return self._os
    
    @os.setter
    def os(self,value: Optional[str] = None) -> None:
        """
        Sets the os property value. Operating system.
        Args:
            value: Value to set for the os property.
        """
        self._os = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Operating system version.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Operating system version.
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
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("lastLoggedOnUser", self.last_logged_on_user)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("location", self.location)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("os", self.os)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_additional_data_value(self.additional_data)
    

