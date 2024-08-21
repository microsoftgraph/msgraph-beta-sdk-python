from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_identity import AzureIdentity
    from .azure_managed_identity import AzureManagedIdentity
    from .azure_service_principal import AzureServicePrincipal
    from .azure_user import AzureUser

@dataclass
class AzureAssociatedIdentities(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The all property
    all: Optional[List[AzureIdentity]] = None
    # The managedIdentities property
    managed_identities: Optional[List[AzureManagedIdentity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The servicePrincipals property
    service_principals: Optional[List[AzureServicePrincipal]] = None
    # The users property
    users: Optional[List[AzureUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureAssociatedIdentities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureAssociatedIdentities
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureAssociatedIdentities()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .azure_identity import AzureIdentity
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser

        from .azure_identity import AzureIdentity
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser

        fields: Dict[str, Callable[[Any], None]] = {
            "all": lambda n : setattr(self, 'all', n.get_collection_of_object_values(AzureIdentity)),
            "managedIdentities": lambda n : setattr(self, 'managed_identities', n.get_collection_of_object_values(AzureManagedIdentity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipals": lambda n : setattr(self, 'service_principals', n.get_collection_of_object_values(AzureServicePrincipal)),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(AzureUser)),
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
        writer.write_collection_of_object_values("all", self.all)
        writer.write_collection_of_object_values("managedIdentities", self.managed_identities)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("servicePrincipals", self.service_principals)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    

