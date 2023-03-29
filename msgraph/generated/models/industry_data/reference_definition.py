from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import entity

from .. import entity

class ReferenceDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new referenceDefinition and sets the default values.
        """
        super().__init__()
        # The code value for the definition that must be unique within the referenceType.
        self._code: Optional[str] = None
        # The date and time when the definition was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # Indicates whether the definition has been disabled.
        self._is_disabled: Optional[bool] = None
        # The date and time when the definition was most recently changed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The categorical type for a collection of enumerated values.
        self._reference_type: Optional[str] = None
        # The ordering index to present the definitions within a type consistently in user interfaces.
        self._sort_index: Optional[int] = None
        # The standards body or organization source which defined the code.
        self._source: Optional[str] = None
    
    @property
    def code(self,) -> Optional[str]:
        """
        Gets the code property value. The code value for the definition that must be unique within the referenceType.
        Returns: Optional[str]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[str] = None) -> None:
        """
        Sets the code property value. The code value for the definition that must be unique within the referenceType.
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the definition was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the definition was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReferenceDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReferenceDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReferenceDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isDisabled": lambda n : setattr(self, 'is_disabled', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "referenceType": lambda n : setattr(self, 'reference_type', n.get_str_value()),
            "sortIndex": lambda n : setattr(self, 'sort_index', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_disabled(self,) -> Optional[bool]:
        """
        Gets the isDisabled property value. Indicates whether the definition has been disabled.
        Returns: Optional[bool]
        """
        return self._is_disabled
    
    @is_disabled.setter
    def is_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDisabled property value. Indicates whether the definition has been disabled.
        Args:
            value: Value to set for the is_disabled property.
        """
        self._is_disabled = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the definition was most recently changed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the definition was most recently changed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def reference_type(self,) -> Optional[str]:
        """
        Gets the referenceType property value. The categorical type for a collection of enumerated values.
        Returns: Optional[str]
        """
        return self._reference_type
    
    @reference_type.setter
    def reference_type(self,value: Optional[str] = None) -> None:
        """
        Sets the referenceType property value. The categorical type for a collection of enumerated values.
        Args:
            value: Value to set for the reference_type property.
        """
        self._reference_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("code", self.code)
        writer.write_bool_value("isDisabled", self.is_disabled)
        writer.write_str_value("referenceType", self.reference_type)
        writer.write_int_value("sortIndex", self.sort_index)
    
    @property
    def sort_index(self,) -> Optional[int]:
        """
        Gets the sortIndex property value. The ordering index to present the definitions within a type consistently in user interfaces.
        Returns: Optional[int]
        """
        return self._sort_index
    
    @sort_index.setter
    def sort_index(self,value: Optional[int] = None) -> None:
        """
        Sets the sortIndex property value. The ordering index to present the definitions within a type consistently in user interfaces.
        Args:
            value: Value to set for the sort_index property.
        """
        self._sort_index = value
    
    @property
    def source(self,) -> Optional[str]:
        """
        Gets the source property value. The standards body or organization source which defined the code.
        Returns: Optional[str]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[str] = None) -> None:
        """
        Sets the source property value. The standards body or organization source which defined the code.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    

