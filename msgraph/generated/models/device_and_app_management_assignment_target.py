from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import all_devices_assignment_target, all_licensed_users_assignment_target, android_fota_deployment_assignment_target, configuration_manager_collection_assignment_target, device_and_app_management_assignment_filter_type, exclusion_group_assignment_target, group_assignment_target

class DeviceAndAppManagementAssignmentTarget(AdditionalDataHolder, Parsable):
    """
    Base type for assignment targets.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceAndAppManagementAssignmentTarget and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Id of the filter for the target assignment.
        self._device_and_app_management_assignment_filter_id: Optional[str] = None
        # Represents type of the assignment filter.
        self._device_and_app_management_assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignmentTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.allDevicesAssignmentTarget":
                from . import all_devices_assignment_target

                return all_devices_assignment_target.AllDevicesAssignmentTarget()
            if mapping_value == "#microsoft.graph.allLicensedUsersAssignmentTarget":
                from . import all_licensed_users_assignment_target

                return all_licensed_users_assignment_target.AllLicensedUsersAssignmentTarget()
            if mapping_value == "#microsoft.graph.androidFotaDeploymentAssignmentTarget":
                from . import android_fota_deployment_assignment_target

                return android_fota_deployment_assignment_target.AndroidFotaDeploymentAssignmentTarget()
            if mapping_value == "#microsoft.graph.configurationManagerCollectionAssignmentTarget":
                from . import configuration_manager_collection_assignment_target

                return configuration_manager_collection_assignment_target.ConfigurationManagerCollectionAssignmentTarget()
            if mapping_value == "#microsoft.graph.exclusionGroupAssignmentTarget":
                from . import exclusion_group_assignment_target

                return exclusion_group_assignment_target.ExclusionGroupAssignmentTarget()
            if mapping_value == "#microsoft.graph.groupAssignmentTarget":
                from . import group_assignment_target

                return group_assignment_target.GroupAssignmentTarget()
        return DeviceAndAppManagementAssignmentTarget()
    
    @property
    def device_and_app_management_assignment_filter_id(self,) -> Optional[str]:
        """
        Gets the deviceAndAppManagementAssignmentFilterId property value. The Id of the filter for the target assignment.
        Returns: Optional[str]
        """
        return self._device_and_app_management_assignment_filter_id
    
    @device_and_app_management_assignment_filter_id.setter
    def device_and_app_management_assignment_filter_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAndAppManagementAssignmentFilterId property value. The Id of the filter for the target assignment.
        Args:
            value: Value to set for the device_and_app_management_assignment_filter_id property.
        """
        self._device_and_app_management_assignment_filter_id = value
    
    @property
    def device_and_app_management_assignment_filter_type(self,) -> Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]:
        """
        Gets the deviceAndAppManagementAssignmentFilterType property value. Represents type of the assignment filter.
        Returns: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]
        """
        return self._device_and_app_management_assignment_filter_type
    
    @device_and_app_management_assignment_filter_type.setter
    def device_and_app_management_assignment_filter_type(self,value: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None) -> None:
        """
        Sets the deviceAndAppManagementAssignmentFilterType property value. Represents type of the assignment filter.
        Args:
            value: Value to set for the device_and_app_management_assignment_filter_type property.
        """
        self._device_and_app_management_assignment_filter_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import all_devices_assignment_target, all_licensed_users_assignment_target, android_fota_deployment_assignment_target, configuration_manager_collection_assignment_target, device_and_app_management_assignment_filter_type, exclusion_group_assignment_target, group_assignment_target

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceAndAppManagementAssignmentFilterId": lambda n : setattr(self, 'device_and_app_management_assignment_filter_id', n.get_str_value()),
            "deviceAndAppManagementAssignmentFilterType": lambda n : setattr(self, 'device_and_app_management_assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("deviceAndAppManagementAssignmentFilterId", self.device_and_app_management_assignment_filter_id)
        writer.write_enum_value("deviceAndAppManagementAssignmentFilterType", self.device_and_app_management_assignment_filter_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

