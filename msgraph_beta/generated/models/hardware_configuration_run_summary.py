from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class HardwareConfigurationRunSummary(Entity):
    """
    Contains properties for the run summary of a hardware configuration script.
    """
    # Number of devices for which hardware configuration state is error
    error_device_count: Optional[int] = None
    # Number of users for which hardware configuration state is error
    error_user_count: Optional[int] = None
    # Number of devices for which hardware configuration found an issue
    failed_device_count: Optional[int] = None
    # Number of users for which hardware configuration found an issue
    failed_user_count: Optional[int] = None
    # Last run time for the configuration across all devices
    last_run_date_time: Optional[datetime.datetime] = None
    # Number of devices for which hardware configuration state is not applicable
    not_applicable_device_count: Optional[int] = None
    # Number of users for which hardware configuration state is not applicable
    not_applicable_user_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of devices for which hardware configuration is in pending state
    pending_device_count: Optional[int] = None
    # Number of users for which hardware configuration is in pending state
    pending_user_count: Optional[int] = None
    # Number of devices for which hardware configured without any issue
    successful_device_count: Optional[int] = None
    # Number of users for which hardware configured without any issue
    successful_user_count: Optional[int] = None
    # Number of devices for which hardware configuration state is unknown
    unknown_device_count: Optional[int] = None
    # Number of users for which hardware configuration state is unknown
    unknown_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HardwareConfigurationRunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareConfigurationRunSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HardwareConfigurationRunSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "errorUserCount": lambda n : setattr(self, 'error_user_count', n.get_int_value()),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "failedUserCount": lambda n : setattr(self, 'failed_user_count', n.get_int_value()),
            "lastRunDateTime": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "notApplicableDeviceCount": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "notApplicableUserCount": lambda n : setattr(self, 'not_applicable_user_count', n.get_int_value()),
            "pendingDeviceCount": lambda n : setattr(self, 'pending_device_count', n.get_int_value()),
            "pendingUserCount": lambda n : setattr(self, 'pending_user_count', n.get_int_value()),
            "successfulDeviceCount": lambda n : setattr(self, 'successful_device_count', n.get_int_value()),
            "successfulUserCount": lambda n : setattr(self, 'successful_user_count', n.get_int_value()),
            "unknownDeviceCount": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
            "unknownUserCount": lambda n : setattr(self, 'unknown_user_count', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("errorUserCount", self.error_user_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("failedUserCount", self.failed_user_count)
        writer.write_datetime_value("lastRunDateTime", self.last_run_date_time)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("notApplicableUserCount", self.not_applicable_user_count)
        writer.write_int_value("pendingDeviceCount", self.pending_device_count)
        writer.write_int_value("pendingUserCount", self.pending_user_count)
        writer.write_int_value("successfulDeviceCount", self.successful_device_count)
        writer.write_int_value("successfulUserCount", self.successful_user_count)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
        writer.write_int_value("unknownUserCount", self.unknown_user_count)
    

