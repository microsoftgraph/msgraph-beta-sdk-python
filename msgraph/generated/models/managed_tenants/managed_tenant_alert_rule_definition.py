from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert_rule_definition_template = lazy_import('msgraph.generated.models.managed_tenants.alert_rule_definition_template')
managed_tenant_alert_rule = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_alert_rule')

class ManagedTenantAlertRuleDefinition(entity.Entity):
    @property
    def alert_rules(self,) -> Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]]:
        """
        Gets the alertRules property value. The alertRules property
        Returns: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]]
        """
        return self._alert_rules
    
    @alert_rules.setter
    def alert_rules(self,value: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]] = None) -> None:
        """
        Sets the alertRules property value. The alertRules property
        Args:
            value: Value to set for the alertRules property.
        """
        self._alert_rules = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedTenantAlertRuleDefinition and sets the default values.
        """
        super().__init__()
        # The alertRules property
        self._alert_rules: Optional[List[managed_tenant_alert_rule.ManagedTenantAlertRule]] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The definitionTemplate property
        self._definition_template: Optional[alert_rule_definition_template.AlertRuleDefinitionTemplate] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The createdByUserId property
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The createdByUserId property
        Args:
            value: Value to set for the createdByUserId property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedTenantAlertRuleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantAlertRuleDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedTenantAlertRuleDefinition()
    
    @property
    def definition_template(self,) -> Optional[alert_rule_definition_template.AlertRuleDefinitionTemplate]:
        """
        Gets the definitionTemplate property value. The definitionTemplate property
        Returns: Optional[alert_rule_definition_template.AlertRuleDefinitionTemplate]
        """
        return self._definition_template
    
    @definition_template.setter
    def definition_template(self,value: Optional[alert_rule_definition_template.AlertRuleDefinitionTemplate] = None) -> None:
        """
        Sets the definitionTemplate property value. The definitionTemplate property
        Args:
            value: Value to set for the definitionTemplate property.
        """
        self._definition_template = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alert_rules": lambda n : setattr(self, 'alert_rules', n.get_collection_of_object_values(managed_tenant_alert_rule.ManagedTenantAlertRule)),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definition_template": lambda n : setattr(self, 'definition_template', n.get_object_value(alert_rule_definition_template.AlertRuleDefinitionTemplate)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The lastActionByUserId property
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The lastActionByUserId property
        Args:
            value: Value to set for the lastActionByUserId property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The lastActionDateTime property
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The lastActionDateTime property
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("alertRules", self.alert_rules)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definitionTemplate", self.definition_template)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
    

