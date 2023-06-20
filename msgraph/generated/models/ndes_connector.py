from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, ndes_connector_state

from . import entity

@dataclass
class NdesConnector(entity.Entity):
    """
    Entity which represents an OnPrem Ndes connector.
    """
    # The build version of the Ndes Connector.
    connector_version: Optional[str] = None
    # The friendly name of the Ndes Connector.
    display_name: Optional[str] = None
    # Timestamp when on-prem certificate connector was enrolled in Intune.
    enrolled_date_time: Optional[datetime] = None
    # Last connection time for the Ndes Connector
    last_connection_date_time: Optional[datetime] = None
    # Name of the machine running on-prem certificate connector service.
    machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # The current status of the Ndes Connector.
    state: Optional[ndes_connector_state.NdesConnectorState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NdesConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NdesConnector
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NdesConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, ndes_connector_state

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("enrolledDateTime", self.enrolled_date_time)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_enum_value("state", self.state)
    

