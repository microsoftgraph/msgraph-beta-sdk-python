from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tenant_allow_block_list_action import TenantAllowBlockListAction
    from .tenant_allow_block_list_entry_result import TenantAllowBlockListEntryResult

@dataclass
class TenantAllowOrBlockListAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Specifies whether the tenant allow-or-block list is an allow or block. The possible values are: allow, block, and unkownFutureValue.
    action: Optional[TenantAllowBlockListAction] = None
    # Specifies when the tenant allow-block-list expires in date time.
    expiration_date_time: Optional[datetime.datetime] = None
    # Specifies the note added to the tenant allow-or-block list entry in the format of string.
    note: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the result of the submission that lead to the tenant allow-block-list entry creation.
    results: Optional[List[TenantAllowBlockListEntryResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantAllowOrBlockListAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantAllowOrBlockListAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TenantAllowOrBlockListAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .tenant_allow_block_list_action import TenantAllowBlockListAction
        from .tenant_allow_block_list_entry_result import TenantAllowBlockListEntryResult

        from .tenant_allow_block_list_action import TenantAllowBlockListAction
        from .tenant_allow_block_list_entry_result import TenantAllowBlockListEntryResult

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(TenantAllowBlockListAction)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(TenantAllowBlockListEntryResult)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("note", self.note)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_additional_data_value(self.additional_data)
    

