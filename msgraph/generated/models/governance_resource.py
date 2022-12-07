from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
governance_role_assignment = lazy_import('msgraph.generated.models.governance_role_assignment')
governance_role_assignment_request = lazy_import('msgraph.generated.models.governance_role_assignment_request')
governance_role_definition = lazy_import('msgraph.generated.models.governance_role_definition')
governance_role_setting = lazy_import('msgraph.generated.models.governance_role_setting')

class GovernanceResource(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new governanceResource and sets the default values.
        """
        super().__init__()
        # The display name of the resource.
        self._display_name: Optional[str] = None
        # The external id of the resource, representing its original id in the external system. For example, a subscription resource's external id can be '/subscriptions/c14ae696-5e0c-4e5d-88cc-bef6637737ac'.
        self._external_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. The parent resource. for pimforazurerbac scenario, it can represent the subscription the resource belongs to.
        self._parent: Optional[GovernanceResource] = None
        # Represents the date time when the resource is registered in PIM.
        self._registered_date_time: Optional[datetime] = None
        # The externalId of the resource's root scope that is registered in PIM. The root scope can be the parent, grandparent, or higher ancestor resources.
        self._registered_root: Optional[str] = None
        # The collection of role assignment requests for the resource.
        self._role_assignment_requests: Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]] = None
        # The collection of role assignments for the resource.
        self._role_assignments: Optional[List[governance_role_assignment.GovernanceRoleAssignment]] = None
        # The collection of role defintions for the resource.
        self._role_definitions: Optional[List[governance_role_definition.GovernanceRoleDefinition]] = None
        # The collection of role settings for the resource.
        self._role_settings: Optional[List[governance_role_setting.GovernanceRoleSetting]] = None
        # The status of a given resource. For example, it could represent whether the resource is locked or not (values: Active/Locked). Note: This property may be extended in the future to support more scenarios.
        self._status: Optional[str] = None
        # Required. Resource type. For example, for Azure resources, the type could be 'Subscription', 'ResourceGroup', 'Microsoft.Sql/server', etc.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the resource.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the resource.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The external id of the resource, representing its original id in the external system. For example, a subscription resource's external id can be '/subscriptions/c14ae696-5e0c-4e5d-88cc-bef6637737ac'.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The external id of the resource, representing its original id in the external system. For example, a subscription resource's external id can be '/subscriptions/c14ae696-5e0c-4e5d-88cc-bef6637737ac'.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(GovernanceResource)),
            "registered_date_time": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
            "registered_root": lambda n : setattr(self, 'registered_root', n.get_str_value()),
            "role_assignment_requests": lambda n : setattr(self, 'role_assignment_requests', n.get_collection_of_object_values(governance_role_assignment_request.GovernanceRoleAssignmentRequest)),
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(governance_role_assignment.GovernanceRoleAssignment)),
            "role_definitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(governance_role_definition.GovernanceRoleDefinition)),
            "role_settings": lambda n : setattr(self, 'role_settings', n.get_collection_of_object_values(governance_role_setting.GovernanceRoleSetting)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def parent(self,) -> Optional[GovernanceResource]:
        """
        Gets the parent property value. Read-only. The parent resource. for pimforazurerbac scenario, it can represent the subscription the resource belongs to.
        Returns: Optional[GovernanceResource]
        """
        return self._parent
    
    @parent.setter
    def parent(self,value: Optional[GovernanceResource] = None) -> None:
        """
        Sets the parent property value. Read-only. The parent resource. for pimforazurerbac scenario, it can represent the subscription the resource belongs to.
        Args:
            value: Value to set for the parent property.
        """
        self._parent = value
    
    @property
    def registered_date_time(self,) -> Optional[datetime]:
        """
        Gets the registeredDateTime property value. Represents the date time when the resource is registered in PIM.
        Returns: Optional[datetime]
        """
        return self._registered_date_time
    
    @registered_date_time.setter
    def registered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the registeredDateTime property value. Represents the date time when the resource is registered in PIM.
        Args:
            value: Value to set for the registeredDateTime property.
        """
        self._registered_date_time = value
    
    @property
    def registered_root(self,) -> Optional[str]:
        """
        Gets the registeredRoot property value. The externalId of the resource's root scope that is registered in PIM. The root scope can be the parent, grandparent, or higher ancestor resources.
        Returns: Optional[str]
        """
        return self._registered_root
    
    @registered_root.setter
    def registered_root(self,value: Optional[str] = None) -> None:
        """
        Sets the registeredRoot property value. The externalId of the resource's root scope that is registered in PIM. The root scope can be the parent, grandparent, or higher ancestor resources.
        Args:
            value: Value to set for the registeredRoot property.
        """
        self._registered_root = value
    
    @property
    def role_assignment_requests(self,) -> Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]]:
        """
        Gets the roleAssignmentRequests property value. The collection of role assignment requests for the resource.
        Returns: Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]]
        """
        return self._role_assignment_requests
    
    @role_assignment_requests.setter
    def role_assignment_requests(self,value: Optional[List[governance_role_assignment_request.GovernanceRoleAssignmentRequest]] = None) -> None:
        """
        Sets the roleAssignmentRequests property value. The collection of role assignment requests for the resource.
        Args:
            value: Value to set for the roleAssignmentRequests property.
        """
        self._role_assignment_requests = value
    
    @property
    def role_assignments(self,) -> Optional[List[governance_role_assignment.GovernanceRoleAssignment]]:
        """
        Gets the roleAssignments property value. The collection of role assignments for the resource.
        Returns: Optional[List[governance_role_assignment.GovernanceRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[governance_role_assignment.GovernanceRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. The collection of role assignments for the resource.
        Args:
            value: Value to set for the roleAssignments property.
        """
        self._role_assignments = value
    
    @property
    def role_definitions(self,) -> Optional[List[governance_role_definition.GovernanceRoleDefinition]]:
        """
        Gets the roleDefinitions property value. The collection of role defintions for the resource.
        Returns: Optional[List[governance_role_definition.GovernanceRoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[governance_role_definition.GovernanceRoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. The collection of role defintions for the resource.
        Args:
            value: Value to set for the roleDefinitions property.
        """
        self._role_definitions = value
    
    @property
    def role_settings(self,) -> Optional[List[governance_role_setting.GovernanceRoleSetting]]:
        """
        Gets the roleSettings property value. The collection of role settings for the resource.
        Returns: Optional[List[governance_role_setting.GovernanceRoleSetting]]
        """
        return self._role_settings
    
    @role_settings.setter
    def role_settings(self,value: Optional[List[governance_role_setting.GovernanceRoleSetting]] = None) -> None:
        """
        Sets the roleSettings property value. The collection of role settings for the resource.
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
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("parent", self.parent)
        writer.write_datetime_value("registeredDateTime", self.registered_date_time)
        writer.write_str_value("registeredRoot", self.registered_root)
        writer.write_collection_of_object_values("roleAssignmentRequests", self.role_assignment_requests)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleSettings", self.role_settings)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status of a given resource. For example, it could represent whether the resource is locked or not (values: Active/Locked). Note: This property may be extended in the future to support more scenarios.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status of a given resource. For example, it could represent whether the resource is locked or not (values: Active/Locked). Note: This property may be extended in the future to support more scenarios.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Required. Resource type. For example, for Azure resources, the type could be 'Subscription', 'ResourceGroup', 'Microsoft.Sql/server', etc.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Required. Resource type. For example, for Azure resources, the type could be 'Subscription', 'ResourceGroup', 'Microsoft.Sql/server', etc.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

