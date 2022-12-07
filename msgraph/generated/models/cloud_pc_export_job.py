from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_export_job_status = lazy_import('msgraph.generated.models.cloud_pc_export_job_status')
cloud_pc_report_name = lazy_import('msgraph.generated.models.cloud_pc_report_name')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcExportJob(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcExportJob and sets the default values.
        """
        super().__init__()
        # The date time when the export job expires.
        self._expiration_date_time: Optional[datetime] = None
        # The status of the export job.The possible values are: notStarted, inProgress, completed, unknownFutureValue. Read-only.
        self._export_job_status: Optional[cloud_pc_export_job_status.CloudPcExportJobStatus] = None
        # The storage account url of the exported report, it can be used to download the file.
        self._export_url: Optional[str] = None
        # The filter applied on the report.
        self._filter: Optional[str] = None
        # The format of the exported report.
        self._format: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The report name.The possible values are: remoteConnectionHistoricalReports, dailyAggregatedRemoteConnectionReports, totalAggregatedRemoteConnectionReports, unknownFutureValue.
        self._report_name: Optional[cloud_pc_report_name.CloudPcReportName] = None
        # The date time when the export job was requested.
        self._request_date_time: Optional[datetime] = None
        # The selected columns of the report.
        self._select: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcExportJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcExportJob
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcExportJob()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The date time when the export job expires.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The date time when the export job expires.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    @property
    def export_job_status(self,) -> Optional[cloud_pc_export_job_status.CloudPcExportJobStatus]:
        """
        Gets the exportJobStatus property value. The status of the export job.The possible values are: notStarted, inProgress, completed, unknownFutureValue. Read-only.
        Returns: Optional[cloud_pc_export_job_status.CloudPcExportJobStatus]
        """
        return self._export_job_status
    
    @export_job_status.setter
    def export_job_status(self,value: Optional[cloud_pc_export_job_status.CloudPcExportJobStatus] = None) -> None:
        """
        Sets the exportJobStatus property value. The status of the export job.The possible values are: notStarted, inProgress, completed, unknownFutureValue. Read-only.
        Args:
            value: Value to set for the exportJobStatus property.
        """
        self._export_job_status = value
    
    @property
    def export_url(self,) -> Optional[str]:
        """
        Gets the exportUrl property value. The storage account url of the exported report, it can be used to download the file.
        Returns: Optional[str]
        """
        return self._export_url
    
    @export_url.setter
    def export_url(self,value: Optional[str] = None) -> None:
        """
        Sets the exportUrl property value. The storage account url of the exported report, it can be used to download the file.
        Args:
            value: Value to set for the exportUrl property.
        """
        self._export_url = value
    
    @property
    def filter(self,) -> Optional[str]:
        """
        Gets the filter property value. The filter applied on the report.
        Returns: Optional[str]
        """
        return self._filter
    
    @filter.setter
    def filter(self,value: Optional[str] = None) -> None:
        """
        Sets the filter property value. The filter applied on the report.
        Args:
            value: Value to set for the filter property.
        """
        self._filter = value
    
    @property
    def format(self,) -> Optional[str]:
        """
        Gets the format property value. The format of the exported report.
        Returns: Optional[str]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[str] = None) -> None:
        """
        Sets the format property value. The format of the exported report.
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "export_job_status": lambda n : setattr(self, 'export_job_status', n.get_enum_value(cloud_pc_export_job_status.CloudPcExportJobStatus)),
            "export_url": lambda n : setattr(self, 'export_url', n.get_str_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "report_name": lambda n : setattr(self, 'report_name', n.get_enum_value(cloud_pc_report_name.CloudPcReportName)),
            "request_date_time": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def report_name(self,) -> Optional[cloud_pc_report_name.CloudPcReportName]:
        """
        Gets the reportName property value. The report name.The possible values are: remoteConnectionHistoricalReports, dailyAggregatedRemoteConnectionReports, totalAggregatedRemoteConnectionReports, unknownFutureValue.
        Returns: Optional[cloud_pc_report_name.CloudPcReportName]
        """
        return self._report_name
    
    @report_name.setter
    def report_name(self,value: Optional[cloud_pc_report_name.CloudPcReportName] = None) -> None:
        """
        Sets the reportName property value. The report name.The possible values are: remoteConnectionHistoricalReports, dailyAggregatedRemoteConnectionReports, totalAggregatedRemoteConnectionReports, unknownFutureValue.
        Args:
            value: Value to set for the reportName property.
        """
        self._report_name = value
    
    @property
    def request_date_time(self,) -> Optional[datetime]:
        """
        Gets the requestDateTime property value. The date time when the export job was requested.
        Returns: Optional[datetime]
        """
        return self._request_date_time
    
    @request_date_time.setter
    def request_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestDateTime property value. The date time when the export job was requested.
        Args:
            value: Value to set for the requestDateTime property.
        """
        self._request_date_time = value
    
    @property
    def select(self,) -> Optional[List[str]]:
        """
        Gets the select property value. The selected columns of the report.
        Returns: Optional[List[str]]
        """
        return self._select
    
    @select.setter
    def select(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the select property value. The selected columns of the report.
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
        writer.write_enum_value("exportJobStatus", self.export_job_status)
        writer.write_str_value("exportUrl", self.export_url)
        writer.write_str_value("filter", self.filter)
        writer.write_str_value("format", self.format)
        writer.write_enum_value("reportName", self.report_name)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_collection_of_primitive_values("select", self.select)
    

