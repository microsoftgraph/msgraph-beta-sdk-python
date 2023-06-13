from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, windows_defender_application_control_supplemental_policy_assignment, windows_defender_application_control_supplemental_policy_deployment_status, windows_defender_application_control_supplemental_policy_deployment_summary

from . import entity

@dataclass
class WindowsDefenderApplicationControlSupplementalPolicy(entity.Entity):
    # The associated group assignments for this WindowsDefenderApplicationControl supplemental policy.
    assignments: Optional[List[windows_defender_application_control_supplemental_policy_assignment.WindowsDefenderApplicationControlSupplementalPolicyAssignment]] = None
    # The WindowsDefenderApplicationControl supplemental policy content in byte array format.
    content: Optional[bytes] = None
    # The WindowsDefenderApplicationControl supplemental policy content's file name.
    content_file_name: Optional[str] = None
    # The date and time when the WindowsDefenderApplicationControl supplemental policy was uploaded.
    creation_date_time: Optional[datetime] = None
    # WindowsDefenderApplicationControl supplemental policy deployment summary.
    deploy_summary: Optional[windows_defender_application_control_supplemental_policy_deployment_summary.WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary] = None
    # The description of WindowsDefenderApplicationControl supplemental policy.
    description: Optional[str] = None
    # The list of device deployment states for this WindowsDefenderApplicationControl supplemental policy.
    device_statuses: Optional[List[windows_defender_application_control_supplemental_policy_deployment_status.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus]] = None
    # The display name of WindowsDefenderApplicationControl supplemental policy.
    display_name: Optional[str] = None
    # The date and time when the WindowsDefenderApplicationControl supplemental policy was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this WindowsDefenderApplicationControl supplemental policy entity.
    role_scope_tag_ids: Optional[List[str]] = None
    # The WindowsDefenderApplicationControl supplemental policy's version.
    version: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, windows_defender_application_control_supplemental_policy_assignment, windows_defender_application_control_supplemental_policy_deployment_status, windows_defender_application_control_supplemental_policy_deployment_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(windows_defender_application_control_supplemental_policy_assignment.WindowsDefenderApplicationControlSupplementalPolicyAssignment)),
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "contentFileName": lambda n : setattr(self, 'content_file_name', n.get_str_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "deploySummary": lambda n : setattr(self, 'deploy_summary', n.get_object_value(windows_defender_application_control_supplemental_policy_deployment_summary.WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(windows_defender_application_control_supplemental_policy_deployment_status.WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
    

