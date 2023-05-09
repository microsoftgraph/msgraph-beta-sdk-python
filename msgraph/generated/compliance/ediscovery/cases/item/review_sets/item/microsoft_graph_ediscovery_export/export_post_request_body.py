from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.ediscovery import export_file_structure, export_options

class ExportPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new exportPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The azureBlobContainer property
        self._azure_blob_container: Optional[str] = None
        # The azureBlobToken property
        self._azure_blob_token: Optional[str] = None
        # The description property
        self._description: Optional[str] = None
        # The exportOptions property
        self._export_options: Optional[export_options.ExportOptions] = None
        # The exportStructure property
        self._export_structure: Optional[export_file_structure.ExportFileStructure] = None
        # The outputName property
        self._output_name: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExportPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExportPostRequestBody()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def export_options(self,) -> Optional[export_options.ExportOptions]:
        """
        Gets the exportOptions property value. The exportOptions property
        Returns: Optional[export_options.ExportOptions]
        """
        return self._export_options
    
    @export_options.setter
    def export_options(self,value: Optional[export_options.ExportOptions] = None) -> None:
        """
        Sets the exportOptions property value. The exportOptions property
        Args:
            value: Value to set for the export_options property.
        """
        self._export_options = value
    
    @property
    def export_structure(self,) -> Optional[export_file_structure.ExportFileStructure]:
        """
        Gets the exportStructure property value. The exportStructure property
        Returns: Optional[export_file_structure.ExportFileStructure]
        """
        return self._export_structure
    
    @export_structure.setter
    def export_structure(self,value: Optional[export_file_structure.ExportFileStructure] = None) -> None:
        """
        Sets the exportStructure property value. The exportStructure property
        Args:
            value: Value to set for the export_structure property.
        """
        self._export_structure = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.ediscovery import export_file_structure, export_options

        fields: Dict[str, Callable[[Any], None]] = {
            "azureBlobContainer": lambda n : setattr(self, 'azure_blob_container', n.get_str_value()),
            "azureBlobToken": lambda n : setattr(self, 'azure_blob_token', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "exportOptions": lambda n : setattr(self, 'export_options', n.get_enum_value(export_options.ExportOptions)),
            "exportStructure": lambda n : setattr(self, 'export_structure', n.get_enum_value(export_file_structure.ExportFileStructure)),
            "outputName": lambda n : setattr(self, 'output_name', n.get_str_value()),
        }
        return fields
    
    @property
    def output_name(self,) -> Optional[str]:
        """
        Gets the outputName property value. The outputName property
        Returns: Optional[str]
        """
        return self._output_name
    
    @output_name.setter
    def output_name(self,value: Optional[str] = None) -> None:
        """
        Sets the outputName property value. The outputName property
        Args:
            value: Value to set for the output_name property.
        """
        self._output_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("azureBlobContainer", self.azure_blob_container)
        writer.write_str_value("azureBlobToken", self.azure_blob_token)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("exportOptions", self.export_options)
        writer.write_enum_value("exportStructure", self.export_structure)
        writer.write_str_value("outputName", self.output_name)
        writer.write_additional_data_value(self.additional_data)
    

