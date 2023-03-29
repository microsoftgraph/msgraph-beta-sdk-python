from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_configuration

from . import unified_role_management_alert_configuration

class StaleSignInAlertConfiguration(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new StaleSignInAlertConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.staleSignInAlertConfiguration"
        # The duration property
        self._duration: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StaleSignInAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StaleSignInAlertConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StaleSignInAlertConfiguration()
    
    @property
    def duration(self,) -> Optional[timedelta]:
        """
        Gets the duration property value. The duration property
        Returns: Optional[timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the duration property value. The duration property
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
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
        writer.write_timedelta_value("duration", self.duration)
    

