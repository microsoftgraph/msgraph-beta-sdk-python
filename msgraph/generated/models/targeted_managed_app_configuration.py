from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_management_level, managed_app_configuration, managed_app_policy_deployment_summary, managed_mobile_app, targeted_managed_app_group_type, targeted_managed_app_policy_assignment

from . import managed_app_configuration

class TargetedManagedAppConfiguration(managed_app_configuration.ManagedAppConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new TargetedManagedAppConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.targetedManagedAppConfiguration"
        # Indicates a collection of apps to target which can be one of several pre-defined lists of apps or a manually selected list of apps
        self._app_group_type: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType] = None
        # List of apps to which the policy is deployed.
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
        # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
        self._assignments: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None
        # Count of apps to which the current policy is deployed.
        self._deployed_app_count: Optional[int] = None
        # Navigation property to deployment summary of the configuration.
        self._deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
        # Indicates if the policy is deployed to any inclusion groups or not.
        self._is_assigned: Optional[bool] = None
        # Management levels for apps
        self._targeted_app_management_levels: Optional[app_management_level.AppManagementLevel] = None
    
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
            value: Value to set for the app_group_type property.
        """
        self._app_group_type = value
    
    @property
    def apps(self,) -> Optional[List[managed_mobile_app.ManagedMobileApp]]:
        """
        Gets the apps property value. List of apps to which the policy is deployed.
        Returns: Optional[List[managed_mobile_app.ManagedMobileApp]]
        """
        return self._apps
    
    @apps.setter
    def apps(self,value: Optional[List[managed_mobile_app.ManagedMobileApp]] = None) -> None:
        """
        Sets the apps property value. List of apps to which the policy is deployed.
        Args:
            value: Value to set for the apps property.
        """
        self._apps = value
    
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
    
    @property
    def deployed_app_count(self,) -> Optional[int]:
        """
        Gets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Returns: Optional[int]
        """
        return self._deployed_app_count
    
    @deployed_app_count.setter
    def deployed_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Args:
            value: Value to set for the deployed_app_count property.
        """
        self._deployed_app_count = value
    
    @property
    def deployment_summary(self,) -> Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]:
        """
        Gets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Returns: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]
        """
        return self._deployment_summary
    
    @deployment_summary.setter
    def deployment_summary(self,value: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None) -> None:
        """
        Sets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Args:
            value: Value to set for the deployment_summary property.
        """
        self._deployment_summary = value
    
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
            value: Value to set for the is_assigned property.
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
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_enum_value("appGroupType", self.app_group_type)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
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
            value: Value to set for the targeted_app_management_levels property.
        """
        self._targeted_app_management_levels = value
    

