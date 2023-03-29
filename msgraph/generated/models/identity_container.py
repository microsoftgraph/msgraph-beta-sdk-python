from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_event_listener, b2c_identity_user_flow, b2x_identity_user_flow, conditional_access_root, continuous_access_evaluation_policy, custom_authentication_extension, identity_api_connector, identity_provider_base, identity_user_flow, identity_user_flow_attribute

class IdentityContainer(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new IdentityContainer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents entry point for API connectors.
        self._api_connectors: Optional[List[identity_api_connector.IdentityApiConnector]] = None
        # The authenticationEventListeners property
        self._authentication_event_listeners: Optional[List[authentication_event_listener.AuthenticationEventListener]] = None
        # Represents entry point for B2C identity userflows.
        self._b2c_user_flows: Optional[List[b2c_identity_user_flow.B2cIdentityUserFlow]] = None
        # Represents entry point for B2X and self-service sign-up identity userflows.
        self._b2x_user_flows: Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]] = None
        # the entry point for the Conditional Access (CA) object model.
        self._conditional_access: Optional[conditional_access_root.ConditionalAccessRoot] = None
        # Represents entry point for continuous access evaluation policy.
        self._continuous_access_evaluation_policy: Optional[continuous_access_evaluation_policy.ContinuousAccessEvaluationPolicy] = None
        # The customAuthenticationExtensions property
        self._custom_authentication_extensions: Optional[List[custom_authentication_extension.CustomAuthenticationExtension]] = None
        # Represents entry point for identity provider base.
        self._identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents entry point for identity userflow attributes.
        self._user_flow_attributes: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None
        # The userFlows property
        self._user_flows: Optional[List[identity_user_flow.IdentityUserFlow]] = None
    
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
    def api_connectors(self,) -> Optional[List[identity_api_connector.IdentityApiConnector]]:
        """
        Gets the apiConnectors property value. Represents entry point for API connectors.
        Returns: Optional[List[identity_api_connector.IdentityApiConnector]]
        """
        return self._api_connectors
    
    @api_connectors.setter
    def api_connectors(self,value: Optional[List[identity_api_connector.IdentityApiConnector]] = None) -> None:
        """
        Sets the apiConnectors property value. Represents entry point for API connectors.
        Args:
            value: Value to set for the api_connectors property.
        """
        self._api_connectors = value
    
    @property
    def authentication_event_listeners(self,) -> Optional[List[authentication_event_listener.AuthenticationEventListener]]:
        """
        Gets the authenticationEventListeners property value. The authenticationEventListeners property
        Returns: Optional[List[authentication_event_listener.AuthenticationEventListener]]
        """
        return self._authentication_event_listeners
    
    @authentication_event_listeners.setter
    def authentication_event_listeners(self,value: Optional[List[authentication_event_listener.AuthenticationEventListener]] = None) -> None:
        """
        Sets the authenticationEventListeners property value. The authenticationEventListeners property
        Args:
            value: Value to set for the authentication_event_listeners property.
        """
        self._authentication_event_listeners = value
    
    @property
    def b2c_user_flows(self,) -> Optional[List[b2c_identity_user_flow.B2cIdentityUserFlow]]:
        """
        Gets the b2cUserFlows property value. Represents entry point for B2C identity userflows.
        Returns: Optional[List[b2c_identity_user_flow.B2cIdentityUserFlow]]
        """
        return self._b2c_user_flows
    
    @b2c_user_flows.setter
    def b2c_user_flows(self,value: Optional[List[b2c_identity_user_flow.B2cIdentityUserFlow]] = None) -> None:
        """
        Sets the b2cUserFlows property value. Represents entry point for B2C identity userflows.
        Args:
            value: Value to set for the b2c_user_flows property.
        """
        self._b2c_user_flows = value
    
    @property
    def b2x_user_flows(self,) -> Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]]:
        """
        Gets the b2xUserFlows property value. Represents entry point for B2X and self-service sign-up identity userflows.
        Returns: Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]]
        """
        return self._b2x_user_flows
    
    @b2x_user_flows.setter
    def b2x_user_flows(self,value: Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]] = None) -> None:
        """
        Sets the b2xUserFlows property value. Represents entry point for B2X and self-service sign-up identity userflows.
        Args:
            value: Value to set for the b2x_user_flows property.
        """
        self._b2x_user_flows = value
    
    @property
    def conditional_access(self,) -> Optional[conditional_access_root.ConditionalAccessRoot]:
        """
        Gets the conditionalAccess property value. the entry point for the Conditional Access (CA) object model.
        Returns: Optional[conditional_access_root.ConditionalAccessRoot]
        """
        return self._conditional_access
    
    @conditional_access.setter
    def conditional_access(self,value: Optional[conditional_access_root.ConditionalAccessRoot] = None) -> None:
        """
        Sets the conditionalAccess property value. the entry point for the Conditional Access (CA) object model.
        Args:
            value: Value to set for the conditional_access property.
        """
        self._conditional_access = value
    
    @property
    def continuous_access_evaluation_policy(self,) -> Optional[continuous_access_evaluation_policy.ContinuousAccessEvaluationPolicy]:
        """
        Gets the continuousAccessEvaluationPolicy property value. Represents entry point for continuous access evaluation policy.
        Returns: Optional[continuous_access_evaluation_policy.ContinuousAccessEvaluationPolicy]
        """
        return self._continuous_access_evaluation_policy
    
    @continuous_access_evaluation_policy.setter
    def continuous_access_evaluation_policy(self,value: Optional[continuous_access_evaluation_policy.ContinuousAccessEvaluationPolicy] = None) -> None:
        """
        Sets the continuousAccessEvaluationPolicy property value. Represents entry point for continuous access evaluation policy.
        Args:
            value: Value to set for the continuous_access_evaluation_policy property.
        """
        self._continuous_access_evaluation_policy = value
    
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
    
    @property
    def custom_authentication_extensions(self,) -> Optional[List[custom_authentication_extension.CustomAuthenticationExtension]]:
        """
        Gets the customAuthenticationExtensions property value. The customAuthenticationExtensions property
        Returns: Optional[List[custom_authentication_extension.CustomAuthenticationExtension]]
        """
        return self._custom_authentication_extensions
    
    @custom_authentication_extensions.setter
    def custom_authentication_extensions(self,value: Optional[List[custom_authentication_extension.CustomAuthenticationExtension]] = None) -> None:
        """
        Sets the customAuthenticationExtensions property value. The customAuthenticationExtensions property
        Args:
            value: Value to set for the custom_authentication_extensions property.
        """
        self._custom_authentication_extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_event_listener, b2c_identity_user_flow, b2x_identity_user_flow, conditional_access_root, continuous_access_evaluation_policy, custom_authentication_extension, identity_api_connector, identity_provider_base, identity_user_flow, identity_user_flow_attribute

        fields: Dict[str, Callable[[Any], None]] = {
            "apiConnectors": lambda n : setattr(self, 'api_connectors', n.get_collection_of_object_values(identity_api_connector.IdentityApiConnector)),
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
    
    @property
    def identity_providers(self,) -> Optional[List[identity_provider_base.IdentityProviderBase]]:
        """
        Gets the identityProviders property value. Represents entry point for identity provider base.
        Returns: Optional[List[identity_provider_base.IdentityProviderBase]]
        """
        return self._identity_providers
    
    @identity_providers.setter
    def identity_providers(self,value: Optional[List[identity_provider_base.IdentityProviderBase]] = None) -> None:
        """
        Sets the identityProviders property value. Represents entry point for identity provider base.
        Args:
            value: Value to set for the identity_providers property.
        """
        self._identity_providers = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_collection_of_object_values("apiConnectors", self.api_connectors)
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
    
    @property
    def user_flow_attributes(self,) -> Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]]:
        """
        Gets the userFlowAttributes property value. Represents entry point for identity userflow attributes.
        Returns: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]]
        """
        return self._user_flow_attributes
    
    @user_flow_attributes.setter
    def user_flow_attributes(self,value: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None) -> None:
        """
        Sets the userFlowAttributes property value. Represents entry point for identity userflow attributes.
        Args:
            value: Value to set for the user_flow_attributes property.
        """
        self._user_flow_attributes = value
    
    @property
    def user_flows(self,) -> Optional[List[identity_user_flow.IdentityUserFlow]]:
        """
        Gets the userFlows property value. The userFlows property
        Returns: Optional[List[identity_user_flow.IdentityUserFlow]]
        """
        return self._user_flows
    
    @user_flows.setter
    def user_flows(self,value: Optional[List[identity_user_flow.IdentityUserFlow]] = None) -> None:
        """
        Sets the userFlows property value. The userFlows property
        Args:
            value: Value to set for the user_flows property.
        """
        self._user_flows = value
    

