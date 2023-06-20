from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, long_running_operation, unified_role_management_alert, unified_role_management_alert_configuration, unified_role_management_alert_definition

from . import entity

@dataclass
class RoleManagementAlert(entity.Entity):
    # The alertConfigurations property
    alert_configurations: Optional[List[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]] = None
    # The alertDefinitions property
    alert_definitions: Optional[List[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]] = None
    # The alerts property
    alerts: Optional[List[unified_role_management_alert.UnifiedRoleManagementAlert]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[List[long_running_operation.LongRunningOperation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleManagementAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleManagementAlert
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RoleManagementAlert()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, long_running_operation, unified_role_management_alert, unified_role_management_alert_configuration, unified_role_management_alert_definition

        from . import entity, long_running_operation, unified_role_management_alert, unified_role_management_alert_configuration, unified_role_management_alert_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "alertConfigurations": lambda n : setattr(self, 'alert_configurations', n.get_collection_of_object_values(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration)),
            "alertDefinitions": lambda n : setattr(self, 'alert_definitions', n.get_collection_of_object_values(unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition)),
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(unified_role_management_alert.UnifiedRoleManagementAlert)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(long_running_operation.LongRunningOperation)),
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
        writer.write_collection_of_object_values("alertConfigurations", self.alert_configurations)
        writer.write_collection_of_object_values("alertDefinitions", self.alert_definitions)
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_collection_of_object_values("operations", self.operations)
    

