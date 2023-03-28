from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_role_management_alert_configuration, unified_role_management_alert_definition, unified_role_management_alert_incident

from . import entity

class UnifiedRoleManagementAlert(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementAlert and sets the default values.
        """
        super().__init__()
        # The alertConfiguration property
        self._alert_configuration: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration] = None
        # The alertDefinition property
        self._alert_definition: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition] = None
        # The alertDefinitionId property
        self._alert_definition_id: Optional[str] = None
        # The alertIncidents property
        self._alert_incidents: Optional[List[unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident]] = None
        # The incidentCount property
        self._incident_count: Optional[int] = None
        # The isActive property
        self._is_active: Optional[bool] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The lastScannedDateTime property
        self._last_scanned_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The scopeId property
        self._scope_id: Optional[str] = None
        # The scopeType property
        self._scope_type: Optional[str] = None
    
    @property
    def alert_configuration(self,) -> Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]:
        """
        Gets the alertConfiguration property value. The alertConfiguration property
        Returns: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration]
        """
        return self._alert_configuration
    
    @alert_configuration.setter
    def alert_configuration(self,value: Optional[unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration] = None) -> None:
        """
        Sets the alertConfiguration property value. The alertConfiguration property
        Args:
            value: Value to set for the alert_configuration property.
        """
        self._alert_configuration = value
    
    @property
    def alert_definition(self,) -> Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]:
        """
        Gets the alertDefinition property value. The alertDefinition property
        Returns: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]
        """
        return self._alert_definition
    
    @alert_definition.setter
    def alert_definition(self,value: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition] = None) -> None:
        """
        Sets the alertDefinition property value. The alertDefinition property
        Args:
            value: Value to set for the alert_definition property.
        """
        self._alert_definition = value
    
    @property
    def alert_definition_id(self,) -> Optional[str]:
        """
        Gets the alertDefinitionId property value. The alertDefinitionId property
        Returns: Optional[str]
        """
        return self._alert_definition_id
    
    @alert_definition_id.setter
    def alert_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the alertDefinitionId property value. The alertDefinitionId property
        Args:
            value: Value to set for the alert_definition_id property.
        """
        self._alert_definition_id = value
    
    @property
    def alert_incidents(self,) -> Optional[List[unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident]]:
        """
        Gets the alertIncidents property value. The alertIncidents property
        Returns: Optional[List[unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident]]
        """
        return self._alert_incidents
    
    @alert_incidents.setter
    def alert_incidents(self,value: Optional[List[unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident]] = None) -> None:
        """
        Sets the alertIncidents property value. The alertIncidents property
        Args:
            value: Value to set for the alert_incidents property.
        """
        self._alert_incidents = value
    
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
    
    @property
    def incident_count(self,) -> Optional[int]:
        """
        Gets the incidentCount property value. The incidentCount property
        Returns: Optional[int]
        """
        return self._incident_count
    
    @incident_count.setter
    def incident_count(self,value: Optional[int] = None) -> None:
        """
        Sets the incidentCount property value. The incidentCount property
        Args:
            value: Value to set for the incident_count property.
        """
        self._incident_count = value
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. The isActive property
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. The isActive property
        Args:
            value: Value to set for the is_active property.
        """
        self._is_active = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def last_scanned_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastScannedDateTime property value. The lastScannedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_scanned_date_time
    
    @last_scanned_date_time.setter
    def last_scanned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastScannedDateTime property value. The lastScannedDateTime property
        Args:
            value: Value to set for the last_scanned_date_time property.
        """
        self._last_scanned_date_time = value
    
    @property
    def scope_id(self,) -> Optional[str]:
        """
        Gets the scopeId property value. The scopeId property
        Returns: Optional[str]
        """
        return self._scope_id
    
    @scope_id.setter
    def scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeId property value. The scopeId property
        Args:
            value: Value to set for the scope_id property.
        """
        self._scope_id = value
    
    @property
    def scope_type(self,) -> Optional[str]:
        """
        Gets the scopeType property value. The scopeType property
        Returns: Optional[str]
        """
        return self._scope_type
    
    @scope_type.setter
    def scope_type(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeType property value. The scopeType property
        Args:
            value: Value to set for the scope_type property.
        """
        self._scope_type = value
    
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
    

