from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import case_operation, ediscovery_review_set, ediscovery_review_set_query, export_file_metadata, export_file_structure, export_options

from . import case_operation

class EdiscoveryExportOperation(case_operation.CaseOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryExportOperation and sets the default values.
        """
        super().__init__()
        # The azureBlobContainer property
        self._azure_blob_container: Optional[str] = None
        # The azureBlobToken property
        self._azure_blob_token: Optional[str] = None
        # The description provided for the export.
        self._description: Optional[str] = None
        # The exportFileMetadata property
        self._export_file_metadata: Optional[List[export_file_metadata.ExportFileMetadata]] = None
        # The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement, fileInfo, tags. The fileInfo member is deprecated and will stop returning data on April 30th, 2023. Going forward, the summary and load file are always included.
        self._export_options: Optional[export_options.ExportOptions] = None
        # The options provided that specify the structure of the export. For more details, see reviewSet: export. Possible values are: none, directory, pst.
        self._export_structure: Optional[export_file_structure.ExportFileStructure] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The outputFolderId property
        self._output_folder_id: Optional[str] = None
        # The name provided for the export.
        self._output_name: Optional[str] = None
        # Review set from where documents are exported.
        self._review_set: Optional[ediscovery_review_set.EdiscoveryReviewSet] = None
        # The review set query which is used to filter the documents for export.
        self._review_set_query: Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery] = None
    
    @property
    def azure_blob_container(self,) -> Optional[str]:
        """
        Gets the azureBlobContainer property value. The azureBlobContainer property
        Returns: Optional[str]
        """
        return self._azure_blob_container
    
    @azure_blob_container.setter
    def azure_blob_container(self,value: Optional[str] = None) -> None:
        """
        Sets the azureBlobContainer property value. The azureBlobContainer property
        Args:
            value: Value to set for the azure_blob_container property.
        """
        self._azure_blob_container = value
    
    @property
    def azure_blob_token(self,) -> Optional[str]:
        """
        Gets the azureBlobToken property value. The azureBlobToken property
        Returns: Optional[str]
        """
        return self._azure_blob_token
    
    @azure_blob_token.setter
    def azure_blob_token(self,value: Optional[str] = None) -> None:
        """
        Sets the azureBlobToken property value. The azureBlobToken property
        Args:
            value: Value to set for the azure_blob_token property.
        """
        self._azure_blob_token = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryExportOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryExportOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryExportOperation()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description provided for the export.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description provided for the export.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def export_file_metadata(self,) -> Optional[List[export_file_metadata.ExportFileMetadata]]:
        """
        Gets the exportFileMetadata property value. The exportFileMetadata property
        Returns: Optional[List[export_file_metadata.ExportFileMetadata]]
        """
        return self._export_file_metadata
    
    @export_file_metadata.setter
    def export_file_metadata(self,value: Optional[List[export_file_metadata.ExportFileMetadata]] = None) -> None:
        """
        Sets the exportFileMetadata property value. The exportFileMetadata property
        Args:
            value: Value to set for the export_file_metadata property.
        """
        self._export_file_metadata = value
    
    @property
    def export_options(self,) -> Optional[export_options.ExportOptions]:
        """
        Gets the exportOptions property value. The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement, fileInfo, tags. The fileInfo member is deprecated and will stop returning data on April 30th, 2023. Going forward, the summary and load file are always included.
        Returns: Optional[export_options.ExportOptions]
        """
        return self._export_options
    
    @export_options.setter
    def export_options(self,value: Optional[export_options.ExportOptions] = None) -> None:
        """
        Sets the exportOptions property value. The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement, fileInfo, tags. The fileInfo member is deprecated and will stop returning data on April 30th, 2023. Going forward, the summary and load file are always included.
        Args:
            value: Value to set for the export_options property.
        """
        self._export_options = value
    
    @property
    def export_structure(self,) -> Optional[export_file_structure.ExportFileStructure]:
        """
        Gets the exportStructure property value. The options provided that specify the structure of the export. For more details, see reviewSet: export. Possible values are: none, directory, pst.
        Returns: Optional[export_file_structure.ExportFileStructure]
        """
        return self._export_structure
    
    @export_structure.setter
    def export_structure(self,value: Optional[export_file_structure.ExportFileStructure] = None) -> None:
        """
        Sets the exportStructure property value. The options provided that specify the structure of the export. For more details, see reviewSet: export. Possible values are: none, directory, pst.
        Args:
            value: Value to set for the export_structure property.
        """
        self._export_structure = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import case_operation, ediscovery_review_set, ediscovery_review_set_query, export_file_metadata, export_file_structure, export_options

        fields: Dict[str, Callable[[Any], None]] = {
            "azureBlobContainer": lambda n : setattr(self, 'azure_blob_container', n.get_str_value()),
            "azureBlobToken": lambda n : setattr(self, 'azure_blob_token', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "exportFileMetadata": lambda n : setattr(self, 'export_file_metadata', n.get_collection_of_object_values(export_file_metadata.ExportFileMetadata)),
            "exportOptions": lambda n : setattr(self, 'export_options', n.get_enum_value(export_options.ExportOptions)),
            "exportStructure": lambda n : setattr(self, 'export_structure', n.get_enum_value(export_file_structure.ExportFileStructure)),
            "outputFolderId": lambda n : setattr(self, 'output_folder_id', n.get_str_value()),
            "outputName": lambda n : setattr(self, 'output_name', n.get_str_value()),
            "reviewSet": lambda n : setattr(self, 'review_set', n.get_object_value(ediscovery_review_set.EdiscoveryReviewSet)),
            "reviewSetQuery": lambda n : setattr(self, 'review_set_query', n.get_object_value(ediscovery_review_set_query.EdiscoveryReviewSetQuery)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def output_folder_id(self,) -> Optional[str]:
        """
        Gets the outputFolderId property value. The outputFolderId property
        Returns: Optional[str]
        """
        return self._output_folder_id
    
    @output_folder_id.setter
    def output_folder_id(self,value: Optional[str] = None) -> None:
        """
        Sets the outputFolderId property value. The outputFolderId property
        Args:
            value: Value to set for the output_folder_id property.
        """
        self._output_folder_id = value
    
    @property
    def output_name(self,) -> Optional[str]:
        """
        Gets the outputName property value. The name provided for the export.
        Returns: Optional[str]
        """
        return self._output_name
    
    @output_name.setter
    def output_name(self,value: Optional[str] = None) -> None:
        """
        Sets the outputName property value. The name provided for the export.
        Args:
            value: Value to set for the output_name property.
        """
        self._output_name = value
    
    @property
    def review_set(self,) -> Optional[ediscovery_review_set.EdiscoveryReviewSet]:
        """
        Gets the reviewSet property value. Review set from where documents are exported.
        Returns: Optional[ediscovery_review_set.EdiscoveryReviewSet]
        """
        return self._review_set
    
    @review_set.setter
    def review_set(self,value: Optional[ediscovery_review_set.EdiscoveryReviewSet] = None) -> None:
        """
        Sets the reviewSet property value. Review set from where documents are exported.
        Args:
            value: Value to set for the review_set property.
        """
        self._review_set = value
    
    @property
    def review_set_query(self,) -> Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery]:
        """
        Gets the reviewSetQuery property value. The review set query which is used to filter the documents for export.
        Returns: Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery]
        """
        return self._review_set_query
    
    @review_set_query.setter
    def review_set_query(self,value: Optional[ediscovery_review_set_query.EdiscoveryReviewSetQuery] = None) -> None:
        """
        Sets the reviewSetQuery property value. The review set query which is used to filter the documents for export.
        Args:
            value: Value to set for the review_set_query property.
        """
        self._review_set_query = value
    
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
        writer.write_collection_of_object_values("exportFileMetadata", self.export_file_metadata)
        writer.write_enum_value("exportOptions", self.export_options)
        writer.write_enum_value("exportStructure", self.export_structure)
        writer.write_str_value("outputFolderId", self.output_folder_id)
        writer.write_str_value("outputName", self.output_name)
        writer.write_object_value("reviewSet", self.review_set)
        writer.write_object_value("reviewSetQuery", self.review_set_query)
    

