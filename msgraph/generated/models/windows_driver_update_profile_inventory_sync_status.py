from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_driver_update_profile_inventory_sync_state = lazy_import('msgraph.generated.models.windows_driver_update_profile_inventory_sync_state')

class WindowsDriverUpdateProfileInventorySyncStatus(AdditionalDataHolder, Parsable):
    """
    A complex type to store the status of a driver and firmware profile inventory sync. The status includes the last successful sync date time and the state of the last sync.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsDriverUpdateProfileInventorySyncStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Windows DnF update inventory sync state.
        self._driver_inventory_sync_state: Optional[windows_driver_update_profile_inventory_sync_state.WindowsDriverUpdateProfileInventorySyncState] = None
        # The last successful sync date and time in UTC.
        self._last_successful_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDriverUpdateProfileInventorySyncStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDriverUpdateProfileInventorySyncStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDriverUpdateProfileInventorySyncStatus()
    
    @property
    def driver_inventory_sync_state(self,) -> Optional[windows_driver_update_profile_inventory_sync_state.WindowsDriverUpdateProfileInventorySyncState]:
        """
        Gets the driverInventorySyncState property value. Windows DnF update inventory sync state.
        Returns: Optional[windows_driver_update_profile_inventory_sync_state.WindowsDriverUpdateProfileInventorySyncState]
        """
        return self._driver_inventory_sync_state
    
    @driver_inventory_sync_state.setter
    def driver_inventory_sync_state(self,value: Optional[windows_driver_update_profile_inventory_sync_state.WindowsDriverUpdateProfileInventorySyncState] = None) -> None:
        """
        Sets the driverInventorySyncState property value. Windows DnF update inventory sync state.
        Args:
            value: Value to set for the driverInventorySyncState property.
        """
        self._driver_inventory_sync_state = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "driver_inventory_sync_state": lambda n : setattr(self, 'driver_inventory_sync_state', n.get_enum_value(windows_driver_update_profile_inventory_sync_state.WindowsDriverUpdateProfileInventorySyncState)),
            "last_successful_sync_date_time": lambda n : setattr(self, 'last_successful_sync_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def last_successful_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSuccessfulSyncDateTime property value. The last successful sync date and time in UTC.
        Returns: Optional[datetime]
        """
        return self._last_successful_sync_date_time
    
    @last_successful_sync_date_time.setter
    def last_successful_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSuccessfulSyncDateTime property value. The last successful sync date and time in UTC.
        Args:
            value: Value to set for the lastSuccessfulSyncDateTime property.
        """
        self._last_successful_sync_date_time = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("driverInventorySyncState", self.driver_inventory_sync_state)
        writer.write_datetime_value("lastSuccessfulSyncDateTime", self.last_successful_sync_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

