from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class IosAvailableUpdateVersion(AdditionalDataHolder, Parsable):
    """
    iOS available update version details
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
        Instantiates a new iosAvailableUpdateVersion and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The expiration date of the update.
        self._expiration_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The posting date of the update.
        self._posting_date_time: Optional[datetime] = None
        # The version of the update.
        self._product_version: Optional[str] = None
        # List of supported devices for the update.
        self._supported_devices: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosAvailableUpdateVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosAvailableUpdateVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosAvailableUpdateVersion()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expiration date of the update.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expiration date of the update.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "posting_date_time": lambda n : setattr(self, 'posting_date_time', n.get_datetime_value()),
            "product_version": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "supported_devices": lambda n : setattr(self, 'supported_devices', n.get_collection_of_primitive_values(str)),
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
    
    @property
    def posting_date_time(self,) -> Optional[datetime]:
        """
        Gets the postingDateTime property value. The posting date of the update.
        Returns: Optional[datetime]
        """
        return self._posting_date_time
    
    @posting_date_time.setter
    def posting_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the postingDateTime property value. The posting date of the update.
        Args:
            value: Value to set for the postingDateTime property.
        """
        self._posting_date_time = value
    
    @property
    def product_version(self,) -> Optional[str]:
        """
        Gets the productVersion property value. The version of the update.
        Returns: Optional[str]
        """
        return self._product_version
    
    @product_version.setter
    def product_version(self,value: Optional[str] = None) -> None:
        """
        Sets the productVersion property value. The version of the update.
        Args:
            value: Value to set for the productVersion property.
        """
        self._product_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("postingDateTime", self.posting_date_time)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_collection_of_primitive_values("supportedDevices", self.supported_devices)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def supported_devices(self,) -> Optional[List[str]]:
        """
        Gets the supportedDevices property value. List of supported devices for the update.
        Returns: Optional[List[str]]
        """
        return self._supported_devices
    
    @supported_devices.setter
    def supported_devices(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedDevices property value. List of supported devices for the update.
        Args:
            value: Value to set for the supportedDevices property.
        """
        self._supported_devices = value
    

