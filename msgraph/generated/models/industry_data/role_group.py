from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import role_reference_value
    from .. import entity

from .. import entity

class RoleGroup(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new roleGroup and sets the default values.
        """
        super().__init__()
        # The name of the role group.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The set of roles included in the role group.
        self._roles: Optional[List[role_reference_value.RoleReferenceValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleGroup()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the role group.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the role group.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import role_reference_value
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(role_reference_value.RoleReferenceValue)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def roles(self,) -> Optional[List[role_reference_value.RoleReferenceValue]]:
        """
        Gets the roles property value. The set of roles included in the role group.
        Returns: Optional[List[role_reference_value.RoleReferenceValue]]
        """
        return self._roles
    
    @roles.setter
    def roles(self,value: Optional[List[role_reference_value.RoleReferenceValue]] = None) -> None:
        """
        Sets the roles property value. The set of roles included in the role group.
        Args:
            value: Value to set for the roles property.
        """
        self._roles = value
    
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
        writer.write_collection_of_object_values("roles", self.roles)
    

