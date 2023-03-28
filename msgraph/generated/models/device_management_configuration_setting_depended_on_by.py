from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DeviceManagementConfigurationSettingDependedOnBy(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationSettingDependedOnBy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identifier of child setting that is dependent on the current setting
        self._depended_on_by: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Value that determines if the child setting is required based on the parent setting's selection
        self._required: Optional[bool] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingDependedOnBy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingDependedOnBy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingDependedOnBy()
    
    @property
    def depended_on_by(self,) -> Optional[str]:
        """
        Gets the dependedOnBy property value. Identifier of child setting that is dependent on the current setting
        Returns: Optional[str]
        """
        return self._depended_on_by
    
    @depended_on_by.setter
    def depended_on_by(self,value: Optional[str] = None) -> None:
        """
        Sets the dependedOnBy property value. Identifier of child setting that is dependent on the current setting
        Args:
            value: Value to set for the depended_on_by property.
        """
        self._depended_on_by = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "dependedOnBy": lambda n : setattr(self, 'depended_on_by', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. Value that determines if the child setting is required based on the parent setting's selection
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. Value that determines if the child setting is required based on the parent setting's selection
        Args:
            value: Value to set for the required property.
        """
        self._required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("dependedOnBy", self.depended_on_by)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("required", self.required)
        writer.write_additional_data_value(self.additional_data)
    

