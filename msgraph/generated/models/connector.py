from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

connector_group = lazy_import('msgraph.generated.models.connector_group')
connector_status = lazy_import('msgraph.generated.models.connector_status')
entity = lazy_import('msgraph.generated.models.entity')

class Connector(entity.Entity):
    """
    Casts the previous resource to application.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new connector and sets the default values.
        """
        super().__init__()
        # The external IP address as detected by the the connector server. Read-only.
        self._external_ip: Optional[str] = None
        # The machine name the connector is installed and running on.
        self._machine_name: Optional[str] = None
        # The connectorGroup that the connector is a member of. Read-only.
        self._member_of: Optional[List[connector_group.ConnectorGroup]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[connector_status.ConnectorStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Connector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Connector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Connector()
    
    @property
    def external_ip(self,) -> Optional[str]:
        """
        Gets the externalIp property value. The external IP address as detected by the the connector server. Read-only.
        Returns: Optional[str]
        """
        return self._external_ip
    
    @external_ip.setter
    def external_ip(self,value: Optional[str] = None) -> None:
        """
        Sets the externalIp property value. The external IP address as detected by the the connector server. Read-only.
        Args:
            value: Value to set for the externalIp property.
        """
        self._external_ip = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "external_ip": lambda n : setattr(self, 'external_ip', n.get_str_value()),
            "machine_name": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "member_of": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(connector_group.ConnectorGroup)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(connector_status.ConnectorStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def machine_name(self,) -> Optional[str]:
        """
        Gets the machineName property value. The machine name the connector is installed and running on.
        Returns: Optional[str]
        """
        return self._machine_name
    
    @machine_name.setter
    def machine_name(self,value: Optional[str] = None) -> None:
        """
        Sets the machineName property value. The machine name the connector is installed and running on.
        Args:
            value: Value to set for the machineName property.
        """
        self._machine_name = value
    
    @property
    def member_of(self,) -> Optional[List[connector_group.ConnectorGroup]]:
        """
        Gets the memberOf property value. The connectorGroup that the connector is a member of. Read-only.
        Returns: Optional[List[connector_group.ConnectorGroup]]
        """
        return self._member_of
    
    @member_of.setter
    def member_of(self,value: Optional[List[connector_group.ConnectorGroup]] = None) -> None:
        """
        Sets the memberOf property value. The connectorGroup that the connector is a member of. Read-only.
        Args:
            value: Value to set for the memberOf property.
        """
        self._member_of = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("externalIp", self.external_ip)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[connector_status.ConnectorStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[connector_status.ConnectorStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[connector_status.ConnectorStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

