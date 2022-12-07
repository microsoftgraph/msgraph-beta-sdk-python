from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Account(entity.Entity):
    @property
    def blocked(self,) -> Optional[bool]:
        """
        Gets the blocked property value. The blocked property
        Returns: Optional[bool]
        """
        return self._blocked
    
    @blocked.setter
    def blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the blocked property value. The blocked property
        Args:
            value: Value to set for the blocked property.
        """
        self._blocked = value
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. The category property
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new account and sets the default values.
        """
        super().__init__()
        # The blocked property
        self._blocked: Optional[bool] = None
        # The category property
        self._category: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The number property
        self._number: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The subCategory property
        self._sub_category: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Account:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Account
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Account()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
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
            "blocked": lambda n : setattr(self, 'blocked', n.get_bool_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "sub_category": lambda n : setattr(self, 'sub_category', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def number(self,) -> Optional[str]:
        """
        Gets the number property value. The number property
        Returns: Optional[str]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[str] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("blocked", self.blocked)
        writer.write_str_value("category", self.category)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_str_value("subCategory", self.sub_category)
    
    @property
    def sub_category(self,) -> Optional[str]:
        """
        Gets the subCategory property value. The subCategory property
        Returns: Optional[str]
        """
        return self._sub_category
    
    @sub_category.setter
    def sub_category(self,value: Optional[str] = None) -> None:
        """
        Sets the subCategory property value. The subCategory property
        Args:
            value: Value to set for the subCategory property.
        """
        self._sub_category = value
    

