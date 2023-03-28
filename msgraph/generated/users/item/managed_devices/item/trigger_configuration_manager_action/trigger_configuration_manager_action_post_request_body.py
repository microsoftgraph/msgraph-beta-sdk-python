from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models import configuration_manager_action

class TriggerConfigurationManagerActionPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new triggerConfigurationManagerActionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Parameter for action triggerConfigurationManagerAction
        self._configuration_manager_action: Optional[configuration_manager_action.ConfigurationManagerAction] = None
    
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
    def configuration_manager_action(self,) -> Optional[configuration_manager_action.ConfigurationManagerAction]:
        """
        Gets the configurationManagerAction property value. Parameter for action triggerConfigurationManagerAction
        Returns: Optional[configuration_manager_action.ConfigurationManagerAction]
        """
        return self._configuration_manager_action
    
    @configuration_manager_action.setter
    def configuration_manager_action(self,value: Optional[configuration_manager_action.ConfigurationManagerAction] = None) -> None:
        """
        Sets the configurationManagerAction property value. Parameter for action triggerConfigurationManagerAction
        Args:
            value: Value to set for the configuration_manager_action property.
        """
        self._configuration_manager_action = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TriggerConfigurationManagerActionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TriggerConfigurationManagerActionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TriggerConfigurationManagerActionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models import configuration_manager_action

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationManagerAction": lambda n : setattr(self, 'configuration_manager_action', n.get_object_value(configuration_manager_action.ConfigurationManagerAction)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("configurationManagerAction", self.configuration_manager_action)
        writer.write_additional_data_value(self.additional_data)
    

