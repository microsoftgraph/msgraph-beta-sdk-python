from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_collection_status import DataCollectionStatus
    from .entitlements_data_collection_info import EntitlementsDataCollectionInfo
    from .permissions_modification_capability import PermissionsModificationCapability

from .entitlements_data_collection_info import EntitlementsDataCollectionInfo

@dataclass
class EntitlementsDataCollection(EntitlementsDataCollectionInfo):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.entitlementsDataCollection"
    # The lastCollectionDateTime property
    last_collection_date_time: Optional[datetime.datetime] = None
    # The permissionsModificationCapability property
    permissions_modification_capability: Optional[PermissionsModificationCapability] = None
    # The status property
    status: Optional[DataCollectionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementsDataCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementsDataCollection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EntitlementsDataCollection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .data_collection_status import DataCollectionStatus
        from .entitlements_data_collection_info import EntitlementsDataCollectionInfo
        from .permissions_modification_capability import PermissionsModificationCapability

        from .data_collection_status import DataCollectionStatus
        from .entitlements_data_collection_info import EntitlementsDataCollectionInfo
        from .permissions_modification_capability import PermissionsModificationCapability

        fields: Dict[str, Callable[[Any], None]] = {
            "lastCollectionDateTime": lambda n : setattr(self, 'last_collection_date_time', n.get_datetime_value()),
            "permissionsModificationCapability": lambda n : setattr(self, 'permissions_modification_capability', n.get_enum_value(PermissionsModificationCapability)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DataCollectionStatus)),
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
        writer.write_datetime_value("lastCollectionDateTime", self.last_collection_date_time)
        writer.write_enum_value("permissionsModificationCapability", self.permissions_modification_capability)
        writer.write_enum_value("status", self.status)
    

