from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_role_management_alert_configuration, unified_role_management_alert_definition, unified_role_management_alert_incident

from . import entity

@dataclass
class UnifiedRoleManagementAlert(entity.Entity):
    # The alertConfiguration property
    alert_configuration: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration] = None
    # The alertDefinition property
    alert_definition: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition] = None
    # The alertDefinitionId property
    alert_definition_id: Optional[str] = None
    # The alertIncidents property
    alert_incidents: Optional[List[unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident]] = None
    # The incidentCount property
    incident_count: Optional[int] = None
    # The isActive property
    is_active: Optional[bool] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The lastScannedDateTime property
    last_scanned_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scopeId property
    scope_id: Optional[str] = None
    # The scopeType property
    scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlert
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementAlert()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_role_management_alert_configuration, unified_role_management_alert_definition, unified_role_management_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
            "alertConfiguration": lambda n : setattr(self, 'alert_configuration', n.get_object_value(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration)),
            "alertDefinition": lambda n : setattr(self, 'alert_definition', n.get_object_value(unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition)),
            "alertDefinitionId": lambda n : setattr(self, 'alert_definition_id', n.get_str_value()),
            "alertIncidents": lambda n : setattr(self, 'alert_incidents', n.get_collection_of_object_values(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident)),
            "incidentCount": lambda n : setattr(self, 'incident_count', n.get_int_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastScannedDateTime": lambda n : setattr(self, 'last_scanned_date_time', n.get_datetime_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
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
        writer.write_object_value("alertConfiguration", self.alert_configuration)
        writer.write_object_value("alertDefinition", self.alert_definition)
        writer.write_str_value("alertDefinitionId", self.alert_definition_id)
        writer.write_collection_of_object_values("alertIncidents", self.alert_incidents)
        writer.write_int_value("incidentCount", self.incident_count)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastScannedDateTime", self.last_scanned_date_time)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

