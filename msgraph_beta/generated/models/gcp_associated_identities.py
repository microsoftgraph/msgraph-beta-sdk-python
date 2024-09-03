from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gcp_identity import GcpIdentity
    from .gcp_service_account import GcpServiceAccount
    from .gcp_user import GcpUser

@dataclass
class GcpAssociatedIdentities(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The all property
    all: Optional[List[GcpIdentity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The serviceAccounts property
    service_accounts: Optional[List[GcpServiceAccount]] = None
    # The users property
    users: Optional[List[GcpUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GcpAssociatedIdentities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpAssociatedIdentities
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GcpAssociatedIdentities()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .gcp_identity import GcpIdentity
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser

        from .gcp_identity import GcpIdentity
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser

        fields: Dict[str, Callable[[Any], None]] = {
            "all": lambda n : setattr(self, 'all', n.get_collection_of_object_values(GcpIdentity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceAccounts": lambda n : setattr(self, 'service_accounts', n.get_collection_of_object_values(GcpServiceAccount)),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(GcpUser)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("serviceAccounts", self.service_accounts)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    

