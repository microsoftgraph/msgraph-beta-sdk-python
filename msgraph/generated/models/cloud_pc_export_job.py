from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_export_job_status, cloud_pc_report_name, entity

from . import entity

@dataclass
class CloudPcExportJob(entity.Entity):
    # The date and time when the export job expires.
    expiration_date_time: Optional[datetime] = None
    # The status of the export job. The possible values are: notStarted, inProgress, completed, unknownFutureValue. Read-only.
    export_job_status: Optional[cloud_pc_export_job_status.CloudPcExportJobStatus] = None
    # The storage account URL of the exported report. It can be used to download the file.
    export_url: Optional[str] = None
    # The filter applied on the report.
    filter: Optional[str] = None
    # The format of the exported report.
    format: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The report name. The possible values are: remoteConnectionHistoricalReports, dailyAggregatedRemoteConnectionReports, totalAggregatedRemoteConnectionReports, sharedUseLicenseUsageReport, sharedUseLicenseUsageRealTimeReport, or unknownFutureValue.
    report_name: Optional[cloud_pc_report_name.CloudPcReportName] = None
    # The date and time when the export job was requested.
    request_date_time: Optional[datetime] = None
    # The selected columns of the report.
    select: Optional[List[str]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_export_job_status, cloud_pc_report_name, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "exportJobStatus": lambda n : setattr(self, 'export_job_status', n.get_enum_value(cloud_pc_export_job_status.CloudPcExportJobStatus)),
            "exportUrl": lambda n : setattr(self, 'export_url', n.get_str_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "reportName": lambda n : setattr(self, 'report_name', n.get_enum_value(cloud_pc_report_name.CloudPcReportName)),
            "requestDateTime": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    

