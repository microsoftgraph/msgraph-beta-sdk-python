from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_list_item import AppListItem

@dataclass
class IosSingleSignOnSettings(AdditionalDataHolder, BackedModel, Parsable):
    """
    iOS Kerberos authentication settings for single sign-on
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # List of app identifiers that are allowed to use this login. If this field is omitted, the login applies to all applications on the device. This collection can contain a maximum of 500 elements.
    allowed_apps_list: Optional[List[AppListItem]] = None
    # List of HTTP URLs that must be matched in order to use this login. With iOS 9.0 or later, a wildcard characters may be used.
    allowed_urls: Optional[List[str]] = None
    # The display name of login settings shown on the receiving device.
    display_name: Optional[str] = None
    # A Kerberos principal name. If not provided, the user is prompted for one during profile installation.
    kerberos_principal_name: Optional[str] = None
    # A Kerberos realm name. Case sensitive.
    kerberos_realm: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosSingleSignOnSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosSingleSignOnSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosSingleSignOnSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_list_item import AppListItem

        from .app_list_item import AppListItem

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedAppsList": lambda n : setattr(self, 'allowed_apps_list', n.get_collection_of_object_values(AppListItem)),
            "allowedUrls": lambda n : setattr(self, 'allowed_urls', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "kerberosPrincipalName": lambda n : setattr(self, 'kerberos_principal_name', n.get_str_value()),
            "kerberosRealm": lambda n : setattr(self, 'kerberos_realm', n.get_str_value()),
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
        writer.write_collection_of_object_values("allowedAppsList", self.allowed_apps_list)
        writer.write_collection_of_primitive_values("allowedUrls", self.allowed_urls)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("kerberosPrincipalName", self.kerberos_principal_name)
        writer.write_str_value("kerberosRealm", self.kerberos_realm)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

