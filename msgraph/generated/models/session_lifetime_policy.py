from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

expiration_requirement = lazy_import('msgraph.generated.models.expiration_requirement')

class SessionLifetimePolicy(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new sessionLifetimePolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The human-readable details of the conditional access session management policy applied to the sign-in.
        self._detail: Optional[str] = None
        # If a conditional access session management policy required the user to authenticate in this sign-in event, this field describes the policy type that required authentication. The possible values are: rememberMultifactorAuthenticationOnTrustedDevices, tenantTokenLifetimePolicy, audienceTokenLifetimePolicy, signInFrequencyPeriodicReauthentication, ngcMfa, signInFrequencyEveryTime, unknownFutureValue.
        self._expiration_requirement: Optional[expiration_requirement.ExpirationRequirement] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SessionLifetimePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SessionLifetimePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SessionLifetimePolicy()
    
    @property
    def detail(self,) -> Optional[str]:
        """
        Gets the detail property value. The human-readable details of the conditional access session management policy applied to the sign-in.
        Returns: Optional[str]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[str] = None) -> None:
        """
        Sets the detail property value. The human-readable details of the conditional access session management policy applied to the sign-in.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def expiration_requirement(self,) -> Optional[expiration_requirement.ExpirationRequirement]:
        """
        Gets the expirationRequirement property value. If a conditional access session management policy required the user to authenticate in this sign-in event, this field describes the policy type that required authentication. The possible values are: rememberMultifactorAuthenticationOnTrustedDevices, tenantTokenLifetimePolicy, audienceTokenLifetimePolicy, signInFrequencyPeriodicReauthentication, ngcMfa, signInFrequencyEveryTime, unknownFutureValue.
        Returns: Optional[expiration_requirement.ExpirationRequirement]
        """
        return self._expiration_requirement
    
    @expiration_requirement.setter
    def expiration_requirement(self,value: Optional[expiration_requirement.ExpirationRequirement] = None) -> None:
        """
        Sets the expirationRequirement property value. If a conditional access session management policy required the user to authenticate in this sign-in event, this field describes the policy type that required authentication. The possible values are: rememberMultifactorAuthenticationOnTrustedDevices, tenantTokenLifetimePolicy, audienceTokenLifetimePolicy, signInFrequencyPeriodicReauthentication, ngcMfa, signInFrequencyEveryTime, unknownFutureValue.
        Args:
            value: Value to set for the expirationRequirement property.
        """
        self._expiration_requirement = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "expiration_requirement": lambda n : setattr(self, 'expiration_requirement', n.get_enum_value(expiration_requirement.ExpirationRequirement)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
            value: Value to set for the OdataType property.
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
        writer.write_str_value("detail", self.detail)
        writer.write_enum_value("expirationRequirement", self.expiration_requirement)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

