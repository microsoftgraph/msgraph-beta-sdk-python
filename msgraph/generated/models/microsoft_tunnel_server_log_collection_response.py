from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
microsoft_tunnel_log_collection_status = lazy_import('msgraph.generated.models.microsoft_tunnel_log_collection_status')

class MicrosoftTunnelServerLogCollectionResponse(entity.Entity):
    """
    Entity that stores the server log collection status.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftTunnelServerLogCollectionResponse and sets the default values.
        """
        super().__init__()
        # The end time of the logs collected
        self._end_date_time: Optional[datetime] = None
        # The time when the log collection is expired
        self._expiry_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The time when the log collection was requested
        self._request_date_time: Optional[datetime] = None
        # ID of the server the log collection is requested upon
        self._server_id: Optional[str] = None
        # The size of the logs in bytes
        self._size_in_bytes: Optional[int] = None
        # The start time of the logs collected
        self._start_date_time: Optional[datetime] = None
        # Enum type that represent the status of log collection
        self._status: Optional[microsoft_tunnel_log_collection_status.MicrosoftTunnelLogCollectionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftTunnelServerLogCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelServerLogCollectionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftTunnelServerLogCollectionResponse()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The end time of the logs collected
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The end time of the logs collected
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    @property
    def expiry_date_time(self,) -> Optional[datetime]:
        """
        Gets the expiryDateTime property value. The time when the log collection is expired
        Returns: Optional[datetime]
        """
        return self._expiry_date_time
    
    @expiry_date_time.setter
    def expiry_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expiryDateTime property value. The time when the log collection is expired
        Args:
            value: Value to set for the expiryDateTime property.
        """
        self._expiry_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "expiry_date_time": lambda n : setattr(self, 'expiry_date_time', n.get_datetime_value()),
            "request_date_time": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "server_id": lambda n : setattr(self, 'server_id', n.get_str_value()),
            "size_in_bytes": lambda n : setattr(self, 'size_in_bytes', n.get_int_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(microsoft_tunnel_log_collection_status.MicrosoftTunnelLogCollectionStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def request_date_time(self,) -> Optional[datetime]:
        """
        Gets the requestDateTime property value. The time when the log collection was requested
        Returns: Optional[datetime]
        """
        return self._request_date_time
    
    @request_date_time.setter
    def request_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestDateTime property value. The time when the log collection was requested
        Args:
            value: Value to set for the requestDateTime property.
        """
        self._request_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("expiryDateTime", self.expiry_date_time)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_str_value("serverId", self.server_id)
        writer.write_int_value("sizeInBytes", self.size_in_bytes)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def server_id(self,) -> Optional[str]:
        """
        Gets the serverId property value. ID of the server the log collection is requested upon
        Returns: Optional[str]
        """
        return self._server_id
    
    @server_id.setter
    def server_id(self,value: Optional[str] = None) -> None:
        """
        Sets the serverId property value. ID of the server the log collection is requested upon
        Args:
            value: Value to set for the serverId property.
        """
        self._server_id = value
    
    @property
    def size_in_bytes(self,) -> Optional[int]:
        """
        Gets the sizeInBytes property value. The size of the logs in bytes
        Returns: Optional[int]
        """
        return self._size_in_bytes
    
    @size_in_bytes.setter
    def size_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the sizeInBytes property value. The size of the logs in bytes
        Args:
            value: Value to set for the sizeInBytes property.
        """
        self._size_in_bytes = value
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The start time of the logs collected
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The start time of the logs collected
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[microsoft_tunnel_log_collection_status.MicrosoftTunnelLogCollectionStatus]:
        """
        Gets the status property value. Enum type that represent the status of log collection
        Returns: Optional[microsoft_tunnel_log_collection_status.MicrosoftTunnelLogCollectionStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[microsoft_tunnel_log_collection_status.MicrosoftTunnelLogCollectionStatus] = None) -> None:
        """
        Sets the status property value. Enum type that represent the status of log collection
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

