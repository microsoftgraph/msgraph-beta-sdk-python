from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import admin_report_settings, admin_windows, edge, service_announcement, sharepoint

class Admin(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new Admin and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A container for Microsoft Edge resources. Read-only.
        self._edge: Optional[edge.Edge] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A container for administrative resources to manage reports.
        self._report_settings: Optional[admin_report_settings.AdminReportSettings] = None
        # A container for service communications resources. Read-only.
        self._service_announcement: Optional[service_announcement.ServiceAnnouncement] = None
        # A container for administrative resources to manage tenant-level settings for SharePoint and OneDrive.
        self._sharepoint: Optional[sharepoint.Sharepoint] = None
        # A container for all Windows administrator functionalities. Read-only.
        self._windows: Optional[admin_windows.AdminWindows] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Admin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Admin
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Admin()
    
    @property
    def edge(self,) -> Optional[edge.Edge]:
        """
        Gets the edge property value. A container for Microsoft Edge resources. Read-only.
        Returns: Optional[edge.Edge]
        """
        return self._edge
    
    @edge.setter
    def edge(self,value: Optional[edge.Edge] = None) -> None:
        """
        Sets the edge property value. A container for Microsoft Edge resources. Read-only.
        Args:
            value: Value to set for the edge property.
        """
        self._edge = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def report_settings(self,) -> Optional[admin_report_settings.AdminReportSettings]:
        """
        Gets the reportSettings property value. A container for administrative resources to manage reports.
        Returns: Optional[admin_report_settings.AdminReportSettings]
        """
        return self._report_settings
    
    @report_settings.setter
    def report_settings(self,value: Optional[admin_report_settings.AdminReportSettings] = None) -> None:
        """
        Sets the reportSettings property value. A container for administrative resources to manage reports.
        Args:
            value: Value to set for the report_settings property.
        """
        self._report_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("edge", self.edge)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("reportSettings", self.report_settings)
        writer.write_object_value("serviceAnnouncement", self.service_announcement)
        writer.write_object_value("sharepoint", self.sharepoint)
        writer.write_object_value("windows", self.windows)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_announcement(self,) -> Optional[service_announcement.ServiceAnnouncement]:
        """
        Gets the serviceAnnouncement property value. A container for service communications resources. Read-only.
        Returns: Optional[service_announcement.ServiceAnnouncement]
        """
        return self._service_announcement
    
    @service_announcement.setter
    def service_announcement(self,value: Optional[service_announcement.ServiceAnnouncement] = None) -> None:
        """
        Sets the serviceAnnouncement property value. A container for service communications resources. Read-only.
        Args:
            value: Value to set for the service_announcement property.
        """
        self._service_announcement = value
    
    @property
    def sharepoint(self,) -> Optional[sharepoint.Sharepoint]:
        """
        Gets the sharepoint property value. A container for administrative resources to manage tenant-level settings for SharePoint and OneDrive.
        Returns: Optional[sharepoint.Sharepoint]
        """
        return self._sharepoint
    
    @sharepoint.setter
    def sharepoint(self,value: Optional[sharepoint.Sharepoint] = None) -> None:
        """
        Sets the sharepoint property value. A container for administrative resources to manage tenant-level settings for SharePoint and OneDrive.
        Args:
            value: Value to set for the sharepoint property.
        """
        self._sharepoint = value
    
    @property
    def windows(self,) -> Optional[admin_windows.AdminWindows]:
        """
        Gets the windows property value. A container for all Windows administrator functionalities. Read-only.
        Returns: Optional[admin_windows.AdminWindows]
        """
        return self._windows
    
    @windows.setter
    def windows(self,value: Optional[admin_windows.AdminWindows] = None) -> None:
        """
        Sets the windows property value. A container for all Windows administrator functionalities. Read-only.
        Args:
            value: Value to set for the windows property.
        """
        self._windows = value
    

