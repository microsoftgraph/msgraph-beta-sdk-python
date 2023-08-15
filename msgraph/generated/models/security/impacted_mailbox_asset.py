from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .impacted_asset import ImpactedAsset
    from .mailbox_asset_identifier import MailboxAssetIdentifier

from .impacted_asset import ImpactedAsset

@dataclass
class ImpactedMailboxAsset(ImpactedAsset):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.impactedMailboxAsset"
    # The identifier property
    identifier: Optional[MailboxAssetIdentifier] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImpactedMailboxAsset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImpactedMailboxAsset
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ImpactedMailboxAsset()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .impacted_asset import ImpactedAsset
        from .mailbox_asset_identifier import MailboxAssetIdentifier

        from .impacted_asset import ImpactedAsset
        from .mailbox_asset_identifier import MailboxAssetIdentifier

        fields: Dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_enum_value(MailboxAssetIdentifier)),
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
        writer.write_enum_value("identifier", self.identifier)
    

