from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
governance_resource = lazy_import('msgraph.generated.models.governance_resource')
governance_role_assignment = lazy_import('msgraph.generated.models.governance_role_assignment')
governance_role_assignment_request = lazy_import('msgraph.generated.models.governance_role_assignment_request')
governance_role_definition = lazy_import('msgraph.generated.models.governance_role_definition')
governance_role_setting = lazy_import('msgraph.generated.models.governance_role_setting')

class PrivilegedAccess(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedAccess and sets the default values.
        """
        super().__init__()
        # The display name of the provider managed by PIM.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of resources for the provider.
        self._resources: Optional[List[governance_resource.GovernanceResource]] = None
        # A collection of role assignment requests for the provider.
        self._role_assignment_requests: Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]] = None
        # A collection of role assignments for the provider.
        self._role_assignments: Optional[List[governance_role_assignment.GovernanceRoleAssignment]] = None
        # A collection of role defintions for the provider.
        self._role_definitions: Optional[List[governance_role_definition.GovernanceRoleDefinition]] = None
        # A collection of role settings for the provider.
        self._role_settings: Optional[List[governance_role_setting.GovernanceRoleSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccess
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccess()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the provider managed by PIM.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the provider managed by PIM.
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
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(governance_resource.GovernanceResource)),
            "role_assignment_requests": lambda n : setattr(self, 'role_assignment_requests', n.get_collection_of_object_values(governance_role_assignment_request.GovernanceRoleAssignmentRequest)),
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(governance_role_assignment.GovernanceRoleAssignment)),
            "role_definitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(governance_role_definition.GovernanceRoleDefinition)),
            "role_settings": lambda n : setattr(self, 'role_settings', n.get_collection_of_object_values(governance_role_setting.GovernanceRoleSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resources(self,) -> Optional[List[governance_resource.GovernanceResource]]:
        """
        Gets the resources property value. A collection of resources for the provider.
        Returns: Optional[List[governance_resource.GovernanceResource]]
        """
        return self._resources
    
    @resources.setter
    def resources(self,value: Optional[List[governance_resource.GovernanceResource]] = None) -> None:
        """
        Sets the resources property value. A collection of resources for the provider.
        Args:
            value: Value to set for the resources property.
        """
        self._resources = value
    
    @property
    def role_assignment_requests(self,) -> Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]]:
        """
        Gets the roleAssignmentRequests property value. A collection of role assignment requests for the provider.
        Returns: Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]]
        """
        return self._role_assignment_requests
    
    @role_assignment_requests.setter
    def role_assignment_requests(self,value: Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]] = None) -> None:
        """
        Sets the roleAssignmentRequests property value. A collection of role assignment requests for the provider.
        Args:
            value: Value to set for the roleAssignmentRequests property.
        """
        self._role_assignment_requests = value
    
    @property
    def role_assignments(self,) -> Optional[List[governance_role_assignment.GovernanceRoleAssignment]]:
        """
        Gets the roleAssignments property value. A collection of role assignments for the provider.
        Returns: Optional[List[governance_role_assignment.GovernanceRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[governance_role_assignment.GovernanceRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. A collection of role assignments for the provider.
        Args:
            value: Value to set for the roleAssignments property.
        """
        self._role_assignments = value
    
    @property
    def role_definitions(self,) -> Optional[List[governance_role_definition.GovernanceRoleDefinition]]:
        """
        Gets the roleDefinitions property value. A collection of role defintions for the provider.
        Returns: Optional[List[governance_role_definition.GovernanceRoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[governance_role_definition.GovernanceRoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. A collection of role defintions for the provider.
        Args:
            value: Value to set for the roleDefinitions property.
        """
        self._role_definitions = value
    
    @property
    def role_settings(self,) -> Optional[List[governance_role_setting.GovernanceRoleSetting]]:
        """
        Gets the roleSettings property value. A collection of role settings for the provider.
        Returns: Optional[List[governance_role_setting.GovernanceRoleSetting]]
        """
        return self._role_settings
    
    @role_settings.setter
    def role_settings(self,value: Optional[List[governance_role_setting.GovernanceRoleSetting]] = None) -> None:
        """
        Sets the roleSettings property value. A collection of role settings for the provider.
        Args:
            value: Value to set for the roleSettings property.
        """
        self._role_settings = value
    
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
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("roleAssignmentRequests", self.role_assignment_requests)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleSettings", self.role_settings)
    

