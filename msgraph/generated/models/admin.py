from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import admin_report_settings, admin_windows, edge, service_announcement, sharepoint

@dataclass
class Admin(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A container for Microsoft Edge resources. Read-only.
    edge: Optional[edge.Edge] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A container for administrative resources to manage reports.
    report_settings: Optional[admin_report_settings.AdminReportSettings] = None
    # A container for service communications resources. Read-only.
    service_announcement: Optional[service_announcement.ServiceAnnouncement] = None
    # The sharepoint property
    sharepoint: Optional[sharepoint.Sharepoint] = None
    # A container for all Windows administrator functionalities. Read-only.
    windows: Optional[admin_windows.AdminWindows] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Admin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Admin
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Admin()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import admin_report_settings, admin_windows, edge, service_announcement, sharepoint

        from . import admin_report_settings, admin_windows, edge, service_announcement, sharepoint

        fields: Dict[str, Callable[[Any], None]] = {
            "edge": lambda n : setattr(self, 'edge', n.get_object_value(edge.Edge)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reportSettings": lambda n : setattr(self, 'report_settings', n.get_object_value(admin_report_settings.AdminReportSettings)),
            "serviceAnnouncement": lambda n : setattr(self, 'service_announcement', n.get_object_value(service_announcement.ServiceAnnouncement)),
            "sharepoint": lambda n : setattr(self, 'sharepoint', n.get_object_value(sharepoint.Sharepoint)),
            "windows": lambda n : setattr(self, 'windows', n.get_object_value(admin_windows.AdminWindows)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("edge", self.edge)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("reportSettings", self.report_settings)
        writer.write_object_value("serviceAnnouncement", self.service_announcement)
        writer.write_object_value("sharepoint", self.sharepoint)
        writer.write_object_value("windows", self.windows)
        writer.write_additional_data_value(self.additional_data)
    

