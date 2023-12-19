from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_operation import CaseOperation
    from .ediscovery_search import EdiscoverySearch
    from .ediscovery_search_export_operation_additional_options import EdiscoverySearchExportOperation_additionalOptions
    from .ediscovery_search_export_operation_export_criteria import EdiscoverySearchExportOperation_exportCriteria
    from .ediscovery_search_export_operation_export_format import EdiscoverySearchExportOperation_exportFormat
    from .ediscovery_search_export_operation_export_location import EdiscoverySearchExportOperation_exportLocation
    from .export_file_metadata import ExportFileMetadata

from .case_operation import CaseOperation

@dataclass
class EdiscoverySearchExportOperation(CaseOperation):
    # The additionalOptions property
    additional_options: Optional[EdiscoverySearchExportOperation_additionalOptions] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The exportCriteria property
    export_criteria: Optional[EdiscoverySearchExportOperation_exportCriteria] = None
    # The exportFileMetadata property
    export_file_metadata: Optional[List[ExportFileMetadata]] = None
    # The exportFormat property
    export_format: Optional[EdiscoverySearchExportOperation_exportFormat] = None
    # The exportLocation property
    export_location: Optional[EdiscoverySearchExportOperation_exportLocation] = None
    # The exportSingleItems property
    export_single_items: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The search property
    search: Optional[EdiscoverySearch] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoverySearchExportOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoverySearchExportOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoverySearchExportOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .case_operation import CaseOperation
        from .ediscovery_search import EdiscoverySearch
        from .ediscovery_search_export_operation_additional_options import EdiscoverySearchExportOperation_additionalOptions
        from .ediscovery_search_export_operation_export_criteria import EdiscoverySearchExportOperation_exportCriteria
        from .ediscovery_search_export_operation_export_format import EdiscoverySearchExportOperation_exportFormat
        from .ediscovery_search_export_operation_export_location import EdiscoverySearchExportOperation_exportLocation
        from .export_file_metadata import ExportFileMetadata

        from .case_operation import CaseOperation
        from .ediscovery_search import EdiscoverySearch
        from .ediscovery_search_export_operation_additional_options import EdiscoverySearchExportOperation_additionalOptions
        from .ediscovery_search_export_operation_export_criteria import EdiscoverySearchExportOperation_exportCriteria
        from .ediscovery_search_export_operation_export_format import EdiscoverySearchExportOperation_exportFormat
        from .ediscovery_search_export_operation_export_location import EdiscoverySearchExportOperation_exportLocation
        from .export_file_metadata import ExportFileMetadata

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalOptions": lambda n : setattr(self, 'additional_options', n.get_enum_value(EdiscoverySearchExportOperation_additionalOptions)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exportCriteria": lambda n : setattr(self, 'export_criteria', n.get_enum_value(EdiscoverySearchExportOperation_exportCriteria)),
            "exportFileMetadata": lambda n : setattr(self, 'export_file_metadata', n.get_collection_of_object_values(ExportFileMetadata)),
            "exportFormat": lambda n : setattr(self, 'export_format', n.get_enum_value(EdiscoverySearchExportOperation_exportFormat)),
            "exportLocation": lambda n : setattr(self, 'export_location', n.get_enum_value(EdiscoverySearchExportOperation_exportLocation)),
            "exportSingleItems": lambda n : setattr(self, 'export_single_items', n.get_bool_value()),
            "search": lambda n : setattr(self, 'search', n.get_object_value(EdiscoverySearch)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("additionalOptions", self.additional_options)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("exportCriteria", self.export_criteria)
        writer.write_collection_of_object_values("exportFileMetadata", self.export_file_metadata)
        writer.write_enum_value("exportFormat", self.export_format)
        writer.write_enum_value("exportLocation", self.export_location)
        writer.write_bool_value("exportSingleItems", self.export_single_items)
        writer.write_object_value("search", self.search)
    

