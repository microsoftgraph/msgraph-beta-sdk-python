from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .repository_o_auth_credential import RepositoryOAuthCredential
    from .repository_pat_credential import RepositoryPatCredential

@dataclass
class RepositoryAccessCredential(AdditionalDataHolder, BackedModel, Parsable):
    """
    Provider credential used to establish or refresh repository access. The concrete type(set via `@odata.type`) selects the credential style. All fields are input only and arenever returned.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RepositoryAccessCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RepositoryAccessCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if not mapping_value:
            return RepositoryAccessCredential()
        if mapping_value.casefold() == "#microsoft.graph.security.contentManagement.repositoryOAuthCredential".casefold():
            from .repository_o_auth_credential import RepositoryOAuthCredential

            return RepositoryOAuthCredential()
        if mapping_value.casefold() == "#microsoft.graph.security.contentManagement.repositoryPatCredential".casefold():
            from .repository_pat_credential import RepositoryPatCredential

            return RepositoryPatCredential()
        return RepositoryAccessCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .repository_o_auth_credential import RepositoryOAuthCredential
        from .repository_pat_credential import RepositoryPatCredential

        from .repository_o_auth_credential import RepositoryOAuthCredential
        from .repository_pat_credential import RepositoryPatCredential

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

