from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

dlp_action_info = lazy_import('msgraph.generated.models.dlp_action_info')
restriction_action = lazy_import('msgraph.generated.models.restriction_action')
restriction_trigger = lazy_import('msgraph.generated.models.restriction_trigger')

class DeviceRestrictionAction(dlp_action_info.DlpActionInfo):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceRestrictionAction and sets the default values.
        """
        super().__init__()
        # The message property
        self._message: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The restrictionAction property
        self._restriction_action: Optional[restriction_action.RestrictionAction] = None
        # The triggers property
        self._triggers: Optional[List[restriction_trigger.RestrictionTrigger]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceRestrictionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceRestrictionAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceRestrictionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "restriction_action": lambda n : setattr(self, 'restriction_action', n.get_enum_value(restriction_action.RestrictionAction)),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_enum_values(restriction_trigger.RestrictionTrigger)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The message property
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The message property
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
    @property
    def restriction_action(self,) -> Optional[restriction_action.RestrictionAction]:
        """
        Gets the restrictionAction property value. The restrictionAction property
        Returns: Optional[restriction_action.RestrictionAction]
        """
        return self._restriction_action
    
    @restriction_action.setter
    def restriction_action(self,value: Optional[restriction_action.RestrictionAction] = None) -> None:
        """
        Sets the restrictionAction property value. The restrictionAction property
        Args:
            value: Value to set for the restrictionAction property.
        """
        self._restriction_action = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("message", self.message)
        writer.write_enum_value("restrictionAction", self.restriction_action)
        writer.write_enum_value("triggers", self.triggers)
    
    @property
    def triggers(self,) -> Optional[List[restriction_trigger.RestrictionTrigger]]:
        """
        Gets the triggers property value. The triggers property
        Returns: Optional[List[restriction_trigger.RestrictionTrigger]]
        """
        return self._triggers
    
    @triggers.setter
    def triggers(self,value: Optional[List[restriction_trigger.RestrictionTrigger]] = None) -> None:
        """
        Sets the triggers property value. The triggers property
        Args:
            value: Value to set for the triggers property.
        """
        self._triggers = value
    

