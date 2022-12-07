from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_external_partner_status = lazy_import('msgraph.generated.models.cloud_pc_external_partner_status')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcExternalPartnerSetting(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcExternalPartnerSetting and sets the default values.
        """
        super().__init__()
        # Enable or disable the connection to an external partner. If true, an external partner API will accept incoming calls from external partners. Required. Supports $filter (eq).
        self._enable_connection: Optional[bool] = None
        # Last data sync time for this external partner. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The external partner ID.
        self._partner_id: Optional[str] = None
        # The status property
        self._status: Optional[cloud_pc_external_partner_status.CloudPcExternalPartnerStatus] = None
        # Status details message.
        self._status_details: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcExternalPartnerSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcExternalPartnerSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcExternalPartnerSetting()
    
    @property
    def enable_connection(self,) -> Optional[bool]:
        """
        Gets the enableConnection property value. Enable or disable the connection to an external partner. If true, an external partner API will accept incoming calls from external partners. Required. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._enable_connection
    
    @enable_connection.setter
    def enable_connection(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableConnection property value. Enable or disable the connection to an external partner. If true, an external partner API will accept incoming calls from external partners. Required. Supports $filter (eq).
        Args:
            value: Value to set for the enableConnection property.
        """
        self._enable_connection = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enable_connection": lambda n : setattr(self, 'enable_connection', n.get_bool_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "partner_id": lambda n : setattr(self, 'partner_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_external_partner_status.CloudPcExternalPartnerStatus)),
            "status_details": lambda n : setattr(self, 'status_details', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Last data sync time for this external partner. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Last data sync time for this external partner. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def partner_id(self,) -> Optional[str]:
        """
        Gets the partnerId property value. The external partner ID.
        Returns: Optional[str]
        """
        return self._partner_id
    
    @partner_id.setter
    def partner_id(self,value: Optional[str] = None) -> None:
        """
        Sets the partnerId property value. The external partner ID.
        Args:
            value: Value to set for the partnerId property.
        """
        self._partner_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enableConnection", self.enable_connection)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("partnerId", self.partner_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusDetails", self.status_details)
    
    @property
    def status(self,) -> Optional[cloud_pc_external_partner_status.CloudPcExternalPartnerStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[cloud_pc_external_partner_status.CloudPcExternalPartnerStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[cloud_pc_external_partner_status.CloudPcExternalPartnerStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def status_details(self,) -> Optional[str]:
        """
        Gets the statusDetails property value. Status details message.
        Returns: Optional[str]
        """
        return self._status_details
    
    @status_details.setter
    def status_details(self,value: Optional[str] = None) -> None:
        """
        Sets the statusDetails property value. Status details message.
        Args:
            value: Value to set for the statusDetails property.
        """
        self._status_details = value
    

