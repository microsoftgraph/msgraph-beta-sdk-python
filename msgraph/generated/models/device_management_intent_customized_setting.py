from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DeviceManagementIntentCustomizedSetting(AdditionalDataHolder, Parsable):
    """
    Default and customized value of a setting in a Security Baseline
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementIntentCustomizedSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # JSON representation of the customized value, if different from default
        self._customized_json: Optional[str] = None
        # JSON representation of the default value from the template
        self._default_json: Optional[str] = None
        # The ID of the setting definition for this setting
        self._definition_id: Optional[str] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementIntentCustomizedSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntentCustomizedSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementIntentCustomizedSetting()
    
    @property
    def customized_json(self,) -> Optional[str]:
        """
        Gets the customizedJson property value. JSON representation of the customized value, if different from default
        Returns: Optional[str]
        """
        return self._customized_json
    
    @customized_json.setter
    def customized_json(self,value: Optional[str] = None) -> None:
        """
        Sets the customizedJson property value. JSON representation of the customized value, if different from default
        Args:
            value: Value to set for the customized_json property.
        """
        self._customized_json = value
    
    @property
    def default_json(self,) -> Optional[str]:
        """
        Gets the defaultJson property value. JSON representation of the default value from the template
        Returns: Optional[str]
        """
        return self._default_json
    
    @default_json.setter
    def default_json(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultJson property value. JSON representation of the default value from the template
        Args:
            value: Value to set for the default_json property.
        """
        self._default_json = value
    
    @property
    def definition_id(self,) -> Optional[str]:
        """
        Gets the definitionId property value. The ID of the setting definition for this setting
        Returns: Optional[str]
        """
        return self._definition_id
    
    @definition_id.setter
    def definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the definitionId property value. The ID of the setting definition for this setting
        Args:
            value: Value to set for the definition_id property.
        """
        self._definition_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "customizedJson": lambda n : setattr(self, 'customized_json', n.get_str_value()),
            "defaultJson": lambda n : setattr(self, 'default_json', n.get_str_value()),
            "definitionId": lambda n : setattr(self, 'definition_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("customizedJson", self.customized_json)
        writer.write_str_value("defaultJson", self.default_json)
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

