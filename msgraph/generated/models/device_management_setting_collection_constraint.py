from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_constraint = lazy_import('msgraph.generated.models.device_management_constraint')

class DeviceManagementSettingCollectionConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingCollectionConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingCollectionConstraint"
        # The maximum number of elements in the collection
        self._maximum_length: Optional[int] = None
        # The minimum number of elements in the collection
        self._minimum_length: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingCollectionConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingCollectionConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingCollectionConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "maximum_length": lambda n : setattr(self, 'maximum_length', n.get_int_value()),
            "minimum_length": lambda n : setattr(self, 'minimum_length', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_length(self,) -> Optional[int]:
        """
        Gets the maximumLength property value. The maximum number of elements in the collection
        Returns: Optional[int]
        """
        return self._maximum_length
    
    @maximum_length.setter
    def maximum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumLength property value. The maximum number of elements in the collection
        Args:
            value: Value to set for the maximumLength property.
        """
        self._maximum_length = value
    
    @property
    def minimum_length(self,) -> Optional[int]:
        """
        Gets the minimumLength property value. The minimum number of elements in the collection
        Returns: Optional[int]
        """
        return self._minimum_length
    
    @minimum_length.setter
    def minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumLength property value. The minimum number of elements in the collection
        Args:
            value: Value to set for the minimumLength property.
        """
        self._minimum_length = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumLength", self.maximum_length)
        writer.write_int_value("minimumLength", self.minimum_length)
    

