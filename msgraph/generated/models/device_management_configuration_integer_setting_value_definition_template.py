from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate(AdditionalDataHolder, Parsable):
    """
    Integer Setting Value Definition Template
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationIntegerSettingValueDefinitionTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Integer Setting Maximum Value. Valid values -2147483648 to 2147483647
        self._max_value: Optional[int] = None
        # Integer Setting Minimum Value. Valid values -2147483648 to 2147483647
        self._min_value: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "maxValue": lambda n : setattr(self, 'max_value', n.get_int_value()),
            "minValue": lambda n : setattr(self, 'min_value', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def max_value(self,) -> Optional[int]:
        """
        Gets the maxValue property value. Integer Setting Maximum Value. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._max_value
    
    @max_value.setter
    def max_value(self,value: Optional[int] = None) -> None:
        """
        Sets the maxValue property value. Integer Setting Maximum Value. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the max_value property.
        """
        self._max_value = value
    
    @property
    def min_value(self,) -> Optional[int]:
        """
        Gets the minValue property value. Integer Setting Minimum Value. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._min_value
    
    @min_value.setter
    def min_value(self,value: Optional[int] = None) -> None:
        """
        Sets the minValue property value. Integer Setting Minimum Value. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the min_value property.
        """
        self._min_value = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_int_value("maxValue", self.max_value)
        writer.write_int_value("minValue", self.min_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

