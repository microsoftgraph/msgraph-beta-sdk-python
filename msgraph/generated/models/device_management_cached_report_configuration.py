from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_report_status = lazy_import('msgraph.generated.models.device_management_report_status')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementCachedReportConfiguration(entity.Entity):
    """
    Entity representing the configuration of a cached report
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementCachedReportConfiguration and sets the default values.
        """
        super().__init__()
        # Time that the cached report expires
        self._expiration_date_time: Optional[datetime] = None
        # Filters applied on report creation.
        self._filter: Optional[str] = None
        # Time that the cached report was last refreshed
        self._last_refresh_date_time: Optional[datetime] = None
        # Caller-managed metadata associated with the report
        self._metadata: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Ordering of columns in the report
        self._order_by: Optional[List[str]] = None
        # Name of the report
        self._report_name: Optional[str] = None
        # Columns selected from the report
        self._select: Optional[List[str]] = None
        # Possible statuses associated with a generated report
        self._status: Optional[device_management_report_status.DeviceManagementReportStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementCachedReportConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementCachedReportConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementCachedReportConfiguration()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Time that the cached report expires
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Time that the cached report expires
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    @property
    def filter(self,) -> Optional[str]:
        """
        Gets the filter property value. Filters applied on report creation.
        Returns: Optional[str]
        """
        return self._filter
    
    @filter.setter
    def filter(self,value: Optional[str] = None) -> None:
        """
        Sets the filter property value. Filters applied on report creation.
        Args:
            value: Value to set for the filter property.
        """
        self._filter = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "last_refresh_date_time": lambda n : setattr(self, 'last_refresh_date_time', n.get_datetime_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_str_value()),
            "order_by": lambda n : setattr(self, 'order_by', n.get_collection_of_primitive_values(str)),
            "report_name": lambda n : setattr(self, 'report_name', n.get_str_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_management_report_status.DeviceManagementReportStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_refresh_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshDateTime property value. Time that the cached report was last refreshed
        Returns: Optional[datetime]
        """
        return self._last_refresh_date_time
    
    @last_refresh_date_time.setter
    def last_refresh_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshDateTime property value. Time that the cached report was last refreshed
        Args:
            value: Value to set for the lastRefreshDateTime property.
        """
        self._last_refresh_date_time = value
    
    @property
    def metadata(self,) -> Optional[str]:
        """
        Gets the metadata property value. Caller-managed metadata associated with the report
        Returns: Optional[str]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[str] = None) -> None:
        """
        Sets the metadata property value. Caller-managed metadata associated with the report
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
    @property
    def order_by(self,) -> Optional[List[str]]:
        """
        Gets the orderBy property value. Ordering of columns in the report
        Returns: Optional[List[str]]
        """
        return self._order_by
    
    @order_by.setter
    def order_by(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the orderBy property value. Ordering of columns in the report
        Args:
            value: Value to set for the orderBy property.
        """
        self._order_by = value
    
    @property
    def report_name(self,) -> Optional[str]:
        """
        Gets the reportName property value. Name of the report
        Returns: Optional[str]
        """
        return self._report_name
    
    @report_name.setter
    def report_name(self,value: Optional[str] = None) -> None:
        """
        Sets the reportName property value. Name of the report
        Args:
            value: Value to set for the reportName property.
        """
        self._report_name = value
    
    @property
    def select(self,) -> Optional[List[str]]:
        """
        Gets the select property value. Columns selected from the report
        Returns: Optional[List[str]]
        """
        return self._select
    
    @select.setter
    def select(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the select property value. Columns selected from the report
        Args:
            value: Value to set for the select property.
        """
        self._select = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("filter", self.filter)
        writer.write_datetime_value("lastRefreshDateTime", self.last_refresh_date_time)
        writer.write_str_value("metadata", self.metadata)
        writer.write_collection_of_primitive_values("orderBy", self.order_by)
        writer.write_str_value("reportName", self.report_name)
        writer.write_collection_of_primitive_values("select", self.select)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[device_management_report_status.DeviceManagementReportStatus]:
        """
        Gets the status property value. Possible statuses associated with a generated report
        Returns: Optional[device_management_report_status.DeviceManagementReportStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[device_management_report_status.DeviceManagementReportStatus] = None) -> None:
        """
        Sets the status property value. Possible statuses associated with a generated report
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

