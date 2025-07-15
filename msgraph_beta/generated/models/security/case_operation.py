from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
    from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
    from .ediscovery_export_operation import EdiscoveryExportOperation
    from .ediscovery_hold_operation import EdiscoveryHoldOperation
    from .ediscovery_index_operation import EdiscoveryIndexOperation
    from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
    from .ediscovery_search_export_operation import EdiscoverySearchExportOperation
    from .ediscovery_tag_operation import EdiscoveryTagOperation

from ..entity import Entity

@dataclass
class CaseOperation(Entity, Parsable):
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CaseOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CaseOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation".casefold():
            from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation

            return EdiscoveryAddToReviewSetOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryEstimateOperation".casefold():
            from .ediscovery_estimate_operation import EdiscoveryEstimateOperation

            return EdiscoveryEstimateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryExportOperation".casefold():
            from .ediscovery_export_operation import EdiscoveryExportOperation

            return EdiscoveryExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryHoldOperation".casefold():
            from .ediscovery_hold_operation import EdiscoveryHoldOperation

            return EdiscoveryHoldOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryIndexOperation".casefold():
            from .ediscovery_index_operation import EdiscoveryIndexOperation

            return EdiscoveryIndexOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryPurgeDataOperation".casefold():
            from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation

            return EdiscoveryPurgeDataOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoverySearchExportOperation".casefold():
            from .ediscovery_search_export_operation import EdiscoverySearchExportOperation

            return EdiscoverySearchExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryTagOperation".casefold():
            from .ediscovery_tag_operation import EdiscoveryTagOperation

            return EdiscoveryTagOperation()
        return CaseOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .ediscovery_export_operation import EdiscoveryExportOperation
        from .ediscovery_hold_operation import EdiscoveryHoldOperation
        from .ediscovery_index_operation import EdiscoveryIndexOperation
        from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .ediscovery_search_export_operation import EdiscoverySearchExportOperation
        from .ediscovery_tag_operation import EdiscoveryTagOperation

        from ..entity import Entity
        from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .ediscovery_export_operation import EdiscoveryExportOperation
        from .ediscovery_hold_operation import EdiscoveryHoldOperation
        from .ediscovery_index_operation import EdiscoveryIndexOperation
        from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .ediscovery_search_export_operation import EdiscoverySearchExportOperation
        from .ediscovery_tag_operation import EdiscoveryTagOperation

        fields: dict[str, Callable[[Any], None]] = {
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

