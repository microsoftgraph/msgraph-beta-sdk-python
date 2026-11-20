from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.security.content_management.deployment_identity import DeploymentIdentity
    from .....models.security.content_management.deployment_scope import DeploymentScope
    from .....models.security.content_management.repository_access_credential import RepositoryAccessCredential
    from .....models.security.content_management.repository_content_type import RepositoryContentType
    from .....models.security.content_management.repository_settings import RepositorySettings
    from .....models.security.content_management.repository_type import RepositoryType

@dataclass
class ConnectPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Provider credential used to establish or refresh repository access. The concrete type(set via `@odata.type`) selects the credential style. All fields are input only and arenever returned.
    access_credential: Optional[RepositoryAccessCredential] = None
    # The contentTypes property
    content_types: Optional[list[RepositoryContentType]] = None
    # The deploymentIdentity property
    deployment_identity: Optional[DeploymentIdentity] = None
    # The deploymentScope property
    deployment_scope: Optional[DeploymentScope] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # Source-control provider.
    repo_type: Optional[RepositoryType] = None
    # Repository location settings.
    source_location: Optional[RepositorySettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.security.content_management.deployment_identity import DeploymentIdentity
        from .....models.security.content_management.deployment_scope import DeploymentScope
        from .....models.security.content_management.repository_access_credential import RepositoryAccessCredential
        from .....models.security.content_management.repository_content_type import RepositoryContentType
        from .....models.security.content_management.repository_settings import RepositorySettings
        from .....models.security.content_management.repository_type import RepositoryType

        from .....models.security.content_management.deployment_identity import DeploymentIdentity
        from .....models.security.content_management.deployment_scope import DeploymentScope
        from .....models.security.content_management.repository_access_credential import RepositoryAccessCredential
        from .....models.security.content_management.repository_content_type import RepositoryContentType
        from .....models.security.content_management.repository_settings import RepositorySettings
        from .....models.security.content_management.repository_type import RepositoryType

        fields: dict[str, Callable[[Any], None]] = {
            "accessCredential": lambda n : setattr(self, 'access_credential', n.get_object_value(RepositoryAccessCredential)),
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_enum_values(RepositoryContentType)),
            "deploymentIdentity": lambda n : setattr(self, 'deployment_identity', n.get_object_value(DeploymentIdentity)),
            "deploymentScope": lambda n : setattr(self, 'deployment_scope', n.get_object_value(DeploymentScope)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "repoType": lambda n : setattr(self, 'repo_type', n.get_enum_value(RepositoryType)),
            "sourceLocation": lambda n : setattr(self, 'source_location', n.get_object_value(RepositorySettings)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("accessCredential", self.access_credential)
        writer.write_collection_of_enum_values("contentTypes", self.content_types)
        writer.write_object_value("deploymentIdentity", self.deployment_identity)
        writer.write_object_value("deploymentScope", self.deployment_scope)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("repoType", self.repo_type)
        writer.write_object_value("sourceLocation", self.source_location)
        writer.write_additional_data_value(self.additional_data)
    

