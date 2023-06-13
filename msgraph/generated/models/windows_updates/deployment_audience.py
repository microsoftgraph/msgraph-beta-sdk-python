from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import applicable_content, updatable_asset
    from .. import entity

from .. import entity

@dataclass
class DeploymentAudience(entity.Entity):
    # Content eligible to deploy to devices in the audience. Not nullable. Read-only.
    applicable_content: Optional[List[applicable_content.ApplicableContent]] = None
    # Specifies the assets to exclude from the audience.
    exclusions: Optional[List[updatable_asset.UpdatableAsset]] = None
    # Specifies the assets to include in the audience.
    members: Optional[List[updatable_asset.UpdatableAsset]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeploymentAudience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentAudience
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeploymentAudience()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import applicable_content, updatable_asset
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableContent": lambda n : setattr(self, 'applicable_content', n.get_collection_of_object_values(applicable_content.ApplicableContent)),
            "exclusions": lambda n : setattr(self, 'exclusions', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
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
        writer.write_collection_of_object_values("applicableContent", self.applicable_content)
        writer.write_collection_of_object_values("exclusions", self.exclusions)
        writer.write_collection_of_object_values("members", self.members)
    

