from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_attribute_collection_page, identity_user_flow_attribute, on_attribute_collection_handler

from . import on_attribute_collection_handler

class OnAttributeCollectionExternalUsersSelfServiceSignUp(on_attribute_collection_handler.OnAttributeCollectionHandler):
    def __init__(self,) -> None:
        """
        Instantiates a new OnAttributeCollectionExternalUsersSelfServiceSignUp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp"
        # Required. The configuration for how attributes are displayed in the sign up experience defined by a user flow, like the externalUsersSelfServiceSignupEventsFlow, specifically on the attribute collection page.
        self._attribute_collection_page: Optional[authentication_attribute_collection_page.AuthenticationAttributeCollectionPage] = None
        # The attributes property
        self._attributes: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None
    
    @property
    def attribute_collection_page(self,) -> Optional[authentication_attribute_collection_page.AuthenticationAttributeCollectionPage]:
        """
        Gets the attributeCollectionPage property value. Required. The configuration for how attributes are displayed in the sign up experience defined by a user flow, like the externalUsersSelfServiceSignupEventsFlow, specifically on the attribute collection page.
        Returns: Optional[authentication_attribute_collection_page.AuthenticationAttributeCollectionPage]
        """
        return self._attribute_collection_page
    
    @attribute_collection_page.setter
    def attribute_collection_page(self,value: Optional[authentication_attribute_collection_page.AuthenticationAttributeCollectionPage] = None) -> None:
        """
        Sets the attributeCollectionPage property value. Required. The configuration for how attributes are displayed in the sign up experience defined by a user flow, like the externalUsersSelfServiceSignupEventsFlow, specifically on the attribute collection page.
        Args:
            value: Value to set for the attribute_collection_page property.
        """
        self._attribute_collection_page = value
    
    @property
    def attributes(self,) -> Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]]:
        """
        Gets the attributes property value. The attributes property
        Returns: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]]
        """
        return self._attributes
    
    @attributes.setter
    def attributes(self,value: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None) -> None:
        """
        Sets the attributes property value. The attributes property
        Args:
            value: Value to set for the attributes property.
        """
        self._attributes = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnAttributeCollectionExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnAttributeCollectionExternalUsersSelfServiceSignUp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnAttributeCollectionExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_attribute_collection_page, identity_user_flow_attribute, on_attribute_collection_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(identity_user_flow_attribute.IdentityUserFlowAttribute)),
            "attributeCollectionPage": lambda n : setattr(self, 'attribute_collection_page', n.get_object_value(authentication_attribute_collection_page.AuthenticationAttributeCollectionPage)),
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
        writer.write_collection_of_object_values("attributes", self.attributes)
        writer.write_object_value("attributeCollectionPage", self.attribute_collection_page)
    

