from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
catalog = lazy_import('msgraph.generated.models.windows_updates.catalog')
deployment = lazy_import('msgraph.generated.models.windows_updates.deployment')
deployment_audience = lazy_import('msgraph.generated.models.windows_updates.deployment_audience')
resource_connection = lazy_import('msgraph.generated.models.windows_updates.resource_connection')
updatable_asset = lazy_import('msgraph.generated.models.windows_updates.updatable_asset')
update_policy = lazy_import('msgraph.generated.models.windows_updates.update_policy')

class AdminWindowsUpdates(entity.Entity):
    @property
    def catalog(self,) -> Optional[catalog.Catalog]:
        """
        Gets the catalog property value. The catalog property
        Returns: Optional[catalog.Catalog]
        """
        return self._catalog
    
    @catalog.setter
    def catalog(self,value: Optional[catalog.Catalog] = None) -> None:
        """
        Sets the catalog property value. The catalog property
        Args:
            value: Value to set for the catalog property.
        """
        self._catalog = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new adminWindowsUpdates and sets the default values.
        """
        super().__init__()
        # The catalog property
        self._catalog: Optional[catalog.Catalog] = None
        # The deploymentAudiences property
        self._deployment_audiences: Optional[List[deployment_audience.DeploymentAudience]] = None
        # The deployments property
        self._deployments: Optional[List[deployment.Deployment]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The resourceConnections property
        self._resource_connections: Optional[List[resource_connection.ResourceConnection]] = None
        # The updatableAssets property
        self._updatable_assets: Optional[List[updatable_asset.UpdatableAsset]] = None
        # The updatePolicies property
        self._update_policies: Optional[List[update_policy.UpdatePolicy]] = None
    
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
        Gets the deploymentAudiences property value. The deploymentAudiences property
        Returns: Optional[List[deployment_audience.DeploymentAudience]]
        """
        return self._deployment_audiences
    
    @deployment_audiences.setter
    def deployment_audiences(self,value: Optional[List[deployment_audience.DeploymentAudience]] = None) -> None:
        """
        Sets the deploymentAudiences property value. The deploymentAudiences property
        Args:
            value: Value to set for the deployment_audiences property.
        """
        self._deployment_audiences = value
    
    @property
    def deployments(self,) -> Optional[List[deployment.Deployment]]:
        """
        Gets the deployments property value. The deployments property
        Returns: Optional[List[deployment.Deployment]]
        """
        return self._deployments
    
    @deployments.setter
    def deployments(self,value: Optional[List[deployment.Deployment]] = None) -> None:
        """
        Sets the deployments property value. The deployments property
        Args:
            value: Value to set for the deployments property.
        """
        self._deployments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
        Gets the resourceConnections property value. The resourceConnections property
        Returns: Optional[List[resource_connection.ResourceConnection]]
        """
        return self._resource_connections
    
    @resource_connections.setter
    def resource_connections(self,value: Optional[List[resource_connection.ResourceConnection]] = None) -> None:
        """
        Sets the resourceConnections property value. The resourceConnections property
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
        Gets the updatableAssets property value. The updatableAssets property
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._updatable_assets
    
    @updatable_assets.setter
    def updatable_assets(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the updatableAssets property value. The updatableAssets property
        Args:
            value: Value to set for the updatable_assets property.
        """
        self._updatable_assets = value
    
    @property
    def update_policies(self,) -> Optional[List[update_policy.UpdatePolicy]]:
        """
        Gets the updatePolicies property value. The updatePolicies property
        Returns: Optional[List[update_policy.UpdatePolicy]]
        """
        return self._update_policies
    
    @update_policies.setter
    def update_policies(self,value: Optional[List[update_policy.UpdatePolicy]] = None) -> None:
        """
        Sets the updatePolicies property value. The updatePolicies property
        Args:
            value: Value to set for the update_policies property.
        """
        self._update_policies = value
    

