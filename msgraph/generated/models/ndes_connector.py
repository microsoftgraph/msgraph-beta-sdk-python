from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
ndes_connector_state = lazy_import('msgraph.generated.models.ndes_connector_state')

class NdesConnector(entity.Entity):
    """
    Entity which represents an OnPrem Ndes connector.
    """
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
            value: Value to set for the connectorVersion property.
        """
        self._connector_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ndesConnector and sets the default values.
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
            value: Value to set for the displayName property.
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
            value: Value to set for the enrolledDateTime property.
        """
        self._enrolled_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connector_version": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolled_date_time": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "last_connection_date_time": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "machine_name": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the lastConnectionDateTime property.
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
            value: Value to set for the machineName property.
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
            value: Value to set for the roleScopeTagIds property.
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
    

