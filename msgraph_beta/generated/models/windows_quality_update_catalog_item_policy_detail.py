from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .windows_quality_update_approval_status import WindowsQualityUpdateApprovalStatus

@dataclass
class WindowsQualityUpdateCatalogItemPolicyDetail(AdditionalDataHolder, BackedModel, Parsable):
    """
    Class to describe quality update policy's approval detail for specific catalog item
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Enum to describe policy's approval status for catalogitems 
    approval_status: Optional[WindowsQualityUpdateApprovalStatus] = None
    # Catalog item id for this approval intend
    catalog_item_id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Policy Id for this approval intend
    policy_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdateCatalogItemPolicyDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateCatalogItemPolicyDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdateCatalogItemPolicyDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_quality_update_approval_status import WindowsQualityUpdateApprovalStatus

        from .windows_quality_update_approval_status import WindowsQualityUpdateApprovalStatus

        fields: dict[str, Callable[[Any], None]] = {
            "approvalStatus": lambda n : setattr(self, 'approval_status', n.get_enum_value(WindowsQualityUpdateApprovalStatus)),
            "catalogItemId": lambda n : setattr(self, 'catalog_item_id', n.get_uuid_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_uuid_value()),
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
        writer.write_enum_value("approvalStatus", self.approval_status)
        writer.write_uuid_value("catalogItemId", self.catalog_item_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_uuid_value("policyId", self.policy_id)
        writer.write_additional_data_value(self.additional_data)
    

