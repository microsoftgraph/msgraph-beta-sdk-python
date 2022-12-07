from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_constraint = lazy_import('msgraph.generated.models.device_management_constraint')

class DeviceManagementSettingAbstractImplementationConstraint(device_management_constraint.DeviceManagementConstraint):
    @property
    def allowed_abstract_implementation_definition_ids(self,) -> Optional[List[str]]:
        """
        Gets the allowedAbstractImplementationDefinitionIds property value. List of value which means not configured for the setting
        Returns: Optional[List[str]]
        """
        return self._allowed_abstract_implementation_definition_ids
    
    @allowed_abstract_implementation_definition_ids.setter
    def allowed_abstract_implementation_definition_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedAbstractImplementationDefinitionIds property value. List of value which means not configured for the setting
        Args:
            value: Value to set for the allowedAbstractImplementationDefinitionIds property.
        """
        self._allowed_abstract_implementation_definition_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingAbstractImplementationConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint"
        # List of value which means not configured for the setting
        self._allowed_abstract_implementation_definition_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingAbstractImplementationConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingAbstractImplementationConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingAbstractImplementationConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_abstract_implementation_definition_ids": lambda n : setattr(self, 'allowed_abstract_implementation_definition_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedAbstractImplementationDefinitionIds", self.allowed_abstract_implementation_definition_ids)
    

