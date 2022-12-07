from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
catalog = lazy_import('msgraph.generated.models.windows_updates.catalog')
deployment = lazy_import('msgraph.generated.models.windows_updates.deployment')
resource_connection = lazy_import('msgraph.generated.models.windows_updates.resource_connection')
updatable_asset = lazy_import('msgraph.generated.models.windows_updates.updatable_asset')

class Updates(entity.Entity):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new updates and sets the default values.
        """
        super().__init__()
        # Catalog of content that can be approved for deployment by the deployment service. Read-only.
        self._catalog: Optional[catalog.Catalog] = None
        # Deployments created using the deployment service. Read-only.
        self._deployments: Optional[List[deployment.Deployment]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Service connections to external resources such as analytics workspaces.
        self._resource_connections: Optional[List[resource_connection.ResourceConnection]] = None
        # Assets registered with the deployment service that can receive updates. Read-only.
        self._updatable_assets: Optional[List[updatable_asset.UpdatableAsset]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Updates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Updates
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Updates()
    
    @property
    def deployments(self,) -> Optional[List[deployment.Deployment]]:
        """
        Gets the deployments property value. Deployments created using the deployment service. Read-only.
        Returns: Optional[List[deployment.Deployment]]
        """
        return self._deployments
    
    @deployments.setter
    def deployments(self,value: Optional[List[deployment.Deployment]] = None) -> None:
        """
        Sets the deployments property value. Deployments created using the deployment service. Read-only.
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
            "resource_connections": lambda n : setattr(self, 'resource_connections', n.get_collection_of_object_values(resource_connection.ResourceConnection)),
            "updatable_assets": lambda n : setattr(self, 'updatable_assets', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
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
            value: Value to set for the resourceConnections property.
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
        writer.write_collection_of_object_values("resourceConnections", self.resource_connections)
        writer.write_collection_of_object_values("updatableAssets", self.updatable_assets)
    
    @property
    def updatable_assets(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the updatableAssets property value. Assets registered with the deployment service that can receive updates. Read-only.
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._updatable_assets
    
    @updatable_assets.setter
    def updatable_assets(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the updatableAssets property value. Assets registered with the deployment service that can receive updates. Read-only.
        Args:
            value: Value to set for the updatableAssets property.
        """
        self._updatable_assets = value
    

