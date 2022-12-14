from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DeviceLogCollectionResponse(entity.Entity):
    """
    Windows Log Collection request entity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceLogCollectionResponse and sets the default values.
        """
        super().__init__()
        # The User Principal Name (UPN) of the user that enrolled the device
        self._enrolled_by_user: Optional[str] = None
        # The error code, if any. Valid values -9.22337203685478E+18 to 9.22337203685478E+18
        self._error_code: Optional[int] = None
        # The DateTime of the expiration of the logs
        self._expiration_date_time_u_t_c: Optional[datetime] = None
        # The UPN for who initiated the request
        self._initiated_by_user_principal_name: Optional[str] = None
        # The device Id
        self._managed_device_id: Optional[Guid] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The DateTime the request was received
        self._received_date_time_u_t_c: Optional[datetime] = None
        # The DateTime of the request
        self._requested_date_time_u_t_c: Optional[datetime] = None
        # The size of the logs. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._size: Optional[float] = None
        # The status of the log collection request
        self._status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceLogCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLogCollectionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceLogCollectionResponse()
    
    @property
    def enrolled_by_user(self,) -> Optional[str]:
        """
        Gets the enrolledByUser property value. The User Principal Name (UPN) of the user that enrolled the device
        Returns: Optional[str]
        """
        return self._enrolled_by_user
    
    @enrolled_by_user.setter
    def enrolled_by_user(self,value: Optional[str] = None) -> None:
        """
        Sets the enrolledByUser property value. The User Principal Name (UPN) of the user that enrolled the device
        Args:
            value: Value to set for the enrolledByUser property.
        """
        self._enrolled_by_user = value
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. The error code, if any. Valid values -9.22337203685478E+18 to 9.22337203685478E+18
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. The error code, if any. Valid values -9.22337203685478E+18 to 9.22337203685478E+18
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    @property
    def expiration_date_time_u_t_c(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTimeUTC property value. The DateTime of the expiration of the logs
        Returns: Optional[datetime]
        """
        return self._expiration_date_time_u_t_c
    
    @expiration_date_time_u_t_c.setter
    def expiration_date_time_u_t_c(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTimeUTC property value. The DateTime of the expiration of the logs
        Args:
            value: Value to set for the expirationDateTimeUTC property.
        """
        self._expiration_date_time_u_t_c = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enrolled_by_user": lambda n : setattr(self, 'enrolled_by_user', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "expiration_date_time_u_t_c": lambda n : setattr(self, 'expiration_date_time_u_t_c', n.get_datetime_value()),
            "initiated_by_user_principal_name": lambda n : setattr(self, 'initiated_by_user_principal_name', n.get_str_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_object_value(Guid)),
            "received_date_time_u_t_c": lambda n : setattr(self, 'received_date_time_u_t_c', n.get_datetime_value()),
            "requested_date_time_u_t_c": lambda n : setattr(self, 'requested_date_time_u_t_c', n.get_datetime_value()),
            "size": lambda n : setattr(self, 'size', n.get_float_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiated_by_user_principal_name(self,) -> Optional[str]:
        """
        Gets the initiatedByUserPrincipalName property value. The UPN for who initiated the request
        Returns: Optional[str]
        """
        return self._initiated_by_user_principal_name
    
    @initiated_by_user_principal_name.setter
    def initiated_by_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the initiatedByUserPrincipalName property value. The UPN for who initiated the request
        Args:
            value: Value to set for the initiatedByUserPrincipalName property.
        """
        self._initiated_by_user_principal_name = value
    
    @property
    def managed_device_id(self,) -> Optional[Guid]:
        """
        Gets the managedDeviceId property value. The device Id
        Returns: Optional[Guid]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the managedDeviceId property value. The device Id
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def received_date_time_u_t_c(self,) -> Optional[datetime]:
        """
        Gets the receivedDateTimeUTC property value. The DateTime the request was received
        Returns: Optional[datetime]
        """
        return self._received_date_time_u_t_c
    
    @received_date_time_u_t_c.setter
    def received_date_time_u_t_c(self,value: Optional[datetime] = None) -> None:
        """
        Sets the receivedDateTimeUTC property value. The DateTime the request was received
        Args:
            value: Value to set for the receivedDateTimeUTC property.
        """
        self._received_date_time_u_t_c = value
    
    @property
    def requested_date_time_u_t_c(self,) -> Optional[datetime]:
        """
        Gets the requestedDateTimeUTC property value. The DateTime of the request
        Returns: Optional[datetime]
        """
        return self._requested_date_time_u_t_c
    
    @requested_date_time_u_t_c.setter
    def requested_date_time_u_t_c(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestedDateTimeUTC property value. The DateTime of the request
        Args:
            value: Value to set for the requestedDateTimeUTC property.
        """
        self._requested_date_time_u_t_c = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("enrolledByUser", self.enrolled_by_user)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_datetime_value("expirationDateTimeUTC", self.expiration_date_time_u_t_c)
        writer.write_str_value("initiatedByUserPrincipalName", self.initiated_by_user_principal_name)
        writer.write_object_value("managedDeviceId", self.managed_device_id)
        writer.write_datetime_value("receivedDateTimeUTC", self.received_date_time_u_t_c)
        writer.write_datetime_value("requestedDateTimeUTC", self.requested_date_time_u_t_c)
        writer.write_float_value("size", self.size)
        writer.write_str_value("status", self.status)
    
    @property
    def size(self,) -> Optional[float]:
        """
        Gets the size property value. The size of the logs. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[float] = None) -> None:
        """
        Sets the size property value. The size of the logs. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status of the log collection request
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status of the log collection request
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

