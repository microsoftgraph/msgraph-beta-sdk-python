from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegate_allowed_actions import DelegateAllowedActions
    from .entity import Entity

from .entity import Entity

@dataclass
class DelegationSettings(Entity, Parsable):
    # The allowedActions property
    allowed_actions: Optional[DelegateAllowedActions] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The isActive property
    is_active: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegationSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delegate_allowed_actions import DelegateAllowedActions
        from .entity import Entity

        from .delegate_allowed_actions import DelegateAllowedActions
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedActions": lambda n : setattr(self, 'allowed_actions', n.get_object_value(DelegateAllowedActions)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .delegate_allowed_actions import DelegateAllowedActions
        from .entity import Entity

        writer.write_object_value("allowedActions", self.allowed_actions)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isActive", self.is_active)
    

