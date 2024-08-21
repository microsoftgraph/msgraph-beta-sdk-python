from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .label_details import LabelDetails

@dataclass
class ParentLabelDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The color that the user interface should display for the label, if configured.
    color: Optional[str] = None
    # The admin-defined description for the label.
    description: Optional[str] = None
    # The label ID is a globally unique identifier (GUID).
    id: Optional[str] = None
    # Indicates whether the label is active or not. Active labels should be hidden or disabled in user interfaces.
    is_active: Optional[bool] = None
    # The plaintext name of the label.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parent property
    parent: Optional[ParentLabelDetails] = None
    # The sensitivity value of the label, where lower is less sensitive.
    sensitivity: Optional[int] = None
    # The tooltip that should be displayed for the label in a user interface.
    tooltip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ParentLabelDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ParentLabelDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.labelDetails".casefold():
            from .label_details import LabelDetails

            return LabelDetails()
        return ParentLabelDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .label_details import LabelDetails

        from .label_details import LabelDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(ParentLabelDetails)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_int_value()),
            "tooltip": lambda n : setattr(self, 'tooltip', n.get_str_value()),
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
        writer.write_str_value("color", self.color)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parent", self.parent)
        writer.write_int_value("sensitivity", self.sensitivity)
        writer.write_str_value("tooltip", self.tooltip)
        writer.write_additional_data_value(self.additional_data)
    

