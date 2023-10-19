from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SecureScoreControlStateUpdate(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The assignedTo property
    assigned_to: Optional[str] = None
    # The comment property
    comment: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[str] = None
    # The updatedBy property
    updated_by: Optional[str] = None
    # The updatedDateTime property
    updated_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecureScoreControlStateUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecureScoreControlStateUpdate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SecureScoreControlStateUpdate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_str_value()),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_additional_data_value(self.additional_data)
    

