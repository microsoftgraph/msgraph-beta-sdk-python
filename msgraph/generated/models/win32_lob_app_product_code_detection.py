from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_detection = lazy_import('msgraph.generated.models.win32_lob_app_detection')
win32_lob_app_detection_operator = lazy_import('msgraph.generated.models.win32_lob_app_detection_operator')

class Win32LobAppProductCodeDetection(win32_lob_app_detection.Win32LobAppDetection):
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppProductCodeDetection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppProductCodeDetection"
        # The product code of Win32 Line of Business (LoB) app.
        self._product_code: Optional[str] = None
        # The product version of Win32 Line of Business (LoB) app.
        self._product_version: Optional[str] = None
        # Contains properties for detection operator.
        self._product_version_operator: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppProductCodeDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppProductCodeDetection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppProductCodeDetection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "product_code": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "product_version": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "product_version_operator": lambda n : setattr(self, 'product_version_operator', n.get_enum_value(win32_lob_app_detection_operator.Win32LobAppDetectionOperator)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def product_code(self,) -> Optional[str]:
        """
        Gets the productCode property value. The product code of Win32 Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._product_code
    
    @product_code.setter
    def product_code(self,value: Optional[str] = None) -> None:
        """
        Sets the productCode property value. The product code of Win32 Line of Business (LoB) app.
        Args:
            value: Value to set for the productCode property.
        """
        self._product_code = value
    
    @property
    def product_version(self,) -> Optional[str]:
        """
        Gets the productVersion property value. The product version of Win32 Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._product_version
    
    @product_version.setter
    def product_version(self,value: Optional[str] = None) -> None:
        """
        Sets the productVersion property value. The product version of Win32 Line of Business (LoB) app.
        Args:
            value: Value to set for the productVersion property.
        """
        self._product_version = value
    
    @property
    def product_version_operator(self,) -> Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator]:
        """
        Gets the productVersionOperator property value. Contains properties for detection operator.
        Returns: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator]
        """
        return self._product_version_operator
    
    @product_version_operator.setter
    def product_version_operator(self,value: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator] = None) -> None:
        """
        Sets the productVersionOperator property value. Contains properties for detection operator.
        Args:
            value: Value to set for the productVersionOperator property.
        """
        self._product_version_operator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_enum_value("productVersionOperator", self.product_version_operator)
    

