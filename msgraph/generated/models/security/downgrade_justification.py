from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DowngradeJustification(AdditionalDataHolder, Parsable):
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
        Instantiates a new downgradeJustification and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the downgrade is or is not justified.
        self._is_downgrade_justified: Optional[bool] = None
        # Message that indicates why a downgrade is justified. The message will appear in administrative logs.
        self._justification_message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DowngradeJustification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DowngradeJustification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DowngradeJustification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_downgrade_justified": lambda n : setattr(self, 'is_downgrade_justified', n.get_bool_value()),
            "justification_message": lambda n : setattr(self, 'justification_message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_downgrade_justified(self,) -> Optional[bool]:
        """
        Gets the isDowngradeJustified property value. Indicates whether the downgrade is or is not justified.
        Returns: Optional[bool]
        """
        return self._is_downgrade_justified
    
    @is_downgrade_justified.setter
    def is_downgrade_justified(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDowngradeJustified property value. Indicates whether the downgrade is or is not justified.
        Args:
            value: Value to set for the isDowngradeJustified property.
        """
        self._is_downgrade_justified = value
    
    @property
    def justification_message(self,) -> Optional[str]:
        """
        Gets the justificationMessage property value. Message that indicates why a downgrade is justified. The message will appear in administrative logs.
        Returns: Optional[str]
        """
        return self._justification_message
    
    @justification_message.setter
    def justification_message(self,value: Optional[str] = None) -> None:
        """
        Sets the justificationMessage property value. Message that indicates why a downgrade is justified. The message will appear in administrative logs.
        Args:
            value: Value to set for the justificationMessage property.
        """
        self._justification_message = value
    
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
        writer.write_bool_value("isDowngradeJustified", self.is_downgrade_justified)
        writer.write_str_value("justificationMessage", self.justification_message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

