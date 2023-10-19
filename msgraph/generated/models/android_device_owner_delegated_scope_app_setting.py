from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType
    from .app_list_item import AppListItem

@dataclass
class AndroidDeviceOwnerDelegatedScopeAppSetting(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents one item in the list of managed apps with app details and its associated delegated scope(s).
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents an app in the list of managed applications
    app_detail: Optional[AppListItem] = None
    # List of scopes an app has been assigned.
    app_scopes: Optional[List[AndroidDeviceOwnerDelegatedAppScopeType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerDelegatedScopeAppSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerDelegatedScopeAppSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerDelegatedScopeAppSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType
        from .app_list_item import AppListItem

        from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType
        from .app_list_item import AppListItem

        fields: Dict[str, Callable[[Any], None]] = {
            "appDetail": lambda n : setattr(self, 'app_detail', n.get_object_value(AppListItem)),
            "appScopes": lambda n : setattr(self, 'app_scopes', n.get_collection_of_enum_values(AndroidDeviceOwnerDelegatedAppScopeType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("appDetail", self.app_detail)
        writer.write_collection_of_enum_values("appScopes", self.app_scopes)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

