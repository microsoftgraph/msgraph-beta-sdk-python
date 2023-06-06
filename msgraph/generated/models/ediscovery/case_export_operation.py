from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import case_operation, export_file_structure, export_options, review_set

from . import case_operation

@dataclass
class CaseExportOperation(case_operation.CaseOperation):
    # The name of the Azure storage location where the export will be stored. This only applies to exports stored in your own Azure storage location.
    azure_blob_container: Optional[str] = None
    # The SAS token for the Azure storage location.  This only applies to exports stored in your own Azure storage location.
    azure_blob_token: Optional[str] = None
    # The description provided for the export.
    description: Optional[str] = None
    # The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement, fileInfo, tags.
    export_options: Optional[export_options.ExportOptions] = None
    # The options provided that specify the structure of the export. For more details, see reviewSet: export. Possible values are: none, directory, pst.
    export_structure: Optional[export_file_structure.ExportFileStructure] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The outputFolderId property
    output_folder_id: Optional[str] = None
    # The name provided for the export.
    output_name: Optional[str] = None
    # The review set the content is being exported from.
    review_set: Optional[review_set.ReviewSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CaseExportOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CaseExportOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CaseExportOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import case_operation, export_file_structure, export_options, review_set

        fields: Dict[str, Callable[[Any], None]] = {
            "azureBlobContainer": lambda n : setattr(self, 'azure_blob_container', n.get_str_value()),
            "azureBlobToken": lambda n : setattr(self, 'azure_blob_token', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "exportOptions": lambda n : setattr(self, 'export_options', n.get_enum_value(export_options.ExportOptions)),
            "exportStructure": lambda n : setattr(self, 'export_structure', n.get_enum_value(export_file_structure.ExportFileStructure)),
            "outputFolderId": lambda n : setattr(self, 'output_folder_id', n.get_str_value()),
            "outputName": lambda n : setattr(self, 'output_name', n.get_str_value()),
            "reviewSet": lambda n : setattr(self, 'review_set', n.get_object_value(review_set.ReviewSet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("azureBlobContainer", self.azure_blob_container)
        writer.write_str_value("azureBlobToken", self.azure_blob_token)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("exportOptions", self.export_options)
        writer.write_enum_value("exportStructure", self.export_structure)
        writer.write_str_value("outputFolderId", self.output_folder_id)
        writer.write_str_value("outputName", self.output_name)
        writer.write_object_value("reviewSet", self.review_set)
    

