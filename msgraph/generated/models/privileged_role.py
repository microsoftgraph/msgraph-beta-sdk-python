from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, privileged_role_assignment, privileged_role_settings, privileged_role_summary

from . import entity

@dataclass
class PrivilegedRole(entity.Entity):
    # The assignments property
    assignments: Optional[List[privileged_role_assignment.PrivilegedRoleAssignment]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings property
    settings: Optional[privileged_role_settings.PrivilegedRoleSettings] = None
    # The summary property
    summary: Optional[privileged_role_summary.PrivilegedRoleSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRole
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedRole()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, privileged_role_assignment, privileged_role_settings, privileged_role_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(privileged_role_assignment.PrivilegedRoleAssignment)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(privileged_role_settings.PrivilegedRoleSettings)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(privileged_role_summary.PrivilegedRoleSummary)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("name", self.name)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("summary", self.summary)
    

