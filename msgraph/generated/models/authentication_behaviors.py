from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class AuthenticationBehaviors(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationBehaviors and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The removeUnverifiedEmailClaim property
        self._remove_unverified_email_claim: Optional[bool] = None
        # The requireClientServicePrincipal property
        self._require_client_service_principal: Optional[bool] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationBehaviors:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationBehaviors
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationBehaviors()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "removeUnverifiedEmailClaim": lambda n : setattr(self, 'remove_unverified_email_claim', n.get_bool_value()),
            "requireClientServicePrincipal": lambda n : setattr(self, 'require_client_service_principal', n.get_bool_value()),
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
    def remove_unverified_email_claim(self,) -> Optional[bool]:
        """
        Gets the removeUnverifiedEmailClaim property value. The removeUnverifiedEmailClaim property
        Returns: Optional[bool]
        """
        return self._remove_unverified_email_claim
    
    @remove_unverified_email_claim.setter
    def remove_unverified_email_claim(self,value: Optional[bool] = None) -> None:
        """
        Sets the removeUnverifiedEmailClaim property value. The removeUnverifiedEmailClaim property
        Args:
            value: Value to set for the remove_unverified_email_claim property.
        """
        self._remove_unverified_email_claim = value
    
    @property
    def require_client_service_principal(self,) -> Optional[bool]:
        """
        Gets the requireClientServicePrincipal property value. The requireClientServicePrincipal property
        Returns: Optional[bool]
        """
        return self._require_client_service_principal
    
    @require_client_service_principal.setter
    def require_client_service_principal(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireClientServicePrincipal property value. The requireClientServicePrincipal property
        Args:
            value: Value to set for the require_client_service_principal property.
        """
        self._require_client_service_principal = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("removeUnverifiedEmailClaim", self.remove_unverified_email_claim)
        writer.write_bool_value("requireClientServicePrincipal", self.require_client_service_principal)
        writer.write_additional_data_value(self.additional_data)
    

