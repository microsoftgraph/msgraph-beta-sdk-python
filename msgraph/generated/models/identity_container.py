from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_events_flow, authentication_event_listener, b2c_identity_user_flow, b2x_identity_user_flow, conditional_access_root, continuous_access_evaluation_policy, custom_authentication_extension, identity_api_connector, identity_provider_base, identity_user_flow, identity_user_flow_attribute

@dataclass
class IdentityContainer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Represents entry point for API connectors.
    api_connectors: Optional[List[identity_api_connector.IdentityApiConnector]] = None
    # The authenticationEventListeners property
    authentication_event_listeners: Optional[List[authentication_event_listener.AuthenticationEventListener]] = None
    # Represents the entry point for self-service sign up and sign in user flows in both Azure AD workforce and customer tenants.
    authentication_events_flows: Optional[List[authentication_events_flow.AuthenticationEventsFlow]] = None
    # Represents entry point for B2C identity userflows.
    b2c_user_flows: Optional[List[b2c_identity_user_flow.B2cIdentityUserFlow]] = None
    # Represents entry point for B2X and self-service sign-up identity userflows.
    b2x_user_flows: Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]] = None
    # the entry point for the Conditional Access (CA) object model.
    conditional_access: Optional[conditional_access_root.ConditionalAccessRoot] = None
    # Represents entry point for continuous access evaluation policy.
    continuous_access_evaluation_policy: Optional[continuous_access_evaluation_policy.ContinuousAccessEvaluationPolicy] = None
    # The customAuthenticationExtensions property
    custom_authentication_extensions: Optional[List[custom_authentication_extension.CustomAuthenticationExtension]] = None
    # Represents entry point for identity provider base.
    identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents entry point for identity userflow attributes.
    user_flow_attributes: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None
    # The userFlows property
    user_flows: Optional[List[identity_user_flow.IdentityUserFlow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_events_flow, authentication_event_listener, b2c_identity_user_flow, b2x_identity_user_flow, conditional_access_root, continuous_access_evaluation_policy, custom_authentication_extension, identity_api_connector, identity_provider_base, identity_user_flow, identity_user_flow_attribute

        fields: Dict[str, Callable[[Any], None]] = {
            "apiConnectors": lambda n : setattr(self, 'api_connectors', n.get_collection_of_object_values(identity_api_connector.IdentityApiConnector)),
            "authenticationEventsFlows": lambda n : setattr(self, 'authentication_events_flows', n.get_collection_of_object_values(authentication_events_flow.AuthenticationEventsFlow)),
            "authenticationEventListeners": lambda n : setattr(self, 'authentication_event_listeners', n.get_collection_of_object_values(authentication_event_listener.AuthenticationEventListener)),
            "b2cUserFlows": lambda n : setattr(self, 'b2c_user_flows', n.get_collection_of_object_values(b2c_identity_user_flow.B2cIdentityUserFlow)),
            "b2xUserFlows": lambda n : setattr(self, 'b2x_user_flows', n.get_collection_of_object_values(b2x_identity_user_flow.B2xIdentityUserFlow)),
            "conditionalAccess": lambda n : setattr(self, 'conditional_access', n.get_object_value(conditional_access_root.ConditionalAccessRoot)),
            "continuousAccessEvaluationPolicy": lambda n : setattr(self, 'continuous_access_evaluation_policy', n.get_object_value(continuous_access_evaluation_policy.ContinuousAccessEvaluationPolicy)),
            "customAuthenticationExtensions": lambda n : setattr(self, 'custom_authentication_extensions', n.get_collection_of_object_values(custom_authentication_extension.CustomAuthenticationExtension)),
            "identityProviders": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userFlows": lambda n : setattr(self, 'user_flows', n.get_collection_of_object_values(identity_user_flow.IdentityUserFlow)),
            "userFlowAttributes": lambda n : setattr(self, 'user_flow_attributes', n.get_collection_of_object_values(identity_user_flow_attribute.IdentityUserFlowAttribute)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("apiConnectors", self.api_connectors)
        writer.write_collection_of_object_values("authenticationEventsFlows", self.authentication_events_flows)
        writer.write_collection_of_object_values("authenticationEventListeners", self.authentication_event_listeners)
        writer.write_collection_of_object_values("b2cUserFlows", self.b2c_user_flows)
        writer.write_collection_of_object_values("b2xUserFlows", self.b2x_user_flows)
        writer.write_object_value("conditionalAccess", self.conditional_access)
        writer.write_object_value("continuousAccessEvaluationPolicy", self.continuous_access_evaluation_policy)
        writer.write_collection_of_object_values("customAuthenticationExtensions", self.custom_authentication_extensions)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("userFlows", self.user_flows)
        writer.write_collection_of_object_values("userFlowAttributes", self.user_flow_attributes)
        writer.write_additional_data_value(self.additional_data)
    

