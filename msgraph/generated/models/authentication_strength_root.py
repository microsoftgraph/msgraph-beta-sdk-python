from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_mode_detail = lazy_import('msgraph.generated.models.authentication_method_mode_detail')
authentication_method_modes = lazy_import('msgraph.generated.models.authentication_method_modes')
authentication_strength_policy = lazy_import('msgraph.generated.models.authentication_strength_policy')
entity = lazy_import('msgraph.generated.models.entity')

class AuthenticationStrengthRoot(entity.Entity):
    @property
    def authentication_combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the authenticationCombinations property value. A collection of all valid authentication method combinations in the system.
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._authentication_combinations
    
    @authentication_combinations.setter
    def authentication_combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the authenticationCombinations property value. A collection of all valid authentication method combinations in the system.
        Args:
            value: Value to set for the authenticationCombinations property.
        """
        self._authentication_combinations = value
    
    @property
    def authentication_method_modes(self,) -> Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]]:
        """
        Gets the authenticationMethodModes property value. Names and descriptions of all valid authentication method modes in the system.
        Returns: Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]]
        """
        return self._authentication_method_modes
    
    @authentication_method_modes.setter
    def authentication_method_modes(self,value: Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]] = None) -> None:
        """
        Sets the authenticationMethodModes property value. Names and descriptions of all valid authentication method modes in the system.
        Args:
            value: Value to set for the authenticationMethodModes property.
        """
        self._authentication_method_modes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationStrengthRoot and sets the default values.
        """
        super().__init__()
        # A collection of all valid authentication method combinations in the system.
        self._authentication_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
        # Names and descriptions of all valid authentication method modes in the system.
        self._authentication_method_modes: Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
        self._policies: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationStrengthRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrengthRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationStrengthRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_combinations": lambda n : setattr(self, 'authentication_combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
            "authentication_method_modes": lambda n : setattr(self, 'authentication_method_modes', n.get_collection_of_object_values(authentication_method_mode_detail.AuthenticationMethodModeDetail)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(authentication_strength_policy.AuthenticationStrengthPolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policies(self,) -> Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]]:
        """
        Gets the policies property value. A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
        Returns: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]]
        """
        return self._policies
    
    @policies.setter
    def policies(self,value: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None) -> None:
        """
        Sets the policies property value. A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
        Args:
            value: Value to set for the policies property.
        """
        self._policies = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("authenticationCombinations", self.authentication_combinations)
        writer.write_collection_of_object_values("authenticationMethodModes", self.authentication_method_modes)
        writer.write_collection_of_object_values("policies", self.policies)
    

