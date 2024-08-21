from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet

@dataclass
class ContentModelUsage(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Identity of the user, device, or application that first applied the contentModel to the library.
    created_by: Optional[IdentitySet] = None
    # Date and time of the contentModel is first applied.
    created_date_time: Optional[datetime.datetime] = None
    # The ID of the drive where the contentModel is applied.
    drive_id: Optional[str] = None
    # Identity of the user, device, or application that last applied the contentModel to the library.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time of the contentModel is last applied.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The ID of the contentModel.
    model_id: Optional[str] = None
    # The version of the current applied contentModel.
    model_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentModelUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentModelUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentModelUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet

        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "driveId": lambda n : setattr(self, 'drive_id', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "modelId": lambda n : setattr(self, 'model_id', n.get_str_value()),
            "modelVersion": lambda n : setattr(self, 'model_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("driveId", self.drive_id)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("modelId", self.model_id)
        writer.write_str_value("modelVersion", self.model_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

