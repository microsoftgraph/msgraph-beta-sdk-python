from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class UserExperienceAnalyticsDeviceStartupProcess(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new UserExperienceAnalyticsDeviceStartupProcess and sets the default values.
        """
        super().__init__()
        # The user experience analytics device id.
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # User experience analytics device startup process name.
        self._process_name: Optional[str] = None
        # The user experience analytics device startup process product name.
        self._product_name: Optional[str] = None
        # The User experience analytics device startup process publisher.
        self._publisher: Optional[str] = None
        # User experience analytics device startup process impact in milliseconds.
        self._startup_impact_in_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceStartupProcess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceStartupProcess
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceStartupProcess()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "processName": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "startupImpactInMs": lambda n : setattr(self, 'startup_impact_in_ms', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The user experience analytics device id.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The user experience analytics device id.
        Args:
            value: Value to set for the managed_device_id property.
        """
        self._managed_device_id = value
    
    @property
    def process_name(self,) -> Optional[str]:
        """
        Gets the processName property value. User experience analytics device startup process name.
        Returns: Optional[str]
        """
        return self._process_name
    
    @process_name.setter
    def process_name(self,value: Optional[str] = None) -> None:
        """
        Sets the processName property value. User experience analytics device startup process name.
        Args:
            value: Value to set for the process_name property.
        """
        self._process_name = value
    
    @property
    def product_name(self,) -> Optional[str]:
        """
        Gets the productName property value. The user experience analytics device startup process product name.
        Returns: Optional[str]
        """
        return self._product_name
    
    @product_name.setter
    def product_name(self,value: Optional[str] = None) -> None:
        """
        Sets the productName property value. The user experience analytics device startup process product name.
        Args:
            value: Value to set for the product_name property.
        """
        self._product_name = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The User experience analytics device startup process publisher.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The User experience analytics device startup process publisher.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("processName", self.process_name)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_int_value("startupImpactInMs", self.startup_impact_in_ms)
    
    @property
    def startup_impact_in_ms(self,) -> Optional[int]:
        """
        Gets the startupImpactInMs property value. User experience analytics device startup process impact in milliseconds.
        Returns: Optional[int]
        """
        return self._startup_impact_in_ms
    
    @startup_impact_in_ms.setter
    def startup_impact_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the startupImpactInMs property value. User experience analytics device startup process impact in milliseconds.
        Args:
            value: Value to set for the startup_impact_in_ms property.
        """
        self._startup_impact_in_ms = value
    

