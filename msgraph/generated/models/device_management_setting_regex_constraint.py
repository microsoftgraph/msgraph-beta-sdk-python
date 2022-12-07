from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_constraint = lazy_import('msgraph.generated.models.device_management_constraint')

class DeviceManagementSettingRegexConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingRegexConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingRegexConstraint"
        # The RegEx pattern to match against
        self._regex: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingRegexConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingRegexConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingRegexConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "regex": lambda n : setattr(self, 'regex', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def regex(self,) -> Optional[str]:
        """
        Gets the regex property value. The RegEx pattern to match against
        Returns: Optional[str]
        """
        return self._regex
    
    @regex.setter
    def regex(self,value: Optional[str] = None) -> None:
        """
        Sets the regex property value. The RegEx pattern to match against
        Args:
            value: Value to set for the regex property.
        """
        self._regex = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("regex", self.regex)
    

