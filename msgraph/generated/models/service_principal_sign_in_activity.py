from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, sign_in_activity

from . import entity

@dataclass
class ServicePrincipalSignInActivity(entity.Entity):
    # The application ID of the resource.
    app_id: Optional[str] = None
    # The sign-in activity of the application in a app-only authentication flow (app-to-app tokens) where the application acts like a client.
    application_authentication_client_sign_in_activity: Optional[sign_in_activity.SignInActivity] = None
    # The sign-in activity of the application in a app-only authentication flow (app-to-app tokens) where the application acts like a resource.
    application_authentication_resource_sign_in_activity: Optional[sign_in_activity.SignInActivity] = None
    # The sign-in activity of the application in a delegated flow (user sign-in) where the application acts like a client.
    delegated_client_sign_in_activity: Optional[sign_in_activity.SignInActivity] = None
    # The sign-in activity of the application in a delegated flow (user sign-in) where the application acts like a resource.
    delegated_resource_sign_in_activity: Optional[sign_in_activity.SignInActivity] = None
    # The most recent sign-in activity of the application across delegated or app-only flows where the application is used either as a client or resource.
    last_sign_in_activity: Optional[sign_in_activity.SignInActivity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipalSignInActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalSignInActivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalSignInActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, sign_in_activity

        from . import entity, sign_in_activity

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "applicationAuthenticationClientSignInActivity": lambda n : setattr(self, 'application_authentication_client_sign_in_activity', n.get_object_value(sign_in_activity.SignInActivity)),
            "applicationAuthenticationResourceSignInActivity": lambda n : setattr(self, 'application_authentication_resource_sign_in_activity', n.get_object_value(sign_in_activity.SignInActivity)),
            "delegatedClientSignInActivity": lambda n : setattr(self, 'delegated_client_sign_in_activity', n.get_object_value(sign_in_activity.SignInActivity)),
            "delegatedResourceSignInActivity": lambda n : setattr(self, 'delegated_resource_sign_in_activity', n.get_object_value(sign_in_activity.SignInActivity)),
            "lastSignInActivity": lambda n : setattr(self, 'last_sign_in_activity', n.get_object_value(sign_in_activity.SignInActivity)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("appId", self.app_id)
        writer.write_object_value("applicationAuthenticationClientSignInActivity", self.application_authentication_client_sign_in_activity)
        writer.write_object_value("applicationAuthenticationResourceSignInActivity", self.application_authentication_resource_sign_in_activity)
        writer.write_object_value("delegatedClientSignInActivity", self.delegated_client_sign_in_activity)
        writer.write_object_value("delegatedResourceSignInActivity", self.delegated_resource_sign_in_activity)
        writer.write_object_value("lastSignInActivity", self.last_sign_in_activity)
    

