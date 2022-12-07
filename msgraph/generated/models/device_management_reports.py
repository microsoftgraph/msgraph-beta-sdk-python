from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_cached_report_configuration = lazy_import('msgraph.generated.models.device_management_cached_report_configuration')
device_management_export_job = lazy_import('msgraph.generated.models.device_management_export_job')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementReports(entity.Entity):
    @property
    def cached_report_configurations(self,) -> Optional[List[device_management_cached_report_configuration.DeviceManagementCachedReportConfiguration]]:
        """
        Gets the cachedReportConfigurations property value. Entity representing the configuration of a cached report
        Returns: Optional[List[device_management_cached_report_configuration.DeviceManagementCachedReportConfiguration]]
        """
        return self._cached_report_configurations
    
    @cached_report_configurations.setter
    def cached_report_configurations(self,value: Optional[List[device_management_cached_report_configuration.DeviceManagementCachedReportConfiguration]] = None) -> None:
        """
        Sets the cachedReportConfigurations property value. Entity representing the configuration of a cached report
        Args:
            value: Value to set for the cachedReportConfigurations property.
        """
        self._cached_report_configurations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementReports and sets the default values.
        """
        super().__init__()
        # Entity representing the configuration of a cached report
        self._cached_report_configurations: Optional[List[device_management_cached_report_configuration.DeviceManagementCachedReportConfiguration]] = None
        # Entity representing a job to export a report
        self._export_jobs: Optional[List[device_management_export_job.DeviceManagementExportJob]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementReports:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementReports
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementReports()
    
    @property
    def export_jobs(self,) -> Optional[List[device_management_export_job.DeviceManagementExportJob]]:
        """
        Gets the exportJobs property value. Entity representing a job to export a report
        Returns: Optional[List[device_management_export_job.DeviceManagementExportJob]]
        """
        return self._export_jobs
    
    @export_jobs.setter
    def export_jobs(self,value: Optional[List[device_management_export_job.DeviceManagementExportJob]] = None) -> None:
        """
        Sets the exportJobs property value. Entity representing a job to export a report
        Args:
            value: Value to set for the exportJobs property.
        """
        self._export_jobs = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cached_report_configurations": lambda n : setattr(self, 'cached_report_configurations', n.get_collection_of_object_values(device_management_cached_report_configuration.DeviceManagementCachedReportConfiguration)),
            "export_jobs": lambda n : setattr(self, 'export_jobs', n.get_collection_of_object_values(device_management_export_job.DeviceManagementExportJob)),
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
        writer.write_collection_of_object_values("cachedReportConfigurations", self.cached_report_configurations)
        writer.write_collection_of_object_values("exportJobs", self.export_jobs)
    

