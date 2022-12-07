from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_action_type = lazy_import('msgraph.generated.models.mobile_app_action_type')
mobile_app_troubleshooting_history_item = lazy_import('msgraph.generated.models.mobile_app_troubleshooting_history_item')
run_state = lazy_import('msgraph.generated.models.run_state')

class MobileAppTroubleshootingAppStateHistory(mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem):
    @property
    def action_type(self,) -> Optional[mobile_app_action_type.MobileAppActionType]:
        """
        Gets the actionType property value. Defines the Action Types for an Intune Application.
        Returns: Optional[mobile_app_action_type.MobileAppActionType]
        """
        return self._action_type
    
    @action_type.setter
    def action_type(self,value: Optional[mobile_app_action_type.MobileAppActionType] = None) -> None:
        """
        Sets the actionType property value. Defines the Action Types for an Intune Application.
        Args:
            value: Value to set for the actionType property.
        """
        self._action_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MobileAppTroubleshootingAppStateHistory and sets the default values.
        """
        super().__init__()
        # Defines the Action Types for an Intune Application.
        self._action_type: Optional[mobile_app_action_type.MobileAppActionType] = None
        # Error code for the failure, empty if no failure.
        self._error_code: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the type of execution status of the device management script.
        self._run_state: Optional[run_state.RunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppTroubleshootingAppStateHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingAppStateHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppTroubleshootingAppStateHistory()
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. Error code for the failure, empty if no failure.
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. Error code for the failure, empty if no failure.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_type": lambda n : setattr(self, 'action_type', n.get_enum_value(mobile_app_action_type.MobileAppActionType)),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "run_state": lambda n : setattr(self, 'run_state', n.get_enum_value(run_state.RunState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def run_state(self,) -> Optional[run_state.RunState]:
        """
        Gets the runState property value. Indicates the type of execution status of the device management script.
        Returns: Optional[run_state.RunState]
        """
        return self._run_state
    
    @run_state.setter
    def run_state(self,value: Optional[run_state.RunState] = None) -> None:
        """
        Sets the runState property value. Indicates the type of execution status of the device management script.
        Args:
            value: Value to set for the runState property.
        """
        self._run_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("actionType", self.action_type)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_enum_value("runState", self.run_state)
    

