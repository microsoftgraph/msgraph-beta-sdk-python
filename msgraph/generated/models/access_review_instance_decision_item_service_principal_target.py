from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_instance_decision_item_target = lazy_import('msgraph.generated.models.access_review_instance_decision_item_target')

class AccessReviewInstanceDecisionItemServicePrincipalTarget(access_review_instance_decision_item_target.AccessReviewInstanceDecisionItemTarget):
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The appId for the service principal entity being reviewed.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The appId for the service principal entity being reviewed.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewInstanceDecisionItemServicePrincipalTarget and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalTarget"
        # The appId for the service principal entity being reviewed.
        self._app_id: Optional[str] = None
        # The display name of the service principal whose access is being reviewed.
        self._service_principal_display_name: Optional[str] = None
        # The servicePrincipalId property
        self._service_principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemServicePrincipalTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemServicePrincipalTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInstanceDecisionItemServicePrincipalTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "service_principal_display_name": lambda n : setattr(self, 'service_principal_display_name', n.get_str_value()),
            "service_principal_id": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
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
        writer.write_str_value("servicePrincipalDisplayName", self.service_principal_display_name)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
    
    @property
    def service_principal_display_name(self,) -> Optional[str]:
        """
        Gets the servicePrincipalDisplayName property value. The display name of the service principal whose access is being reviewed.
        Returns: Optional[str]
        """
        return self._service_principal_display_name
    
    @service_principal_display_name.setter
    def service_principal_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalDisplayName property value. The display name of the service principal whose access is being reviewed.
        Args:
            value: Value to set for the servicePrincipalDisplayName property.
        """
        self._service_principal_display_name = value
    
    @property
    def service_principal_id(self,) -> Optional[str]:
        """
        Gets the servicePrincipalId property value. The servicePrincipalId property
        Returns: Optional[str]
        """
        return self._service_principal_id
    
    @service_principal_id.setter
    def service_principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalId property value. The servicePrincipalId property
        Args:
            value: Value to set for the servicePrincipalId property.
        """
        self._service_principal_id = value
    

