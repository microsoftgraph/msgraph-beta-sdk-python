from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_management_level, managed_app_configuration, managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_group_type, targeted_managed_app_policy_assignment

from . import managed_app_configuration

@dataclass
class TargetedManagedAppConfiguration(managed_app_configuration.ManagedAppConfiguration):
    odata_type = "#microsoft.graph.targetedManagedAppConfiguration"
    # Indicates a collection of apps to target which can be one of several pre-defined lists of apps or a manually selected list of apps
    app_group_type: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType] = None
    # List of apps to which the policy is deployed.
    apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
    # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
    assignments: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
    # Indicates if the policy is deployed to any inclusion groups or not.
    is_assigned: Optional[bool] = None
    # Management levels for apps
    targeted_app_management_levels: Optional[app_management_level.AppManagementLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TargetedManagedAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TargetedManagedAppConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TargetedManagedAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_management_level, managed_app_configuration, managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_group_type, targeted_managed_app_policy_assignment

        fields: Dict[str, Callable[[Any], None]] = {
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "appGroupType": lambda n : setattr(self, 'app_group_type', n.get_enum_value(targeted_managed_app_group_type.TargetedManagedAppGroupType)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment)),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "targetedAppManagementLevels": lambda n : setattr(self, 'targeted_app_management_levels', n.get_enum_value(app_management_level.AppManagementLevel)),
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
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_enum_value("appGroupType", self.app_group_type)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("isAssigned", self.is_assigned)
        writer.write_enum_value("targetedAppManagementLevels", self.targeted_app_management_levels)
    

