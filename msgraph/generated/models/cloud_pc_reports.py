from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_export_job = lazy_import('msgraph.generated.models.cloud_pc_export_job')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcReports(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcReports and sets the default values.
        """
        super().__init__()
        # The export jobs created for downloading reports.
        self._export_jobs: Optional[List[cloud_pc_export_job.CloudPcExportJob]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcReports:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcReports
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcReports()
    
    @property
    def export_jobs(self,) -> Optional[List[cloud_pc_export_job.CloudPcExportJob]]:
        """
        Gets the exportJobs property value. The export jobs created for downloading reports.
        Returns: Optional[List[cloud_pc_export_job.CloudPcExportJob]]
        """
        return self._export_jobs
    
    @export_jobs.setter
    def export_jobs(self,value: Optional[List[cloud_pc_export_job.CloudPcExportJob]] = None) -> None:
        """
        Sets the exportJobs property value. The export jobs created for downloading reports.
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
            "export_jobs": lambda n : setattr(self, 'export_jobs', n.get_collection_of_object_values(cloud_pc_export_job.CloudPcExportJob)),
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
        writer.write_collection_of_object_values("exportJobs", self.export_jobs)
    

