from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..generic_error import GenericError
    from .workload_action_status import WorkloadActionStatus

@dataclass
class WorkloadActionDeploymentStatus(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The unique identifier for the workload action. Required. Read-only.
    action_id: Optional[str] = None
    # The identifier of any policy that was created by applying the workload action. Optional. Read-only.
    deployed_policy_id: Optional[str] = None
    # The detailed information for exceptions that occur when deploying the workload action. Optional. Required.
    error: Optional[GenericError] = None
    # The excludeGroups property
    exclude_groups: Optional[List[str]] = None
    # The includeAllUsers property
    include_all_users: Optional[bool] = None
    # The includeGroups property
    include_groups: Optional[List[str]] = None
    # The date and time the workload action was last deployed. Optional.
    last_deployment_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[WorkloadActionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkloadActionDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkloadActionDeploymentStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkloadActionDeploymentStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..generic_error import GenericError
        from .workload_action_status import WorkloadActionStatus

        from ..generic_error import GenericError
        from .workload_action_status import WorkloadActionStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "actionId": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "deployedPolicyId": lambda n : setattr(self, 'deployed_policy_id', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(GenericError)),
            "excludeGroups": lambda n : setattr(self, 'exclude_groups', n.get_collection_of_primitive_values(str)),
            "includeAllUsers": lambda n : setattr(self, 'include_all_users', n.get_bool_value()),
            "includeGroups": lambda n : setattr(self, 'include_groups', n.get_collection_of_primitive_values(str)),
            "lastDeploymentDateTime": lambda n : setattr(self, 'last_deployment_date_time', n.get_datetime_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(WorkloadActionStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("actionId", self.action_id)
        writer.write_str_value("deployedPolicyId", self.deployed_policy_id)
        writer.write_object_value("error", self.error)
        writer.write_collection_of_primitive_values("excludeGroups", self.exclude_groups)
        writer.write_bool_value("includeAllUsers", self.include_all_users)
        writer.write_collection_of_primitive_values("includeGroups", self.include_groups)
        writer.write_datetime_value("lastDeploymentDateTime", self.last_deployment_date_time)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

