from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
management_action_deployment_status = lazy_import('msgraph.generated.models.managed_tenants.management_action_deployment_status')

class ManagementActionTenantDeploymentStatus(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managementActionTenantDeploymentStatus and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of deployment status for each instance of a management action. Optional.
        self._statuses: Optional[List[management_action_deployment_status.ManagementActionDeploymentStatus]] = None
        # The identifier for the tenant group that is associated with the management action. Required. Read-only.
        self._tenant_group_id: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementActionTenantDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementActionTenantDeploymentStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementActionTenantDeploymentStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "statuses": lambda n : setattr(self, 'statuses', n.get_collection_of_object_values(management_action_deployment_status.ManagementActionDeploymentStatus)),
            "tenant_group_id": lambda n : setattr(self, 'tenant_group_id', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("statuses", self.statuses)
        writer.write_str_value("tenantGroupId", self.tenant_group_id)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def statuses(self,) -> Optional[List[management_action_deployment_status.ManagementActionDeploymentStatus]]:
        """
        Gets the statuses property value. The collection of deployment status for each instance of a management action. Optional.
        Returns: Optional[List[management_action_deployment_status.ManagementActionDeploymentStatus]]
        """
        return self._statuses
    
    @statuses.setter
    def statuses(self,value: Optional[List[management_action_deployment_status.ManagementActionDeploymentStatus]] = None) -> None:
        """
        Sets the statuses property value. The collection of deployment status for each instance of a management action. Optional.
        Args:
            value: Value to set for the statuses property.
        """
        self._statuses = value
    
    @property
    def tenant_group_id(self,) -> Optional[str]:
        """
        Gets the tenantGroupId property value. The identifier for the tenant group that is associated with the management action. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_group_id
    
    @tenant_group_id.setter
    def tenant_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantGroupId property value. The identifier for the tenant group that is associated with the management action. Required. Read-only.
        Args:
            value: Value to set for the tenantGroupId property.
        """
        self._tenant_group_id = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

