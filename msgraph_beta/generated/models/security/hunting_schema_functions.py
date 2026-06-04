from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hunting_schema_built_in_function import HuntingSchemaBuiltInFunction
    from .hunting_schema_saved_function import HuntingSchemaSavedFunction

@dataclass
class HuntingSchemaFunctions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The builtInFunctions property
    built_in_functions: Optional[list[HuntingSchemaBuiltInFunction]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The savedFunctions property
    saved_functions: Optional[list[HuntingSchemaSavedFunction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HuntingSchemaFunctions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HuntingSchemaFunctions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HuntingSchemaFunctions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hunting_schema_built_in_function import HuntingSchemaBuiltInFunction
        from .hunting_schema_saved_function import HuntingSchemaSavedFunction

        from .hunting_schema_built_in_function import HuntingSchemaBuiltInFunction
        from .hunting_schema_saved_function import HuntingSchemaSavedFunction

        fields: dict[str, Callable[[Any], None]] = {
            "builtInFunctions": lambda n : setattr(self, 'built_in_functions', n.get_collection_of_object_values(HuntingSchemaBuiltInFunction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "savedFunctions": lambda n : setattr(self, 'saved_functions', n.get_collection_of_object_values(HuntingSchemaSavedFunction)),
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
        writer.write_collection_of_object_values("builtInFunctions", self.built_in_functions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("savedFunctions", self.saved_functions)
        writer.write_additional_data_value(self.additional_data)
    

