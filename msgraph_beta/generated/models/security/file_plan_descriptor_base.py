from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applied_category import AppliedCategory
    from .authority import Authority
    from .citation import Citation
    from .department import Department
    from .file_plan_reference import FilePlanReference
    from .sub_category import SubCategory

@dataclass
class FilePlanDescriptorBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Unique string that defines the name for each file plan descriptor associated with a particular retention label.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilePlanDescriptorBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilePlanDescriptorBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.appliedCategory".casefold():
            from .applied_category import AppliedCategory

            return AppliedCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.authority".casefold():
            from .authority import Authority

            return Authority()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.citation".casefold():
            from .citation import Citation

            return Citation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.department".casefold():
            from .department import Department

            return Department()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanReference".casefold():
            from .file_plan_reference import FilePlanReference

            return FilePlanReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.subCategory".casefold():
            from .sub_category import SubCategory

            return SubCategory()
        return FilePlanDescriptorBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .applied_category import AppliedCategory
        from .authority import Authority
        from .citation import Citation
        from .department import Department
        from .file_plan_reference import FilePlanReference
        from .sub_category import SubCategory

        from .applied_category import AppliedCategory
        from .authority import Authority
        from .citation import Citation
        from .department import Department
        from .file_plan_reference import FilePlanReference
        from .sub_category import SubCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

