from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CloudPcBulkActionSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The failedCount property
    failed_count: Optional[int] = None
    # The inProgressCount property
    in_progress_count: Optional[int] = None
    # The notSupportedCount property
    not_supported_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The pendingCount property
    pending_count: Optional[int] = None
    # The successfulCount property
    successful_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcBulkActionSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkActionSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcBulkActionSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "failedCount": lambda n : setattr(self, 'failed_count', n.get_int_value()),
            "inProgressCount": lambda n : setattr(self, 'in_progress_count', n.get_int_value()),
            "notSupportedCount": lambda n : setattr(self, 'not_supported_count', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pendingCount": lambda n : setattr(self, 'pending_count', n.get_int_value()),
            "successfulCount": lambda n : setattr(self, 'successful_count', n.get_int_value()),
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
        writer.write_int_value("failedCount", self.failed_count)
        writer.write_int_value("inProgressCount", self.in_progress_count)
        writer.write_int_value("notSupportedCount", self.not_supported_count)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("pendingCount", self.pending_count)
        writer.write_int_value("successfulCount", self.successful_count)
        writer.write_additional_data_value(self.additional_data)
    

