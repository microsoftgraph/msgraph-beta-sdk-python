from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WebPartPosition(AdditionalDataHolder, Parsable):
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
    def column_id(self,) -> Optional[float]:
        """
        Gets the columnId property value. Indicates the identifier of the column where the web part is located.
        Returns: Optional[float]
        """
        return self._column_id
    
    @column_id.setter
    def column_id(self,value: Optional[float] = None) -> None:
        """
        Sets the columnId property value. Indicates the identifier of the column where the web part is located.
        Args:
            value: Value to set for the columnId property.
        """
        self._column_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new webPartPosition and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the identifier of the column where the web part is located.
        self._column_id: Optional[float] = None
        # Indicates the horizontal section where the web part is located.
        self._horizontal_section_id: Optional[float] = None
        # Indicates whether the web part is located in the vertical section.
        self._is_in_vertical_section: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Index of the current web part. Represents the order of the web part in this column or section.
        self._web_part_index: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebPartPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebPartPosition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebPartPosition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "column_id": lambda n : setattr(self, 'column_id', n.get_float_value()),
            "horizontal_section_id": lambda n : setattr(self, 'horizontal_section_id', n.get_float_value()),
            "is_in_vertical_section": lambda n : setattr(self, 'is_in_vertical_section', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "web_part_index": lambda n : setattr(self, 'web_part_index', n.get_float_value()),
        }
        return fields
    
    @property
    def horizontal_section_id(self,) -> Optional[float]:
        """
        Gets the horizontalSectionId property value. Indicates the horizontal section where the web part is located.
        Returns: Optional[float]
        """
        return self._horizontal_section_id
    
    @horizontal_section_id.setter
    def horizontal_section_id(self,value: Optional[float] = None) -> None:
        """
        Sets the horizontalSectionId property value. Indicates the horizontal section where the web part is located.
        Args:
            value: Value to set for the horizontalSectionId property.
        """
        self._horizontal_section_id = value
    
    @property
    def is_in_vertical_section(self,) -> Optional[bool]:
        """
        Gets the isInVerticalSection property value. Indicates whether the web part is located in the vertical section.
        Returns: Optional[bool]
        """
        return self._is_in_vertical_section
    
    @is_in_vertical_section.setter
    def is_in_vertical_section(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInVerticalSection property value. Indicates whether the web part is located in the vertical section.
        Args:
            value: Value to set for the isInVerticalSection property.
        """
        self._is_in_vertical_section = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_float_value("columnId", self.column_id)
        writer.write_float_value("horizontalSectionId", self.horizontal_section_id)
        writer.write_bool_value("isInVerticalSection", self.is_in_vertical_section)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("webPartIndex", self.web_part_index)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def web_part_index(self,) -> Optional[float]:
        """
        Gets the webPartIndex property value. Index of the current web part. Represents the order of the web part in this column or section.
        Returns: Optional[float]
        """
        return self._web_part_index
    
    @web_part_index.setter
    def web_part_index(self,value: Optional[float] = None) -> None:
        """
        Sets the webPartIndex property value. Index of the current web part. Represents the order of the web part in this column or section.
        Args:
            value: Value to set for the webPartIndex property.
        """
        self._web_part_index = value
    

