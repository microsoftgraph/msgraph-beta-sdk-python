from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_fota_deployment_assignment, entity, zebra_fota_deployment_settings, zebra_fota_deployment_status

from . import entity

class ZebraFotaDeployment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ZebraFotaDeployment and sets the default values.
        """
        super().__init__()
        # Collection of Android FOTA Assignment
        self._deployment_assignments: Optional[List[android_fota_deployment_assignment.AndroidFotaDeploymentAssignment]] = None
        # The Zebra FOTA deployment complex type that describes the settings required to create a FOTA deployment.
        self._deployment_settings: Optional[zebra_fota_deployment_settings.ZebraFotaDeploymentSettings] = None
        # Represents the deployment status from Zebra. The status is a high level status of the deployment as opposed being a detailed status per device.
        self._deployment_status: Optional[zebra_fota_deployment_status.ZebraFotaDeploymentStatus] = None
        # A human readable description of the deployment.
        self._description: Optional[str] = None
        # A human readable name of the deployment.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Entity instance
        self._role_scope_tag_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ZebraFotaDeployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaDeployment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ZebraFotaDeployment()
    
    @property
    def deployment_assignments(self,) -> Optional[List[android_fota_deployment_assignment.AndroidFotaDeploymentAssignment]]:
        """
        Gets the deploymentAssignments property value. Collection of Android FOTA Assignment
        Returns: Optional[List[android_fota_deployment_assignment.AndroidFotaDeploymentAssignment]]
        """
        return self._deployment_assignments
    
    @deployment_assignments.setter
    def deployment_assignments(self,value: Optional[List[android_fota_deployment_assignment.AndroidFotaDeploymentAssignment]] = None) -> None:
        """
        Sets the deploymentAssignments property value. Collection of Android FOTA Assignment
        Args:
            value: Value to set for the deployment_assignments property.
        """
        self._deployment_assignments = value
    
    @property
    def deployment_settings(self,) -> Optional[zebra_fota_deployment_settings.ZebraFotaDeploymentSettings]:
        """
        Gets the deploymentSettings property value. The Zebra FOTA deployment complex type that describes the settings required to create a FOTA deployment.
        Returns: Optional[zebra_fota_deployment_settings.ZebraFotaDeploymentSettings]
        """
        return self._deployment_settings
    
    @deployment_settings.setter
    def deployment_settings(self,value: Optional[zebra_fota_deployment_settings.ZebraFotaDeploymentSettings] = None) -> None:
        """
        Sets the deploymentSettings property value. The Zebra FOTA deployment complex type that describes the settings required to create a FOTA deployment.
        Args:
            value: Value to set for the deployment_settings property.
        """
        self._deployment_settings = value
    
    @property
    def deployment_status(self,) -> Optional[zebra_fota_deployment_status.ZebraFotaDeploymentStatus]:
        """
        Gets the deploymentStatus property value. Represents the deployment status from Zebra. The status is a high level status of the deployment as opposed being a detailed status per device.
        Returns: Optional[zebra_fota_deployment_status.ZebraFotaDeploymentStatus]
        """
        return self._deployment_status
    
    @deployment_status.setter
    def deployment_status(self,value: Optional[zebra_fota_deployment_status.ZebraFotaDeploymentStatus] = None) -> None:
        """
        Sets the deploymentStatus property value. Represents the deployment status from Zebra. The status is a high level status of the deployment as opposed being a detailed status per device.
        Args:
            value: Value to set for the deployment_status property.
        """
        self._deployment_status = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A human readable description of the deployment.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A human readable description of the deployment.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. A human readable name of the deployment.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. A human readable name of the deployment.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_fota_deployment_assignment, entity, zebra_fota_deployment_settings, zebra_fota_deployment_status

        fields: Dict[str, Callable[[Any], None]] = {
            "deploymentAssignments": lambda n : setattr(self, 'deployment_assignments', n.get_collection_of_object_values(android_fota_deployment_assignment.AndroidFotaDeploymentAssignment)),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(zebra_fota_deployment_settings.ZebraFotaDeploymentSettings)),
            "deploymentStatus": lambda n : setattr(self, 'deployment_status', n.get_object_value(zebra_fota_deployment_status.ZebraFotaDeploymentStatus)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance
        Args:
            value: Value to set for the role_scope_tag_ids property.
        """
        self._role_scope_tag_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("deploymentAssignments", self.deployment_assignments)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
        writer.write_object_value("deploymentStatus", self.deployment_status)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

