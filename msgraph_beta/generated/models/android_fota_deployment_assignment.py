from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

@dataclass
class AndroidFotaDeploymentAssignment(AdditionalDataHolder, BackedModel, Parsable):
    """
    Describes deployment security group to assign a deployment to. The backend will expand the security Group ID to extract device serial numbers prior sending a create deployment request to Zebra.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The Azure Active Directory (Azure AD) we are deploying firmware updates to (e.g.: d93c8f48-bd42-4514-ba40-bc6b84780930). NOTE: Use this property moving forward because the existing property, target, is deprecated.
    assignment_target: Optional[DeviceAndAppManagementAssignmentTarget] = None
    # The display name of the Azure AD security group used for the assignment.
    display_name: Optional[str] = None
    # A unique identifier assigned to each Android FOTA Assignment entity
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The AAD Group we are deploying firmware updates to
    target: Optional[AndroidFotaDeploymentAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidFotaDeploymentAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidFotaDeploymentAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidFotaDeploymentAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        from .android_fota_deployment_assignment_target import AndroidFotaDeploymentAssignmentTarget
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentTarget": lambda n : setattr(self, 'assignment_target', n.get_object_value(DeviceAndAppManagementAssignmentTarget)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(AndroidFotaDeploymentAssignmentTarget)),
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
        writer.write_object_value("assignmentTarget", self.assignment_target)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

