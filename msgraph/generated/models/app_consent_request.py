from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_consent_request_scope, entity, user_consent_request

from . import entity

@dataclass
class AppConsentRequest(entity.Entity):
    # The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
    app_display_name: Optional[str] = None
    # The identifier of the application. Required. Supports $filter (eq only) and $orderby.
    app_id: Optional[str] = None
    # The consent type of the request. Possible values are: Static and Dynamic. These represent static and dynamic permissions, respectively, requested in the consent workflow. Supports $filter (eq only) and $orderby. Required.
    consent_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A list of pending scopes waiting for approval. This is empty if the consentType is Static. Required.
    pending_scopes: Optional[List[app_consent_request_scope.AppConsentRequestScope]] = None
    # A list of pending user consent requests. Supports $filter (eq).
    user_consent_requests: Optional[List[user_consent_request.UserConsentRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppConsentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppConsentRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppConsentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_consent_request_scope, entity, user_consent_request

        from . import app_consent_request_scope, entity, user_consent_request

        fields: Dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "consentType": lambda n : setattr(self, 'consent_type', n.get_str_value()),
            "pendingScopes": lambda n : setattr(self, 'pending_scopes', n.get_collection_of_object_values(app_consent_request_scope.AppConsentRequestScope)),
            "userConsentRequests": lambda n : setattr(self, 'user_consent_requests', n.get_collection_of_object_values(user_consent_request.UserConsentRequest)),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("consentType", self.consent_type)
        writer.write_collection_of_object_values("pendingScopes", self.pending_scopes)
        writer.write_collection_of_object_values("userConsentRequests", self.user_consent_requests)
    

