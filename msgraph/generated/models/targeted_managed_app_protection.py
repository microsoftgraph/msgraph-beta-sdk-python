from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_management_level = lazy_import('msgraph.generated.models.app_management_level')
managed_app_protection = lazy_import('msgraph.generated.models.managed_app_protection')
targeted_managed_app_group_type = lazy_import('msgraph.generated.models.targeted_managed_app_group_type')
targeted_managed_app_policy_assignment = lazy_import('msgraph.generated.models.targeted_managed_app_policy_assignment')

class TargetedManagedAppProtection(managed_app_protection.ManagedAppProtection):
    @property
    def app_group_type(self,) -> Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType]:
        """
        Gets the appGroupType property value. Indicates a collection of apps to target which can be one of several pre-defined lists of apps or a manually selected list of apps
        Returns: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType]
        """
        return self._app_group_type
    
    @app_group_type.setter
    def app_group_type(self,value: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType] = None) -> None:
        """
        Sets the appGroupType property value. Indicates a collection of apps to target which can be one of several pre-defined lists of apps or a manually selected list of apps
        Args:
            value: Value to set for the appGroupType property.
        """
        self._app_group_type = value
    
    @property
    def assignments(self,) -> Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]]:
        """
        Gets the assignments property value. Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
        Returns: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new TargetedManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.targetedManagedAppProtection"
        # Indicates a collection of apps to target which can be one of several pre-defined lists of apps or a manually selected list of apps
        self._app_group_type: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType] = None
        # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
        self._assignments: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None
        # Indicates if the policy is deployed to any inclusion groups or not.
        self._is_assigned: Optional[bool] = None
        # Management levels for apps
        self._targeted_app_management_levels: Optional[app_management_level.AppManagementLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TargetedManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TargetedManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TargetedManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_group_type": lambda n : setattr(self, 'app_group_type', n.get_enum_value(targeted_managed_app_group_type.TargetedManagedAppGroupType)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment)),
            "is_assigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "targeted_app_management_levels": lambda n : setattr(self, 'targeted_app_management_levels', n.get_enum_value(app_management_level.AppManagementLevel)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_assigned(self,) -> Optional[bool]:
        """
        Gets the isAssigned property value. Indicates if the policy is deployed to any inclusion groups or not.
        Returns: Optional[bool]
        """
        return self._is_assigned
    
    @is_assigned.setter
    def is_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAssigned property value. Indicates if the policy is deployed to any inclusion groups or not.
        Args:
            value: Value to set for the isAssigned property.
        """
        self._is_assigned = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("appGroupType", self.app_group_type)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_bool_value("isAssigned", self.is_assigned)
        writer.write_enum_value("targetedAppManagementLevels", self.targeted_app_management_levels)
    
    @property
    def targeted_app_management_levels(self,) -> Optional[app_management_level.AppManagementLevel]:
        """
        Gets the targetedAppManagementLevels property value. Management levels for apps
        Returns: Optional[app_management_level.AppManagementLevel]
        """
        return self._targeted_app_management_levels
    
    @targeted_app_management_levels.setter
    def targeted_app_management_levels(self,value: Optional[app_management_level.AppManagementLevel] = None) -> None:
        """
        Sets the targetedAppManagementLevels property value. Management levels for apps
        Args:
            value: Value to set for the targetedAppManagementLevels property.
        """
        self._targeted_app_management_levels = value
    

