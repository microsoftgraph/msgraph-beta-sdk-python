from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
windows_autopilot_sync_status = lazy_import('msgraph.generated.models.windows_autopilot_sync_status')

class WindowsAutopilotSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new windowsAutopilotSettings and sets the default values.
        """
        super().__init__()
        # Last data sync date time with DDS service.
        self._last_manual_sync_trigger_date_time: Optional[datetime] = None
        # Last data sync date time with DDS service.
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The syncStatus property
        self._sync_status: Optional[windows_autopilot_sync_status.WindowsAutopilotSyncStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsAutopilotSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsAutopilotSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_manual_sync_trigger_date_time": lambda n : setattr(self, 'last_manual_sync_trigger_date_time', n.get_datetime_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "sync_status": lambda n : setattr(self, 'sync_status', n.get_enum_value(windows_autopilot_sync_status.WindowsAutopilotSyncStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_manual_sync_trigger_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastManualSyncTriggerDateTime property value. Last data sync date time with DDS service.
        Returns: Optional[datetime]
        """
        return self._last_manual_sync_trigger_date_time
    
    @last_manual_sync_trigger_date_time.setter
    def last_manual_sync_trigger_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastManualSyncTriggerDateTime property value. Last data sync date time with DDS service.
        Args:
            value: Value to set for the lastManualSyncTriggerDateTime property.
        """
        self._last_manual_sync_trigger_date_time = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Last data sync date time with DDS service.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Last data sync date time with DDS service.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastManualSyncTriggerDateTime", self.last_manual_sync_trigger_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_enum_value("syncStatus", self.sync_status)
    
    @property
    def sync_status(self,) -> Optional[windows_autopilot_sync_status.WindowsAutopilotSyncStatus]:
        """
        Gets the syncStatus property value. The syncStatus property
        Returns: Optional[windows_autopilot_sync_status.WindowsAutopilotSyncStatus]
        """
        return self._sync_status
    
    @sync_status.setter
    def sync_status(self,value: Optional[windows_autopilot_sync_status.WindowsAutopilotSyncStatus] = None) -> None:
        """
        Sets the syncStatus property value. The syncStatus property
        Args:
            value: Value to set for the syncStatus property.
        """
        self._sync_status = value
    

