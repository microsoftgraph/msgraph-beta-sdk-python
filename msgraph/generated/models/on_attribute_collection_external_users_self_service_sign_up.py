from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_attribute_collection_page, identity_user_flow_attribute, on_attribute_collection_handler

from . import on_attribute_collection_handler

@dataclass
class OnAttributeCollectionExternalUsersSelfServiceSignUp(on_attribute_collection_handler.OnAttributeCollectionHandler):
    odata_type = "#microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp"
    # Required. The configuration for how attributes are displayed in the sign up experience defined by a user flow, like the externalUsersSelfServiceSignupEventsFlow, specifically on the attribute collection page.
    attribute_collection_page: Optional[authentication_attribute_collection_page.AuthenticationAttributeCollectionPage] = None
    # The attributes property
    attributes: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnAttributeCollectionExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnAttributeCollectionExternalUsersSelfServiceSignUp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnAttributeCollectionExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_attribute_collection_page, identity_user_flow_attribute, on_attribute_collection_handler

        from . import authentication_attribute_collection_page, identity_user_flow_attribute, on_attribute_collection_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "attributeCollectionPage": lambda n : setattr(self, 'attribute_collection_page', n.get_object_value(authentication_attribute_collection_page.AuthenticationAttributeCollectionPage)),
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(identity_user_flow_attribute.IdentityUserFlowAttribute)),
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
        writer.write_object_value("attributeCollectionPage", self.attribute_collection_page)
        writer.write_collection_of_object_values("attributes", self.attributes)
    

