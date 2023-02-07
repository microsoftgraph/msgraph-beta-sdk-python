from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

service_now_authentication_method = lazy_import('msgraph.generated.models.service_now_authentication_method')

class ServiceNowOauthSecretAuthentication(service_now_authentication_method.ServiceNowAuthenticationMethod):
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. Tenant appId registered with Azure AD
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. Tenant appId registered with Azure AD
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceNowOauthSecretAuthentication and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.serviceNowOauthSecretAuthentication"
        # Tenant appId registered with Azure AD
        self._app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceNowOauthSecretAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceNowOauthSecretAuthentication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceNowOauthSecretAuthentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
    

