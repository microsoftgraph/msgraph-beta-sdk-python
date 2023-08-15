from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apps_and_services_settings import AppsAndServicesSettings
    from .entity import Entity

from .entity import Entity

@dataclass
class AdminAppsAndServices(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings property
    settings: Optional[AppsAndServicesSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminAppsAndServices:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminAppsAndServices
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AdminAppsAndServices()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .apps_and_services_settings import AppsAndServicesSettings
        from .entity import Entity

        from .apps_and_services_settings import AppsAndServicesSettings
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(AppsAndServicesSettings)),
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
        writer.write_object_value("settings", self.settings)
    

