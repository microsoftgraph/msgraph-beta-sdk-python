from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EducationSynchronizationCustomization(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether the display name of the resource can be overwritten by the sync.
    allow_display_name_update: Optional[bool] = None
    # Indicates whether synchronization of the parent entity is deferred to a later date.
    is_sync_deferred: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of property names to sync. If set to null, all properties will be synchronized. Does not apply to Student Enrollments or Teacher Rosters
    optional_properties_to_sync: Optional[List[str]] = None
    # The date that the synchronization should start. This value should be set to a future date. If set to null, the resource will be synchronized when the profile setup completes. Only applies to Student Enrollments
    synchronization_start_date: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSynchronizationCustomization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationCustomization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationCustomization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowDisplayNameUpdate": lambda n : setattr(self, 'allow_display_name_update', n.get_bool_value()),
            "isSyncDeferred": lambda n : setattr(self, 'is_sync_deferred', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "optionalPropertiesToSync": lambda n : setattr(self, 'optional_properties_to_sync', n.get_collection_of_primitive_values(str)),
            "synchronizationStartDate": lambda n : setattr(self, 'synchronization_start_date', n.get_datetime_value()),
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
        writer.write_bool_value("allowDisplayNameUpdate", self.allow_display_name_update)
        writer.write_bool_value("isSyncDeferred", self.is_sync_deferred)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("optionalPropertiesToSync", self.optional_properties_to_sync)
        writer.write_datetime_value("synchronizationStartDate", self.synchronization_start_date)
        writer.write_additional_data_value(self.additional_data)
    

