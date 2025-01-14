from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assigned_role_definition import DeviceAndAppManagementAssignedRoleDefinition

@dataclass
class DeviceAndAppManagementAssignedRoleDetail(AdditionalDataHolder, BackedModel, Parsable):
    """
    The DeviceAndAppManagementAssignedRoleDetail is a complex type in Microsoft Intune used to represent the Role Definitions and Permissions that are assigned to a specific user. This type provides a detailed view of the roles a user holds, along with the associated permissions that determine the specific actions the user can perform within Intune environment.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of permissions assigned to a specific user based on their associated role definitions. Each permission defines the specific actions the user can perform on Intune resources, such as managing devices, applications, or configurations. Some possible values are: Microsoft.Intune/MobileApps/Read, Microsoft.Intune/DeviceConfigurations/Write, Microsoft.Intune/ManagedDevices/Retire, and Microsoft.Intune/DeviceCompliancePolicies/Assign. This Permissions property provides a comprehensive view of the user's effective access rights, ensuring that they can only perform actions relevant to their assigned roles. This property is read-only.
    permissions: Optional[list[str]] = None
    # A collection of RoleDefinitions represents the various administrative roles that define permissions and access levels within Microsoft Intune. Each RoleDefinition outlines a set of permissions that determine the actions an admin or user can perform in the Intune environment. These permissions can include actions like reading or writing to specific resources, managing device configurations, deploying policies, or handling user data. RoleDefinitions are critical for enforcing role-based access control (RBAC), ensuring that administrators can only interact with the features and data relevant to their responsibilities. RoleDefinitions in Intune can either be built-in roles provided by Microsoft or custom roles created by an organization to tailor access based on specific needs. These definitions are referenced when assigning roles to users or groups, effectively controlling the scope of their administrative privileges. The collection of RoleDefinitions is managed through the Intune console or the Graph API, allowing for scalable role management across large environments. This property is read-only.
    role_definitions: Optional[list[DeviceAndAppManagementAssignedRoleDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceAndAppManagementAssignedRoleDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignedRoleDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceAndAppManagementAssignedRoleDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assigned_role_definition import DeviceAndAppManagementAssignedRoleDefinition

        from .device_and_app_management_assigned_role_definition import DeviceAndAppManagementAssignedRoleDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(DeviceAndAppManagementAssignedRoleDefinition)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

