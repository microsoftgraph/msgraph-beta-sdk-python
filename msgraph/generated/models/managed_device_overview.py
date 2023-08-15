from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_exchange_access_state_summary import DeviceExchangeAccessStateSummary
    from .device_operating_system_summary import DeviceOperatingSystemSummary
    from .entity import Entity
    from .managed_device_models_and_manufacturers import ManagedDeviceModelsAndManufacturers

from .entity import Entity

@dataclass
class ManagedDeviceOverview(Entity):
    """
    Summary data for managed devices
    """
    # Distribution of Exchange Access State in Intune
    device_exchange_access_state_summary: Optional[DeviceExchangeAccessStateSummary] = None
    # Device operating system summary.
    device_operating_system_summary: Optional[DeviceOperatingSystemSummary] = None
    # The number of devices enrolled in both MDM and EAS
    dual_enrolled_device_count: Optional[int] = None
    # Total enrolled device count. Does not include PC devices managed via Intune PC Agent
    enrolled_device_count: Optional[int] = None
    # Last modified date time of device overview
    last_modified_date_time: Optional[datetime.datetime] = None
    # Models and Manufactures meatadata for managed devices in the account
    managed_device_models_and_manufacturers: Optional[ManagedDeviceModelsAndManufacturers] = None
    # The number of devices enrolled in MDM
    mdm_enrolled_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceOverview
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_exchange_access_state_summary import DeviceExchangeAccessStateSummary
        from .device_operating_system_summary import DeviceOperatingSystemSummary
        from .entity import Entity
        from .managed_device_models_and_manufacturers import ManagedDeviceModelsAndManufacturers

        from .device_exchange_access_state_summary import DeviceExchangeAccessStateSummary
        from .device_operating_system_summary import DeviceOperatingSystemSummary
        from .entity import Entity
        from .managed_device_models_and_manufacturers import ManagedDeviceModelsAndManufacturers

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceExchangeAccessStateSummary": lambda n : setattr(self, 'device_exchange_access_state_summary', n.get_object_value(DeviceExchangeAccessStateSummary)),
            "deviceOperatingSystemSummary": lambda n : setattr(self, 'device_operating_system_summary', n.get_object_value(DeviceOperatingSystemSummary)),
            "dualEnrolledDeviceCount": lambda n : setattr(self, 'dual_enrolled_device_count', n.get_int_value()),
            "enrolledDeviceCount": lambda n : setattr(self, 'enrolled_device_count', n.get_int_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managedDeviceModelsAndManufacturers": lambda n : setattr(self, 'managed_device_models_and_manufacturers', n.get_object_value(ManagedDeviceModelsAndManufacturers)),
            "mdmEnrolledCount": lambda n : setattr(self, 'mdm_enrolled_count', n.get_int_value()),
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
        writer.write_object_value("deviceExchangeAccessStateSummary", self.device_exchange_access_state_summary)
        writer.write_object_value("deviceOperatingSystemSummary", self.device_operating_system_summary)
        writer.write_int_value("dualEnrolledDeviceCount", self.dual_enrolled_device_count)
        writer.write_int_value("enrolledDeviceCount", self.enrolled_device_count)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("managedDeviceModelsAndManufacturers", self.managed_device_models_and_manufacturers)
        writer.write_int_value("mdmEnrolledCount", self.mdm_enrolled_count)
    

