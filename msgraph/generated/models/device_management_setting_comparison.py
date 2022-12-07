from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_comparison_result = lazy_import('msgraph.generated.models.device_management_comparison_result')

class DeviceManagementSettingComparison(AdditionalDataHolder, Parsable):
    """
    Entity representing setting comparison result
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
    
    @property
    def comparison_result(self,) -> Optional[device_management_comparison_result.DeviceManagementComparisonResult]:
        """
        Gets the comparisonResult property value. Setting comparison result type
        Returns: Optional[device_management_comparison_result.DeviceManagementComparisonResult]
        """
        return self._comparison_result
    
    @comparison_result.setter
    def comparison_result(self,value: Optional[device_management_comparison_result.DeviceManagementComparisonResult] = None) -> None:
        """
        Sets the comparisonResult property value. Setting comparison result type
        Args:
            value: Value to set for the comparisonResult property.
        """
        self._comparison_result = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettingComparison and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Setting comparison result type
        self._comparison_result: Optional[device_management_comparison_result.DeviceManagementComparisonResult] = None
        # JSON representation of current intent (or) template setting's value
        self._current_value_json: Optional[str] = None
        # The ID of the setting definition for this instance
        self._definition_id: Optional[str] = None
        # The setting's display name
        self._display_name: Optional[str] = None
        # The setting ID
        self._id: Optional[str] = None
        # JSON representation of new template setting's value
        self._new_value_json: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingComparison:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingComparison
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingComparison()
    
    @property
    def current_value_json(self,) -> Optional[str]:
        """
        Gets the currentValueJson property value. JSON representation of current intent (or) template setting's value
        Returns: Optional[str]
        """
        return self._current_value_json
    
    @current_value_json.setter
    def current_value_json(self,value: Optional[str] = None) -> None:
        """
        Sets the currentValueJson property value. JSON representation of current intent (or) template setting's value
        Args:
            value: Value to set for the currentValueJson property.
        """
        self._current_value_json = value
    
    @property
    def definition_id(self,) -> Optional[str]:
        """
        Gets the definitionId property value. The ID of the setting definition for this instance
        Returns: Optional[str]
        """
        return self._definition_id
    
    @definition_id.setter
    def definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the definitionId property value. The ID of the setting definition for this instance
        Args:
            value: Value to set for the definitionId property.
        """
        self._definition_id = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The setting's display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The setting's display name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comparison_result": lambda n : setattr(self, 'comparison_result', n.get_enum_value(device_management_comparison_result.DeviceManagementComparisonResult)),
            "current_value_json": lambda n : setattr(self, 'current_value_json', n.get_str_value()),
            "definition_id": lambda n : setattr(self, 'definition_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "new_value_json": lambda n : setattr(self, 'new_value_json', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The setting ID
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The setting ID
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def new_value_json(self,) -> Optional[str]:
        """
        Gets the newValueJson property value. JSON representation of new template setting's value
        Returns: Optional[str]
        """
        return self._new_value_json
    
    @new_value_json.setter
    def new_value_json(self,value: Optional[str] = None) -> None:
        """
        Sets the newValueJson property value. JSON representation of new template setting's value
        Args:
            value: Value to set for the newValueJson property.
        """
        self._new_value_json = value
    
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
        writer.write_enum_value("comparisonResult", self.comparison_result)
        writer.write_str_value("currentValueJson", self.current_value_json)
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("newValueJson", self.new_value_json)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

