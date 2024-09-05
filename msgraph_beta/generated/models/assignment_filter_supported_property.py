from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_filter_operator import AssignmentFilterOperator

@dataclass
class AssignmentFilterSupportedProperty(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents the information about the property which is supported in crafting the rule of AssignmentFilter.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The data type of the property.
    data_type: Optional[str] = None
    # Indicates whether the property is a collection type or not.
    is_collection: Optional[bool] = None
    # Name of the property.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Regex string to do validation on the property value.
    property_regex_constraint: Optional[str] = None
    # List of all supported operators on this property.
    supported_operators: Optional[List[AssignmentFilterOperator]] = None
    # List of all supported values for this property, empty if everything is supported.
    supported_values: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignmentFilterSupportedProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterSupportedProperty
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignmentFilterSupportedProperty()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_filter_operator import AssignmentFilterOperator

        from .assignment_filter_operator import AssignmentFilterOperator

        fields: Dict[str, Callable[[Any], None]] = {
            "dataType": lambda n : setattr(self, 'data_type', n.get_str_value()),
            "isCollection": lambda n : setattr(self, 'is_collection', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propertyRegexConstraint": lambda n : setattr(self, 'property_regex_constraint', n.get_str_value()),
            "supportedOperators": lambda n : setattr(self, 'supported_operators', n.get_collection_of_enum_values(AssignmentFilterOperator)),
            "supportedValues": lambda n : setattr(self, 'supported_values', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("dataType", self.data_type)
        writer.write_bool_value("isCollection", self.is_collection)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("propertyRegexConstraint", self.property_regex_constraint)
        writer.write_collection_of_enum_values("supportedOperators", self.supported_operators)
        writer.write_collection_of_primitive_values("supportedValues", self.supported_values)
        writer.write_additional_data_value(self.additional_data)
    

