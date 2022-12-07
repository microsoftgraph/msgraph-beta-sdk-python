from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert_record = lazy_import('msgraph.generated.models.device_management.alert_record')
alert_rule = lazy_import('msgraph.generated.models.device_management.alert_rule')

class Monitoring(entity.Entity):
    @property
    def alert_records(self,) -> Optional[List[alert_record.AlertRecord]]:
        """
        Gets the alertRecords property value. The collection of records of alert events.
        Returns: Optional[List[alert_record.AlertRecord]]
        """
        return self._alert_records
    
    @alert_records.setter
    def alert_records(self,value: Optional[List[alert_record.AlertRecord]] = None) -> None:
        """
        Sets the alertRecords property value. The collection of records of alert events.
        Args:
            value: Value to set for the alertRecords property.
        """
        self._alert_records = value
    
    @property
    def alert_rules(self,) -> Optional[List[alert_rule.AlertRule]]:
        """
        Gets the alertRules property value. The collection of alert rules.
        Returns: Optional[List[alert_rule.AlertRule]]
        """
        return self._alert_rules
    
    @alert_rules.setter
    def alert_rules(self,value: Optional[List[alert_rule.AlertRule]] = None) -> None:
        """
        Sets the alertRules property value. The collection of alert rules.
        Args:
            value: Value to set for the alertRules property.
        """
        self._alert_rules = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new monitoring and sets the default values.
        """
        super().__init__()
        # The collection of records of alert events.
        self._alert_records: Optional[List[alert_record.AlertRecord]] = None
        # The collection of alert rules.
        self._alert_rules: Optional[List[alert_rule.AlertRule]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Monitoring:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Monitoring
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Monitoring()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alert_records": lambda n : setattr(self, 'alert_records', n.get_collection_of_object_values(alert_record.AlertRecord)),
            "alert_rules": lambda n : setattr(self, 'alert_rules', n.get_collection_of_object_values(alert_rule.AlertRule)),
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
        writer.write_collection_of_object_values("alertRecords", self.alert_records)
        writer.write_collection_of_object_values("alertRules", self.alert_rules)
    

