from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
privileged_role_assignment = lazy_import('msgraph.generated.models.privileged_role_assignment')
privileged_role_settings = lazy_import('msgraph.generated.models.privileged_role_settings')
privileged_role_summary = lazy_import('msgraph.generated.models.privileged_role_summary')

class PrivilegedRole(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def assignments(self,) -> Optional[List[privileged_role_assignment.PrivilegedRoleAssignment]]:
        """
        Gets the assignments property value. The assignments for this role. Read-only. Nullable.
        Returns: Optional[List[privileged_role_assignment.PrivilegedRoleAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[privileged_role_assignment.PrivilegedRoleAssignment]] = None) -> None:
        """
        Sets the assignments property value. The assignments for this role. Read-only. Nullable.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedRole and sets the default values.
        """
        super().__init__()
        # The assignments for this role. Read-only. Nullable.
        self._assignments: Optional[List[privileged_role_assignment.PrivilegedRoleAssignment]] = None
        # Role name.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings for this role. Read-only. Nullable.
        self._settings: Optional[privileged_role_settings.PrivilegedRoleSettings] = None
        # The summary information for this role. Read-only. Nullable.
        self._summary: Optional[privileged_role_summary.PrivilegedRoleSummary] = None
    
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
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(privileged_role_assignment.PrivilegedRoleAssignment)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(privileged_role_settings.PrivilegedRoleSettings)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(privileged_role_summary.PrivilegedRoleSummary)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Role name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Role name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    
    @property
    def settings(self,) -> Optional[privileged_role_settings.PrivilegedRoleSettings]:
        """
        Gets the settings property value. The settings for this role. Read-only. Nullable.
        Returns: Optional[privileged_role_settings.PrivilegedRoleSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[privileged_role_settings.PrivilegedRoleSettings] = None) -> None:
        """
        Sets the settings property value. The settings for this role. Read-only. Nullable.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def summary(self,) -> Optional[privileged_role_summary.PrivilegedRoleSummary]:
        """
        Gets the summary property value. The summary information for this role. Read-only. Nullable.
        Returns: Optional[privileged_role_summary.PrivilegedRoleSummary]
        """
        return self._summary
    
    @summary.setter
    def summary(self,value: Optional[privileged_role_summary.PrivilegedRoleSummary] = None) -> None:
        """
        Sets the summary property value. The summary information for this role. Read-only. Nullable.
        Args:
            value: Value to set for the summary property.
        """
        self._summary = value
    

