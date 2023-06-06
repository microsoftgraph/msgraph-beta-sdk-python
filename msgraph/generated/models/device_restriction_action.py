from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dlp_action_info, restriction_action, restriction_trigger

from . import dlp_action_info

@dataclass
class DeviceRestrictionAction(dlp_action_info.DlpActionInfo):
    # The message property
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The restrictionAction property
    restriction_action: Optional[restriction_action.RestrictionAction] = None
    # The triggers property
    triggers: Optional[List[restriction_trigger.RestrictionTrigger]] = None
    
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
        from . import dlp_action_info, restriction_action, restriction_trigger

        fields: Dict[str, Callable[[Any], None]] = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "restrictionAction": lambda n : setattr(self, 'restriction_action', n.get_enum_value(restriction_action.RestrictionAction)),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_enum_values(restriction_trigger.RestrictionTrigger)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    

