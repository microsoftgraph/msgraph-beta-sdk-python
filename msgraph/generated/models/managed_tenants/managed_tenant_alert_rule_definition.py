from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_rule_definition_template, managed_tenant_alert_rule
    from .. import entity

from .. import entity

@dataclass
class ManagedTenantAlertRuleDefinition(entity.Entity):
    # The alertRules property
    alert_rules: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime] = None
    # The definitionTemplate property
    definition_template: Optional[alert_rule_definition_template.AlertRuleDefinitionTemplate] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedTenantAlertRuleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantAlertRuleDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedTenantAlertRuleDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_rule_definition_template, managed_tenant_alert_rule
        from .. import entity

        from . import alert_rule_definition_template, managed_tenant_alert_rule
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "alertRules": lambda n : setattr(self, 'alert_rules', n.get_collection_of_object_values(managed_tenant_alert_rule.ManagedTenantAlertRule)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definitionTemplate": lambda n : setattr(self, 'definition_template', n.get_object_value(alert_rule_definition_template.AlertRuleDefinitionTemplate)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("alertRules", self.alert_rules)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definitionTemplate", self.definition_template)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
    

