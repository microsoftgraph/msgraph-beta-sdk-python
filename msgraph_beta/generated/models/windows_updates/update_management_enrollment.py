from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .updatable_asset_enrollment import UpdatableAssetEnrollment
    from .update_category import UpdateCategory

from .updatable_asset_enrollment import UpdatableAssetEnrollment

@dataclass
class UpdateManagementEnrollment(UpdatableAssetEnrollment):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.updateManagementEnrollment"
    # The updateCategory property
    update_category: Optional[UpdateCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateManagementEnrollment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateManagementEnrollment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateManagementEnrollment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .updatable_asset_enrollment import UpdatableAssetEnrollment
        from .update_category import UpdateCategory

        from .updatable_asset_enrollment import UpdatableAssetEnrollment
        from .update_category import UpdateCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "updateCategory": lambda n : setattr(self, 'update_category', n.get_enum_value(UpdateCategory)),
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
        writer.write_enum_value("updateCategory", self.update_category)
    

