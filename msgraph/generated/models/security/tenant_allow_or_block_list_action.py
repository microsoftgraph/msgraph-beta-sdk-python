from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import tenant_allow_block_list_action, tenant_allow_block_list_entry_result

@dataclass
class TenantAllowOrBlockListAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies whether the tenant allow block list is an allow or block. The possible values are: allow, block, and unkownFutureValue.
    action: Optional[tenant_allow_block_list_action.TenantAllowBlockListAction] = None
    # Specifies when the tenant allow-block-list expires in date time.
    expiration_date_time: Optional[datetime] = None
    # Specifies the note added to the tenant allow block list entry in the format of string.
    note: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the result of the submission that lead to the tenant allow-block-list entry creation.
    results: Optional[List[tenant_allow_block_list_entry_result.TenantAllowBlockListEntryResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantAllowOrBlockListAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import tenant_allow_block_list_action, tenant_allow_block_list_entry_result

        from . import tenant_allow_block_list_action, tenant_allow_block_list_entry_result

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(tenant_allow_block_list_action.TenantAllowBlockListAction)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(tenant_allow_block_list_entry_result.TenantAllowBlockListEntryResult)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("note", self.note)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_additional_data_value(self.additional_data)
    

