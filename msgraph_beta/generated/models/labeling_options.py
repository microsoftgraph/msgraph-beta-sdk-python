from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_method import AssignmentMethod
    from .downgrade_justification import DowngradeJustification
    from .key_value_pair import KeyValuePair

@dataclass
class LabelingOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The assignmentMethod property
    assignment_method: Optional[AssignmentMethod] = None
    # The downgrade justification object that indicates if downgrade was justified and, if so, the reason.
    downgrade_justification: Optional[DowngradeJustification] = None
    # Extended properties will be parsed and returned in the standard MIP labeled metadata format as part of the label information.
    extended_properties: Optional[List[KeyValuePair]] = None
    # The GUID of the label that should be applied to the information.
    label_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LabelingOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LabelingOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LabelingOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_method import AssignmentMethod
        from .downgrade_justification import DowngradeJustification
        from .key_value_pair import KeyValuePair

        from .assignment_method import AssignmentMethod
        from .downgrade_justification import DowngradeJustification
        from .key_value_pair import KeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentMethod": lambda n : setattr(self, 'assignment_method', n.get_enum_value(AssignmentMethod)),
            "downgradeJustification": lambda n : setattr(self, 'downgrade_justification', n.get_object_value(DowngradeJustification)),
            "extendedProperties": lambda n : setattr(self, 'extended_properties', n.get_collection_of_object_values(KeyValuePair)),
            "labelId": lambda n : setattr(self, 'label_id', n.get_str_value()),
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
        writer.write_enum_value("assignmentMethod", self.assignment_method)
        writer.write_object_value("downgradeJustification", self.downgrade_justification)
        writer.write_collection_of_object_values("extendedProperties", self.extended_properties)
        writer.write_str_value("labelId", self.label_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

