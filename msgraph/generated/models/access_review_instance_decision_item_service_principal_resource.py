from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_instance_decision_item_resource

from . import access_review_instance_decision_item_resource

class AccessReviewInstanceDecisionItemServicePrincipalResource(access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewInstanceDecisionItemServicePrincipalResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource"
        # The appId property
        self._app_id: Optional[str] = None
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The appId property
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The appId property
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemServicePrincipalResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemServicePrincipalResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInstanceDecisionItemServicePrincipalResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_instance_decision_item_resource

        fields: Dict[str, Callable[[Any], None]] = {
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
    

