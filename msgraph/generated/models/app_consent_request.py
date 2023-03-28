from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_consent_request_scope, entity, user_consent_request

from . import entity

class AppConsentRequest(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new appConsentRequest and sets the default values.
        """
        super().__init__()
        # The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
        self._app_display_name: Optional[str] = None
        # The identifier of the application. Required. Supports $filter (eq only) and $orderby.
        self._app_id: Optional[str] = None
        # The consent type of the request. Possible values are: Static and Dynamic. These represent static and dynamic permissions, respectively, requested in the consent workflow. Supports $filter (eq only) and $orderby. Required.
        self._consent_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A list of pending scopes waiting for approval. This is empty if the consentType is Static. Required.
        self._pending_scopes: Optional[List[app_consent_request_scope.AppConsentRequestScope]] = None
        # A list of pending user consent requests. Supports $filter (eq).
        self._user_consent_requests: Optional[List[user_consent_request.UserConsentRequest]] = None
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
        Args:
            value: Value to set for the app_display_name property.
        """
        self._app_display_name = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The identifier of the application. Required. Supports $filter (eq only) and $orderby.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The identifier of the application. Required. Supports $filter (eq only) and $orderby.
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    @property
    def consent_type(self,) -> Optional[str]:
        """
        Gets the consentType property value. The consent type of the request. Possible values are: Static and Dynamic. These represent static and dynamic permissions, respectively, requested in the consent workflow. Supports $filter (eq only) and $orderby. Required.
        Returns: Optional[str]
        """
        return self._consent_type
    
    @consent_type.setter
    def consent_type(self,value: Optional[str] = None) -> None:
        """
        Sets the consentType property value. The consent type of the request. Possible values are: Static and Dynamic. These represent static and dynamic permissions, respectively, requested in the consent workflow. Supports $filter (eq only) and $orderby. Required.
        Args:
            value: Value to set for the consent_type property.
        """
        self._consent_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppConsentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppConsentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppConsentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def pending_scopes(self,) -> Optional[List[app_consent_request_scope.AppConsentRequestScope]]:
        """
        Gets the pendingScopes property value. A list of pending scopes waiting for approval. This is empty if the consentType is Static. Required.
        Returns: Optional[List[app_consent_request_scope.AppConsentRequestScope]]
        """
        return self._pending_scopes
    
    @pending_scopes.setter
    def pending_scopes(self,value: Optional[List[app_consent_request_scope.AppConsentRequestScope]] = None) -> None:
        """
        Sets the pendingScopes property value. A list of pending scopes waiting for approval. This is empty if the consentType is Static. Required.
        Args:
            value: Value to set for the pending_scopes property.
        """
        self._pending_scopes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("consentType", self.consent_type)
        writer.write_collection_of_object_values("pendingScopes", self.pending_scopes)
        writer.write_collection_of_object_values("userConsentRequests", self.user_consent_requests)
    
    @property
    def user_consent_requests(self,) -> Optional[List[user_consent_request.UserConsentRequest]]:
        """
        Gets the userConsentRequests property value. A list of pending user consent requests. Supports $filter (eq).
        Returns: Optional[List[user_consent_request.UserConsentRequest]]
        """
        return self._user_consent_requests
    
    @user_consent_requests.setter
    def user_consent_requests(self,value: Optional[List[user_consent_request.UserConsentRequest]] = None) -> None:
        """
        Sets the userConsentRequests property value. A list of pending user consent requests. Supports $filter (eq).
        Args:
            value: Value to set for the user_consent_requests property.
        """
        self._user_consent_requests = value
    

