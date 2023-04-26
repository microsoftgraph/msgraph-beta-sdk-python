from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, ndes_connector_state

from . import entity

class NdesConnector(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new NdesConnector and sets the default values.
        """
        super().__init__()
        # The build version of the Ndes Connector.
        self._connector_version: Optional[str] = None
        # The friendly name of the Ndes Connector.
        self._display_name: Optional[str] = None
        # Timestamp when on-prem certificate connector was enrolled in Intune.
        self._enrolled_date_time: Optional[datetime] = None
        # Last connection time for the Ndes Connector
        self._last_connection_date_time: Optional[datetime] = None
        # Name of the machine running on-prem certificate connector service.
        self._machine_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Entity instance.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The current status of the Ndes Connector.
        self._state: Optional[ndes_connector_state.NdesConnectorState] = None
    
    @property
    def connector_version(self,) -> Optional[str]:
        """
        Gets the connectorVersion property value. The build version of the Ndes Connector.
        Returns: Optional[str]
        """
        return self._connector_version
    
    @connector_version.setter
    def connector_version(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorVersion property value. The build version of the Ndes Connector.
        Args:
            value: Value to set for the connector_version property.
        """
        self._connector_version = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NdesConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NdesConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NdesConnector()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The friendly name of the Ndes Connector.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The friendly name of the Ndes Connector.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def enrolled_date_time(self,) -> Optional[datetime]:
        """
        Gets the enrolledDateTime property value. Timestamp when on-prem certificate connector was enrolled in Intune.
        Returns: Optional[datetime]
        """
        return self._enrolled_date_time
    
    @enrolled_date_time.setter
    def enrolled_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the enrolledDateTime property value. Timestamp when on-prem certificate connector was enrolled in Intune.
        Args:
            value: Value to set for the enrolled_date_time property.
        """
        self._enrolled_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, ndes_connector_state

        fields: Dict[str, Callable[[Any], None]] = {
            "connectorVersion": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolledDateTime": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "lastConnectionDateTime": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ndes_connector_state.NdesConnectorState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_connection_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastConnectionDateTime property value. Last connection time for the Ndes Connector
        Returns: Optional[datetime]
        """
        return self._last_connection_date_time
    
    @last_connection_date_time.setter
    def last_connection_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastConnectionDateTime property value. Last connection time for the Ndes Connector
        Args:
            value: Value to set for the last_connection_date_time property.
        """
        self._last_connection_date_time = value
    
    @property
    def machine_name(self,) -> Optional[str]:
        """
        Gets the machineName property value. Name of the machine running on-prem certificate connector service.
        Returns: Optional[str]
        """
        return self._machine_name
    
    @machine_name.setter
    def machine_name(self,value: Optional[str] = None) -> None:
        """
        Sets the machineName property value. Name of the machine running on-prem certificate connector service.
        Args:
            value: Value to set for the machine_name property.
        """
        self._machine_name = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Entity instance.
        Args:
            value: Value to set for the role_scope_tag_ids property.
        """
        self._role_scope_tag_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("enrolledDateTime", self.enrolled_date_time)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[ndes_connector_state.NdesConnectorState]:
        """
        Gets the state property value. The current status of the Ndes Connector.
        Returns: Optional[ndes_connector_state.NdesConnectorState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[ndes_connector_state.NdesConnectorState] = None) -> None:
        """
        Sets the state property value. The current status of the Ndes Connector.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

