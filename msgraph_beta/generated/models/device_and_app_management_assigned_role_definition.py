from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceAndAppManagementAssignedRoleDefinition(AdditionalDataHolder, BackedModel, Parsable):
    """
    Complex type to represent the role that is assigned to the user. This type contains the ID, the display name, and the permissions of the role.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # A list of permissions based on its associated role. Each permission defines the specific actions the user can perform on Intune resources, such as managing devices, applications, or configurations. Some possible values are: Microsoft.Intune/MobileApps/Read, Microsoft.Intune/DeviceConfigurations/Write, Microsoft.Intune/ManagedDevices/Retire, and Microsoft.Intune/DeviceCompliancePolicies/Assign. This Permissions property offers a comprehensive view of the user's effective access rights, ensuring that they can only perform actions relevant to their assigned roles. This property is read-only.
    permissions: Optional[list[str]] = None
    # The RoleDefinitionDisplayName property represents the human-readable name of a specific role definition in Microsoft Intune. This property provides a clear and descriptive name that indicates the purpose or scope of the role, helping administrators identify and assign appropriate roles to users or groups.Some example values for RoleDefinitionDisplayName might include: 'Helpdesk Operator,' 'Application Manager,' or 'Policy Administrator.' This display name is primarily used in the Intune console or Graph API to present roles in a user-friendly manner, making it easier for administrators to manage role-based access control (RBAC) efficiently. This property is read-only.
    role_definition_display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceAndAppManagementAssignedRoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignedRoleDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceAndAppManagementAssignedRoleDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "roleDefinitionDisplayName": lambda n : setattr(self, 'role_definition_display_name', n.get_str_value()),
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
    

