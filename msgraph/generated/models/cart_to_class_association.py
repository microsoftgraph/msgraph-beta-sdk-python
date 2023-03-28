from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class CartToClassAssociation(entity.Entity):
    """
    CartToClassAssociation for associating device carts with classrooms.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new cartToClassAssociation and sets the default values.
        """
        super().__init__()
        # Identifiers of classrooms to be associated with device carts.
        self._classroom_ids: Optional[List[str]] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Admin provided description of the CartToClassAssociation.
        self._description: Optional[str] = None
        # Identifiers of device carts to be associated with classes.
        self._device_cart_ids: Optional[List[str]] = None
        # Admin provided name of the device configuration.
        self._display_name: Optional[str] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Version of the CartToClassAssociation.
        self._version: Optional[int] = None
    
    @property
    def classroom_ids(self,) -> Optional[List[str]]:
        """
        Gets the classroomIds property value. Identifiers of classrooms to be associated with device carts.
        Returns: Optional[List[str]]
        """
        return self._classroom_ids
    
    @classroom_ids.setter
    def classroom_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the classroomIds property value. Identifiers of classrooms to be associated with device carts.
        Args:
            value: Value to set for the classroom_ids property.
        """
        self._classroom_ids = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. DateTime the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. DateTime the object was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CartToClassAssociation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CartToClassAssociation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CartToClassAssociation()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Admin provided description of the CartToClassAssociation.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Admin provided description of the CartToClassAssociation.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_cart_ids(self,) -> Optional[List[str]]:
        """
        Gets the deviceCartIds property value. Identifiers of device carts to be associated with classes.
        Returns: Optional[List[str]]
        """
        return self._device_cart_ids
    
    @device_cart_ids.setter
    def device_cart_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the deviceCartIds property value. Identifiers of device carts to be associated with classes.
        Args:
            value: Value to set for the device_cart_ids property.
        """
        self._device_cart_ids = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Admin provided name of the device configuration.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Admin provided name of the device configuration.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "classroomIds": lambda n : setattr(self, 'classroom_ids', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceCartIds": lambda n : setattr(self, 'device_cart_ids', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("classroomIds", self.classroom_ids)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("deviceCartIds", self.device_cart_ids)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("version", self.version)
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Version of the CartToClassAssociation.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Version of the CartToClassAssociation.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

