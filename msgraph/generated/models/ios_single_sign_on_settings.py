from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_list_item = lazy_import('msgraph.generated.models.app_list_item')

class IosSingleSignOnSettings(AdditionalDataHolder, Parsable):
    """
    iOS Kerberos authentication settings for single sign-on
    """
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
    
    @property
    def allowed_apps_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the allowedAppsList property value. List of app identifiers that are allowed to use this login. If this field is omitted, the login applies to all applications on the device. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._allowed_apps_list
    
    @allowed_apps_list.setter
    def allowed_apps_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the allowedAppsList property value. List of app identifiers that are allowed to use this login. If this field is omitted, the login applies to all applications on the device. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the allowedAppsList property.
        """
        self._allowed_apps_list = value
    
    @property
    def allowed_urls(self,) -> Optional[List[str]]:
        """
        Gets the allowedUrls property value. List of HTTP URLs that must be matched in order to use this login. With iOS 9.0 or later, a wildcard characters may be used.
        Returns: Optional[List[str]]
        """
        return self._allowed_urls
    
    @allowed_urls.setter
    def allowed_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedUrls property value. List of HTTP URLs that must be matched in order to use this login. With iOS 9.0 or later, a wildcard characters may be used.
        Args:
            value: Value to set for the allowedUrls property.
        """
        self._allowed_urls = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosSingleSignOnSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of app identifiers that are allowed to use this login. If this field is omitted, the login applies to all applications on the device. This collection can contain a maximum of 500 elements.
        self._allowed_apps_list: Optional[List[app_list_item.AppListItem]] = None
        # List of HTTP URLs that must be matched in order to use this login. With iOS 9.0 or later, a wildcard characters may be used.
        self._allowed_urls: Optional[List[str]] = None
        # The display name of login settings shown on the receiving device.
        self._display_name: Optional[str] = None
        # A Kerberos principal name. If not provided, the user is prompted for one during profile installation.
        self._kerberos_principal_name: Optional[str] = None
        # A Kerberos realm name. Case sensitive.
        self._kerberos_realm: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosSingleSignOnSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosSingleSignOnSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosSingleSignOnSettings()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of login settings shown on the receiving device.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of login settings shown on the receiving device.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_apps_list": lambda n : setattr(self, 'allowed_apps_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "allowed_urls": lambda n : setattr(self, 'allowed_urls', n.get_collection_of_primitive_values(str)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "kerberos_principal_name": lambda n : setattr(self, 'kerberos_principal_name', n.get_str_value()),
            "kerberos_realm": lambda n : setattr(self, 'kerberos_realm', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def kerberos_principal_name(self,) -> Optional[str]:
        """
        Gets the kerberosPrincipalName property value. A Kerberos principal name. If not provided, the user is prompted for one during profile installation.
        Returns: Optional[str]
        """
        return self._kerberos_principal_name
    
    @kerberos_principal_name.setter
    def kerberos_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the kerberosPrincipalName property value. A Kerberos principal name. If not provided, the user is prompted for one during profile installation.
        Args:
            value: Value to set for the kerberosPrincipalName property.
        """
        self._kerberos_principal_name = value
    
    @property
    def kerberos_realm(self,) -> Optional[str]:
        """
        Gets the kerberosRealm property value. A Kerberos realm name. Case sensitive.
        Returns: Optional[str]
        """
        return self._kerberos_realm
    
    @kerberos_realm.setter
    def kerberos_realm(self,value: Optional[str] = None) -> None:
        """
        Sets the kerberosRealm property value. A Kerberos realm name. Case sensitive.
        Args:
            value: Value to set for the kerberosRealm property.
        """
        self._kerberos_realm = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("allowedAppsList", self.allowed_apps_list)
        writer.write_collection_of_primitive_values("allowedUrls", self.allowed_urls)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("kerberosPrincipalName", self.kerberos_principal_name)
        writer.write_str_value("kerberosRealm", self.kerberos_realm)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

