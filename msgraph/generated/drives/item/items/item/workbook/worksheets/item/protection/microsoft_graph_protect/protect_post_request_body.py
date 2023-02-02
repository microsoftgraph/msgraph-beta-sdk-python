from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

workbook_worksheet_protection_options = lazy_import('msgraph.generated.models.workbook_worksheet_protection_options')

class ProtectPostRequestBody(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new protectPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The options property
        self._options: Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProtectPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProtectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "options": lambda n : setattr(self, 'options', n.get_object_value(workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions)),
        }
        return fields
    
    @property
    def options(self,) -> Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions]:
        """
        Gets the options property value. The options property
        Returns: Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions]
        """
        return self._options
    
    @options.setter
    def options(self,value: Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions] = None) -> None:
        """
        Sets the options property value. The options property
        Args:
            value: Value to set for the options property.
        """
        self._options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("options", self.options)
        writer.write_additional_data_value(self.additional_data)
    

