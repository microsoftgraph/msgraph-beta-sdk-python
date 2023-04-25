from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import verifiable_credential_type

class VerifiableCredentialSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new verifiableCredentialSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The types of verifiable credentials that a requestor must present when requesting an access package that has the policy.
        self._credential_types: Optional[List[verifiable_credential_type.VerifiableCredentialType]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerifiableCredentialSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerifiableCredentialSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VerifiableCredentialSettings()
    
    @property
    def credential_types(self,) -> Optional[List[verifiable_credential_type.VerifiableCredentialType]]:
        """
        Gets the credentialTypes property value. The types of verifiable credentials that a requestor must present when requesting an access package that has the policy.
        Returns: Optional[List[verifiable_credential_type.VerifiableCredentialType]]
        """
        return self._credential_types
    
    @credential_types.setter
    def credential_types(self,value: Optional[List[verifiable_credential_type.VerifiableCredentialType]] = None) -> None:
        """
        Sets the credentialTypes property value. The types of verifiable credentials that a requestor must present when requesting an access package that has the policy.
        Args:
            value: Value to set for the credential_types property.
        """
        self._credential_types = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import verifiable_credential_type

        fields: Dict[str, Callable[[Any], None]] = {
            "credentialTypes": lambda n : setattr(self, 'credential_types', n.get_collection_of_object_values(verifiable_credential_type.VerifiableCredentialType)),
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
        writer.write_collection_of_object_values("credentialTypes", self.credential_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

