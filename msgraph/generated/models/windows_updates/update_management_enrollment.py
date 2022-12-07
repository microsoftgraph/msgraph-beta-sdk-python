from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

updatable_asset_enrollment = lazy_import('msgraph.generated.models.windows_updates.updatable_asset_enrollment')
update_category = lazy_import('msgraph.generated.models.windows_updates.update_category')

class UpdateManagementEnrollment(updatable_asset_enrollment.UpdatableAssetEnrollment):
    def __init__(self,) -> None:
        """
        Instantiates a new UpdateManagementEnrollment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.updateManagementEnrollment"
        # The updateCategory property
        self._update_category: Optional[update_category.UpdateCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateManagementEnrollment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateManagementEnrollment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateManagementEnrollment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "update_category": lambda n : setattr(self, 'update_category', n.get_enum_value(update_category.UpdateCategory)),
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
        writer.write_enum_value("updateCategory", self.update_category)
    
    @property
    def update_category(self,) -> Optional[update_category.UpdateCategory]:
        """
        Gets the updateCategory property value. The updateCategory property
        Returns: Optional[update_category.UpdateCategory]
        """
        return self._update_category
    
    @update_category.setter
    def update_category(self,value: Optional[update_category.UpdateCategory] = None) -> None:
        """
        Sets the updateCategory property value. The updateCategory property
        Args:
            value: Value to set for the updateCategory property.
        """
        self._update_category = value
    

