from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import oma_setting

from . import oma_setting

class OmaSettingInteger(oma_setting.OmaSetting):
    def __init__(self,) -> None:
        """
        Instantiates a new OmaSettingInteger and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.omaSettingInteger"
        # By setting to true, the CSP (configuration service provider) specified in the OMA-URI will perform a get, instead of set
        self._is_read_only: Optional[bool] = None
        # Value.
        self._value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OmaSettingInteger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OmaSettingInteger
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OmaSettingInteger()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import oma_setting

        fields: Dict[str, Callable[[Any], None]] = {
            "isReadOnly": lambda n : setattr(self, 'is_read_only', n.get_bool_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_read_only(self,) -> Optional[bool]:
        """
        Gets the isReadOnly property value. By setting to true, the CSP (configuration service provider) specified in the OMA-URI will perform a get, instead of set
        Returns: Optional[bool]
        """
        return self._is_read_only
    
    @is_read_only.setter
    def is_read_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReadOnly property value. By setting to true, the CSP (configuration service provider) specified in the OMA-URI will perform a get, instead of set
        Args:
            value: Value to set for the is_read_only property.
        """
        self._is_read_only = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isReadOnly", self.is_read_only)
        writer.write_int_value("value", self.value)
    
    @property
    def value(self,) -> Optional[int]:
        """
        Gets the value property value. Value.
        Returns: Optional[int]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[int] = None) -> None:
        """
        Sets the value property value. Value.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

