from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import all_devices_assignment_target, all_licensed_users_assignment_target, android_fota_deployment_assignment_target, configuration_manager_collection_assignment_target, device_and_app_management_assignment_filter_type, exclusion_group_assignment_target, group_assignment_target

@dataclass
class DeviceAndAppManagementAssignmentTarget(AdditionalDataHolder, Parsable):
    """
    Base type for assignment targets.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Id of the filter for the target assignment.
    device_and_app_management_assignment_filter_id: Optional[str] = None
    # Represents type of the assignment filter.
    device_and_app_management_assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignmentTarget
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allDevicesAssignmentTarget".casefold():
            from . import all_devices_assignment_target

            return all_devices_assignment_target.AllDevicesAssignmentTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allLicensedUsersAssignmentTarget".casefold():
            from . import all_licensed_users_assignment_target

            return all_licensed_users_assignment_target.AllLicensedUsersAssignmentTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidFotaDeploymentAssignmentTarget".casefold():
            from . import android_fota_deployment_assignment_target

            return android_fota_deployment_assignment_target.AndroidFotaDeploymentAssignmentTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.configurationManagerCollectionAssignmentTarget".casefold():
            from . import configuration_manager_collection_assignment_target

            return configuration_manager_collection_assignment_target.ConfigurationManagerCollectionAssignmentTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exclusionGroupAssignmentTarget".casefold():
            from . import exclusion_group_assignment_target

            return exclusion_group_assignment_target.ExclusionGroupAssignmentTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupAssignmentTarget".casefold():
            from . import group_assignment_target

            return group_assignment_target.GroupAssignmentTarget()
        return DeviceAndAppManagementAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import all_devices_assignment_target, all_licensed_users_assignment_target, android_fota_deployment_assignment_target, configuration_manager_collection_assignment_target, device_and_app_management_assignment_filter_type, exclusion_group_assignment_target, group_assignment_target

        from . import all_devices_assignment_target, all_licensed_users_assignment_target, android_fota_deployment_assignment_target, configuration_manager_collection_assignment_target, device_and_app_management_assignment_filter_type, exclusion_group_assignment_target, group_assignment_target

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceAndAppManagementAssignmentFilterId": lambda n : setattr(self, 'device_and_app_management_assignment_filter_id', n.get_str_value()),
            "deviceAndAppManagementAssignmentFilterType": lambda n : setattr(self, 'device_and_app_management_assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("deviceAndAppManagementAssignmentFilterId", self.device_and_app_management_assignment_filter_id)
        writer.write_enum_value("deviceAndAppManagementAssignmentFilterType", self.device_and_app_management_assignment_filter_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

