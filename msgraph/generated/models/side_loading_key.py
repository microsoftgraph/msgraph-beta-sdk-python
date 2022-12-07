from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class SideLoadingKey(entity.Entity):
    """
    SideLoadingKey entity is required for Windows 8 and 8.1 devices to intall Line Of Business Apps for a tenant.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new sideLoadingKey and sets the default values.
        """
        super().__init__()
        # Side Loading Key description displayed to the ITPro Admins..
        self._description: Optional[str] = None
        # Side Loading Key Name displayed to the ITPro Admins.
        self._display_name: Optional[str] = None
        # Side Loading Key Last Updated Date displayed to the ITPro Admins.
        self._last_updated_date_time: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Side Loading Key Total Activation displayed to the ITPro Admins.
        self._total_activation: Optional[int] = None
        # Side Loading Key Value, it is 5x5 value, seperated by hiphens.
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SideLoadingKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SideLoadingKey
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SideLoadingKey()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Side Loading Key description displayed to the ITPro Admins..
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Side Loading Key description displayed to the ITPro Admins..
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Side Loading Key Name displayed to the ITPro Admins.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Side Loading Key Name displayed to the ITPro Admins.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_str_value()),
            "total_activation": lambda n : setattr(self, 'total_activation', n.get_int_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[str]:
        """
        Gets the lastUpdatedDateTime property value. Side Loading Key Last Updated Date displayed to the ITPro Admins.
        Returns: Optional[str]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Side Loading Key Last Updated Date displayed to the ITPro Admins.
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_int_value("totalActivation", self.total_activation)
        writer.write_str_value("value", self.value)
    
    @property
    def total_activation(self,) -> Optional[int]:
        """
        Gets the totalActivation property value. Side Loading Key Total Activation displayed to the ITPro Admins.
        Returns: Optional[int]
        """
        return self._total_activation
    
    @total_activation.setter
    def total_activation(self,value: Optional[int] = None) -> None:
        """
        Sets the totalActivation property value. Side Loading Key Total Activation displayed to the ITPro Admins.
        Args:
            value: Value to set for the totalActivation property.
        """
        self._total_activation = value
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Side Loading Key Value, it is 5x5 value, seperated by hiphens.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Side Loading Key Value, it is 5x5 value, seperated by hiphens.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

