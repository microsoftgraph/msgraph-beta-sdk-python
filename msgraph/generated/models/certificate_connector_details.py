from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CertificateConnectorDetails(entity.Entity):
    """
    Entity used to retrieve information about Intune Certificate Connectors.
    """
    @property
    def connector_name(self,) -> Optional[str]:
        """
        Gets the connectorName property value. Connector name (set during enrollment).
        Returns: Optional[str]
        """
        return self._connector_name
    
    @connector_name.setter
    def connector_name(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorName property value. Connector name (set during enrollment).
        Args:
            value: Value to set for the connectorName property.
        """
        self._connector_name = value
    
    @property
    def connector_version(self,) -> Optional[str]:
        """
        Gets the connectorVersion property value. Version of the connector installed.
        Returns: Optional[str]
        """
        return self._connector_version
    
    @connector_version.setter
    def connector_version(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorVersion property value. Version of the connector installed.
        Args:
            value: Value to set for the connectorVersion property.
        """
        self._connector_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new certificateConnectorDetails and sets the default values.
        """
        super().__init__()
        # Connector name (set during enrollment).
        self._connector_name: Optional[str] = None
        # Version of the connector installed.
        self._connector_version: Optional[str] = None
        # Date/time when this connector was enrolled.
        self._enrollment_date_time: Optional[datetime] = None
        # Date/time when this connector last connected to the service.
        self._last_checkin_date_time: Optional[datetime] = None
        # Name of the machine hosting this connector service.
        self._machine_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CertificateConnectorDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CertificateConnectorDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CertificateConnectorDetails()
    
    @property
    def enrollment_date_time(self,) -> Optional[datetime]:
        """
        Gets the enrollmentDateTime property value. Date/time when this connector was enrolled.
        Returns: Optional[datetime]
        """
        return self._enrollment_date_time
    
    @enrollment_date_time.setter
    def enrollment_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the enrollmentDateTime property value. Date/time when this connector was enrolled.
        Args:
            value: Value to set for the enrollmentDateTime property.
        """
        self._enrollment_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connector_name": lambda n : setattr(self, 'connector_name', n.get_str_value()),
            "connector_version": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "enrollment_date_time": lambda n : setattr(self, 'enrollment_date_time', n.get_datetime_value()),
            "last_checkin_date_time": lambda n : setattr(self, 'last_checkin_date_time', n.get_datetime_value()),
            "machine_name": lambda n : setattr(self, 'machine_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_checkin_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckinDateTime property value. Date/time when this connector last connected to the service.
        Returns: Optional[datetime]
        """
        return self._last_checkin_date_time
    
    @last_checkin_date_time.setter
    def last_checkin_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckinDateTime property value. Date/time when this connector last connected to the service.
        Args:
            value: Value to set for the lastCheckinDateTime property.
        """
        self._last_checkin_date_time = value
    
    @property
    def machine_name(self,) -> Optional[str]:
        """
        Gets the machineName property value. Name of the machine hosting this connector service.
        Returns: Optional[str]
        """
        return self._machine_name
    
    @machine_name.setter
    def machine_name(self,value: Optional[str] = None) -> None:
        """
        Sets the machineName property value. Name of the machine hosting this connector service.
        Args:
            value: Value to set for the machineName property.
        """
        self._machine_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("connectorName", self.connector_name)
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_datetime_value("enrollmentDateTime", self.enrollment_date_time)
        writer.write_datetime_value("lastCheckinDateTime", self.last_checkin_date_time)
        writer.write_str_value("machineName", self.machine_name)
    

