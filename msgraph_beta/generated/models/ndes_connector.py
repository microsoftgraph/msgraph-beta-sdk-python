from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .ndes_connector_state import NdesConnectorState

from .entity import Entity

@dataclass
class NdesConnector(Entity):
    """
    Entity which represents an OnPrem Ndes connector.
    """
    # The build version of the Ndes Connector.
    connector_version: Optional[str] = None
    # The friendly name of the Ndes Connector.
    display_name: Optional[str] = None
    # Timestamp when on-prem certificate connector was enrolled in Intune.
    enrolled_date_time: Optional[datetime.datetime] = None
    # Last connection time for the Ndes Connector
    last_connection_date_time: Optional[datetime.datetime] = None
    # Name of the machine running on-prem certificate connector service.
    machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # The current status of the Ndes Connector.
    state: Optional[NdesConnectorState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NdesConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NdesConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NdesConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .ndes_connector_state import NdesConnectorState

        from .entity import Entity
        from .ndes_connector_state import NdesConnectorState

        fields: Dict[str, Callable[[Any], None]] = {
            "connectorVersion": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolledDateTime": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "lastConnectionDateTime": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(NdesConnectorState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("enrolledDateTime", self.enrolled_date_time)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_enum_value("state", self.state)
    

