from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OsVersionCount(AdditionalDataHolder, Parsable):
    """
    Count of devices with malware for each OS version
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
        Instantiates a new osVersionCount and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Count of devices with malware for the OS version
        self._device_count: Optional[int] = None
        # The Timestamp of the last update for the device count in UTC
        self._last_update_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # OS version
        self._os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OsVersionCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OsVersionCount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OsVersionCount()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. Count of devices with malware for the OS version
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. Count of devices with malware for the OS version
        Args:
            value: Value to set for the deviceCount property.
        """
        self._device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "last_update_date_time": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
        }
        return fields
    
    @property
    def last_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdateDateTime property value. The Timestamp of the last update for the device count in UTC
        Returns: Optional[datetime]
        """
        return self._last_update_date_time
    
    @last_update_date_time.setter
    def last_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdateDateTime property value. The Timestamp of the last update for the device count in UTC
        Args:
            value: Value to set for the lastUpdateDateTime property.
        """
        self._last_update_date_time = value
    
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
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. OS version
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. OS version
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
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_additional_data_value(self.additional_data)
    

