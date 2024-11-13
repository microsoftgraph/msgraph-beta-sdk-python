from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert import Alert
    from .alert_configuration import AlertConfiguration

from ..entity import Entity

@dataclass
class HealthMonitoringRoot(Entity, Parsable):
    # The configuration of an alert type, which defines behavior that occurs when an alert is created.
    alert_configurations: Optional[List[AlertConfiguration]] = None
    # The collection of health monitoring system detected alerts for anomalous usage patterns found in a Microsoft Entra tenant.
    alerts: Optional[List[Alert]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HealthMonitoringRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HealthMonitoringRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HealthMonitoringRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert import Alert
        from .alert_configuration import AlertConfiguration

        from ..entity import Entity
        from .alert import Alert
        from .alert_configuration import AlertConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "alertConfigurations": lambda n : setattr(self, 'alert_configurations', n.get_collection_of_object_values(AlertConfiguration)),
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(Alert)),
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
        from ..entity import Entity
        from .alert import Alert
        from .alert_configuration import AlertConfiguration

        writer.write_collection_of_object_values("alertConfigurations", self.alert_configurations)
        writer.write_collection_of_object_values("alerts", self.alerts)
    

