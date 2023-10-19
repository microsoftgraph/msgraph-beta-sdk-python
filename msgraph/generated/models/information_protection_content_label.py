from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_method import AssignmentMethod
    from .label_details import LabelDetails

@dataclass
class InformationProtectionContentLabel(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The assignmentMethod property
    assignment_method: Optional[AssignmentMethod] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    creation_date_time: Optional[datetime.datetime] = None
    # Details on the label that is currently applied to the file.
    label: Optional[LabelDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionContentLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionContentLabel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InformationProtectionContentLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_method import AssignmentMethod
        from .label_details import LabelDetails

        from .assignment_method import AssignmentMethod
        from .label_details import LabelDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentMethod": lambda n : setattr(self, 'assignment_method', n.get_enum_value(AssignmentMethod)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_object_value(LabelDetails)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("assignmentMethod", self.assignment_method)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("label", self.label)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

