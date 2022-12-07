from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_detection_operator = lazy_import('msgraph.generated.models.win32_lob_app_detection_operator')

class Win32LobAppRequirement(AdditionalDataHolder, Parsable):
    """
    Base class to detect a Win32 App
    """
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
        Instantiates a new win32LobAppRequirement and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The detection value
        self._detection_value: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Contains properties for detection operator.
        self._operator: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRequirement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppRequirement()
    
    @property
    def detection_value(self,) -> Optional[str]:
        """
        Gets the detectionValue property value. The detection value
        Returns: Optional[str]
        """
        return self._detection_value
    
    @detection_value.setter
    def detection_value(self,value: Optional[str] = None) -> None:
        """
        Sets the detectionValue property value. The detection value
        Args:
            value: Value to set for the detectionValue property.
        """
        self._detection_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detection_value": lambda n : setattr(self, 'detection_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(win32_lob_app_detection_operator.Win32LobAppDetectionOperator)),
        }
        return fields
    
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
    
    @property
    def operator(self,) -> Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator]:
        """
        Gets the operator property value. Contains properties for detection operator.
        Returns: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[win32_lob_app_detection_operator.Win32LobAppDetectionOperator] = None) -> None:
        """
        Sets the operator property value. Contains properties for detection operator.
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("detectionValue", self.detection_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_additional_data_value(self.additional_data)
    

