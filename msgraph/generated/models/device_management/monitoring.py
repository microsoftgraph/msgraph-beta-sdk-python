from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_record import AlertRecord
    from .alert_rule import AlertRule

from ..entity import Entity

@dataclass
class Monitoring(Entity):
    # The collection of records of alert events.
    alert_records: Optional[List[AlertRecord]] = None
    # The collection of alert rules.
    alert_rules: Optional[List[AlertRule]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Monitoring:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Monitoring
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Monitoring()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_record import AlertRecord
        from .alert_rule import AlertRule

        from ..entity import Entity
        from .alert_record import AlertRecord
        from .alert_rule import AlertRule

        fields: Dict[str, Callable[[Any], None]] = {
            "alertRecords": lambda n : setattr(self, 'alert_records', n.get_collection_of_object_values(AlertRecord)),
            "alertRules": lambda n : setattr(self, 'alert_rules', n.get_collection_of_object_values(AlertRule)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("alertRecords", self.alert_records)
        writer.write_collection_of_object_values("alertRules", self.alert_rules)
    

