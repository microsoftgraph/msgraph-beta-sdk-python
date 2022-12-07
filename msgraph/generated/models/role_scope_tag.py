from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
role_scope_tag_auto_assignment = lazy_import('msgraph.generated.models.role_scope_tag_auto_assignment')

class RoleScopeTag(entity.Entity):
    """
    Role Scope Tag
    """
    @property
    def assignments(self,) -> Optional[List[role_scope_tag_auto_assignment.RoleScopeTagAutoAssignment]]:
        """
        Gets the assignments property value. The list of assignments for this Role Scope Tag.
        Returns: Optional[List[role_scope_tag_auto_assignment.RoleScopeTagAutoAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[role_scope_tag_auto_assignment.RoleScopeTagAutoAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for this Role Scope Tag.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new roleScopeTag and sets the default values.
        """
        super().__init__()
        # The list of assignments for this Role Scope Tag.
        self._assignments: Optional[List[role_scope_tag_auto_assignment.RoleScopeTagAutoAssignment]] = None
        # Description of the Role Scope Tag.
        self._description: Optional[str] = None
        # The display or friendly name of the Role Scope Tag.
        self._display_name: Optional[str] = None
        # Description of the Role Scope Tag. This property is read-only.
        self._is_built_in: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleScopeTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleScopeTag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleScopeTag()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the Role Scope Tag.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the Role Scope Tag.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display or friendly name of the Role Scope Tag.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display or friendly name of the Role Scope Tag.
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(role_scope_tag_auto_assignment.RoleScopeTagAutoAssignment)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_built_in": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_built_in(self,) -> Optional[bool]:
        """
        Gets the isBuiltIn property value. Description of the Role Scope Tag. This property is read-only.
        Returns: Optional[bool]
        """
        return self._is_built_in
    
    @is_built_in.setter
    def is_built_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltIn property value. Description of the Role Scope Tag. This property is read-only.
        Args:
            value: Value to set for the isBuiltIn property.
        """
        self._is_built_in = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

