from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_constraint

from . import device_management_constraint

class DeviceManagementSettingFileConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingFileConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingFileConstraint"
        # Acceptable file extensions to upload for this setting
        self._supported_extensions: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingFileConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingFileConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingFileConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_constraint

        fields: Dict[str, Callable[[Any], None]] = {
            "supportedExtensions": lambda n : setattr(self, 'supported_extensions', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("supportedExtensions", self.supported_extensions)
    
    @property
    def supported_extensions(self,) -> Optional[List[str]]:
        """
        Gets the supportedExtensions property value. Acceptable file extensions to upload for this setting
        Returns: Optional[List[str]]
        """
        return self._supported_extensions
    
    @supported_extensions.setter
    def supported_extensions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedExtensions property value. Acceptable file extensions to upload for this setting
        Args:
            value: Value to set for the supported_extensions property.
        """
        self._supported_extensions = value
    

