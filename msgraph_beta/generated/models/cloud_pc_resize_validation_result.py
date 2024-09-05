from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_resize_validation_code import CloudPcResizeValidationCode

@dataclass
class CloudPcResizeValidationResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The cloudPC ID that corresponds to its unique identifier.
    cloud_pc_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Describes a list of the validation result for the Cloud PC resize action. The possible values are: success, cloudPcNotFound, operationCnflict, operationNotSupported, targetLicenseHasAssigned, internalServerError, and unknownFutureValue.
    validation_result: Optional[CloudPcResizeValidationCode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcResizeValidationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcResizeValidationResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcResizeValidationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_resize_validation_code import CloudPcResizeValidationCode

        from .cloud_pc_resize_validation_code import CloudPcResizeValidationCode

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPcId": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "validationResult": lambda n : setattr(self, 'validation_result', n.get_enum_value(CloudPcResizeValidationCode)),
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
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("validationResult", self.validation_result)
        writer.write_additional_data_value(self.additional_data)
    

