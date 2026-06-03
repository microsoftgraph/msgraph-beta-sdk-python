from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hunting_schema_function_parameter import HuntingSchemaFunctionParameter
    from .hunting_schema_table_column import HuntingSchemaTableColumn

@dataclass
class HuntingSchemaSavedFunction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The createdBy property
    created_by: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The huntingFunctionId property
    hunting_function_id: Optional[int] = None
    # The inputParameters property
    input_parameters: Optional[list[HuntingSchemaFunctionParameter]] = None
    # The lastModifiedBy property
    last_modified_by: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The outputColumns property
    output_columns: Optional[list[HuntingSchemaTableColumn]] = None
    # The path property
    path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HuntingSchemaSavedFunction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HuntingSchemaSavedFunction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HuntingSchemaSavedFunction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hunting_schema_function_parameter import HuntingSchemaFunctionParameter
        from .hunting_schema_table_column import HuntingSchemaTableColumn

        from .hunting_schema_function_parameter import HuntingSchemaFunctionParameter
        from .hunting_schema_table_column import HuntingSchemaTableColumn

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "huntingFunctionId": lambda n : setattr(self, 'hunting_function_id', n.get_int_value()),
            "inputParameters": lambda n : setattr(self, 'input_parameters', n.get_collection_of_object_values(HuntingSchemaFunctionParameter)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outputColumns": lambda n : setattr(self, 'output_columns', n.get_collection_of_object_values(HuntingSchemaTableColumn)),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
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
        writer.write_str_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("inputParameters", self.input_parameters)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("outputColumns", self.output_columns)
        writer.write_str_value("path", self.path)
        writer.write_additional_data_value(self.additional_data)
    

