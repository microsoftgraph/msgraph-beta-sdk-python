from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, long_running_operation, unified_role_management_alert, unified_role_management_alert_configuration, unified_role_management_alert_definition

from . import entity

class RoleManagementAlert(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RoleManagementAlert and sets the default values.
        """
        super().__init__()
        # The alertConfigurations property
        self._alert_configurations: Optional[List[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]] = None
        # The alertDefinitions property
        self._alert_definitions: Optional[List[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]] = None
        # The alerts property
        self._alerts: Optional[List[unified_role_management_alert.UnifiedRoleManagementAlert]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[long_running_operation.LongRunningOperation]] = None
    
    @property
    def alert_configurations(self,) -> Optional[List[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]]:
        """
        Gets the alertConfigurations property value. The alertConfigurations property
        Returns: Optional[List[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]]
        """
        return self._alert_configurations
    
    @alert_configurations.setter
    def alert_configurations(self,value: Optional[List[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]] = None) -> None:
        """
        Sets the alertConfigurations property value. The alertConfigurations property
        Args:
            value: Value to set for the alert_configurations property.
        """
        self._alert_configurations = value
    
    @property
    def alert_definitions(self,) -> Optional[List[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]]:
        """
        Gets the alertDefinitions property value. The alertDefinitions property
        Returns: Optional[List[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]]
        """
        return self._alert_definitions
    
    @alert_definitions.setter
    def alert_definitions(self,value: Optional[List[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]] = None) -> None:
        """
        Sets the alertDefinitions property value. The alertDefinitions property
        Args:
            value: Value to set for the alert_definitions property.
        """
        self._alert_definitions = value
    
    @property
    def alerts(self,) -> Optional[List[unified_role_management_alert.UnifiedRoleManagementAlert]]:
        """
        Gets the alerts property value. The alerts property
        Returns: Optional[List[unified_role_management_alert.UnifiedRoleManagementAlert]]
        """
        return self._alerts
    
    @alerts.setter
    def alerts(self,value: Optional[List[unified_role_management_alert.UnifiedRoleManagementAlert]] = None) -> None:
        """
        Sets the alerts property value. The alerts property
        Args:
            value: Value to set for the alerts property.
        """
        self._alerts = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleManagementAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleManagementAlert
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleManagementAlert()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, long_running_operation, unified_role_management_alert, unified_role_management_alert_configuration, unified_role_management_alert_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(unified_role_management_alert.UnifiedRoleManagementAlert)),
            "alertConfigurations": lambda n : setattr(self, 'alert_configurations', n.get_collection_of_object_values(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration)),
            "alertDefinitions": lambda n : setattr(self, 'alert_definitions', n.get_collection_of_object_values(unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(long_running_operation.LongRunningOperation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def operations(self,) -> Optional[List[long_running_operation.LongRunningOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[long_running_operation.LongRunningOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[long_running_operation.LongRunningOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_collection_of_object_values("alertConfigurations", self.alert_configurations)
        writer.write_collection_of_object_values("alertDefinitions", self.alert_definitions)
        writer.write_collection_of_object_values("operations", self.operations)
    

