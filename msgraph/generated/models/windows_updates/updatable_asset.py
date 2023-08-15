from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .azure_a_d_device import AzureADDevice
    from .updatable_asset_group import UpdatableAssetGroup

from ..entity import Entity

@dataclass
class UpdatableAsset(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatableAsset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdatableAsset
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.azureADDevice".casefold():
            from .azure_a_d_device import AzureADDevice

            return AzureADDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.updatableAssetGroup".casefold():
            from .updatable_asset_group import UpdatableAssetGroup

            return UpdatableAssetGroup()
        return UpdatableAsset()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .azure_a_d_device import AzureADDevice
        from .updatable_asset_group import UpdatableAssetGroup

        from ..entity import Entity
        from .azure_a_d_device import AzureADDevice
        from .updatable_asset_group import UpdatableAssetGroup

        fields: Dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

