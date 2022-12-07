from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

updatable_asset = lazy_import('msgraph.generated.models.windows_updates.updatable_asset')

class UpdatableAssetGroup(updatable_asset.UpdatableAsset):
    def __init__(self,) -> None:
        """
        Instantiates a new UpdatableAssetGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.updatableAssetGroup"
        # Members of the group. Read-only.
        self._members: Optional[List[updatable_asset.UpdatableAsset]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatableAssetGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdatableAssetGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdatableAssetGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def members(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the members property value. Members of the group. Read-only.
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the members property value. Members of the group. Read-only.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("members", self.members)
    

