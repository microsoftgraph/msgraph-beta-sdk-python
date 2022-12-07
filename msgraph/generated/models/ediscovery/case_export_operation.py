from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

case_operation = lazy_import('msgraph.generated.models.ediscovery.case_operation')
export_file_structure = lazy_import('msgraph.generated.models.ediscovery.export_file_structure')
export_options = lazy_import('msgraph.generated.models.ediscovery.export_options')
review_set = lazy_import('msgraph.generated.models.ediscovery.review_set')

class CaseExportOperation(case_operation.CaseOperation):
    @property
    def azure_blob_container(self,) -> Optional[str]:
        """
        Gets the azureBlobContainer property value. The name of the Azure storage location where the export will be stored. This only applies to exports stored in your own Azure storage location.
        Returns: Optional[str]
        """
        return self._azure_blob_container
    
    @azure_blob_container.setter
    def azure_blob_container(self,value: Optional[str] = None) -> None:
        """
        Sets the azureBlobContainer property value. The name of the Azure storage location where the export will be stored. This only applies to exports stored in your own Azure storage location.
        Args:
            value: Value to set for the azureBlobContainer property.
        """
        self._azure_blob_container = value
    
    @property
    def azure_blob_token(self,) -> Optional[str]:
        """
        Gets the azureBlobToken property value. The SAS token for the Azure storage location.  This only applies to exports stored in your own Azure storage location.
        Returns: Optional[str]
        """
        return self._azure_blob_token
    
    @azure_blob_token.setter
    def azure_blob_token(self,value: Optional[str] = None) -> None:
        """
        Sets the azureBlobToken property value. The SAS token for the Azure storage location.  This only applies to exports stored in your own Azure storage location.
        Args:
            value: Value to set for the azureBlobToken property.
        """
        self._azure_blob_token = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CaseExportOperation and sets the default values.
        """
        super().__init__()
        # The name of the Azure storage location where the export will be stored. This only applies to exports stored in your own Azure storage location.
        self._azure_blob_container: Optional[str] = None
        # The SAS token for the Azure storage location.  This only applies to exports stored in your own Azure storage location.
        self._azure_blob_token: Optional[str] = None
        # The description provided for the export.
        self._description: Optional[str] = None
        # The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement, fileInfo, tags.
        self._export_options: Optional[export_options.ExportOptions] = None
        # The options provided that specify the structure of the export. For more details, see reviewSet: export. Possible values are: none, directory, pst.
        self._export_structure: Optional[export_file_structure.ExportFileStructure] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The outputFolderId property
        self._output_folder_id: Optional[str] = None
        # The name provided for the export.
        self._output_name: Optional[str] = None
        # The review set the content is being exported from.
        self._review_set: Optional[review_set.ReviewSet] = None
    
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
    def export_options(self,) -> Optional[export_options.ExportOptions]:
        """
        Gets the exportOptions property value. The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement, fileInfo, tags.
        Returns: Optional[export_options.ExportOptions]
        """
        return self._export_options
    
    @export_options.setter
    def export_options(self,value: Optional[export_options.ExportOptions] = None) -> None:
        """
        Sets the exportOptions property value. The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement, fileInfo, tags.
        Args:
            value: Value to set for the exportOptions property.
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
            value: Value to set for the exportStructure property.
        """
        self._export_structure = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_blob_container": lambda n : setattr(self, 'azure_blob_container', n.get_str_value()),
            "azure_blob_token": lambda n : setattr(self, 'azure_blob_token', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "export_options": lambda n : setattr(self, 'export_options', n.get_enum_value(export_options.ExportOptions)),
            "export_structure": lambda n : setattr(self, 'export_structure', n.get_enum_value(export_file_structure.ExportFileStructure)),
            "output_folder_id": lambda n : setattr(self, 'output_folder_id', n.get_str_value()),
            "output_name": lambda n : setattr(self, 'output_name', n.get_str_value()),
            "review_set": lambda n : setattr(self, 'review_set', n.get_object_value(review_set.ReviewSet)),
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
            value: Value to set for the outputFolderId property.
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
            value: Value to set for the outputName property.
        """
        self._output_name = value
    
    @property
    def review_set(self,) -> Optional[review_set.ReviewSet]:
        """
        Gets the reviewSet property value. The review set the content is being exported from.
        Returns: Optional[review_set.ReviewSet]
        """
        return self._review_set
    
    @review_set.setter
    def review_set(self,value: Optional[review_set.ReviewSet] = None) -> None:
        """
        Sets the reviewSet property value. The review set the content is being exported from.
        Args:
            value: Value to set for the reviewSet property.
        """
        self._review_set = value
    
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
    

