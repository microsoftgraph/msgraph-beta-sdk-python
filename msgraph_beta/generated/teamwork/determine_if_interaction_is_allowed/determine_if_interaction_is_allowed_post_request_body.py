from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.identity import Identity
    from ...models.teamwork_interaction_type import TeamworkInteractionType

@dataclass
class DetermineIfInteractionIsAllowedPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The interactionType property
    interaction_type: Optional[TeamworkInteractionType] = None
    # The users property
    users: Optional[list[Identity]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetermineIfInteractionIsAllowedPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetermineIfInteractionIsAllowedPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetermineIfInteractionIsAllowedPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...models.identity import Identity
        from ...models.teamwork_interaction_type import TeamworkInteractionType

        from ...models.identity import Identity
        from ...models.teamwork_interaction_type import TeamworkInteractionType

        fields: dict[str, Callable[[Any], None]] = {
            "interactionType": lambda n : setattr(self, 'interaction_type', n.get_enum_value(TeamworkInteractionType)),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(Identity)),
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
        writer.write_enum_value("interactionType", self.interaction_type)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    

