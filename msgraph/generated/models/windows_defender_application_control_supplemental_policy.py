from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
windows_defender_application_control_supplemental_policy_assignment = lazy_import('msgraph.generated.models.windows_defender_application_control_supplemental_policy_assignment')
windows_defender_application_control_supplemental_policy_deployment_status = lazy_import('msgraph.generated.models.windows_defender_application_control_supplemental_policy_deployment_status')
windows_defender_application_control_supplemental_policy_deployment_summary = lazy_import('msgraph.generated.models.windows_defender_application_control_supplemental_policy_deployment_summary')

class WindowsDefenderApplicationControlSupplementalPolicy(entity.Entity):
    """
    Provides operations to manage the deviceAppManagement singleton.
    """
    @property
    def assignments(self,) -> Optional[List[windows_defender_application_control_supplemental_policy_assignment.WindowsDefenderApplicationControlSupplementalPolicyAssignment]]:
        """
        Gets the assignments property value. The associated group assignments for this WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[List[windows_defender_application_control_supplemental_policy_assignment.WindowsDefenderApplicationControlSupplementalPolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[windows_defender_application_control_supplemental_policy_assignment.WindowsDefenderApplicationControlSupplementalPolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. The associated group assignments for this WindowsDefenderApplicationControl supplemental policy.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsDefenderApplicationControlSupplementalPolicy and sets the default values.
        """
        super().__init__()
        # The associated group assignments for this WindowsDefenderApplicationControl supplemental policy.
        self._assignments: Optional[List[windows_defender_application_control_supplemental_policy_assignment.WindowsDefenderApplicationControlSupplementalPolicyAssignment]] = None
        # The WindowsDefenderApplicationControl supplemental policy content in byte array format.
        self._content: Optional[bytes] = None
        # The WindowsDefenderApplicationControl supplemental policy content's file name.
        self._content_file_name: Optional[str] = None
        # The date and time when the WindowsDefenderApplicationControl supplemental policy was uploaded.
        self._creation_date_time: Optional[datetime] = None
        # WindowsDefenderApplicationControl supplemental policy deployment summary.
        self._deploy_summary: Optional[windows_defender_application_control_supplemental_policy_deployment_summary.WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary] = None
        # The description of WindowsDefenderApplicationControl supplemental policy.
        self._description: Optional[str] = None
        # The list of device deployment states for this WindowsDefenderApplicationControl supplemental policy.
        self._device_statuses: Optional[List[windows_defender_application_control_supplemental_policy_deployment_status.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus]] = None
        # The display name of WindowsDefenderApplicationControl supplemental policy.
        self._display_name: Optional[str] = None
        # The date and time when the WindowsDefenderApplicationControl supplemental policy was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this WindowsDefenderApplicationControl supplemental policy entity.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The WindowsDefenderApplicationControl supplemental policy's version.
        self._version: Optional[str] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The WindowsDefenderApplicationControl supplemental policy content in byte array format.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The WindowsDefenderApplicationControl supplemental policy content in byte array format.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def content_file_name(self,) -> Optional[str]:
        """
        Gets the contentFileName property value. The WindowsDefenderApplicationControl supplemental policy content's file name.
        Returns: Optional[str]
        """
        return self._content_file_name
    
    @content_file_name.setter
    def content_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the contentFileName property value. The WindowsDefenderApplicationControl supplemental policy content's file name.
        Args:
            value: Value to set for the contentFileName property.
        """
        self._content_file_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderApplicationControlSupplementalPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderApplicationControlSupplementalPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDefenderApplicationControlSupplementalPolicy()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. The date and time when the WindowsDefenderApplicationControl supplemental policy was uploaded.
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. The date and time when the WindowsDefenderApplicationControl supplemental policy was uploaded.
        Args:
            value: Value to set for the creationDateTime property.
        """
        self._creation_date_time = value
    
    @property
    def deploy_summary(self,) -> Optional[windows_defender_application_control_supplemental_policy_deployment_summary.WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary]:
        """
        Gets the deploySummary property value. WindowsDefenderApplicationControl supplemental policy deployment summary.
        Returns: Optional[windows_defender_application_control_supplemental_policy_deployment_summary.WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary]
        """
        return self._deploy_summary
    
    @deploy_summary.setter
    def deploy_summary(self,value: Optional[windows_defender_application_control_supplemental_policy_deployment_summary.WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary] = None) -> None:
        """
        Sets the deploySummary property value. WindowsDefenderApplicationControl supplemental policy deployment summary.
        Args:
            value: Value to set for the deploySummary property.
        """
        self._deploy_summary = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of WindowsDefenderApplicationControl supplemental policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_statuses(self,) -> Optional[List[windows_defender_application_control_supplemental_policy_deployment_status.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus]]:
        """
        Gets the deviceStatuses property value. The list of device deployment states for this WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[List[windows_defender_application_control_supplemental_policy_deployment_status.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[windows_defender_application_control_supplemental_policy_deployment_status.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. The list of device deployment states for this WindowsDefenderApplicationControl supplemental policy.
        Args:
            value: Value to set for the deviceStatuses property.
        """
        self._device_statuses = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of WindowsDefenderApplicationControl supplemental policy.
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(windows_defender_application_control_supplemental_policy_assignment.WindowsDefenderApplicationControlSupplementalPolicyAssignment)),
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "content_file_name": lambda n : setattr(self, 'content_file_name', n.get_str_value()),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "deploy_summary": lambda n : setattr(self, 'deploy_summary', n.get_object_value(windows_defender_application_control_supplemental_policy_deployment_summary.WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_statuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(windows_defender_application_control_supplemental_policy_deployment_status.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the WindowsDefenderApplicationControl supplemental policy was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the WindowsDefenderApplicationControl supplemental policy was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this WindowsDefenderApplicationControl supplemental policy entity.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this WindowsDefenderApplicationControl supplemental policy entity.
        Args:
            value: Value to set for the roleScopeTagIds property.
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_object_value("content", self.content)
        writer.write_str_value("contentFileName", self.content_file_name)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("deploySummary", self.deploy_summary)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The WindowsDefenderApplicationControl supplemental policy's version.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The WindowsDefenderApplicationControl supplemental policy's version.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

