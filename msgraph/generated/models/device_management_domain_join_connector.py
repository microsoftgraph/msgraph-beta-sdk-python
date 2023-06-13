from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_domain_join_connector_state, entity

from . import entity

@dataclass
class DeviceManagementDomainJoinConnector(entity.Entity):
    """
    A Domain Join Connector is a connector that is responsible to allocate (and delete) machine account blobs
    """
    # The connector display name.
    display_name: Optional[str] = None
    # Last time connector contacted Intune.
    last_connection_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ODJ request states.
    state: Optional[device_management_domain_join_connector_state.DeviceManagementDomainJoinConnectorState] = None
    # The version of the connector.
    version: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_domain_join_connector_state, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastConnectionDateTime": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(device_management_domain_join_connector_state.DeviceManagementDomainJoinConnectorState)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("version", self.version)
    

