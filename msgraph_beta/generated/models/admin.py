from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin_apps_and_services import AdminAppsAndServices
    from .admin_dynamics import AdminDynamics
    from .admin_forms import AdminForms
    from .admin_microsoft365_apps import AdminMicrosoft365Apps
    from .admin_report_settings import AdminReportSettings
    from .admin_todo import AdminTodo
    from .admin_windows import AdminWindows
    from .edge import Edge
    from .entra import Entra
    from .people_admin_settings import PeopleAdminSettings
    from .service_announcement import ServiceAnnouncement
    from .sharepoint import Sharepoint

@dataclass
class Admin(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The appsAndServices property
    apps_and_services: Optional[AdminAppsAndServices] = None
    # The dynamics property
    dynamics: Optional[AdminDynamics] = None
    # A container for Microsoft Edge resources. Read-only.
    edge: Optional[Edge] = None
    # The entra property
    entra: Optional[Entra] = None
    # The forms property
    forms: Optional[AdminForms] = None
    # A container for the Microsoft 365 apps admin functionality.
    microsoft365_apps: Optional[AdminMicrosoft365Apps] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a setting to control people-related admin settings in the tenant.
    people: Optional[PeopleAdminSettings] = None
    # A container for administrative resources to manage reports.
    report_settings: Optional[AdminReportSettings] = None
    # A container for service communications resources. Read-only.
    service_announcement: Optional[ServiceAnnouncement] = None
    # The sharepoint property
    sharepoint: Optional[Sharepoint] = None
    # The todo property
    todo: Optional[AdminTodo] = None
    # A container for all Windows administrator functionalities. Read-only.
    windows: Optional[AdminWindows] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Admin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Admin
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Admin()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .admin_apps_and_services import AdminAppsAndServices
        from .admin_dynamics import AdminDynamics
        from .admin_forms import AdminForms
        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .admin_todo import AdminTodo
        from .admin_windows import AdminWindows
        from .edge import Edge
        from .entra import Entra
        from .people_admin_settings import PeopleAdminSettings
        from .service_announcement import ServiceAnnouncement
        from .sharepoint import Sharepoint

        from .admin_apps_and_services import AdminAppsAndServices
        from .admin_dynamics import AdminDynamics
        from .admin_forms import AdminForms
        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .admin_todo import AdminTodo
        from .admin_windows import AdminWindows
        from .edge import Edge
        from .entra import Entra
        from .people_admin_settings import PeopleAdminSettings
        from .service_announcement import ServiceAnnouncement
        from .sharepoint import Sharepoint

        fields: Dict[str, Callable[[Any], None]] = {
            "appsAndServices": lambda n : setattr(self, 'apps_and_services', n.get_object_value(AdminAppsAndServices)),
            "dynamics": lambda n : setattr(self, 'dynamics', n.get_object_value(AdminDynamics)),
            "edge": lambda n : setattr(self, 'edge', n.get_object_value(Edge)),
            "entra": lambda n : setattr(self, 'entra', n.get_object_value(Entra)),
            "forms": lambda n : setattr(self, 'forms', n.get_object_value(AdminForms)),
            "microsoft365Apps": lambda n : setattr(self, 'microsoft365_apps', n.get_object_value(AdminMicrosoft365Apps)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "people": lambda n : setattr(self, 'people', n.get_object_value(PeopleAdminSettings)),
            "reportSettings": lambda n : setattr(self, 'report_settings', n.get_object_value(AdminReportSettings)),
            "serviceAnnouncement": lambda n : setattr(self, 'service_announcement', n.get_object_value(ServiceAnnouncement)),
            "sharepoint": lambda n : setattr(self, 'sharepoint', n.get_object_value(Sharepoint)),
            "todo": lambda n : setattr(self, 'todo', n.get_object_value(AdminTodo)),
            "windows": lambda n : setattr(self, 'windows', n.get_object_value(AdminWindows)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("appsAndServices", self.apps_and_services)
        writer.write_object_value("dynamics", self.dynamics)
        writer.write_object_value("edge", self.edge)
        writer.write_object_value("entra", self.entra)
        writer.write_object_value("forms", self.forms)
        writer.write_object_value("microsoft365Apps", self.microsoft365_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("people", self.people)
        writer.write_object_value("reportSettings", self.report_settings)
        writer.write_object_value("serviceAnnouncement", self.service_announcement)
        writer.write_object_value("sharepoint", self.sharepoint)
        writer.write_object_value("todo", self.todo)
        writer.write_object_value("windows", self.windows)
        writer.write_additional_data_value(self.additional_data)
    

