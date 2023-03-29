from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity
    from .windows_updates import catalog, deployment, deployment_audience, resource_connection, updatable_asset, update_policy

from . import entity

class AdminWindowsUpdates(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new adminWindowsUpdates and sets the default values.
        """
        super().__init__()
        # Catalog of content that can be approved for deployment by the deployment service. Read-only.
        self._catalog: Optional[catalog.Catalog] = None
        # The set of updatableAsset resources to which a deployment can apply.
        self._deployment_audiences: Optional[List[deployment_audience.DeploymentAudience]] = None
        # Deployments created using the deployment service.
        self._deployments: Optional[List[deployment.Deployment]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Service connections to external resources such as analytics workspaces.
        self._resource_connections: Optional[List[resource_connection.ResourceConnection]] = None
        # Assets registered with the deployment service that can receive updates.
        self._updatable_assets: Optional[List[updatable_asset.UpdatableAsset]] = None
        # A collection of policies for approving the deployment of different content to an audience over time.
        self._update_policies: Optional[List[update_policy.UpdatePolicy]] = None
    
    @property
    def catalog(self,) -> Optional[catalog.Catalog]:
        """
        Gets the catalog property value. Catalog of content that can be approved for deployment by the deployment service. Read-only.
        Returns: Optional[catalog.Catalog]
        """
        return self._catalog
    
    @catalog.setter
    def catalog(self,value: Optional[catalog.Catalog] = None) -> None:
        """
        Sets the catalog property value. Catalog of content that can be approved for deployment by the deployment service. Read-only.
        Args:
            value: Value to set for the catalog property.
        """
        self._catalog = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminWindowsUpdates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdminWindowsUpdates
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdminWindowsUpdates()
    
    @property
    def deployment_audiences(self,) -> Optional[List[deployment_audience.DeploymentAudience]]:
        """
        Gets the deploymentAudiences property value. The set of updatableAsset resources to which a deployment can apply.
        Returns: Optional[List[deployment_audience.DeploymentAudience]]
        """
        return self._deployment_audiences
    
    @deployment_audiences.setter
    def deployment_audiences(self,value: Optional[List[deployment_audience.DeploymentAudience]] = None) -> None:
        """
        Sets the deploymentAudiences property value. The set of updatableAsset resources to which a deployment can apply.
        Args:
            value: Value to set for the deployment_audiences property.
        """
        self._deployment_audiences = value
    
    @property
    def deployments(self,) -> Optional[List[deployment.Deployment]]:
        """
        Gets the deployments property value. Deployments created using the deployment service.
        Returns: Optional[List[deployment.Deployment]]
        """
        return self._deployments
    
    @deployments.setter
    def deployments(self,value: Optional[List[deployment.Deployment]] = None) -> None:
        """
        Sets the deployments property value. Deployments created using the deployment service.
        Args:
            value: Value to set for the deployments property.
        """
        self._deployments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity
        from .windows_updates import catalog, deployment, deployment_audience, resource_connection, updatable_asset, update_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(catalog.Catalog)),
            "deployments": lambda n : setattr(self, 'deployments', n.get_collection_of_object_values(deployment.Deployment)),
            "deploymentAudiences": lambda n : setattr(self, 'deployment_audiences', n.get_collection_of_object_values(deployment_audience.DeploymentAudience)),
            "resourceConnections": lambda n : setattr(self, 'resource_connections', n.get_collection_of_object_values(resource_connection.ResourceConnection)),
            "updatableAssets": lambda n : setattr(self, 'updatable_assets', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
            "updatePolicies": lambda n : setattr(self, 'update_policies', n.get_collection_of_object_values(update_policy.UpdatePolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_connections(self,) -> Optional[List[resource_connection.ResourceConnection]]:
        """
        Gets the resourceConnections property value. Service connections to external resources such as analytics workspaces.
        Returns: Optional[List[resource_connection.ResourceConnection]]
        """
        return self._resource_connections
    
    @resource_connections.setter
    def resource_connections(self,value: Optional[List[resource_connection.ResourceConnection]] = None) -> None:
        """
        Sets the resourceConnections property value. Service connections to external resources such as analytics workspaces.
        Args:
            value: Value to set for the resource_connections property.
        """
        self._resource_connections = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("catalog", self.catalog)
        writer.write_collection_of_object_values("deployments", self.deployments)
        writer.write_collection_of_object_values("deploymentAudiences", self.deployment_audiences)
        writer.write_collection_of_object_values("resourceConnections", self.resource_connections)
        writer.write_collection_of_object_values("updatableAssets", self.updatable_assets)
        writer.write_collection_of_object_values("updatePolicies", self.update_policies)
    
    @property
    def updatable_assets(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the updatableAssets property value. Assets registered with the deployment service that can receive updates.
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._updatable_assets
    
    @updatable_assets.setter
    def updatable_assets(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the updatableAssets property value. Assets registered with the deployment service that can receive updates.
        Args:
            value: Value to set for the updatable_assets property.
        """
        self._updatable_assets = value
    
    @property
    def update_policies(self,) -> Optional[List[update_policy.UpdatePolicy]]:
        """
        Gets the updatePolicies property value. A collection of policies for approving the deployment of different content to an audience over time.
        Returns: Optional[List[update_policy.UpdatePolicy]]
        """
        return self._update_policies
    
    @update_policies.setter
    def update_policies(self,value: Optional[List[update_policy.UpdatePolicy]] = None) -> None:
        """
        Sets the updatePolicies property value. A collection of policies for approving the deployment of different content to an audience over time.
        Args:
            value: Value to set for the update_policies property.
        """
        self._update_policies = value
    

