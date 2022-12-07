from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

generic_error = lazy_import('msgraph.generated.models.generic_error')
workload_action_status = lazy_import('msgraph.generated.models.managed_tenants.workload_action_status')

class WorkloadActionDeploymentStatus(AdditionalDataHolder, Parsable):
    @property
    def action_id(self,) -> Optional[str]:
        """
        Gets the actionId property value. The unique identifier for the workload action. Required. Read-only.
        Returns: Optional[str]
        """
        return self._action_id
    
    @action_id.setter
    def action_id(self,value: Optional[str] = None) -> None:
        """
        Sets the actionId property value. The unique identifier for the workload action. Required. Read-only.
        Args:
            value: Value to set for the actionId property.
        """
        self._action_id = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new workloadActionDeploymentStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier for the workload action. Required. Read-only.
        self._action_id: Optional[str] = None
        # The identifier of any policy that was created by applying the workload action. Optional. Read-only.
        self._deployed_policy_id: Optional[str] = None
        # The detailed information for exceptions that occur when deploying the workload action. Optional. Required.
        self._error: Optional[generic_error.GenericError] = None
        # The excludeGroups property
        self._exclude_groups: Optional[List[str]] = None
        # The includeAllUsers property
        self._include_all_users: Optional[bool] = None
        # The includeGroups property
        self._include_groups: Optional[List[str]] = None
        # The date and time the workload action was last deployed. Optional.
        self._last_deployment_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status property
        self._status: Optional[workload_action_status.WorkloadActionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkloadActionDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkloadActionDeploymentStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkloadActionDeploymentStatus()
    
    @property
    def deployed_policy_id(self,) -> Optional[str]:
        """
        Gets the deployedPolicyId property value. The identifier of any policy that was created by applying the workload action. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._deployed_policy_id
    
    @deployed_policy_id.setter
    def deployed_policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deployedPolicyId property value. The identifier of any policy that was created by applying the workload action. Optional. Read-only.
        Args:
            value: Value to set for the deployedPolicyId property.
        """
        self._deployed_policy_id = value
    
    @property
    def error(self,) -> Optional[generic_error.GenericError]:
        """
        Gets the error property value. The detailed information for exceptions that occur when deploying the workload action. Optional. Required.
        Returns: Optional[generic_error.GenericError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[generic_error.GenericError] = None) -> None:
        """
        Sets the error property value. The detailed information for exceptions that occur when deploying the workload action. Optional. Required.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    @property
    def exclude_groups(self,) -> Optional[List[str]]:
        """
        Gets the excludeGroups property value. The excludeGroups property
        Returns: Optional[List[str]]
        """
        return self._exclude_groups
    
    @exclude_groups.setter
    def exclude_groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeGroups property value. The excludeGroups property
        Args:
            value: Value to set for the excludeGroups property.
        """
        self._exclude_groups = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "deployed_policy_id": lambda n : setattr(self, 'deployed_policy_id', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(generic_error.GenericError)),
            "exclude_groups": lambda n : setattr(self, 'exclude_groups', n.get_collection_of_primitive_values(str)),
            "include_all_users": lambda n : setattr(self, 'include_all_users', n.get_bool_value()),
            "include_groups": lambda n : setattr(self, 'include_groups', n.get_collection_of_primitive_values(str)),
            "last_deployment_date_time": lambda n : setattr(self, 'last_deployment_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(workload_action_status.WorkloadActionStatus)),
        }
        return fields
    
    @property
    def include_all_users(self,) -> Optional[bool]:
        """
        Gets the includeAllUsers property value. The includeAllUsers property
        Returns: Optional[bool]
        """
        return self._include_all_users
    
    @include_all_users.setter
    def include_all_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeAllUsers property value. The includeAllUsers property
        Args:
            value: Value to set for the includeAllUsers property.
        """
        self._include_all_users = value
    
    @property
    def include_groups(self,) -> Optional[List[str]]:
        """
        Gets the includeGroups property value. The includeGroups property
        Returns: Optional[List[str]]
        """
        return self._include_groups
    
    @include_groups.setter
    def include_groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeGroups property value. The includeGroups property
        Args:
            value: Value to set for the includeGroups property.
        """
        self._include_groups = value
    
    @property
    def last_deployment_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastDeploymentDateTime property value. The date and time the workload action was last deployed. Optional.
        Returns: Optional[datetime]
        """
        return self._last_deployment_date_time
    
    @last_deployment_date_time.setter
    def last_deployment_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastDeploymentDateTime property value. The date and time the workload action was last deployed. Optional.
        Args:
            value: Value to set for the lastDeploymentDateTime property.
        """
        self._last_deployment_date_time = value
    
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
            value: Value to set for the OdataType property.
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
        writer.write_str_value("actionId", self.action_id)
        writer.write_str_value("deployedPolicyId", self.deployed_policy_id)
        writer.write_object_value("error", self.error)
        writer.write_collection_of_primitive_values("excludeGroups", self.exclude_groups)
        writer.write_bool_value("includeAllUsers", self.include_all_users)
        writer.write_collection_of_primitive_values("includeGroups", self.include_groups)
        writer.write_datetime_value("lastDeploymentDateTime", self.last_deployment_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[workload_action_status.WorkloadActionStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[workload_action_status.WorkloadActionStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[workload_action_status.WorkloadActionStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

