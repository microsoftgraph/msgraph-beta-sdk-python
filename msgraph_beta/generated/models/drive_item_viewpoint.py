from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_item_access_operations_viewpoint import DriveItemAccessOperationsViewpoint
    from .sharing_viewpoint import SharingViewpoint

@dataclass
class DriveItemViewpoint(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether the user can perform the described actions on this item.
    access_operations: Optional[DriveItemAccessOperationsViewpoint] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates sharing operations the current user can take on the specified item.
    sharing: Optional[SharingViewpoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveItemViewpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveItemViewpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveItemViewpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .drive_item_access_operations_viewpoint import DriveItemAccessOperationsViewpoint
        from .sharing_viewpoint import SharingViewpoint

        from .drive_item_access_operations_viewpoint import DriveItemAccessOperationsViewpoint
        from .sharing_viewpoint import SharingViewpoint

        fields: Dict[str, Callable[[Any], None]] = {
            "accessOperations": lambda n : setattr(self, 'access_operations', n.get_object_value(DriveItemAccessOperationsViewpoint)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sharing": lambda n : setattr(self, 'sharing', n.get_object_value(SharingViewpoint)),
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
        writer.write_object_value("accessOperations", self.access_operations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sharing", self.sharing)
        writer.write_additional_data_value(self.additional_data)
    

