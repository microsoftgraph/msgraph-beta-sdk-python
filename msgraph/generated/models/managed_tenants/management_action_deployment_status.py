from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

management_action_status = lazy_import('msgraph.generated.models.managed_tenants.management_action_status')
workload_action_deployment_status = lazy_import('msgraph.generated.models.managed_tenants.workload_action_deployment_status')

class ManagementActionDeploymentStatus(AdditionalDataHolder, Parsable):
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
        Instantiates a new managementActionDeploymentStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier for the management action. Required. Read-only.
        self._management_action_id: Optional[str] = None
        # The management template identifier that was used to generate the management action. Required. Read-only.
        self._management_template_id: Optional[str] = None
        # The managementTemplateVersion property
        self._management_template_version: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status property
        self._status: Optional[management_action_status.ManagementActionStatus] = None
        # The collection of workload action deployment statues for the given management action. Optional.
        self._workload_action_deployment_statuses: Optional[List[workload_action_deployment_status.WorkloadActionDeploymentStatus]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementActionDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementActionDeploymentStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementActionDeploymentStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "management_action_id": lambda n : setattr(self, 'management_action_id', n.get_str_value()),
            "management_template_id": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "management_template_version": lambda n : setattr(self, 'management_template_version', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(management_action_status.ManagementActionStatus)),
            "workload_action_deployment_statuses": lambda n : setattr(self, 'workload_action_deployment_statuses', n.get_collection_of_object_values(workload_action_deployment_status.WorkloadActionDeploymentStatus)),
        }
        return fields
    
    @property
    def management_action_id(self,) -> Optional[str]:
        """
        Gets the managementActionId property value. The identifier for the management action. Required. Read-only.
        Returns: Optional[str]
        """
        return self._management_action_id
    
    @management_action_id.setter
    def management_action_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementActionId property value. The identifier for the management action. Required. Read-only.
        Args:
            value: Value to set for the managementActionId property.
        """
        self._management_action_id = value
    
    @property
    def management_template_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateId property value. The management template identifier that was used to generate the management action. Required. Read-only.
        Returns: Optional[str]
        """
        return self._management_template_id
    
    @management_template_id.setter
    def management_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateId property value. The management template identifier that was used to generate the management action. Required. Read-only.
        Args:
            value: Value to set for the managementTemplateId property.
        """
        self._management_template_id = value
    
    @property
    def management_template_version(self,) -> Optional[int]:
        """
        Gets the managementTemplateVersion property value. The managementTemplateVersion property
        Returns: Optional[int]
        """
        return self._management_template_version
    
    @management_template_version.setter
    def management_template_version(self,value: Optional[int] = None) -> None:
        """
        Sets the managementTemplateVersion property value. The managementTemplateVersion property
        Args:
            value: Value to set for the managementTemplateVersion property.
        """
        self._management_template_version = value
    
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
        writer.write_str_value("managementActionId", self.management_action_id)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_int_value("managementTemplateVersion", self.management_template_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("workloadActionDeploymentStatuses", self.workload_action_deployment_statuses)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[management_action_status.ManagementActionStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[management_action_status.ManagementActionStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[management_action_status.ManagementActionStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def workload_action_deployment_statuses(self,) -> Optional[List[workload_action_deployment_status.WorkloadActionDeploymentStatus]]:
        """
        Gets the workloadActionDeploymentStatuses property value. The collection of workload action deployment statues for the given management action. Optional.
        Returns: Optional[List[workload_action_deployment_status.WorkloadActionDeploymentStatus]]
        """
        return self._workload_action_deployment_statuses
    
    @workload_action_deployment_statuses.setter
    def workload_action_deployment_statuses(self,value: Optional[List[workload_action_deployment_status.WorkloadActionDeploymentStatus]] = None) -> None:
        """
        Sets the workloadActionDeploymentStatuses property value. The collection of workload action deployment statues for the given management action. Optional.
        Args:
            value: Value to set for the workloadActionDeploymentStatuses property.
        """
        self._workload_action_deployment_statuses = value
    

