from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_domain_join_connector_state = lazy_import('msgraph.generated.models.device_management_domain_join_connector_state')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementDomainJoinConnector(entity.Entity):
    """
    A Domain Join Connector is a connector that is responsible to allocate (and delete) machine account blobs
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementDomainJoinConnector and sets the default values.
        """
        super().__init__()
        # The connector display name.
        self._display_name: Optional[str] = None
        # Last time connector contacted Intune.
        self._last_connection_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ODJ request states.
        self._state: Optional[device_management_domain_join_connector_state.DeviceManagementDomainJoinConnectorState] = None
        # The version of the connector.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementDomainJoinConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementDomainJoinConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementDomainJoinConnector()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The connector display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The connector display name.
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
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_connection_date_time": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(device_management_domain_join_connector_state.DeviceManagementDomainJoinConnectorState)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_connection_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastConnectionDateTime property value. Last time connector contacted Intune.
        Returns: Optional[datetime]
        """
        return self._last_connection_date_time
    
    @last_connection_date_time.setter
    def last_connection_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastConnectionDateTime property value. Last time connector contacted Intune.
        Args:
            value: Value to set for the lastConnectionDateTime property.
        """
        self._last_connection_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("version", self.version)
    
    @property
    def state(self,) -> Optional[device_management_domain_join_connector_state.DeviceManagementDomainJoinConnectorState]:
        """
        Gets the state property value. The ODJ request states.
        Returns: Optional[device_management_domain_join_connector_state.DeviceManagementDomainJoinConnectorState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[device_management_domain_join_connector_state.DeviceManagementDomainJoinConnectorState] = None) -> None:
        """
        Sets the state property value. The ODJ request states.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version of the connector.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version of the connector.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

