from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_strength_policy, conditional_access_grant_control

class ConditionalAccessGrantControls(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessGrantControls and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The authenticationStrength property
        self._authentication_strength: Optional[authentication_strength_policy.AuthenticationStrengthPolicy] = None
        # List of values of built-in controls required by the policy. Possible values: block, mfa, compliantDevice, domainJoinedDevice, approvedApplication, compliantApplication, passwordChange, unknownFutureValue.
        self._built_in_controls: Optional[List[conditional_access_grant_control.ConditionalAccessGrantControl]] = None
        # List of custom controls IDs required by the policy. To learn more about custom control, see Custom controls (preview).
        self._custom_authentication_factors: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines the relationship of the grant controls. Possible values: AND, OR.
        self._operator: Optional[str] = None
        # List of terms of use IDs required by the policy.
        self._terms_of_use: Optional[List[str]] = None
    
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
    def authentication_strength(self,) -> Optional[authentication_strength_policy.AuthenticationStrengthPolicy]:
        """
        Gets the authenticationStrength property value. The authenticationStrength property
        Returns: Optional[authentication_strength_policy.AuthenticationStrengthPolicy]
        """
        return self._authentication_strength
    
    @authentication_strength.setter
    def authentication_strength(self,value: Optional[authentication_strength_policy.AuthenticationStrengthPolicy] = None) -> None:
        """
        Sets the authenticationStrength property value. The authenticationStrength property
        Args:
            value: Value to set for the authentication_strength property.
        """
        self._authentication_strength = value
    
    @property
    def built_in_controls(self,) -> Optional[List[conditional_access_grant_control.ConditionalAccessGrantControl]]:
        """
        Gets the builtInControls property value. List of values of built-in controls required by the policy. Possible values: block, mfa, compliantDevice, domainJoinedDevice, approvedApplication, compliantApplication, passwordChange, unknownFutureValue.
        Returns: Optional[List[conditional_access_grant_control.ConditionalAccessGrantControl]]
        """
        return self._built_in_controls
    
    @built_in_controls.setter
    def built_in_controls(self,value: Optional[List[conditional_access_grant_control.ConditionalAccessGrantControl]] = None) -> None:
        """
        Sets the builtInControls property value. List of values of built-in controls required by the policy. Possible values: block, mfa, compliantDevice, domainJoinedDevice, approvedApplication, compliantApplication, passwordChange, unknownFutureValue.
        Args:
            value: Value to set for the built_in_controls property.
        """
        self._built_in_controls = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessGrantControls:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessGrantControls
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessGrantControls()
    
    @property
    def custom_authentication_factors(self,) -> Optional[List[str]]:
        """
        Gets the customAuthenticationFactors property value. List of custom controls IDs required by the policy. To learn more about custom control, see Custom controls (preview).
        Returns: Optional[List[str]]
        """
        return self._custom_authentication_factors
    
    @custom_authentication_factors.setter
    def custom_authentication_factors(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the customAuthenticationFactors property value. List of custom controls IDs required by the policy. To learn more about custom control, see Custom controls (preview).
        Args:
            value: Value to set for the custom_authentication_factors property.
        """
        self._custom_authentication_factors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_strength_policy, conditional_access_grant_control

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(authentication_strength_policy.AuthenticationStrengthPolicy)),
            "builtInControls": lambda n : setattr(self, 'built_in_controls', n.get_collection_of_enum_values(conditional_access_grant_control.ConditionalAccessGrantControl)),
            "customAuthenticationFactors": lambda n : setattr(self, 'custom_authentication_factors', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "termsOfUse": lambda n : setattr(self, 'terms_of_use', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
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
    
    @property
    def operator(self,) -> Optional[str]:
        """
        Gets the operator property value. Defines the relationship of the grant controls. Possible values: AND, OR.
        Returns: Optional[str]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[str] = None) -> None:
        """
        Sets the operator property value. Defines the relationship of the grant controls. Possible values: AND, OR.
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_enum_value("builtInControls", self.built_in_controls)
        writer.write_collection_of_primitive_values("customAuthenticationFactors", self.custom_authentication_factors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operator", self.operator)
        writer.write_collection_of_primitive_values("termsOfUse", self.terms_of_use)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def terms_of_use(self,) -> Optional[List[str]]:
        """
        Gets the termsOfUse property value. List of terms of use IDs required by the policy.
        Returns: Optional[List[str]]
        """
        return self._terms_of_use
    
    @terms_of_use.setter
    def terms_of_use(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the termsOfUse property value. List of terms of use IDs required by the policy.
        Args:
            value: Value to set for the terms_of_use property.
        """
        self._terms_of_use = value
    

