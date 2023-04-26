from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import verified_credential_claims

class VerifiedCredentialData(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new verifiedCredentialData and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The authority ID for the issuer.
        self._authority: Optional[str] = None
        # Key-value pair of claims retrieved from the credential that the user presented, and the service verified.
        self._claims: Optional[verified_credential_claims.VerifiedCredentialClaims] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The list of credential types provided by the issuer.
        self._type: Optional[List[str]] = None
    
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
    def authority(self,) -> Optional[str]:
        """
        Gets the authority property value. The authority ID for the issuer.
        Returns: Optional[str]
        """
        return self._authority
    
    @authority.setter
    def authority(self,value: Optional[str] = None) -> None:
        """
        Sets the authority property value. The authority ID for the issuer.
        Args:
            value: Value to set for the authority property.
        """
        self._authority = value
    
    @property
    def claims(self,) -> Optional[verified_credential_claims.VerifiedCredentialClaims]:
        """
        Gets the claims property value. Key-value pair of claims retrieved from the credential that the user presented, and the service verified.
        Returns: Optional[verified_credential_claims.VerifiedCredentialClaims]
        """
        return self._claims
    
    @claims.setter
    def claims(self,value: Optional[verified_credential_claims.VerifiedCredentialClaims] = None) -> None:
        """
        Sets the claims property value. Key-value pair of claims retrieved from the credential that the user presented, and the service verified.
        Args:
            value: Value to set for the claims property.
        """
        self._claims = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerifiedCredentialData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedCredentialData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VerifiedCredentialData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import verified_credential_claims

        fields: Dict[str, Callable[[Any], None]] = {
            "authority": lambda n : setattr(self, 'authority', n.get_str_value()),
            "claims": lambda n : setattr(self, 'claims', n.get_object_value(verified_credential_claims.VerifiedCredentialClaims)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_collection_of_primitive_values(str)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("authority", self.authority)
        writer.write_object_value("claims", self.claims)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[List[str]]:
        """
        Gets the type property value. The list of credential types provided by the issuer.
        Returns: Optional[List[str]]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the type property value. The list of credential types provided by the issuer.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

