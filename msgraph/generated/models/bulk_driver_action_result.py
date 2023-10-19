from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BulkDriverActionResult(AdditionalDataHolder, BackedModel, Parsable):
    """
    A complex type to represent the result of bulk driver action.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # List of driver Ids where the action is failed.
    failed_driver_ids: Optional[List[str]] = None
    # List of driver Ids that are not found.
    not_found_driver_ids: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of driver Ids where the action is successful.
    successful_driver_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BulkDriverActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BulkDriverActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BulkDriverActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "failedDriverIds": lambda n : setattr(self, 'failed_driver_ids', n.get_collection_of_primitive_values(str)),
            "notFoundDriverIds": lambda n : setattr(self, 'not_found_driver_ids', n.get_collection_of_primitive_values(str)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulDriverIds": lambda n : setattr(self, 'successful_driver_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("failedDriverIds", self.failed_driver_ids)
        writer.write_collection_of_primitive_values("notFoundDriverIds", self.not_found_driver_ids)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_primitive_values("successfulDriverIds", self.successful_driver_ids)
        writer.write_additional_data_value(self.additional_data)
    

