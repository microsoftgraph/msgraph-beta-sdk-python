from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_auto_update_superseded_apps import Win32LobAppAutoUpdateSupersededApps

@dataclass
class Win32LobAppAutoUpdateSettings(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties used to perform the auto-update of an application.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Contains value for auto-update superseded apps.
    auto_update_superseded_apps: Optional[Win32LobAppAutoUpdateSupersededApps] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppAutoUpdateSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppAutoUpdateSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppAutoUpdateSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_auto_update_superseded_apps import Win32LobAppAutoUpdateSupersededApps

        from .win32_lob_app_auto_update_superseded_apps import Win32LobAppAutoUpdateSupersededApps

        fields: Dict[str, Callable[[Any], None]] = {
            "autoUpdateSupersededApps": lambda n : setattr(self, 'auto_update_superseded_apps', n.get_enum_value(Win32LobAppAutoUpdateSupersededApps)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("autoUpdateSupersededApps", self.auto_update_superseded_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

