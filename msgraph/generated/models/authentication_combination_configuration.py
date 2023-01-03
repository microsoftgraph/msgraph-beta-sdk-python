from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_modes = lazy_import('msgraph.generated.models.authentication_method_modes')
entity = lazy_import('msgraph.generated.models.entity')

class AuthenticationCombinationConfiguration(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def applies_to_combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the appliesToCombinations property value. Which authentication method combinations this configuration applies to. Must be an allowedCombinations object that's defined for the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._applies_to_combinations
    
    @applies_to_combinations.setter
    def applies_to_combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the appliesToCombinations property value. Which authentication method combinations this configuration applies to. Must be an allowedCombinations object that's defined for the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
        Args:
            value: Value to set for the appliesToCombinations property.
        """
        self._applies_to_combinations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationCombinationConfiguration and sets the default values.
        """
        super().__init__()
        # Which authentication method combinations this configuration applies to. Must be an allowedCombinations object that's defined for the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
        self._applies_to_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationCombinationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationCombinationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationCombinationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applies_to_combinations": lambda n : setattr(self, 'applies_to_combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
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
        writer.write_enum_value("appliesToCombinations", self.applies_to_combinations)
    

