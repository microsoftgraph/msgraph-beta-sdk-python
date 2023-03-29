from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import user_matching_setting
    from .. import entity

from .. import entity

class SourceSystemDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new sourceSystemDefinition and sets the default values.
        """
        super().__init__()
        # The name of the source system. Maximum supported length is 100 characters.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of user matching settings by roleGroup.
        self._user_matching_settings: Optional[List[user_matching_setting.UserMatchingSetting]] = None
        # The name of the vendor who supplies the source system. Maximum supported length is 100 characters.
        self._vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SourceSystemDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SourceSystemDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SourceSystemDefinition()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the source system. Maximum supported length is 100 characters.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the source system. Maximum supported length is 100 characters.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import user_matching_setting
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "userMatchingSettings": lambda n : setattr(self, 'user_matching_settings', n.get_collection_of_object_values(user_matching_setting.UserMatchingSetting)),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("userMatchingSettings", self.user_matching_settings)
        writer.write_str_value("vendor", self.vendor)
    
    @property
    def user_matching_settings(self,) -> Optional[List[user_matching_setting.UserMatchingSetting]]:
        """
        Gets the userMatchingSettings property value. A collection of user matching settings by roleGroup.
        Returns: Optional[List[user_matching_setting.UserMatchingSetting]]
        """
        return self._user_matching_settings
    
    @user_matching_settings.setter
    def user_matching_settings(self,value: Optional[List[user_matching_setting.UserMatchingSetting]] = None) -> None:
        """
        Sets the userMatchingSettings property value. A collection of user matching settings by roleGroup.
        Args:
            value: Value to set for the user_matching_settings property.
        """
        self._user_matching_settings = value
    
    @property
    def vendor(self,) -> Optional[str]:
        """
        Gets the vendor property value. The name of the vendor who supplies the source system. Maximum supported length is 100 characters.
        Returns: Optional[str]
        """
        return self._vendor
    
    @vendor.setter
    def vendor(self,value: Optional[str] = None) -> None:
        """
        Sets the vendor property value. The name of the vendor who supplies the source system. Maximum supported length is 100 characters.
        Args:
            value: Value to set for the vendor property.
        """
        self._vendor = value
    

