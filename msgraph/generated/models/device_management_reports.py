from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
    from .device_management_export_job import DeviceManagementExportJob
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementReports(Entity):
    """
    Singleton entity that acts as a container for all reports functionality.
    """
    # Entity representing the configuration of a cached report
    cached_report_configurations: Optional[List[DeviceManagementCachedReportConfiguration]] = None
    # Entity representing a job to export a report
    export_jobs: Optional[List[DeviceManagementExportJob]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementReports:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementReports
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementReports()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
        from .device_management_export_job import DeviceManagementExportJob
        from .entity import Entity

        from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
        from .device_management_export_job import DeviceManagementExportJob
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "cachedReportConfigurations": lambda n : setattr(self, 'cached_report_configurations', n.get_collection_of_object_values(DeviceManagementCachedReportConfiguration)),
            "exportJobs": lambda n : setattr(self, 'export_jobs', n.get_collection_of_object_values(DeviceManagementExportJob)),
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
        writer.write_collection_of_object_values("cachedReportConfigurations", self.cached_report_configurations)
        writer.write_collection_of_object_values("exportJobs", self.export_jobs)
    

