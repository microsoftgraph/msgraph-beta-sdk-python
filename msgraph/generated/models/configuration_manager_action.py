from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import configuration_manager_action_type

class ConfigurationManagerAction(AdditionalDataHolder, Parsable):
    """
    Parameter for action triggerConfigurationManagerAction
    """
    def __init__(self,) -> None:
        """
        Instantiates a new configurationManagerAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Action type on Configuration Manager client
        self._action: Optional[configuration_manager_action_type.ConfigurationManagerActionType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def action(self,) -> Optional[configuration_manager_action_type.ConfigurationManagerActionType]:
        """
        Gets the action property value. Action type on Configuration Manager client
        Returns: Optional[configuration_manager_action_type.ConfigurationManagerActionType]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[configuration_manager_action_type.ConfigurationManagerActionType] = None) -> None:
        """
        Sets the action property value. Action type on Configuration Manager client
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigurationManagerAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConfigurationManagerAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import configuration_manager_action_type

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(configuration_manager_action_type.ConfigurationManagerActionType)),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

